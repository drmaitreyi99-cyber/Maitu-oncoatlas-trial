#!/usr/bin/env python3
"""Build multi-page DM Medical Oncology exam-answer PDFs with diagrams."""
from __future__ import annotations

import re
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    ListFlowable,
    ListItem,
    HRFlowable,
    Flowable,
)

PAGE_W, PAGE_H = A4
MARGIN = 1.6 * cm

NAVY = colors.HexColor("#1a365d")
TEAL = colors.HexColor("#0d9488")
AMBER = colors.HexColor("#b45309")
LIGHT = colors.HexColor("#f0f9ff")
NCCN_BG = colors.HexColor("#fef3c7")
PEARL_BG = colors.HexColor("#ecfdf5")
BOX_BG = colors.HexColor("#f8fafc")
LINE = colors.HexColor("#94a3b8")


class FlowChart(Flowable):
    """Simple vertical/horizontal flowchart for exam notes."""

    def __init__(self, boxes: list[str], title: str = "", width: float = 16 * cm):
        super().__init__()
        self.boxes = boxes
        self.title = title
        self.box_w = width
        self.row_h = 1.2 * cm
        self.gap = 0.45 * cm
        self.height = (len(boxes) * (self.row_h + self.gap)) + (0.7 * cm if title else 0.3 * cm)

    def wrap(self, aw, ah):
        return self.box_w, self.height

    def draw(self):
        c = self.canv
        y = self.height
        if self.title:
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(NAVY)
            c.drawString(0, y - 10, self.title)
            y -= 0.55 * cm
        for i, text in enumerate(self.boxes):
            y -= self.row_h
            c.setFillColor(colors.HexColor("#e0f2fe") if i % 2 == 0 else colors.HexColor("#ccfbf1"))
            c.setStrokeColor(NAVY)
            c.roundRect(0, y, self.box_w, self.row_h - 2, 4, fill=1, stroke=1)
            c.setFillColor(colors.black)
            c.setFont("Helvetica", 8)
            # wrap roughly
            max_chars = 95
            line = text if len(text) <= max_chars else text[: max_chars - 1] + "…"
            c.drawCentredString(self.box_w / 2, y + self.row_h / 2 - 4, line)
            if i < len(self.boxes) - 1:
                c.setStrokeColor(TEAL)
                c.setLineWidth(1.2)
                mid = self.box_w / 2
                c.line(mid, y, mid, y - self.gap + 2)
                c.line(mid - 3, y - self.gap + 8, mid, y - self.gap + 2)
                c.line(mid + 3, y - self.gap + 8, mid, y - self.gap + 2)
                y -= self.gap


class MechanismBox(Flowable):
    def __init__(self, rows: list[tuple[str, str]], width: float = 16 * cm):
        super().__init__()
        self.rows = rows
        self.width = width
        self.row_h = 0.85 * cm
        self.height = len(rows) * self.row_h + 0.2 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        y = self.height - self.row_h
        for i, (left, right) in enumerate(self.rows):
            c.setFillColor(colors.HexColor("#f1f5f9") if i % 2 == 0 else colors.white)
            c.rect(0, y, self.width * 0.32, self.row_h, fill=1, stroke=1)
            c.rect(self.width * 0.32, y, self.width * 0.68, self.row_h, fill=1, stroke=1)
            c.setFillColor(NAVY)
            c.setFont("Helvetica-Bold", 7.5)
            c.drawString(4, y + 8, left[:40])
            c.setFillColor(colors.black)
            c.setFont("Helvetica", 7.5)
            c.drawString(self.width * 0.32 + 4, y + 8, right[:85])
            y -= self.row_h


def make_styles():
    ss = getSampleStyleSheet()
    styles = {
        "cover_title": ParagraphStyle(
            "cover_title", parent=ss["Title"], fontName="Helvetica-Bold", fontSize=16,
            textColor=NAVY, leading=20, alignment=TA_CENTER, spaceAfter=8,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub", parent=ss["Normal"], fontName="Helvetica", fontSize=10,
            textColor=TEAL, leading=13, alignment=TA_CENTER, spaceAfter=4,
        ),
        "h1": ParagraphStyle(
            "h1", parent=ss["Heading1"], fontName="Helvetica-Bold", fontSize=12.5,
            textColor=NAVY, leading=16, spaceBefore=12, spaceAfter=8,
            borderPadding=3,
        ),
        "h2": ParagraphStyle(
            "h2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=11,
            textColor=TEAL, leading=14, spaceBefore=10, spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "body", parent=ss["Normal"], fontName="Helvetica", fontSize=10,
            leading=14.5, alignment=TA_JUSTIFY, spaceAfter=8,
        ),
        "bullet": ParagraphStyle(
            "bullet", parent=ss["Normal"], fontName="Helvetica", fontSize=10,
            leading=14, leftIndent=8, spaceAfter=4,
        ),
        "small": ParagraphStyle(
            "small", parent=ss["Normal"], fontName="Helvetica", fontSize=8,
            leading=10, textColor=colors.HexColor("#334155"),
        ),
        "caption": ParagraphStyle(
            "caption", parent=ss["Normal"], fontName="Helvetica-Oblique", fontSize=8,
            leading=10, textColor=colors.HexColor("#64748b"), alignment=TA_CENTER, spaceAfter=6,
        ),
        "box_title": ParagraphStyle(
            "box_title", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=9,
            textColor=AMBER, leading=11, spaceAfter=3,
        ),
        "pearl": ParagraphStyle(
            "pearl", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=9,
            textColor=colors.HexColor("#065f46"), leading=11,
        ),
        "footer": ParagraphStyle(
            "footer", parent=ss["Normal"], fontName="Helvetica", fontSize=7,
            textColor=colors.HexColor("#64748b"), alignment=TA_CENTER,
        ),
        "table_cell": ParagraphStyle(
            "table_cell", parent=ss["Normal"], fontName="Helvetica", fontSize=7.5,
            leading=9.5,
        ),
        "table_head": ParagraphStyle(
            "table_head", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=8,
            leading=10, textColor=colors.white,
        ),
    }
    return styles


def _header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(1)
    canvas.line(MARGIN, PAGE_H - 1.1 * cm, PAGE_W - MARGIN, PAGE_H - 1.1 * cm)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(NAVY)
    canvas.drawString(MARGIN, PAGE_H - 0.85 * cm, "DM Medical Oncology · Paper IV · Exam Answer Notes")
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.85 * cm, "NCCN 2026 updates included")
    canvas.setStrokeColor(LINE)
    canvas.line(MARGIN, 1.2 * cm, PAGE_W - MARGIN, 1.2 * cm)
    canvas.setFillColor(colors.HexColor("#64748b"))
    canvas.drawCentredString(PAGE_W / 2, 0.7 * cm, f"Page {doc.page}  |  For university exam revision — verify latest NCCN/FDA before clinical use")
    canvas.restoreState()


def boxed_paragraphs(title: str, lines: list[str], styles, bg=NCCN_BG):
    data = [[Paragraph(f"<b>{title}</b>", styles["box_title"])]]
    for ln in lines:
        data.append([Paragraph(f"• {ln}", styles["small"])])
    t = Table(data, colWidths=[16.5 * cm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("BOX", (0, 0), (-1, -1), 0.8, AMBER if bg == NCCN_BG else TEAL),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return t


def trial_table(rows: list[tuple[str, str]], styles):
    data = [[
        Paragraph("<b>Trial</b>", styles["table_head"]),
        Paragraph("<b>Key result / exam takeaway</b>", styles["table_head"]),
    ]]
    for a, b in rows:
        data.append([Paragraph(a, styles["table_cell"]), Paragraph(b, styles["table_cell"])])
    t = Table(data, colWidths=[5.5 * cm, 11 * cm])
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), LIGHT))
    t.setStyle(TableStyle(style_cmds))
    return t


def dose_table(items: list[tuple[str, str]], styles):
    data = [[
        Paragraph("<b>Drug / regimen</b>", styles["table_head"]),
        Paragraph("<b>Dose / schedule (exam pearls)</b>", styles["table_head"]),
    ]]
    for a, b in items:
        data.append([Paragraph(a, styles["table_cell"]), Paragraph(b, styles["table_cell"])])
    t = Table(data, colWidths=[4.5 * cm, 12 * cm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), TEAL),
                ("GRID", (0, 0), (-1, -1), 0.4, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return t


def build_pdf(path: Path, meta: dict, sections: list[dict]):
    """sections: list of {heading, level, paragraphs, bullets, flowchart, mechanism, table_trials, table_doses, nccn, pearls}"""
    styles = make_styles()
    doc = BaseDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=1.5 * cm,
        bottomMargin=1.6 * cm,
        title=meta.get("title", "DM Oncology Notes"),
        author="DM Medical Oncology Exam Notes",
    )
    frame = Frame(MARGIN, 1.5 * cm, PAGE_W - 2 * MARGIN, PAGE_H - 3.1 * cm, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=_header_footer)])

    story = []
    # Cover
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("D.M. MEDICAL ONCOLOGY — PAPER IV", styles["cover_sub"]))
    story.append(Paragraph("RECENT ADVANCES · EXAM ANSWER NOTES", styles["cover_sub"]))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(meta["question"], styles["cover_title"]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(
        Paragraph(
            f"<b>{meta['exam']}</b>  |  {meta['code']}  |  Q{meta['number']} ({meta['type']})  |  "
            f"<b>{meta['marks']} marks</b>  |  Target ~{meta['target_pages']} pages",
            styles["cover_sub"],
        )
    )
    story.append(Spacer(1, 0.15 * cm))
    story.append(
        Paragraph(
            "Includes: mechanisms · doses/regimens · landmark clinical trials · hallmarks · "
            "<b>NCCN 2026 / 2027 updates</b> · flow charts · exam pearls",
            styles["caption"],
        )
    )
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY, spaceAfter=8))

    for sec in sections:
        level = sec.get("level", 1)
        story.append(Paragraph(sec["heading"], styles["h1"] if level == 1 else styles["h2"]))
        for p in sec.get("paragraphs", []):
            story.append(Paragraph(p, styles["body"]))
        for b in sec.get("bullets", []):
            story.append(Paragraph(f"• {b}", styles["bullet"]))
        if sec.get("flowchart"):
            story.append(Spacer(1, 0.15 * cm))
            story.append(FlowChart(sec["flowchart"], title=sec.get("flowchart_title", "Clinical algorithm")))
            story.append(Paragraph(sec.get("flowchart_caption", "Figure: stepwise exam algorithm"), styles["caption"]))
        if sec.get("mechanism"):
            story.append(MechanismBox(sec["mechanism"]))
            story.append(Paragraph("Figure: mechanism / pathway map", styles["caption"]))
        if sec.get("table_trials"):
            story.append(trial_table(sec["table_trials"], styles))
            story.append(Paragraph("Table: landmark clinical trials", styles["caption"]))
        if sec.get("table_doses"):
            story.append(dose_table(sec["table_doses"], styles))
            story.append(Paragraph("Table: doses and regimens", styles["caption"]))
        if sec.get("nccn"):
            story.append(Spacer(1, 0.1 * cm))
            vers = "; ".join(sec["nccn"].get("versions", []))
            lines = [f"<i>Referenced versions:</i> {vers}"] + sec["nccn"].get("bullets", [])
            story.append(boxed_paragraphs("NCCN 2026 / 2027 UPDATES (include in answer)", lines, styles, NCCN_BG))
            story.append(Spacer(1, 0.15 * cm))
        if sec.get("pearls"):
            story.append(boxed_paragraphs("EXAM PEARLS / HALLMARKS", sec["pearls"], styles, PEARL_BG))
            story.append(Spacer(1, 0.15 * cm))
        story.append(Spacer(1, 0.1 * cm))

    # Closing disclaimer
    story.append(HRFlowable(width="100%", thickness=0.8, color=LINE, spaceBefore=6, spaceAfter=6))
    story.append(
        Paragraph(
            "<b>Disclaimer:</b> Compiled for DM exam revision from published trials and NCCN 2026/2027 public summaries "
            "(ASCO Post, OncLive, JNCCN selections, NCCN category list). Always verify the current full NCCN PDF, "
            "FDA/CDSCO labels, and institutional protocols before patient care. Doses require BSA/organ-function adjustment.",
            styles["small"],
        )
    )

    doc.build(story)
    return path

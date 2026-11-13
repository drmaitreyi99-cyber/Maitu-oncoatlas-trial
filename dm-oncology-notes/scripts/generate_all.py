#!/usr/bin/env python3
"""Generate one PDF per question + master index + NCCN 2026 cheat sheet."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "content"))

from content_engine import compose_answer  # noqa: E402
from nccn_2026_updates import NCCN_VERSIONS, UPDATES  # noqa: E402
from pdf_builder import build_pdf, make_styles, boxed_paragraphs, NAVY, TEAL, MARGIN, PAGE_W, PAGE_H, _header_footer  # noqa: E402
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import cm


def generate_question_pdfs(limit: int | None = None, only_ids: list[str] | None = None):
    bank = json.loads((ROOT / "questions" / "question_bank.json").read_text())
    out_dir = ROOT / "pdfs" / "by_question"
    out_dir.mkdir(parents=True, exist_ok=True)
    arts = Path("/opt/cursor/artifacts/dm-oncology-exam-notes")
    arts.mkdir(parents=True, exist_ok=True)

    questions = bank["questions"]
    if only_ids:
        questions = [q for q in questions if q["id"] in only_ids]
    if limit:
        questions = questions[:limit]

    manifest = []
    for i, q in enumerate(questions, 1):
        sections = compose_answer(q)
        fname = f"{q['id']}_{q['slug'][:60]}.pdf"
        path = out_dir / fname
        meta = {
            "title": f"{q['id']} {q['question'][:80]}",
            "question": q["question"],
            "exam": q["exam"],
            "code": q["code"],
            "number": q["number"],
            "type": "Essay / Elaborate" if q["type"] == "essay" else "Short note / Write notes",
            "marks": q["marks"],
            "target_pages": q["target_pages"],
        }
        build_pdf(path, meta, sections)
        # also copy to artifacts in batches optionally
        manifest.append(
            {
                "id": q["id"],
                "exam": q["exam"],
                "marks": q["marks"],
                "type": q["type"],
                "question": q["question"],
                "file": str(path.relative_to(ROOT)),
                "pages_target": q["target_pages"],
            }
        )
        if i % 20 == 0 or i == len(questions):
            print(f"Generated {i}/{len(questions)}: {q['id']}")

    man_path = ROOT / "pdfs" / "manifest.json"
    man_path.write_text(json.dumps({"count": len(manifest), "items": manifest}, indent=2))
    return manifest


def generate_nccn_cheatsheet():
    styles = make_styles()
    path = ROOT / "pdfs" / "NCCN_2026_Updates_CheatSheet.pdf"
    arts = Path("/opt/cursor/artifacts/dm-oncology-exam-notes")
    arts.mkdir(parents=True, exist_ok=True)

    doc = BaseDocTemplate(
        str(path),
        pagesize=(PAGE_W, PAGE_H),
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=1.5 * cm,
        bottomMargin=1.6 * cm,
        title="NCCN 2026 Updates Cheat Sheet",
    )
    frame = Frame(MARGIN, 1.5 * cm, PAGE_W - 2 * MARGIN, PAGE_H - 3.1 * cm, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=_header_footer)])
    story = []
    story.append(Paragraph("NCCN 2026 / 2027 GUIDELINE UPDATES — EXAM CHEAT SHEET", styles["cover_title"]))
    story.append(
        Paragraph(
            "Use these bullets inside every Paper IV answer under a heading “Recent NCCN updates (2026)”. "
            "Sources: NCCN version list; ASCO Post May 2026 conference roundup; OncLive notable changes into 2026.",
            styles["body"],
        )
    )
    story.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceAfter=8))

    # versions table-like bullets
    story.append(Paragraph("Current version anchors (cite year)", styles["h1"]))
    for k, v in sorted(NCCN_VERSIONS.items(), key=lambda x: x[1]):
        story.append(Paragraph(f"• <b>{k}</b>: {v}", styles["bullet"]))

    story.append(Paragraph("Disease-wise high-yield 2026 updates", styles["h1"]))
    for topic, bullets in UPDATES.items():
        vers = NCCN_VERSIONS.get(topic, "NCCN latest 2026/2027")
        story.append(Paragraph(f"{topic.upper()} — {vers}", styles["h2"]))
        story.append(boxed_paragraphs(f"NCCN updates: {topic}", bullets, styles))
        story.append(Spacer(1, 0.15 * cm))

    story.append(Paragraph("How to write it in the answer booklet", styles["h1"]))
    story.append(
        Paragraph(
            "“As per NCCN Guidelines® [Disease] Version X.2026/2027, key practice-changing points include: (1)… (2)… (3)… "
            "These are Category [1/2A] preferred / other recommended options supported by [trial]. "
            "In the Indian context, correlate with CDSCO approval and NCG resource-stratified pathways.”",
            styles["body"],
        )
    )
    doc.build(story)
    # copy
    dest = arts / "NCCN_2026_Updates_CheatSheet.pdf"
    dest.write_bytes(path.read_bytes())
    print(f"Wrote {path}")
    return path


def generate_index_pdf(manifest):
    styles = make_styles()
    path = ROOT / "pdfs" / "00_Master_Index.pdf"
    doc = BaseDocTemplate(
        str(path),
        pagesize=(PAGE_W, PAGE_H),
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=1.5 * cm,
        bottomMargin=1.6 * cm,
        title="Master Index DM Oncology Notes",
    )
    frame = Frame(MARGIN, 1.5 * cm, PAGE_W - 2 * MARGIN, PAGE_H - 3.1 * cm, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=_header_footer)])
    story = []
    story.append(Paragraph("MASTER INDEX — DM MEDICAL ONCOLOGY PAPER IV", styles["cover_title"]))
    story.append(
        Paragraph(
            f"Total questions answered: <b>{len(manifest)}</b> (each as a separate PDF). "
            "Essays target ~15 pages; short notes target ~10–12 pages. All include NCCN 2026 updates, trials, doses, and flowcharts.",
            styles["body"],
        )
    )
    story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=6))
    current_exam = None
    for item in manifest:
        if item["exam"] != current_exam:
            current_exam = item["exam"]
            story.append(Paragraph(current_exam, styles["h1"]))
        story.append(
            Paragraph(
                f"<b>{item['id']}</b> [{item['marks']}m · {item['type']}] {item['question']}<br/>"
                f"<font size='7'>{item['file']}</font>",
                styles["small"],
            )
        )
    doc.build(story)
    arts = Path("/opt/cursor/artifacts/dm-oncology-exam-notes")
    (arts / "00_Master_Index.pdf").write_bytes(path.read_bytes())
    print(f"Wrote {path}")


def main():
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--ids", nargs="*", default=None)
    ap.add_argument("--skip-questions", action="store_true")
    args = ap.parse_args()

    generate_nccn_cheatsheet()
    manifest = []
    if not args.skip_questions:
        manifest = generate_question_pdfs(limit=args.limit, only_ids=args.ids)
        generate_index_pdf(manifest)
        # sync a zip of all pdfs to artifacts
        import shutil

        arts = Path("/opt/cursor/artifacts/dm-oncology-exam-notes")
        src = ROOT / "pdfs"
        zip_base = arts / "DM_Oncology_PaperIV_All_Answers"
        shutil.make_archive(str(zip_base), "zip", root_dir=src)
        print(f"Archive: {zip_base}.zip")
    print("Done")


if __name__ == "__main__":
    main()

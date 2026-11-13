#!/usr/bin/env python3
"""Topic-wise study index PDF for DM Paper IV answers."""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from pdf_builder import (  # noqa: E402
    PAGE_W,
    PAGE_H,
    MARGIN,
    NAVY,
    TEAL,
    _header_footer,
    make_styles,
)
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
)
from reportlab.lib.units import cm

TOPICS = [
    ("Breast / HER2 / TNBC / endocrine", r"breast|her2|trastuzumab|tnbc|emilia|axilla|dcis|alpelisib|pertuzumab|sacituzumab|pregnancy associated breast"),
    ("Lung / EGFR / ALK / NSCLC / SCLC", r"lung|nsclc|egfr|osimertinib|alk|sclc|dato|amivantamab|capmatinib"),
    ("Colorectal / rectal / MMR / MSI", r"colon|rectal|colorectal|mmr|msi|atomic|ctdna"),
    ("Gastric / esophageal / HIPEC GI", r"gastric|esophageal|flot|claudin|hipec"),
    ("CML / TKI / TFR", r"\bcml\b|imatinib|asciminib|dasatinib|nilotinib|ponatinib|stopping tki"),
    ("AML / APML / MDS / myeloid", r"\baml\b|apml|apl|mds|myeloid|flt3|venetoclax|eln 2022|who 2022"),
    ("CLL / BTK / lymphoma / Hodgkin", r"\bcll\b|lymphoma|hodgkin|brentuximab|beacopp|rituximab|bite|blinatumomab"),
    ("Myeloma / CAR-T / BiTE / cellular", r"myeloma|car.?t|bite|bcma|teclistamab|icans|adoptive"),
    ("Melanoma / immunotherapy / CPI", r"melanoma|checkpoint|pd.?1|ctla|nivolumab|pembrolizumab|immunotherapy"),
    ("RCC / prostate / bladder / GU", r"renal|rcc|prostate|bladder|urothelial|nm.?crpc|enfortumab|psma"),
    ("Ovarian / PARP / gynae", r"ovarian|parp|olaparib|endometrial|uterine|cervix|hipec"),
    ("ADC / targeted / KRAS / NGS", r"adc|antibody.?drug|kras|targeted|ngs|microarray|pharmacogenomic"),
    ("Supportive care / pain / FN / VTE", r"supportive|pain|febrile|neutropen|thrombo|vte|nutrition|geriatric|fertility"),
    ("Transplant / GVHD / haplo", r"transplant|gvhd|haplo|engraftment|conditioning|donor"),
    ("HIV / infection / prevention", r"hiv|aspergill|antifungal|vaccine preventable|chemoprevention"),
]


def main():
    bank = json.loads((ROOT / "questions" / "question_bank.json").read_text())
    buckets = defaultdict(list)
    for q in bank["questions"]:
        matched = False
        for name, pat in TOPICS:
            if re.search(pat, q["question"], re.I):
                buckets[name].append(q)
                matched = True
        if not matched:
            buckets["Other / cross-cutting topics"].append(q)

    styles = make_styles()
    path = ROOT / "pdfs" / "Topic_Wise_Study_Index.pdf"
    doc = BaseDocTemplate(
        str(path),
        pagesize=(PAGE_W, PAGE_H),
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=1.5 * cm,
        bottomMargin=1.6 * cm,
        title="Topic-wise Study Index",
    )
    frame = Frame(MARGIN, 1.5 * cm, PAGE_W - 2 * MARGIN, PAGE_H - 3.1 * cm, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=_header_footer)])
    story = []
    story.append(Paragraph("TOPIC-WISE STUDY INDEX — DM PAPER IV", styles["cover_title"]))
    story.append(
        Paragraph(
            "Use this map to revise by disease rather than by year. File names live in "
            "<b>pdfs/by_question/</b>. Prioritise FOCUS 2022–2026 essays (deepened) first, then shorts, then older repeats. "
            "Every answer embeds <b>NCCN 2026/2027</b> update boxes.",
            styles["body"],
        )
    )
    story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=8))

    # Priority revision order
    story.append(Paragraph("Suggested 10-day revision order", styles["h1"]))
    plan = [
        "Day 1–2: Breast HER2/TNBC + ADCs (incl. deep essays Q361, Q373, Q385)",
        "Day 3: Lung early + EGFR metastatic sequencing (Q362 + osimertinib shorts)",
        "Day 4: CRC/MMR/ATOMIC + gastric FLOT pathways (Q349)",
        "Day 5: AML/ELN2022 + CML TKI/TFR (Q350)",
        "Day 6: Myeloma bispecifics/CAR-T + lymphoma CPI",
        "Day 7: RCC IO+VEGF (Q338) + prostate/bladder",
        "Day 8: Melanoma mucosal (Q374) + immunotherapy toxicities",
        "Day 9: Supportive care (Q326) + HIV lymphomas (Q337) + transplant",
        "Day 10: RWE/digital (Q386) + microarray (Q325) + NCCN cheat sheet memorisation",
    ]
    for p in plan:
        story.append(Paragraph(f"• {p}", styles["bullet"]))

    story.append(Spacer(1, 0.3 * cm))
    for name in [t[0] for t in TOPICS] + ["Other / cross-cutting topics"]:
        items = buckets.get(name, [])
        if not items:
            continue
        story.append(Paragraph(f"{name} ({len(items)})", styles["h1"]))
        # essays first
        essays = [q for q in items if q["type"] == "essay"]
        shorts = [q for q in items if q["type"] == "short"]
        if essays:
            story.append(Paragraph("Essays", styles["h2"]))
            for q in essays:
                deep = " · DEEP" if q["id"] in {
                    "Q325","Q326","Q337","Q338","Q349","Q350","Q361","Q362","Q373","Q374","Q385","Q386"
                } else ""
                story.append(
                    Paragraph(
                        f"<b>{q['id']}</b> [{q['marks']}m · {q['exam']}]{deep}<br/>{q['question']}",
                        styles["small"],
                    )
                )
        if shorts:
            story.append(Paragraph("Short notes (selected listing)", styles["h2"]))
            for q in shorts[:25]:
                story.append(
                    Paragraph(
                        f"<b>{q['id']}</b> [{q['marks']}m · {q['exam']}] {q['question']}",
                        styles["small"],
                    )
                )
            if len(shorts) > 25:
                story.append(Paragraph(f"… +{len(shorts)-25} more in master index", styles["caption"]))

    doc.build(story)
    arts = Path("/opt/cursor/artifacts/dm-oncology-exam-notes")
    arts.mkdir(parents=True, exist_ok=True)
    (arts / "Topic_Wise_Study_Index.pdf").write_bytes(path.read_bytes())
    print(f"Wrote {path} pages check later")


if __name__ == "__main__":
    main()

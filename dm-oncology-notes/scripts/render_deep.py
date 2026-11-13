#!/usr/bin/env python3
"""Render deepened focus-pack PDFs using DEEP essay modules + enriched shorts."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "content"))

from content_engine import compose_answer, nccn_section, summary_section  # noqa: E402
from nccn_2026_updates import get_nccn_block  # noqa: E402
from pdf_builder import build_pdf  # noqa: E402
from deep_essays_batch_a import DEEP as DEEP_A  # noqa: E402
from deep_essays_batch_b import DEEP as DEEP_B  # noqa: E402
from deep_essays_batch_c import DEEP as DEEP_C  # noqa: E402

DEEP = {}
DEEP.update(DEEP_A)
DEEP.update(DEEP_B)
DEEP.update(DEEP_C)

FOCUS_EXAMS = {
    "February 2022",
    "August 2022",
    "February 2023",
    "January 2024",
    "February 2025",
    "January 2026",
}


def enrich_deep(qid: str, meta: dict) -> list[dict]:
    """Prefer hand-crafted DEEP sections, then append template expanders for page length."""
    deep_sections = list(DEEP[qid])
    # Prefix banner
    banner = {
        "heading": "0. How to use this DEEP answer",
        "level": 1,
        "paragraphs": [
            "Sections below are <b>high-yield, trial-dense content</b> written for a 15-mark Paper IV elaboration. "
            "After the deep core, additional revision modules (algorithms, supportive care, flash cards) extend the note to full booklet length.",
        ],
        "pearls": [
            "In the exam hall, prioritise the DEEP trial tables + NCCN 2026 boxes first.",
            "Draw at least one flowchart from the deep sections.",
        ],
    }
    # Template expansion for length + extra diagrams
    m = dict(meta)
    m["target_pages"] = 16
    template_tail = compose_answer(m)
    # Drop duplicate intro-ish first 2 template sections to reduce redundancy
    template_tail = template_tail[2:]
    sections = [banner] + deep_sections + [
        {
            "heading": "— Additional exam-length revision modules —",
            "level": 1,
            "paragraphs": [
                "The following modules reinforce algorithms, toxicities, Indian/NCG context, and last-page summary structure."
            ],
        }
    ] + template_tail
    sections.append(
        {
            "heading": "Final NCCN 2026 box",
            "level": 2,
            "nccn": get_nccn_block(meta["question"]),
            "paragraphs": [
                "Copy these bullets onto the last page of your answer booklet for Paper IV currency marks."
            ],
        }
    )
    return sections


def main():
    bank = json.loads((ROOT / "questions" / "question_bank.json").read_text())
    focus = [q for q in bank["questions"] if q["exam"] in FOCUS_EXAMS]
    out_dir = ROOT / "pdfs" / "focus_2022_2026"
    out_dir.mkdir(parents=True, exist_ok=True)
    byq = ROOT / "pdfs" / "by_question"
    byq.mkdir(parents=True, exist_ok=True)

    arts = Path("/opt/cursor/artifacts/dm-oncology-exam-notes")
    focus_arts = arts / "focus_2022_2026"
    if focus_arts.exists():
        shutil.rmtree(focus_arts)
    focus_arts.mkdir(parents=True)
    arts.mkdir(parents=True, exist_ok=True)

    for i, q in enumerate(focus, 1):
        if q["id"] in DEEP:
            sections = enrich_deep(q["id"], q)
            label = "DEEP Essay / Elaborate (FOCUS 2022–2026)"
            target = 16
        else:
            meta = dict(q)
            meta["target_pages"] = 13 if q["type"] == "short" else 16
            sections = compose_answer(meta)
            label = (
                "Essay / Elaborate (FOCUS 2022–2026)"
                if q["type"] == "essay"
                else "Short note (FOCUS 2022–2026 · NCCN 2026)"
            )
            target = meta["target_pages"]

        fname = f"{q['id']}_{q['slug'][:55]}.pdf"
        path = out_dir / fname
        build_pdf(
            path,
            {
                "title": q["question"][:80],
                "question": q["question"],
                "exam": q["exam"],
                "code": q["code"],
                "number": q["number"],
                "type": label,
                "marks": q["marks"],
                "target_pages": target,
            },
            sections,
        )
        shutil.copy(path, focus_arts / fname)
        # also refresh by_question copy for deep essays
        if q["id"] in DEEP:
            shutil.copy(path, byq / fname)
        if i % 12 == 0 or i == len(focus):
            print(f"{i}/{len(focus)} {q['id']} deep={q['id'] in DEEP}")

    zip_base = arts / "DM_Oncology_Focus_2022_2026"
    shutil.make_archive(str(zip_base), "zip", root_dir=out_dir)
    print("Wrote", zip_base.with_suffix(".zip"))


if __name__ == "__main__":
    main()

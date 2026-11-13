#!/usr/bin/env python3
"""Build a 2022–2026 focus pack with deepened PDFs + index."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "content"))

from content_engine import compose_answer  # noqa: E402
from pdf_builder import build_pdf  # noqa: E402


FOCUS_EXAMS = {
    "February 2022",
    "August 2022",
    "February 2023",
    "January 2024",
    "February 2025",
    "January 2026",
}


def deepen(meta: dict) -> dict:
    m = dict(meta)
    # push page targets up for focus pack
    if m["type"] == "essay":
        m["target_pages"] = max(m.get("target_pages", 15), 16)
        m["marks"] = max(m.get("marks", 15), 15)
    else:
        m["target_pages"] = max(m.get("target_pages", 11), 12)
    return m


def main():
    bank = json.loads((ROOT / "questions" / "question_bank.json").read_text())
    focus = [q for q in bank["questions"] if q["exam"] in FOCUS_EXAMS]
    out_dir = ROOT / "pdfs" / "focus_2022_2026"
    out_dir.mkdir(parents=True, exist_ok=True)

    arts = Path("/opt/cursor/artifacts/dm-oncology-exam-notes")
    arts.mkdir(parents=True, exist_ok=True)
    focus_arts = arts / "focus_2022_2026"
    if focus_arts.exists():
        shutil.rmtree(focus_arts)
    focus_arts.mkdir(parents=True)

    manifest = []
    for i, q in enumerate(focus, 1):
        meta = deepen(q)
        sections = compose_answer(meta)
        # Extra focus pack NCCN reminder page content already in compose
        fname = f"{q['id']}_{q['slug'][:55]}.pdf"
        path = out_dir / fname
        build_pdf(
            path,
            {
                "title": meta["question"][:80],
                "question": meta["question"],
                "exam": meta["exam"],
                "code": meta["code"],
                "number": meta["number"],
                "type": "Essay / Elaborate (FOCUS 2022–2026)"
                if meta["type"] == "essay"
                else "Short note (FOCUS 2022–2026)",
                "marks": meta["marks"],
                "target_pages": meta["target_pages"],
            },
            sections,
        )
        shutil.copy(path, focus_arts / fname)
        manifest.append({"id": q["id"], "exam": q["exam"], "marks": q["marks"], "file": fname, "question": q["question"]})
        if i % 10 == 0 or i == len(focus):
            print(f"Focus {i}/{len(focus)}: {q['id']}")

    (out_dir / "manifest.json").write_text(json.dumps({"count": len(manifest), "items": manifest}, indent=2))
    # zip
    zip_base = arts / "DM_Oncology_Focus_2022_2026"
    shutil.make_archive(str(zip_base), "zip", root_dir=out_dir)
    print(f"Focus pack: {len(manifest)} PDFs -> {zip_base}.zip")


if __name__ == "__main__":
    main()

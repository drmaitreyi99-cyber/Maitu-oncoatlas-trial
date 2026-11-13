#!/usr/bin/env python3
"""Append OCR-recovered 2001–2008 papers into the question bank and regenerate IDs."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EARLY = [
    {
        "exam": "April 2001",
        "code": "KD 020",
        "marks_essay": 25,
        "marks_short": 10,
        "essays": [
            "Discuss the role of biological response modifiers in management of cancer.",
            "Discuss the various aspects of high dose chemotherapy in cancer.",
        ],
        "shorts": [
            "Topoisomerase inhibitors",
            "Hyperthermia",
            "Late effects of cancer chemotherapy",
            "All-trans retinoic acid (ATRA)",
            "Gene therapy",
        ],
    },
    {
        "exam": "November 2001",
        "code": "KE 020",
        "marks_essay": 25,
        "marks_short": 10,
        "essays": [
            "Discuss critically the role of chemotherapy in the treatment of anal canal cancer.",
            "Discuss management of standard prognosis AML.",
        ],
        "shorts": [
            "STI-571 (Tyrosine kinase inhibitor)",
            "Gene therapy in gliomas",
            "Thalidomide",
            "Hormone replacement therapy",
            "Antibody targeted therapy in non-Hodgkin’s lymphoma",
        ],
    },
    {
        "exam": "March 2002",
        "code": "KG 020",
        "marks_essay": 25,
        "marks_short": 10,
        "essays": [
            "Discuss outpatient management of febrile neutropenia following cancer chemotherapy.",
            "Discuss critically the role of concurrent chemoradiotherapy in head and neck cancer.",
        ],
        "shorts": [
            "Arsenic trioxide",
            "Mycophenolate mofetil (MMF)",
            "Advances in the chemotherapy of pancreatic cancer",
            "Mixed chimerism in marrow transplants",
            "Multiagent antifolate in non-small cell lung cancer",
        ],
    },
    {
        "exam": "April 2004",
        "code": "KK 020",
        "marks_essay": 15,
        "marks_short": 5,
        "essays": [
            "Describe briefly the hierarchy of haemopoiesis. How do stem cells play a part in tissue repair?",
            "Discuss critically the role of concurrent chemoradiotherapy in the management of anal canal cancer.",
        ],
        "shorts": [
            "Target based therapy for head and neck cancer",
            "Immunotherapy for the treatment of malignant gliomas",
            "Role of monoclonal antibodies in lymphomas",
            "Bortezomib",
            "Stem cell transplantation in childhood ALL",
            "Flow cytometry",
            "Treatment of secondary leukemia",
            "Chemotherapy for medulloblastoma",
            "Hormone therapy for metastatic breast cancer",
            "Gene therapy for malignant melanoma",
        ],
    },
    {
        "exam": "August 2004",
        "code": "KL 020",
        "marks_essay": 15,
        "marks_short": 5,
        "essays": [
            "Describe critically the management of a 30-year-old male recently diagnosed with chronic phase chronic myeloid leukemia.",
            "Discuss critically the role of neoadjuvant chemotherapy in the management of locally advanced breast cancer.",
        ],
        "shorts": [
            "Monoclonal antibodies in the treatment of leukemias",
            "Mycophenolate mofetil",
            "Treatment of metastatic neuroblastoma",
            "Large cell anaplastic lymphoma",
            "Guidelines for the treatment of relapsed ovarian cancer",
            "Role of chemotherapy for extremity soft tissue sarcomas among adults",
            "Rituximab",
            "Treatment of metastatic choriocarcinoma",
            "Genetics of retinoblastoma",
            "Role of adjuvant chemotherapy for gastric cancer",
        ],
    },
    {
        "exam": "February 2005",
        "code": "KM 020",
        "marks_essay": 15,
        "marks_short": 5,
        "essays": [
            "Discuss the role of autologous stem cell transplantation in present practice of oncology.",
            "Discuss the role and recent trends of targeted therapy.",
        ],
        "shorts": [
            "Cancer vaccines",
            "Chemoprevention",
            "Role of laparoscopy in diagnosis and treatment of cancer",
            "Chemotherapy of prostate cancer",
            "Bisphosphonates",
            "Meta-analysis",
            "Aromatase inhibitors",
            "Epidemiology of cancer in India",
            "Role of erythropoietin in cancer anaemia",
            "Cancer in the immunosuppressed",
        ],
    },
    {
        "exam": "February 2006",
        "code": "KO 020",
        "marks_essay": 15,
        "marks_short": 5,
        "essays": [
            "Describe critically the management of Hodgkin’s disease which relapsed after standard ABVD.",
            "Discuss the neoadjuvant treatment of cancer of rectum.",
        ],
        "shorts": [
            "Hormonal treatment of breast cancer in premenopausal female",
            "Angiogenesis inhibitors",
            "Cytoprotection during chemotherapy",
            "Chemoprevention of cancer",
            "Chemotherapy for mesothelioma",
            "Imatinib mesylate",
            "Treatment of gastric lymphoma",
            "Immunohistochemistry for small round cell tumors",
            "Radioimmunopharmaceuticals in hematologic malignancies",
            "Somatostatin",
        ],
    },
    {
        "exam": "September 2006",
        "code": "KP 020",
        "marks_essay": 15,
        "marks_short": 5,
        "essays": [
            "Critically evaluate the role of sentinel lymph node biopsy, along with the various techniques used, in the management of tumours at different sites.",
            "Discuss the etiopathogenesis of deep vein thrombosis in cancer. Suggest an investigative work-up and outline a management approach.",
            "Discuss neoplastic angiogenesis and antiangiogenesis therapy.",
        ],
        "shorts": [
            "Chemoradiotherapy in the management of carcinoma of the anal canal",
            "Management of metastatic endometrial stromal sarcoma",
            "Cyclooxygenase-2 (COX-2) inhibitors in prevention of cancer",
            "Temozolomide for metastatic brain tumours",
            "Magnetic resonance spectroscopy",
            "Suicide gene therapy",
        ],
    },
    {
        "exam": "February 2007",
        "code": "KQ 020",
        "marks_essay": 15,
        "marks_short": 5,
        "essays": [
            "Critically evaluate breast conservative surgery versus radical surgery in the management of breast cancer.",
            "Discuss immuno-surveillance mechanisms and the different immunotherapeutic strategies.",
            "Discuss the plasma cell–stromal interactions in multiple myeloma and various therapeutic strategies in the treatment of myeloma.",
        ],
        "shorts": [
            "Chemoradiotherapy in the management of carcinoma of cervix",
            "Metastatic renal cell carcinoma",
            "Prevention of oral cancer",
            "Dendritic cell vaccines",
            "Carcinomatous meningitis",
            "LASER in the management of cancer of the upper aerodigestive tract",
        ],
    },
    {
        "exam": "August 2007",
        "code": "KR 020",
        "marks_essay": 15,
        "marks_short": 5,
        "essays": [
            "Discuss the phases of clinical trials in cancer. Enumerate the pros and cons of using Indian patients in multinational clinical trials.",
            "Discuss the role of antifungal drugs in the management of febrile neutropenia in the remission induction therapy of acute leukemias.",
            "‘Cancer is a multistep process’ – Explain with the example of head and neck cancer. What could be possible interventions at each step?",
        ],
        "shorts": [
            "Microarrays in breast cancer",
            "Immunoconjugates for cancer therapy",
            "Compare and contrast 5-Fluorouracil and Capecitabine",
            "Compare and contrast liposomal and non-liposomal doxorubicin",
            "Post-transfusion graft versus host disease",
            "Pulmonary blastoma",
        ],
    },
    {
        "exam": "February 2008",
        "code": "KS 020",
        "marks_essay": 20,
        "marks_short": 6,
        "essays": [
            "Discuss the pathophysiology of pain and the advances in the management of acute pain in subjects with cancer.",
            "Discuss the status of geriatric assessment in the elderly and briefly elaborate on the treatment of older subjects with colorectal cancer.",
        ],
        "shorts": [
            "Extreme drug resistance assay",
            "Vulnerable population in clinical research",
            "Bexarotene",
            "Transfusion related acute lung injury (TRALI)",
            "Molecular imaging",
            "Prognostic factors in myelodysplastic syndrome",
            "Differentiating agents",
            "Bortezomib",
            "Preventable cancer",
            "Neuroendocrine tumours",
        ],
    },
]


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:80]


def build_questions(papers, start_id=1):
    qs = []
    qid = start_id
    for paper in papers:
        for i, q in enumerate(paper["essays"], 1):
            marks = paper["marks_essay"]
            qs.append(
                {
                    "id": f"Q{qid:03d}",
                    "exam": paper["exam"],
                    "code": paper["code"],
                    "type": "essay",
                    "number": i,
                    "marks": marks,
                    "target_pages": 15 if marks >= 15 else 12,
                    "question": q,
                    "slug": slugify(f"{paper['exam']}-essay-{i}-{q}"),
                    "era": "early" if paper.get("era") == "early" or True else "modern",
                }
            )
            qid += 1
        for i, q in enumerate(paper["shorts"], 1):
            marks = paper["marks_short"]
            qs.append(
                {
                    "id": f"Q{qid:03d}",
                    "exam": paper["exam"],
                    "code": paper["code"],
                    "type": "short",
                    "number": i,
                    "marks": marks,
                    "target_pages": 11 if marks >= 7 else 10,
                    "question": q,
                    "slug": slugify(f"{paper['exam']}-short-{i}-{q}"),
                }
            )
            qid += 1
    return qs, qid


def main():
    # Load existing modern bank from parse_questions module by re-running logic
    import sys

    sys.path.insert(0, str(ROOT / "scripts"))
    from parse_questions import PAPERS, build_bank

    modern = build_bank()
    # rebuild early with E prefix then renumber all chronologically
    for p in EARLY:
        p["era"] = "early"

    early_qs, _ = build_questions(EARLY, start_id=1)
    # Renumber: early first then modern
    all_qs = []
    qid = 1
    for q in early_qs + modern:
        q = dict(q)
        q["id"] = f"Q{qid:03d}"
        all_qs.append(q)
        qid += 1

    out = ROOT / "questions" / "question_bank.json"
    payload = {
        "count": len(all_qs),
        "early_count": len(early_qs),
        "modern_count": len(modern),
        "questions": all_qs,
    }
    out.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {len(all_qs)} questions (early {len(early_qs)} + modern {len(modern)}) -> {out}")

    # also save early OCR source note
    (ROOT / "questions" / "early_ocr_recovered.json").write_text(json.dumps(EARLY, indent=2))


if __name__ == "__main__":
    main()

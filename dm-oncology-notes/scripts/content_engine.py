#!/usr/bin/env python3
"""Compose exam-style multi-section answers for each DM Oncology question."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "content"))
sys.path.insert(0, str(ROOT / "scripts"))

from nccn_2026_updates import get_nccn_block  # noqa: E402
from trials_doses import DOSES, HALLMARKS, LANDMARK_TRIALS  # noqa: E402
from topic_modules import modules_for  # noqa: E402


def _match(q: str, *patterns: str) -> bool:
    return any(re.search(p, q, re.I) for p in patterns)


def _pick_trials(q: str) -> list[tuple[str, str]]:
    qlow = q.lower()
    out: list[tuple[str, str]] = []
    mapping = [
        (r"her2|breast|trastuzumab|emilia|destiny|pertuzumab|tnbc", "HER2 breast"),
        (r"egfr|osimertinib|nsclc|lung|amivantamab|dato", "EGFR NSCLC"),
        (r"colon|colorectal|rectal|msi|mmr|atomic", "CRC"),
        (r"\bcml\b|imatinib|asciminib|tki", "CML"),
        (r"\baml\b|flt3|venetoclax|npm1|apml|apl", "AML"),
        (r"\bcll\b|btk|pirtobrutinib", "CLL"),
        (r"myeloma|teclistamab|bcma|daratumumab|proteasome", "Myeloma"),
        (r"melanoma|relatlimab", "Melanoma"),
        (r"renal|rcc|cabozantinib|vegf", "RCC"),
        (r"bladder|urothelial|enfortumab|bcg", "Bladder"),
        (r"gastric|flot|claudin|esophageal", "Gastric"),
        (r"ovarian|parp|olaparib|hipec|mirvetuximab", "Ovarian"),
        (r"prostate|abiraterone|psma|nm.?crpc", "Prostate"),
        (r"car.?t|bite|blinatumomab|icans|adoptive", "CAR-T / cellular"),
        (r"parp|olaparib|talazoparib", "PARP general"),
    ]
    for pat, key in mapping:
        if re.search(pat, qlow):
            for row in LANDMARK_TRIALS.get(key, []):
                if row not in out:
                    out.append(row)
    if not out:
        # general immuno-oncology + targeted sampling
        for key in ("HER2 breast", "EGFR NSCLC", "CRC", "CAR-T / cellular"):
            out.extend(LANDMARK_TRIALS[key][:2])
    return out[:12]


def _pick_doses(q: str) -> list[tuple[str, str]]:
    keys = list(DOSES.keys())
    qlow = q.lower()
    selected = []
    for k in keys:
        token = k.split()[0].lower().replace("-", "")
        if token[:5] in qlow.replace("-", "") or k.lower() in qlow:
            selected.append((k, DOSES[k]))
    # Always add a few high-yield related doses by topic
    extras = []
    if _match(qlow, r"her2|breast"):
        extras = ["Trastuzumab", "Pertuzumab", "T-DXd", "T-DM1", "Olaparib"]
    elif _match(qlow, r"egfr|lung|nsclc|osimertinib"):
        extras = ["Osimertinib", "Amivantamab", "Pembrolizumab", "Carboplatin AUC"]
    elif _match(qlow, r"myeloma"):
        extras = ["Bortezomib", "Lenalidomide", "Daratumumab", "Venetoclax (AML)"]
    elif _match(qlow, r"\bcml\b|imatinib"):
        extras = ["Imatinib", "Dasatinib", "Nilotinib", "Ponatinib", "Asciminib"]
    elif _match(qlow, r"\baml\b|venetoclax"):
        extras = ["Venetoclax (AML)", "Azacitidine note" if False else "Venetoclax (CLL)"]
    elif _match(qlow, r"gastric|flot|colon|rectal"):
        extras = ["FLOT", "FOLFOX", "CAPOX", "Pembrolizumab", "Nivolumab"]
    elif _match(qlow, r"bladder|enfortumab"):
        extras = ["Enfortumab vedotin", "Pembrolizumab"]
    elif _match(qlow, r"prostate"):
        extras = ["Abiraterone", "Enzalutamide", "Docetaxel"]
    elif _match(qlow, r"parp|olaparib"):
        extras = ["Olaparib", "Niraparib"]
    elif _match(qlow, r"checkpoint|immuno|pd.?1|nivolumab|pembrolizumab"):
        extras = ["Pembrolizumab", "Nivolumab"]
    for e in extras:
        if e in DOSES and (e, DOSES[e]) not in selected:
            selected.append((e, DOSES[e]))
    if len(selected) < 4:
        for e in ["Pembrolizumab", "Nivolumab", "Olaparib", "Trastuzumab"]:
            if (e, DOSES[e]) not in selected:
                selected.append((e, DOSES[e]))
    return selected[:10]


def intro_section(q: str, marks: int) -> dict:
    return {
        "heading": "1. Introduction & exam framing",
        "level": 1,
        "paragraphs": [
            f"This answer addresses: <b>{q}</b>",
            f"For a <b>{marks}-mark</b> university answer, structure the response as: definition/epidemiology → "
            "biology/hallmarks → diagnosis & biomarkers → staging/risk → management algorithm with doses → "
            "key clinical trials with endpoints → toxicities/supportive care → <b>NCCN 2026 updates</b> → "
            "Indian/NCG context → summary table. Draw at least one flowchart and one mechanism diagram.",
            "Marking examiners reward: accurate mechanisms, named trials with phase and primary endpoint, "
            "practical doses, Category evidence (NCCN/ESMO), and a clear final recommended pathway.",
        ],
        "bullets": [
            "Start with a one-line definition + why the topic is ‘recent advances’ relevant.",
            "Always state predictive vs prognostic biomarkers.",
            "Quote Category 1 preferred regimens from NCCN 2026/2027 when applicable.",
            "End with 5 high-yield exam pearls.",
        ],
    }


def biology_section(q: str) -> dict:
    paragraphs = [
        "Cancer biology for this topic should be linked to Hanahan–Weinberg hallmarks (sustained proliferation, "
        "evading growth suppressors, resisting cell death, enabling replicative immortality, induction of angiogenesis, "
        "activating invasion/metastasis, avoiding immune destruction, deregulating cellular energetics, genome instability, "
        "tumor-promoting inflammation).",
        "Where a driver oncogene/fusion/epigenetic lesion is known, explain the pathway from ligand/receptor → "
        "intracellular kinase cascade → transcription → phenotype, and mark the drug target with an arrow in your diagram.",
    ]
    mechanism = [
        ("Driver / target", "State oncogene, fusion, receptor, or immune checkpoint involved"),
        ("Pathway", "MAPK / PI3K-AKT-mTOR / JAK-STAT / DDR / BCR signaling / angiogenesis"),
        ("Hallmark effect", "Proliferation, survival, angiogenesis, immune escape, or DNA repair addiction"),
        ("Drug class", "mAb / TKI / ADC / BiTE / CAR-T / CPI / PARPi / IMiD / BH3 mimetic"),
        ("Resistance", "Secondary mutation, bypass track, phenotypic switch, antigen loss, TME suppression"),
    ]
    if _match(q, r"her2|breast"):
        paragraphs.append(
            "HER2 (ERBB2) is a ligand-independent receptor tyrosine kinase; amplification → homodimers/heterodimers "
            "(HER2-HER3) → PI3K-AKT and MAPK. Dual blockade (trastuzumab+pertuzumab) covers subdomain IV and dimerization domain II. "
            "ADCs (T-DM1, T-DXd) deliver cytotoxic payloads; T-DXd has a cleavable linker and membrane-permeable topoisomerase-I payload → bystander effect (HER2-low activity)."
        )
        mechanism = [
            ("HER2 amplification", "IHC 3+ or ISH amplified — ASCO/CAP"),
            ("Trastuzumab", "ADCC + subdomain IV binding"),
            ("Pertuzumab", "Inhibits HER2-HER3 dimerization"),
            ("T-DXd", "Topo-I ADC; bystander kill; ILD risk"),
            ("Resistance", "PIK3CA, PTEN loss, incomplete internalization, CNS sanctuary"),
        ]
    elif _match(q, r"egfr|osimertinib|nsclc"):
        paragraphs.append(
            "EGFR activating mutations (exon 19 del, L858R) → constitutive kinase signaling. "
            "T790M mediates 1st/2nd-gen TKI resistance; osimertinib covers T790M and has CNS penetration. "
            "MET amplification, C797X, histologic transformation (SCLC), and EGFR-independent bypass are common resistance maps after osimertinib."
        )
        mechanism = [
            ("EGFR mut+", "ex19del / L858R / uncommon / ex20ins"),
            ("3rd-gen TKI", "Osimertinib covalent Cys797"),
            ("Bispecific", "Amivantamab: EGFR+MET domains"),
            ("ADC post-TKI", "Dato-DXd (TROP2) — NCCN 2026 preferred post osi+chemo"),
            ("Resistance", "MET amp, C797S, SCLC transformation"),
        ]
    elif _match(q, r"parp|mmr|hrd|olaparib"):
        paragraphs.append(
            "Synthetic lethality: PARP inhibitors trap PARP on DNA and block base-excision/single-strand repair; "
            "in BRCA/HRD cells, double-strand break repair fails → cell death. MMR deficiency → MSI-H → high neoantigen load → CPI sensitivity."
        )
    elif _match(q, r"car.?t|bite|adoptive|blinatumomab"):
        paragraphs.append(
            "Adoptive cellular therapy redirects immunity: CAR-T grafts an antigen binder + signaling domains (CD3ζ ± 4-1BB/CD28) onto T cells; "
            "BiTEs are off-the-shelf engagers linking CD3 to tumor antigen (CD19/BCMA/GPRC5D). Toxicities CRS/ICANS are on-target immune activation."
        )
    return {
        "heading": "2. Pathobiology, hallmarks & mechanism",
        "level": 1,
        "paragraphs": paragraphs,
        "mechanism": mechanism,
        "pearls": [
            HALLMARKS.get("HER2 testing", "State ASCO/CAP criteria when discussing HER2."),
            "Draw the pathway once; label drug targets — examiners love this.",
            "Always mention one primary resistance mechanism.",
        ],
    }


def diagnosis_section(q: str) -> dict:
    bullets = [
        "Tissue diagnosis with adequate IHC panel; never treat metastatic disease without molecular profiling when actionable targets exist.",
        "Use validated assays (FDA/companion diagnostics where mandated).",
        "Stage with AJCC 8th/9th as applicable (NSCLC NCCN 2026 uses AJCC 9th).",
        "Performance status, organ function, comorbidities, geriatric assessment, and goals of care before regimen selection.",
    ]
    flowchart = [
        "Clinical suspicion / screening abnormality",
        "Biopsy + histopathology + IHC",
        "Molecular profiling (NGS / PCR / ISH) + staging imaging (CT/PET/MRI as indicated)",
        "MDT discussion → risk / stage / biomarker stratified plan",
        "Treatment + response assessment (RECIST / Lugano / IMWG / ELN)",
    ]
    if _match(q, r"her2|breast"):
        bullets.extend([
            "ER/PR/HER2 mandatory; HER2-low reporting now clinically actionable (DESTINY-Breast04/06).",
            "gBRCA testing for therapy (olaparib/talazoparib; OlympiA adjuvant).",
            "ESR1 mutation testing at endocrine resistance — imlunestrant listed in NCCN 2026 updates.",
        ])
    if _match(q, r"lung|nsclc"):
        bullets.extend([
            "Broad NGS preferred: EGFR, ALK, ROS1, BRAF, MET ex14, RET, NTRK, KRAS, ERBB2, NRG1.",
            "PD-L1 TPS for immunotherapy decisions in driver-negative disease.",
        ])
    if _match(q, r"mmr|msi|colon|rectal|immunotherapy"):
        bullets.append("Universal MMR IHC / MSI testing in CRC; guides CPI and ATOMIC adjuvant pathway.")
    return {
        "heading": "3. Diagnosis, biomarkers & staging",
        "level": 1,
        "paragraphs": [
            "A modern oncology answer must separate <b>diagnostic</b>, <b>prognostic</b>, and <b>predictive</b> markers. "
            "Predictive markers change drug choice (EGFR, HER2, BRCA, MSI, Claudin18.2, FGFR, NTRK)."
        ],
        "bullets": bullets,
        "flowchart": flowchart,
        "flowchart_title": "Work-up algorithm (draw this in the answer booklet)",
    }


def management_section(q: str, marks: int) -> dict:
    paragraphs = [
        "Structure management as: (A) localized/curative-intent pathways, (B) advanced/metastatic systemic therapy, "
        "(C) special populations (CNS, elderly, organ dysfunction, pregnancy), (D) supportive care.",
        "For each line of therapy state: eligibility, preferred regimen, dose, key toxicity monitoring, and the trial that supports it.",
    ]
    bullets = [
        "Localized disease: multimodality — surgery/RT/systemic as per disease chapter.",
        "Neoadjuvant vs adjuvant: cite pathologic response and adjuvant switch trials (e.g., KATHERINE, CheckMate 577, KEYNOTE-522).",
        "Metastatic: biomarker-first; avoid empiric chemo when a high-level targeted/IO option exists.",
        "Oligometastatic disease: consider metastasis-directed therapy where NCCN supports (e.g., prostate APMS 2026).",
        "Re-biopsy / liquid biopsy at progression to map resistance.",
    ]
    flowchart = [
        "Confirm stage + biomarkers + fitness",
        "MDT: curative vs palliative intent",
        "Preferred 1L (NCCN Cat 1 / ESMO-MCBS high)",
        "Assess response (interval imaging + markers)",
        "Progression → molecular reassessment → 2L preferred",
        "Best supportive care / trials / palliative integration",
    ]
    if _match(q, r"her2|breast"):
        bullets.extend([
            "Early HER2+: dual blockade neoadjuvant if tumor >2 cm or node+; adjuvant HP; T-DM1 if residual disease (KATHERINE).",
            "1L mBC HER2+: taxane + trastuzumab + pertuzumab (CLEOPATRA).",
            "2L: T-DXd preferred (DESTINY-Breast03) over T-DM1.",
            "HER2+ brain mets: tucatinib triplet (HER2CLIMB); SRS/WBRT as indicated.",
        ])
        flowchart = [
            "HER2 testing (IHC±ISH) + stage",
            "Early: NAT HP+chemo → surgery → adjuvant HP or T-DM1 if RD",
            "Metastatic 1L: taxane+H+P",
            "2L: T-DXd (DB-03)",
            "Later: tucatinib regimen / lapatinib / neratinib / chemo-backbone",
            "gBRCA: add PARPi considerations per setting",
        ]
    if _match(q, r"egfr|osimertinib"):
        bullets.extend([
            "1L EGFR ex19del/L858R: osimertinib; OR osi+chemo (FLAURA2); OR amivantamab+lazertinib (MARIPOSA) — both combinations now NCCN Cat 1 preferred.",
            "After osi+chemo progression: Dato-DXd preferred (NCCN 2026).",
            "Adjuvant osi (ADAURA); post-CRT osi (LAURA) for unresectable stage III EGFR+.",
        ])
    if _match(q, r"\bcml\b"):
        bullets.extend([
            "Newly diagnosed CP-CML: imatinib or 2G TKI based on risk (ELTS), comorbidities, and TFR goals.",
            "Monitor q3mo BCR::ABL1 IS; milestones per ELN.",
            "Resistance: mutation analysis; ponatinib for T315I; asciminib STAMP inhibitor.",
            "TFR if MR4/MR4.5 sustained and monitored monthly initially.",
        ])
    if _match(q, r"car.?t|adoptive"):
        bullets.extend([
            "Indications: R/R LBCL, B-ALL, mantle, follicular (product-specific), myeloma BCMA CAR-T.",
            "Pathway: apheresis → manufacturing → lymphodepletion (Flu/Cy) → infusion → CRS/ICANS watch.",
            "Bridging therapy may be needed; manufacturing failure contingency.",
        ])
    return {
        "heading": "4. Management algorithm, doses & regimens",
        "level": 1,
        "paragraphs": paragraphs,
        "bullets": bullets,
        "flowchart": flowchart,
        "flowchart_title": "Management flowchart (reproduce in exam)",
        "table_doses": _pick_doses(q),
    }


def trials_section(q: str) -> dict:
    trials = _pick_trials(q)
    return {
        "heading": "5. Landmark clinical trials (must quote in answer)",
        "level": 1,
        "paragraphs": [
            "Present trials in a table: name → design/population → intervention → primary endpoint → absolute/relative benefit → practice change. "
            "Examiners award marks for correct trial names and one numeric result (HR or median PFS/OS).",
        ],
        "table_trials": trials,
        "bullets": [
            "Mention phase (III preferred for standards) and whether endpoint was PFS, OS, MRD, pCR, or EFS.",
            "Distinguish statistical vs clinical significance; note crossover and subgroup caveats.",
            "For India-focused answers, mention access/biosimilars/NCG guidance after the trial table.",
        ],
    }


def toxicity_section(q: str) -> dict:
    bullets = [
        "Anticipate class toxicities and counsel patients; use CTCAE grading.",
        "Cardio-oncology: anthracyclines, HER2 mAbs, ibrutinib, checkpoint myocarditis — baseline ECG/echo when indicated.",
        "IO toxicities: irAEs — hold drug, steroids, specialty referral; endocrine irAEs often permanent replacement.",
        "ADC pulmonary toxicity (T-DXd ILD): hold permanently for ≥grade 2 in many protocols; imaging + steroids.",
        "TLS prophylaxis for venetoclax/BLIN/CAR-T; rasburicase if high-risk.",
        "Fertility, sexuality, survivorship, and psychosocial support are part of comprehensive answers.",
    ]
    if _match(q, r"car.?t|bite|icans|blinatumomab"):
        bullets.extend([
            "CRS: tocilizumab ± dexamethasone; ICU for grade ≥3.",
            "ICANS: ICE score q shift; dexamethasone; seizure prophylaxis in high-risk protocols; neuroimaging/EEG PRN.",
            "Prolonged cytopenias, hypogammaglobulinemia (IVIG), infections — PJP/VZV prophylaxis per center.",
        ])
    if _match(q, r"checkpoint|immuno|pd.?1|ctla"):
        bullets.append("Algorithm: grade 1 → continue with close watch; grade 2 → hold + steroids; grade 3–4 → discontinue permanently for many toxicities + high-dose steroids ± infliximab/vedolizumab/MMF.")
    return {
        "heading": "6. Toxicities, supportive care & monitoring",
        "level": 1,
        "paragraphs": [
            "A complete answer links efficacy to safety. List monitoring schedules (CBC, chemistry, ECG, TFTs, cortisol, LFTs, PFTs/CT for ILD risk drugs)."
        ],
        "bullets": bullets,
        "flowchart": [
            "Start therapy + baseline organ assessment",
            "Scheduled labs / imaging / patient-reported toxicity",
            "Grade toxicity (CTCAE)",
            "Hold / dose-reduce / discontinue + specific antidote (tocilizumab, steroids, growth factors)",
            "Rechallenge only if benefit ≫ risk and protocol allows",
        ],
        "flowchart_title": "Toxicity management loop",
    }


def nccn_section(q: str) -> dict:
    block = get_nccn_block(q)
    return {
        "heading": "7. NCCN 2026 / 2027 updates (high-yield for ‘recent advances’)",
        "level": 1,
        "paragraphs": [
            "Paper IV rewards currency. Explicitly write: <b>“As per NCCN Guidelines updates in 2026/2027…”</b> "
            "and list 3–5 bullets. Also mention ESMO guidelines / Indian NCG where relevant for balance.",
        ],
        "nccn": block,
        "bullets": [
            "State Category (1 / 2A / 2B) and preferred vs other recommended vs useful in certain circumstances.",
            "If Indian exam: reconcile NCCN with CDSCO approvals and NCG practical pathways.",
        ],
        "pearls": [
            "NCCN versions change frequently — cite year/version (e.g., NSCLC v9.2026, Breast v9.2026, Myeloma v2.2027).",
            "Category 1 = high-level evidence + uniform NCCN consensus.",
        ],
    }


def special_topics_section(q: str) -> dict:
    """Extra depth sections that expand page count with authentic content."""
    paragraphs = []
    bullets = []
    if _match(q, r"breast|her2|tnbc"):
        paragraphs.append(
            "Intrinsic subtypes (luminal A/B, HER2-enriched, basal-like) from PAM50 approximate IHC surrogates but are not identical. "
            "TNBC biology includes DNA repair defects, AR-positive luminal androgen receptor subset, and immune-rich tumors benefiting from CPI (KEYNOTE-522; KEYNOTE-355 CPS≥10)."
        )
        bullets.extend([
            "Neoadjuvant pCR is a strong surrogate in HER2+ and TNBC for escalation/de-escalation.",
            "Antibody-drug conjugates reshaped sequencing: T-DXd before many older anti-HER2 TKIs in metastatic HER2+.",
            "Pregnancy-associated breast cancer: tailor imaging (no gadolinium/PET routine), surgery, anthracycline after first trimester; anti-HER2 contraindicated in pregnancy.",
        ])
    if _match(q, r"lung|nsclc|egfr|alk"):
        paragraphs.append(
            "Stage III unresectable: concurrent CRT then consolidative durvalumab (PACIFIC) if no driver contraindication; "
            "EGFR+ unresectable III → osimertinib (LAURA). Perioperative IO (CheckMate 816, KEYNOTE-671, AEGEAN) changed early NSCLC."
        )
        bullets.extend([
            "Never smoke ≠ no drivers; test all nonsquamous and consider squamous with clinical features.",
            "CNS staging MRI important before TKI selection; prefer CNS-active agents.",
        ])
    if _match(q, r"myeloma|amyloid"):
        paragraphs.append(
            "IMWG diagnostic criteria: ≥10% clonal BMPCs or biopsy-proven plasmacytoma PLUS myeloma-defining event (CRAB or SLiM: ≥60% PCs, FLC ratio ≥100, >1 focal lesion ≥5 mm on MRI)."
        )
        bullets.extend([
            "Response: sCR/CR/VGPR/PR/MR/SD/PD + MRD (NGF/NGS 10^-5).",
            "Quadruplets + ASCT + maintenance remain backbone for fit NDMM; bispecifics/CAR-T dominate mid/late relapse — see NCCN 2026 Tec-Dara.",
        ])
    if _match(q, r"aml|mds|leukemia"):
        paragraphs.append(
            "ELN 2022 risk (favorable/intermediate/adverse) integrates cytogenetics and mutations (NPM1, FLT3-ITD allelic ratio historically, TP53, MECOM, complex karyotype, etc.). "
            "WHO 2022 / ICC classifications emphasize genetically defined entities."
        )
    if _match(q, r"transplant|gvhd|haplo|engraftment"):
        paragraphs.append(
            "Allogeneic HCT platform: donor (MSD/MUD/haplo), conditioning (MAC vs RIC), GVHD prophylaxis (CNI+MTX; PTCy-based haplo). "
            "Graft-versus-tumor effect underpins cure in leukemias; balanced against GVHD."
        )
        bullets.extend([
            "PTCy haplo expanded donor access globally including India.",
            "Vaccinations post-HCT per CDC/EBMT schedules — delayed live vaccines.",
        ])
    if not paragraphs:
        paragraphs = [
            "Discuss differentials, mimics, and when to refer to radiation oncology, surgery, palliative care, genetics, or cell-therapy centers.",
            "Include brief notes on health economics (cost-effectiveness, biosimilars) and clinical trial enrollment as standard options.",
        ]
        bullets = [
            "MDT documentation improves outcomes and exam completeness.",
            "Survivorship care plans: late effects, second malignancies, cardiac, endocrine, psychosocial.",
            "Real-world evidence and digital tools increasingly complement RCT data (relevant to 2026 Paper IV themes).",
        ]
    return {
        "heading": "8. Special situations, differentials & practical issues",
        "level": 1,
        "paragraphs": paragraphs,
        "bullets": bullets,
    }


def evidence_rights_benefits_section(q: str) -> dict:
    return {
        "heading": "9. Evidence hierarchy, patient rights & benefits",
        "level": 1,
        "paragraphs": [
            "Quote evidence using: Phase III RCT > meta-analysis of RCTs > prospective registries / RWE > retrospective > expert consensus. "
            "NCCN Categories and ESMO-MCBS scores help communicate strength of benefit.",
            "Patient-centered care: informed consent for toxicities (especially CRS/ICANS, ILD, infertility), shared decision-making, "
            "financial toxicity counseling, and access to supportive/palliative care concurrent with active therapy.",
        ],
        "bullets": [
            "Benefits to highlight: OS, PFS, pCR, MRD negativity, organ preservation, QoL, reduced hospitalization.",
            "Rights: autonomy, confidentiality (EMR), right to second opinion, trial participation, refusal of care, end-of-life preferences.",
            "Equity: molecular testing access, biosimilars, NCG/Ayushman Bharat practical pathways for Indian exams.",
            "Pharmacovigilance: report ADRs; Phase IV / post-marketing commitments.",
        ],
        "pearls": [
            "Write one sentence on absolute benefit (e.g., ‘median OS improved from X to Y months’).)",
            "Mention number-needed-to-treat conceptually if space permits.",
        ],
    }


def summary_section(q: str, marks: int) -> dict:
    return {
        "heading": "10. Summary checklist (write this last page in the booklet)",
        "level": 1,
        "paragraphs": [
            f"Close the {marks}-mark answer with a crisp numbered summary the examiner can tick.",
        ],
        "bullets": [
            "Definition + epidemiology one-liner",
            "Key biology / hallmark diagram",
            "Essential diagnostics & biomarkers",
            "Risk/stage stratification",
            "Preferred treatment algorithm with ≥2 doses",
            "≥3 named trials with endpoints",
            "Major toxicities + monitoring",
            "NCCN 2026 update bullets (3–5)",
            "Special situations",
            "Five exam pearls",
        ],
        "flowchart": [
            "Remember biology",
            "Test biomarkers",
            "Choose NCCN-preferred regimen",
            "Monitor toxicity & response",
            "Sequence next line using trials + NCCN 2026",
        ],
        "flowchart_title": "30-second revision flowchart",
        "pearls": [
            "Neat flowchart + trial table often separates a 10/15 from a 13–15/15.",
            "Do not dump drug lists without doses or evidence.",
            "Currency: say ‘NCCN 2026’ explicitly for Paper IV.",
        ],
    }


def expand_pages(sections: list[dict], target_pages: int, q: str) -> list[dict]:
    """Add additional depth sections so PDFs approach requested page counts."""
    extra = []
    # Deep dive pharmacology
    extra.append({
        "heading": "11. Pharmacology deep-dive (class, PK/PD, interactions)",
        "level": 1,
        "paragraphs": [
            "For drug-centered questions, present: chemical/biologic class → target epitope/kinase → PK (oral bioavailability, half-life, hepatic/renal clearance) → "
            "food effects → CYP interactions → dose adjustments → therapeutic drug monitoring if any.",
            "Example interaction pearls: acid-suppressive therapy with some TKIs; QT-prolonging combinations; azole antifungals with vinca/TKIs; "
            "strong CYP3A inducers reducing exposure to many oral targeted agents.",
        ],
        "bullets": [
            "State renal/hepatic dose modifications when known.",
            "Note formulation differences (olaparib tablets vs capsules; IV vs SC daratumumab).",
            "Infusion reactions: premedication protocols for mAbs/BiTEs.",
        ],
        "table_doses": _pick_doses(q)[:6],
    })
    extra.append({
        "heading": "12. Response assessment & follow-up schedules",
        "level": 1,
        "paragraphs": [
            "Use disease-specific criteria: RECIST 1.1 solid tumors; iRECIST for immunotherapy; Lugano/Deauville for lymphoma; "
            "IMWG for myeloma; ELN molecular response for CML/AML; PSA working group for prostate.",
        ],
        "bullets": [
            "Typical imaging interval q2–3 cycles in metastatic disease unless clinically indicated sooner.",
            "PET-adapted strategies in Hodgkin lymphoma (RATHL, AHL2011) — cite Deauville 1–3 negative vs 4–5 positive.",
            "ctDNA MRD emerging for escalation/de-escalation (CRC, lymphoma, breast — exam discussion point).",
        ],
        "flowchart": [
            "Baseline measurable disease",
            "On-treatment assessment",
            "CR / PR / SD / PD (or molecular response)",
            "Continue / escalate / switch / stop + surveillance",
        ],
    })
    if target_pages >= 12:
        extra.append({
            "heading": "13. Comparison tables useful for exams",
            "level": 1,
            "paragraphs": [
                "Draw 2×N tables comparing old standard vs new standard; or drug A vs B (efficacy, toxicity, CNS activity, cost/access).",
            ],
            "table_trials": _pick_trials(q)[:6],
            "bullets": [
                "Column ideas: target, dose, PFS, OS, grade ≥3 AEs, CNS activity, NCCN category.",
                "Another table: resistance mutation → preferred next drug.",
            ],
        })
        extra.append({
            "heading": "14. Indian context, NCG & practical exam tips",
            "level": 1,
            "paragraphs": [
                "National Cancer Grid (NCG) resource-stratified guidelines are frequently expected in Indian DM exams. "
                "Discuss biosimilars (trastuzumab, rituximab), generic TKIs, and center-based cell therapy availability.",
            ],
            "bullets": [
                "Document MDT decisions; clinical trial referral when standard options exhausted.",
                "Counsel financial toxicity transparently; prioritize highest-value Category 1 options.",
                "Infection prophylaxis algorithms crucial in hematologic topics (antifungal, antiviral, PJP).",
            ],
        })
    if target_pages >= 14:
        extra.append({
            "heading": "15. Sample ‘examiner hot spots’ & model closing paragraph",
            "level": 1,
            "paragraphs": [
                f"Model closing: “In summary, management of this problem is biomarker-driven. Current standards are supported by phase III trials "
                f"and reflected in NCCN 2026/2027 updates. Sequencing should maximize OS and QoL while mitigating class-specific toxicities. "
                f"Enrollment in clinical trials and adherence to MDT pathways remain integral.”",
                "Hot spots: exact doses, one HR/median, resistance mechanism, NCCN category, and a drawn algorithm.",
            ],
            "pearls": [
                "If stuck on memory: write mechanism → class → one trial → one dose → one toxicity → NCCN 2026 line.",
                "Never contradict yourself between algorithm and trial table.",
            ],
        })
    # For shorter notes still add a quick revision strip
    if target_pages < 12:
        extra = extra[:2]
    return sections + extra


def compose_answer(meta: dict) -> list[dict]:
    q = meta["question"]
    marks = meta["marks"]
    target = meta.get("target_pages", 12)
    sections = [
        intro_section(q, marks),
        biology_section(q),
        diagnosis_section(q),
        management_section(q, marks),
        trials_section(q),
        toxicity_section(q),
        nccn_section(q),
        special_topics_section(q),
        evidence_rights_benefits_section(q),
        summary_section(q, marks),
    ]
    sections = expand_pages(sections, target, q)
    # Long-form topic modules to reach ~10–15 pages
    sections.extend(modules_for(q))
    # Extra prose pages for essay-length targets
    if target >= 14 or marks >= 15:
        sections.append({
            "heading": "I2. Full-length essay addendum — tables to copy into the answer book",
            "level": 1,
            "paragraphs": [
                "For 15-mark elaborations, add two hand-drawn tables: (Table A) Drug–dose–pearl; (Table B) Trial–population–endpoint–practice change. "
                "Then write a short paragraph on quality-of-life and patient-reported outcomes, which modern trials increasingly report.",
                "Discuss biomarker evolution on therapy (liquid biopsy cadence), and when to stop therapy (duration of CPI, TFR in CML, maintenance stopping rules).",
                "Include a brief note on second malignancies and late effects when curative-intent therapy is discussed (alkylators, RT fields, PARPi MDS/AML risk, CHL survivors).",
            ],
            "table_trials": _pick_trials(q),
            "table_doses": _pick_doses(q),
            "bullets": [
                "Table A columns: Drug | Dose | Key toxicity | Pearl",
                "Table B columns: Trial | Arm | Primary endpoint | Result | Change in practice",
                "One paragraph on shared decision-making and financial counseling",
            ],
            "nccn": get_nccn_block(q),
        })
    if target >= 12:
        sections.append({
            "heading": "I. Extended notes — resistance, sequencing & future directions",
            "level": 1,
            "paragraphs": [
                "Resistance biology should occupy a dedicated half-page: on-target secondary mutations, bypass signaling, lineage plasticity "
                "(e.g., EGFR NSCLC → SCLC), antigen loss after cellular therapy, and immunosuppressive TME changes after CPI.",
                "Sequencing principles: use the agent with largest OS benefit early when toxicities allow; reserve cross-resistant drugs; "
                "consider cumulative neuropathy/cardiotoxicity; plan CNS-active agents if brain metastases are present or likely.",
                "Future directions appropriate for 2026 answers: tumor-agnostic indications (NTRK, RET, BRAF, MSI-H, TMB-H, HER2-mut), "
                "radioligand therapy, CAR-NK/off-the-shelf products, ctDNA-guided escalation/de-escalation, AI decision-support, and microbiome modulation adjuncts.",
                "Health services angle: real-world evidence validating trial results in older/comorbid patients; digital remote toxicity monitoring; "
                "and equity of molecular testing access — themes also reflected in recent Paper IV questions.",
            ],
            "bullets": [
                "Write one ‘if progression then…’ resistance table.",
                "Mention at least one tumor-agnostic approval if biology overlaps.",
                "Close with trial enrollment as a standard option.",
            ],
        })
        sections.append({
            "heading": "J. Quick-revision flash cards (last 1–2 pages)",
            "level": 1,
            "paragraphs": [
                "Convert the topic into 8–10 flash cards mentally: (1) definition (2) hallmark gene (3) key test (4) 1L preferred (5) dose "
                "(6) trial (7) top toxicity (8) NCCN 2026 update (9) Indian/NCG pearl (10) one differential.",
            ],
            "bullets": [
                "Flash 1: One-line definition",
                "Flash 2: Driver / pathway",
                "Flash 3: Mandatory biomarker",
                "Flash 4: NCCN preferred 1L",
                "Flash 5: Exact dose",
                "Flash 6: Landmark phase III + endpoint",
                "Flash 7: Grade ≥3 toxicity to warn",
                "Flash 8: 2026 guideline change",
                "Flash 9: Resistance next step",
                "Flash 10: Supportive care must-do",
            ],
            "pearls": [
                "If time-poor in the hall: draw algorithm + trial table + NCCN box — captures most marks.",
                "Keep handwriting large for doses and HRs.",
            ],
        })
    # Duplicate NCCN reminder near end for visibility
    block = get_nccn_block(q)
    sections.append({
        "heading": "Final box — paste into last page of answer sheet",
        "level": 2,
        "nccn": block,
        "paragraphs": [
            "Re-list NCCN 2026 updates here so the examiner sees currency even if earlier pages are rushed.",
        ],
    })
    return sections

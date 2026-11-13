"""Deep essay modules — Batch C (Q373, Q374, Q385, Q386).

Export DEEP = {qid: sections_list} for focus-pack PDF deepening.
Section keys match pdf_builder.build_pdf:
  heading, level, paragraphs, bullets, flowchart, flowchart_title,
  mechanism, table_trials, table_doses, nccn, pearls
"""

from __future__ import annotations

DEEP: dict[str, list[dict]] = {}

# =============================================================================
# Q373 — Feb 2025 Essay 1: Antibody-drug conjugates in medical oncology practice
# =============================================================================
DEEP["Q373"] = [
    {
        "heading": "1. Introduction & definition (open the 15-mark answer)",
        "level": 1,
        "paragraphs": [
            "Antibody–drug conjugates (ADCs) are targeted chemotherapeutics: a monoclonal antibody delivers a highly potent cytotoxic payload to antigen-expressing tumor cells, "
            "improving the therapeutic index versus conventional cytotoxics. They now span solid tumors (breast, lung, gastric, urothelial, ovarian) and hematologic malignancies "
            "(Hodgkin/T-cell lymphoma, DLBCL, myeloma).",
            "For Paper IV, structure the answer as: (i) ADC anatomy & bystander biology → (ii) catalogue by antigen/payload → (iii) landmark phase III trials with doses → "
            "(iv) class toxicities (ILD, neuropathy, ocular, cytopenias) → (v) NCCN 2026 expansions → (vi) sequencing pearls.",
        ],
        "bullets": [
            "Definition one-liner: mAb + linker + payload ± bystander kill of antigen-low neighbors.",
            "Exam currency phrase: ‘ADC footprint expanded across NCCN Guidelines® 2026/2027.’",
            "Contrast briefly with naked mAbs, BiTEs, and CAR-T (delivery of toxin vs immune engagement).",
        ],
        "pearls": [
            "Draw the three-part ADC cartoon in the first 2 minutes — examiners reward mechanism diagrams.",
            "Always pair each named ADC with one trial + one dose + one signature toxicity.",
        ],
    },
    {
        "heading": "2. ADC structure — antibody, linker, payload, DAR",
        "level": 1,
        "paragraphs": [
            "Antibody: usually IgG1 recognizing a surface antigen enriched on tumor (HER2, TROP2, Nectin-4, folate receptor-α, CD30, CD79b, BCMA/BCMA-adjacent, CD19). "
            "Internalization after binding is required for most payloads; antigen density, trafficking, and shedding modulate efficacy.",
            "Linker: cleavable (enzyme-/pH-/reducible-sensitive) vs non-cleavable. Cleavable linkers liberate membrane-permeable toxins → bystander effect. "
            "Non-cleavable linkers (e.g., T-DM1 thioether) release active catabolites mainly inside the lysosome → less bystander, more antigen-restricted kill.",
            "Payload: microtubule inhibitors (DM1, MMAE, MMAF) or topoisomerase-I inhibitors (DXd, SN-38). Drug-to-antibody ratio (DAR) typically 2–8; "
            "higher DAR and permeable topo-I payloads partly explain activity in HER2-low disease with T-DXd.",
        ],
        "mechanism": [
            ("mAb", "Targets tumor antigen; Fc may add ADCC"),
            ("Linker", "Cleavable → bystander; non-cleavable → intracellular"),
            ("Payload", "Microtubule toxin or topo-I poison"),
            ("DAR", "Payload molecules per Ab (design trade-offs)"),
            ("Internalization", "Lysosomal processing → free toxin"),
        ],
        "flowchart": [
            "Bind antigen",
            "Internalize (endosome/lysosome)",
            "Linker cleavage / catabolism",
            "Payload release",
            "DNA damage or mitotic arrest ± bystander diffusion",
        ],
        "flowchart_title": "ADC cellular itinerary",
    },
    {
        "heading": "3. Bystander effect & HER2-low paradigm",
        "level": 1,
        "paragraphs": [
            "Bystander killing: membrane-permeable payloads (DXd, SN-38, some MMAE contexts) diffuse to neighboring antigen-negative/low cells within heterogeneous tumors. "
            "This underpins DESTINY-Breast04/06 activity in HER2-low (IHC 1+ or 2+/ISH−) and ultralow disease — a conceptual leap beyond classical HER2-positive thresholds.",
            "Resistance themes: antigen downregulation/heterogeneity, impaired internalization, payload efflux (MDR1), lysosomal changes, and payload-pathway alterations. "
            "Sequencing across ADCs with non-overlapping payloads (microtubule → topo-I or vice versa) is an active clinical question.",
        ],
        "bullets": [
            "T-DM1: limited bystander → needs stronger HER2 expression historically.",
            "T-DXd / SG / Dato-DXd: cleavable + permeable payload → broader antigen spectrum.",
            "Report HER2-low explicitly on pathology — changes metastatic options.",
        ],
        "pearls": [
            "One exam sentence: ‘Bystander effect + high DAR explain T-DXd benefit beyond IHC 3+/ISH+.’",
        ],
    },
    {
        "heading": "4. HER2 ADCs — T-DXd and T-DM1",
        "level": 1,
        "paragraphs": [
            "Ado-trastuzumab emtansine (T-DM1): trastuzumab + non-cleavable linker + DM1. Landmark EMILIA (post-trastuzumab metastatic) and KATHERINE (adjuvant residual disease after neoadjuvant HER2 therapy). "
            "Dose 3.6 mg/kg IV Q3W. Toxicities: thrombocytopenia, transaminitis, cardiotoxicity monitoring continues.",
            "Trastuzumab deruxtecan (T-DXd): cleavable linker + DXd (topo-I), DAR ≈8, potent bystander. DESTINY-Breast03 established superiority over T-DM1 in 2L HER2+ mBC (mPFS ~28.8 vs 6.8 mo). "
            "DESTINY-Breast04/06 expanded to HER2-low/ultralow. DESTINY-Gastric01/04 support gastric/GEJ after trastuzumab (often 6.4 mg/kg). DESTINY-Lung / NSCLC HER2-mutated niches; urothelial HER2-expressing subsequent lines evolving in NCCN.",
            "Breast metastatic dose typically 5.4 mg/kg IV Q3W. Mandatory ILD/pneumonitis counseling and CT monitoring.",
        ],
        "table_doses": [
            ("T-DM1", "3.6 mg/kg IV Q3W"),
            ("T-DXd (breast)", "5.4 mg/kg IV Q3W — hold/discontinue per ILD grade"),
            ("T-DXd (gastric)", "6.4 mg/kg IV Q3W per label/indication"),
            ("Trastuzumab (context)", "8 → 6 mg/kg IV Q3W with pertuzumab CLEOPATRA backbone"),
        ],
        "table_trials": [
            ("EMILIA", "T-DM1 > lapatinib+capecitabine post-trastuzumab"),
            ("KATHERINE", "Adjuvant T-DM1 > trastuzumab if residual disease"),
            ("DESTINY-Breast03", "T-DXd ≫ T-DM1 2L HER2+ mBC"),
            ("DESTINY-Breast04", "T-DXd practice-changing in HER2-low"),
            ("DESTINY-Breast06", "Earlier HR+/HER2-low–ultralow, chemo-naive metastatic"),
            ("DESTINY-Gastric04", "OS benefit T-DXd 2L HER2+ gastric after trastuzumab"),
        ],
    },
    {
        "heading": "5. TROP2 ADCs — sacituzumab govitecan & datopotamab deruxtecan",
        "level": 1,
        "paragraphs": [
            "Sacituzumab govitecan (SG): anti-TROP2 + hydrolyzable linker + SN-38 (irinotecan active metabolite). ASCENT: SG vs physician’s-choice chemo in relapsed TNBC — PFS/OS benefit. "
            "TROPiCS-02: HR+/HER2− metastatic breast after endocrine and chemo. Also approved/used in pretreated urothelial carcinoma. Dose 10 mg/kg IV D1,8 Q21D.",
            "Datopotamab deruxtecan (Dato-DXd): TROP2-directed DXd ADC. TROPION-Lung program and NCCN 2026 NSCLC pathway place Dato-DXd as preferred subsequent therapy after osimertinib + chemotherapy "
            "in EGFR-mutated disease, and as preferred options in later lines — high-yield 2026 currency point.",
        ],
        "table_doses": [
            ("Sacituzumab govitecan", "10 mg/kg IV D1,8 every 21 days"),
            ("Dato-DXd", "Weight-based IV Q3W per trial/label — monitor ILD/stomatitis"),
        ],
        "table_trials": [
            ("ASCENT", "SG > chemo in R/R TNBC — PFS/OS"),
            ("TROPiCS-02", "SG in HR+/HER2− mBC post-endocrine/chemo"),
            ("TROPION-Lung datasets", "Dato-DXd activity → NCCN preferred post-osi+chemo"),
        ],
        "bullets": [
            "SG pearls: early diarrhea/neutropenia management; UGT1A1 caution analogous to irinotecan biology.",
            "Do not confuse SG (SN-38) with DXd ADCs — shared TROP2 target, different payloads/toxicity profiles.",
        ],
    },
    {
        "heading": "6. Nectin-4 & FRα — enfortumab vedotin & mirvetuximab",
        "level": 1,
        "paragraphs": [
            "Enfortumab vedotin (EV): anti-Nectin-4 + MMAE. EV-301 established OS in previously treated urothelial cancer. EV-302 (EV + pembrolizumab) remade 1L la/mUC — now sole preferred metastatic regimen in NCCN Bladder 2026. "
            "Perioperative EV+P data (KEYNOTE-905/EV-303) for cisplatin-ineligible MIBC. Dose 1.25 mg/kg IV D1,8,15 Q28D (adjust with pembrolizumab schedules).",
            "Mirvetuximab soravtansine: anti–folate receptor-α + maytansinoid. MIRASOL: OS benefit in FRα-high platinum-resistant ovarian cancer vs chemo. Ocular toxicity (keratopathy) requires proactive ophthalmologic care and dose holds. "
            "NCCN ovarian pathways incorporate mirvetuximab in FRα+ platinum-resistant/sensitive contexts alongside 2026 updates (ROSELLA, KEYNOTE-B96).",
        ],
        "table_trials": [
            ("EV-301", "EV > chemo previously treated urothelial — OS"),
            ("EV-302", "EV + pembrolizumab 1L la/mUC — new standard"),
            ("KEYNOTE-905 / EV-303", "Perioperative EV+P cisplatin-ineligible MIBC"),
            ("MIRASOL", "Mirvetuximab > chemo FRα-high PROC — OS"),
        ],
        "table_doses": [
            ("Enfortumab vedotin", "1.25 mg/kg IV D1,8,15 Q28D (± pembrolizumab)"),
            ("Mirvetuximab", "6 mg/kg adjusted ideal body weight IV Q3W — ocular monitoring"),
        ],
        "flowchart": [
            "Metastatic urothelial diagnosis",
            "1L EV + pembrolizumab (NCCN preferred)",
            "Progression → platinum / FGFR / HER2 ADC options",
            "FRα+ PROC → mirvetuximab (MIRASOL)",
        ],
        "flowchart_title": "EV / mirvetuximab clinical hooks",
    },
    {
        "heading": "7. Hematologic ADCs — brentuximab, polatuzumab, belantamab, loncastuximab",
        "level": 1,
        "paragraphs": [
            "Brentuximab vedotin (BV): anti-CD30 + MMAE. ECHELON-1 (BV-AVD in advanced Hodgkin), ECHELON-2 (BV-CHP in CD30+ PTCL), and relapsed HL/ALCL indications. Neuropathy is dose-limiting; PML rare but boxed historically with related agents.",
            "Polatuzumab vedotin: anti-CD79b + MMAE. POLARIX: pola-R-CHP vs R-CHOP in previously untreated DLBCL — PFS benefit; integrate per risk/regulatory context. Also used in transplant-ineligible R/R DLBCL combinations.",
            "Belantamab mafodotin: anti-BCMA + MMAF (non-cleavable). Ocular keratopathy hallmark. DREAMM-7 (belantamab + Vd) informs NCCN Myeloma 2026/2027 Cat 1 other recommended after ≥2 prior lines (PI+IMiD).",
            "Loncastuximab tesirine: anti-CD19 + PBD dimer payload for R/R large B-cell lymphoma after ≥2 lines (LOTIS program). Edema/effusions and myelosuppression need vigilance; PBD class differs from MMAE neuropathy pattern.",
        ],
        "table_trials": [
            ("ECHELON-1 / ECHELON-2", "BV in 1L HL / CD30+ PTCL"),
            ("POLARIX", "Pola-R-CHP vs R-CHOP 1L DLBCL"),
            ("DREAMM-7", "Belantamab + Vd — NCCN myeloma listing"),
            ("LOTIS-2", "Loncastuximab in R/R LBCL"),
        ],
        "table_doses": [
            ("Brentuximab vedotin", "1.2 mg/kg with AVD (ECHELON-1) or 1.8 mg/kg Q3W R/R schedules"),
            ("Polatuzumab vedotin", "1.8 mg/kg IV Q3W in pola-R-CHP / R/R combos"),
            ("Belantamab mafodotin", "Combination dosing per DREAMM-7 — ocular REMS-style monitoring"),
            ("Loncastuximab tesirine", "0.15 mg/kg Q3W ×2 then 0.075 mg/kg Q3W (label schedule)"),
        ],
    },
    {
        "heading": "8. Cross-tumor ADC catalogue (exam table to redraw)",
        "level": 1,
        "paragraphs": [
            "Present a single comparison table the examiner can tick. Columns: ADC | Target | Payload | Key trial | Signature toxicity | NCCN niche.",
        ],
        "bullets": [
            "T-DXd — HER2 — DXd — DESTINY program — ILD — breast/gastric/NSCLC/urothelial niches",
            "T-DM1 — HER2 — DM1 — EMILIA/KATHERINE — platelets/LFTs — residual HER2+ EBC; selected metastatic",
            "SG — TROP2 — SN-38 — ASCENT/TROPiCS — neutropenia/diarrhea — TNBC & HR+ mBC; urothelial",
            "Dato-DXd — TROP2 — DXd — TROPION — ILD/stomatitis — EGFR+ NSCLC subsequent (NCCN 2026)",
            "EV — Nectin-4 — MMAE — EV-302 — neuropathy/rash/hyperglycemia — 1L urothelial ± peri-op",
            "Mirvetuximab — FRα — maytansinoid — MIRASOL — ocular — FRα+ ovarian",
            "BV — CD30 — MMAE — ECHELON — neuropathy — HL/PTCL",
            "Pola — CD79b — MMAE — POLARIX — neuropathy/cytopenias — DLBCL",
            "Belantamab — BCMA — MMAF — DREAMM-7 — ocular — myeloma combinations",
            "Loncastuximab — CD19 — PBD — LOTIS — edema/myelosuppression — R/R LBCL",
        ],
        "pearls": [
            "Microtubule payloads → neuropathy; DXd → ILD; MMAF/mirvetuximab → ocular; SN-38 → diarrhea/neutropenia.",
        ],
    },
    {
        "heading": "9. Toxicities — ILD, neuropathy, ocular, metabolic",
        "level": 1,
        "paragraphs": [
            "ILD/pneumonitis: class effect of deruxtecan ADCs (T-DXd, Dato-DXd). Grade-based algorithm: hold for suspected ILD, start steroids promptly for ≥grade 2, permanently discontinue for grade 3–4 per labels. "
            "Educate patients on cough/dyspnea/fever; low threshold for HRCT.",
            "Peripheral neuropathy: MMAE ADCs (EV, BV, polatuzumab) and taxane carryover. Dose reduce/delay; distinguish from CPI neurologic irAEs when combinations used (EV+P).",
            "Ocular: mirvetuximab and belantamab — lubricating drops, dose holds, ophthalmology partnerships. Hyperglycemia and skin toxicity notable with EV. Neutropenia/diarrhea with SG — growth factors and early loperamide protocols.",
        ],
        "flowchart": [
            "Baseline education + organ-function labs",
            "On-Rx monitoring (CT for DXd; neuro exam; eye scores)",
            "Toxicity → grade",
            "Hold / reduce / steroid / discontinue per label",
            "Document & consider alternate-payload ADC later",
        ],
        "flowchart_title": "ADC toxicity management loop",
        "bullets": [
            "Cardiac monitoring still relevant when HER2 ADCs follow anthracyclines.",
            "Infusion reactions: premedication per product monograph.",
            "Infection risk with cytopenias — especially hematologic ADCs + steroids for ILD.",
        ],
    },
    {
        "heading": "10. Sequencing principles across diseases",
        "level": 1,
        "paragraphs": [
            "Breast HER2+: dual blockade 1L (CLEOPATRA) → T-DXd 2L (DB-03) preferred over T-DM1; tucatinib triplet for CNS-predominant progression (HER2CLIMB). Adjuvant residual disease still T-DM1 (KATHERINE) — different disease setting.",
            "TNBC / HR+: SG after prior lines; T-DXd if HER2-low; pembrolizumab combinations when CPS eligible; PARPi if gBRCA — avoid stacking overlapping marrow toxicity without plan.",
            "Urothelial: EV+P first; genomic switchboard after progression (FGFR → erdafitinib; HER2 → T-DXd). Ovarian: FRα → mirvetuximab; HER2-expressing → T-DXd discussion; platinum-resistant non-ADC options include nab-paclitaxel+relacorilant (ROSELLA) per NCCN 2026.",
        ],
        "flowchart": [
            "Confirm antigen / biomarker",
            "Use OS-proven ADC earliest tolerable line",
            "On progression: re-biopsy/liquid if actionable drivers",
            "Switch payload class if antigen retained",
            "Trial / best supportive care",
        ],
        "flowchart_title": "ADC sequencing skeleton",
    },
    {
        "heading": "11. Landmark trials master table",
        "level": 1,
        "paragraphs": [
            "Memorize five ‘must-quote’ programs: DESTINY (T-DXd), ASCENT & TROPiCS (SG), EV-302 (EV+P), MIRASOL (mirvetuximab). Add KATHERINE/EMILIA for T-DM1 and POLARIX/ECHELON/DREAMM/LOTIS for heme.",
        ],
        "table_trials": [
            ("DESTINY-Breast03/04/06", "T-DXd reshapes HER2+ and HER2-low breast"),
            ("ASCENT", "SG OS benefit R/R TNBC"),
            ("TROPiCS-02", "SG in HR+/HER2− mBC"),
            ("EV-302", "EV+P sole preferred 1L metastatic UC (NCCN)"),
            ("MIRASOL", "Mirvetuximab OS in FRα-high PROC"),
            ("KATHERINE", "Adjuvant T-DM1 residual HER2+ EBC"),
            ("POLARIX", "Pola-R-CHP 1L DLBCL"),
            ("DREAMM-7", "Belantamab+Vd myeloma — NCCN 2026/27"),
        ],
    },
    {
        "heading": "12. NCCN 2026 / 2027 — ADC expansions (boxed content)",
        "level": 1,
        "paragraphs": [
            "State versions explicitly. ADC-related bullets appear across Breast v9.2026, NSCLC v9.2026, Gastric v4.2026, Bladder v3.2026, Ovarian 2026 updates, Myeloma v2.2027, and B-cell lymphoma pathways.",
        ],
        "nccn": {
            "versions": [
                "Breast Cancer v9.2026",
                "NSCLC v9.2026",
                "Gastric v4.2026",
                "Bladder Cancer v3.2026",
                "Ovarian Cancer 2026 panel updates",
                "Multiple Myeloma v2.2027",
                "B-Cell Lymphomas pathways",
            ],
            "bullets": [
                "T-DXd pathways: HER2+ and HER2-low/ultralow breast; HER2+ gastric 2L; HER2-mut/expressing NSCLC & urothelial subsequent niches.",
                "Dato-DXd preferred after osimertinib + chemo in EGFR+ NSCLC (and listed across EGFR alteration subsequent settings).",
                "SG retained in TNBC/HR+ breast and urothelial algorithms.",
                "EV + pembrolizumab sole preferred 1L la/mUC; perioperative EV+P for cisplatin-ineligible MIBC.",
                "Mirvetuximab for FRα+ ovarian; belantamab combinations in myeloma; loncastuximab in R/R LBCL; polatuzumab in DLBCL.",
                "Cross-cutting: expanding ADC footprint is an explicit NCCN 2026 theme for exam answers.",
            ],
        },
        "pearls": [
            "Write ‘NCCN 2026’ next to EV-302 and Dato-DXd — signals currency for Paper IV.",
        ],
    },
    {
        "heading": "13. Special situations & Indian/NCG practical notes",
        "level": 1,
        "paragraphs": [
            "Access and cost: ADCs are expensive; discuss biosimilar trastuzumab backbones before ADC lines, trial enrollment, and center capability for ILD steroid protocols. CDSCO approvals may lag FDA/EMA — reconcile in the answer.",
            "Pregnancy: cytotoxic payloads contraindicated. Breastfeeding contraindicated. Fertility counseling before MMAE/topo-I ADCs. Elderly: neuropathy risk with EV/BV; ILD risk with DXd in smokers/prior chest RT — individualize.",
        ],
        "bullets": [
            "MDT + ophthalmology/pulmonology co-management pathways.",
            "Document antigen assay method (IHC clone, FRα scoring, HER2-low).",
            "Pharmacovigilance: report ILD and ocular events.",
        ],
    },
    {
        "heading": "14. Summary checklist & exam pearls",
        "level": 1,
        "paragraphs": [
            "Close with a numbered summary: structure → bystander → 10 named ADCs → 5 trial acronyms → doses → toxicities → NCCN 2026.",
        ],
        "bullets": [
            "Anatomy: Ab + linker + payload ± bystander",
            "Solid tumor stars: T-DXd, T-DM1, SG, Dato-DXd, EV, mirvetuximab",
            "Heme stars: brentuximab, polatuzumab, belantamab, loncastuximab",
            "Trials: DESTINY, ASCENT, TROPiCS, EV-302, MIRASOL",
            "Tox: ILD (DXd), neuropathy (MMAE), ocular (mirv/belantamab)",
            "NCCN 2026: Dato-DXd EGFR NSCLC; EV+P bladder; ADC catalogue expansion",
        ],
        "pearls": [
            "KATHERINE ≠ metastatic sequencing — adjuvant residual disease only.",
            "EV neuropathy + pembrolizumab irAE overlap needs careful grading.",
            "HER2-low is an ADC story, not classical trastuzumab monotherapy story.",
            "Payload class switch may salvage antigen-persistent progression.",
            "Always mention monitoring: HRCT/steroids for ILD; eye exams for FRα/BCMA ADCs.",
        ],
        "flowchart": [
            "Define ADC",
            "List targets",
            "Quote trials+doses",
            "Box toxicities",
            "Paste NCCN 2026 bullets",
        ],
        "flowchart_title": "15-mark ADC answer skeleton",
    },
]

# =============================================================================
# Q374 — Feb 2025 Essay 2: Mucosal melanoma
# =============================================================================
DEEP["Q374"] = [
    {
        "heading": "1. Introduction — why mucosal melanoma is a distinct entity",
        "level": 1,
        "paragraphs": [
            "Mucosal melanoma (MM) arises from melanocytes in ectodermal mucosa — ~1–2% of melanomas in Western series but a higher fraction of melanoma in Asian/Indian cohorts where cutaneous UV-driven disease is less dominant. "
            "It is biologically and clinically distinct from cutaneous melanoma: different molecular drivers, later stage at diagnosis, richer local invasion, and inferior outcomes with surgery, radiotherapy, and checkpoint inhibitors.",
            "Exam framing: sites → pathology/molecular (KIT/NRAS/BRAF) → staging work-up → local therapy (surgery/RT) → systemic CPI (± targeted) → prognosis vs cutaneous → NCCN cutaneous neoadjuvant contrast.",
        ],
        "pearls": [
            "Opening contrast sentence scores marks: ‘Unlike cutaneous melanoma, mucosal disease is UV-independent, KIT-enriched, and CPI-hyporesponsive.’",
        ],
    },
    {
        "heading": "2. Epidemiology & anatomic sites",
        "level": 1,
        "paragraphs": [
            "Major site groups: (1) Head and neck mucosal — sinonasal cavity, oral cavity, oropharynx, larynx (sinonasal often presents with epistaxis/obstruction). "
            "(2) Anorectal — rectal/anal melanomas; may mimic hemorrhoids. (3) Vulvovaginal — vaginal > vulvar mucosal primaries. Rarer: urinary tract, esophagus, gallbladder.",
            "Age typically older adults; equal or site-dependent sex skew (vulvovaginal in women; anorectal slight female predominance in some series). No clear UV association — sun-protection counseling still relevant for cutaneous surveillance but not causal for MM.",
        ],
        "bullets": [
            "India/Asia: higher proportional burden of mucosal/acral vs superficial spreading cutaneous subtypes.",
            "Delayed diagnosis common → thicker/locally advanced primaries.",
            "Rule out metastatic cutaneous melanoma to mucosa (history, skin exam, regression scars).",
        ],
        "flowchart": [
            "Pigmented/amenable mucosal lesion",
            "Full skin + node exam",
            "Biopsy with IHC",
            "Site-directed imaging + PET-CT staging",
            "MDT: H&N / GI / gyn oncology + melanoma medical oncology",
        ],
        "flowchart_title": "Initial MM pathway",
    },
    {
        "heading": "3. Pathology & diagnosis",
        "level": 1,
        "paragraphs": [
            "Histology: atypical melanocytes ± melanin; amelanotic tumors frequent — IHC mandatory (S100, SOX10, Melan-A/MART-1, HMB-45; cytokeratin negative helps exclude carcinoma). "
            "Breslow depth analogs and ulceration still reported when measurable; for sinonasal, local extent into bone/skull base often dominates staging language.",
            "Differential: mucosal melanosis, carcinoma, sarcoma, lymphoma, clear cell sarcoma (EWSR1), metastatic cutaneous melanoma. Document margins meticulously — R0 rare in sinonasal disease.",
        ],
        "bullets": [
            "Always photograph and map lesions before wide resection.",
            "PD-L1 not reliable sole selector for CPI in MM.",
            "Send NGS panel covering BRAF, NRAS, KIT, NF1, SF3B1 (esp. uveal — different entity), TMB/MSI rarely high.",
        ],
        "mechanism": [
            ("UV cutaneous", "High TMB, BRAF V600 common"),
            ("Mucosal", "Low TMB, KIT/NRAS enriched"),
            ("Uveal (contrast)", "GNAQ/G11, BAP1 — not mucosal"),
            ("IHC", "SOX10/Melan-A confirm melanocytic"),
            ("NGS", "Actionable KIT / rare BRAF"),
        ],
    },
    {
        "heading": "4. Molecular biology — KIT, NRAS, BRAF (rarer)",
        "level": 1,
        "paragraphs": [
            "KIT mutations/amplifications enriched in mucosal and acral melanomas (exon 11, 13, 17 hotspots). NRAS mutations occur at meaningful frequency. BRAF V600 mutations are substantially rarer than in cutaneous melanoma (~6–15% vs ~50%) — still test because MEK/BRAF inhibitors remain options if present.",
            "Tumor mutational burden is typically lower → fewer neoantigens → partly explains inferior CPI response versus cutaneous melanoma. SF3B1 and other alterations appear in some mucosal series; fusions uncommon but NGS may reveal trial options.",
        ],
        "bullets": [
            "Always sequence KIT before declaring ‘no targeted option’.",
            "KIT exon 11 often more imatinib-sensitive than exon 17 (pattern shared with GIST teaching).",
            "Do not start BRAF/MEKi without confirmed BRAF V600.",
        ],
        "pearls": [
            "Mnemonic: Mucosal → KIT/NRAS; Cutaneous → BRAF/UV-TMB; Uveal → GNAQ/G11.",
        ],
    },
    {
        "heading": "5. Staging & risk assessment",
        "level": 1,
        "paragraphs": [
            "AJCC cutaneous TNM is imperfect for MM; site-specific systems and clinical staging (local / regional / distant) guide practice. MRI for sinonasal/skull base and pelvic MM; endoscopic staging for anorectal; CT/PET for distant disease (lung, liver, bone).",
            "Prognostic factors: site (anorectal often worse), tumor thickness/size, nodal status, resectability, LDH, performance status, and molecular findings. Five-year OS historically much lower than stage-matched cutaneous melanoma.",
        ],
        "table_trials": [
            ("Institutional MM series", "Inferior OS vs cutaneous; late presentation"),
            ("Meta-analyses CPI MM", "ORR typically ~20–35% vs higher cutaneous"),
        ],
    },
    {
        "heading": "6. Local therapy — surgery",
        "level": 1,
        "paragraphs": [
            "Surgery remains the backbone for localized disease when R0/R1-meaningful resection is feasible without catastrophic morbidity. Wide margins akin to cutaneous norms are often anatomically impossible in sinonasal/vaginal sites — balance oncologic clearance with function (vision, speech, continence, sexual function).",
            "Elective node dissection is not uniformly standardized; sample clinically involved nodes. Sentinel node concepts less validated than cutaneous. Anorectal: abdominoperineal resection historically used; organ preservation debates exist for early lesions with RT/systemic combinations in specialized centers.",
        ],
        "bullets": [
            "Refer sinonasal MM to high-volume skull-base teams.",
            "Avoid piecemeal inadequate excisions that seed mucosa.",
            "Metastasectomy rarely curative but may palliate selected oligometastases after systemic control.",
        ],
        "flowchart": [
            "Localized MM at MDT",
            "Resectable with acceptable morbidity?",
            "Yes → surgery ± adjuvant RT/systemic",
            "No → definitive RT / systemic first / palliative",
            "Recurrence → re-resect vs CPI/TKI/trial",
        ],
        "flowchart_title": "Local therapy decision",
    },
    {
        "heading": "7. Radiotherapy",
        "level": 1,
        "paragraphs": [
            "Melanoma is relatively radioresistant, yet RT is important for local control in incompletely resected sinonasal/oral disease, vaginal primaries, and palliation of bleeding/pain. Techniques: IMRT/VMAT, stereotactic approaches for skull base; consider proton therapy discussion for sinonasal OAR sparing in selected centers.",
            "Adjuvant RT after close/positive margins can improve local control without clear OS proof — state this nuance. Hypofractionation historically used in melanoma; modern conformal fractionation individualized. Combine carefully with CPI (recall additive dermatitis/mucositis and rare recall phenomena).",
        ],
        "bullets": [
            "Palliative RT for symptomatic metastases remains valuable.",
            "Document dental/endocrine/sexual late effects risk.",
        ],
    },
    {
        "heading": "8. Systemic therapy — checkpoint inhibitors (CheckMate / KEYNOTE mucosal subgroups)",
        "level": 1,
        "paragraphs": [
            "Anti–PD-1 monotherapy (nivolumab, pembrolizumab) and combinations (nivolumab+ipilimumab; nivolumab+relatlimab) are used by extrapolation from cutaneous paradigms, but mucosal subgroup analyses and dedicated series show lower ORR and shorter survival than cutaneous melanoma.",
            "CheckMate 067 mucosal subgroups and pooled anti–PD-1 analyses: responses occur and durable benefit is possible — still offer CPI as standard systemic backbone for unresectable/metastatic MM absent a better targeted option. KEYNOTE-006/KEYNOTE mucosal cohorts similarly support pembrolizumab activity at a lower response rate.",
            "Neoadjuvant CPI is transforming resectable cutaneous nodal melanoma (SWOG S1801, NADINA) — evidence in mucosal primaries is far thinner; do not uncritically copy cutaneous neoadjuvant algorithms without MDT caveats.",
        ],
        "table_trials": [
            ("CheckMate 067 (mucosal subgroup)", "Nivo±ipi active but inferior outcomes vs cutaneous"),
            ("KEYNOTE-006 / mucosal cohorts", "Pembrolizumab activity; lower ORR than cutaneous"),
            ("Pooled anti–PD-1 MM analyses", "ORR ~23–30%; some durable remissions"),
            ("RELATIVITY-047 context", "Nivo+relatlimab — limited MM-specific level-1 data"),
            ("SWOG S1801 / NADINA", "Neoadjuvant CPI — cutaneous resectable nodal; contrast with MM"),
        ],
        "table_doses": [
            ("Nivolumab", "240 mg Q2W or 480 mg Q4W"),
            ("Pembrolizumab", "200 mg Q3W or 400 mg Q6W"),
            ("Nivo + ipi (melanoma)", "Nivo 1 mg/kg + ipi 3 mg/kg Q3W ×4 → nivo maintenance"),
            ("Nivo + relatlimab", "Fixed-dose combo per label Q4W"),
        ],
        "pearls": [
            "Quote ‘lower ORR than cutaneous but still first systemic choice for most unresectable MM’.",
        ],
    },
    {
        "heading": "9. Targeted therapy if KIT (and rare BRAF)",
        "level": 1,
        "paragraphs": [
            "Imatinib: phase II data in KIT-mutant melanoma (including mucosal) show responses enriched for exon 11 mutations; median PFS modest — use when CPI contraindicated, after CPI, or in molecularly selected rapid progression. Dose often 400 mg daily (some escalate). Nilotinib/dasatinib studied with mixed results; ripretinib/other KIT inhibitors via trials.",
            "BRAF V600–mutant MM (uncommon): dabrafenib+trametinib or encorafenib+binimetinib per cutaneous dosing. NRAS: MEK inhibitor trials historically; no robust standard — prefer CPI/trial. Avoid empiric KIT TKI without mutation.",
        ],
        "table_doses": [
            ("Imatinib (KIT-mut MM)", "400 mg PO daily (selected escalation)"),
            ("Dabrafenib + trametinib", "150 mg BID + 2 mg daily if BRAF V600"),
            ("Encorafenib + binimetinib", "450 mg daily + 45 mg BID if BRAF V600"),
        ],
        "flowchart": [
            "Unresectable/metastatic MM",
            "NGS: BRAF V600? → BRAF/MEKi option",
            "KIT exon 11/13? → consider imatinib ± after/with CPI strategy",
            "Wild-type drivers → CPI combination vs PD-1 alone",
            "Progression → alternate CPI strategy / TKI / local therapy / trial",
        ],
        "flowchart_title": "Systemic algorithm for MM",
    },
    {
        "heading": "10. Prognosis vs cutaneous melanoma",
        "level": 1,
        "paragraphs": [
            "MM carries poorer prognosis stage-for-stage: delayed detection, difficult R0, early hematogenous spread (anorectal), and lower CPI sensitivity tied to low TMB. Five-year survival for advanced MM is substantially inferior to cutaneous cohorts in CPI landmark trials.",
            "Counsel patients honestly while emphasizing that durable CPI responses still occur. Supportive care, nutrition, and psychosocial support are integral — facial disfigurement and sexual/continence morbidity need rehabilitation planning.",
        ],
        "bullets": [
            "Surveillance: frequent local exams + imaging; pattern-of-failure often local+distant.",
            "Second opinions at melanoma referral centers appropriate.",
        ],
    },
    {
        "heading": "11. Multidisciplinary & site-specific pearls",
        "level": 1,
        "paragraphs": [
            "Sinonasal: endoscopy, MRI, skull-base surgery, adjuvant RT, early CPI for unresectable. Oral: dental oncology. Anorectal: surgical oncology + RT + systemic; distinguish from squamous anal HPV disease. Vulvovaginal: gyn-oncology radicality vs function; RT for organ preservation discussions.",
        ],
        "bullets": [
            "Amelanotic anorectal MM — biopsy every atypical ‘hemorrhoid’.",
            "HPV testing does not diagnose melanoma — IHC does.",
            "Screen for synchronous cutaneous primaries.",
        ],
    },
    {
        "heading": "12. NCCN 2026 melanoma context — neoadjuvant contrast",
        "level": 1,
        "paragraphs": [
            "NCCN Melanoma: Cutaneous v3.2026 elevates neoadjuvant systemic therapy as preferred initial approach for resectable nodal disease — pembrolizumab or ipilimumab+nivolumab (Cat 1), with other IO options and BRAF/MEKi in certain BRAF V600 circumstances. "
            "This cutaneous paradigm should be cited as contrast: mucosal primaries are not the evidence base for S1801/NADINA; resectability and local control constraints differ.",
            "Still use NCCN cutaneous systemic agents as the practical drug menu for MM while stating evidence quality is extrapolated. Mucosal-specific guideline sections and European site-specific guidance may supplement.",
        ],
        "nccn": {
            "versions": [
                "Melanoma: Cutaneous v3.2026",
                "Head and Neck Cancers v2.2026 (sinonasal context)",
            ],
            "bullets": [
                "Cutaneous resectable nodal: neoadjuvant CPI preferred (pembro; ipi+nivo Cat 1) — do not blindly equate to mucosal primaries.",
                "Metastatic melanoma systemic options (PD-1 ± CTLA-4/LAG-3; BRAF/MEKi if V600) used for MM by extrapolation.",
                "Emphasize molecular testing (BRAF/KIT/NRAS) in non-cutaneous subtypes.",
                "Local therapy remains decisive for mucosal sites despite systemic advances.",
            ],
        },
    },
    {
        "heading": "13. irAE & supportive care in MM patients",
        "level": 1,
        "paragraphs": [
            "Standard irAE algorithms apply (skin, colitis, hepatitis, endocrinopathy, pneumonitis). Head-and-neck RT fields plus CPI may intensify mucositis — coordinate supportive care. Post-surgical wounds need infection surveillance during steroids for irAEs.",
        ],
        "bullets": [
            "Vaccinate appropriately before IO when feasible.",
            "Thromboprophylaxis individualized for pelvic surgery patients.",
        ],
    },
    {
        "heading": "14. Summary checklist & exam pearls",
        "level": 1,
        "paragraphs": [
            "End with a crisp comparison table: cutaneous vs mucosal across UV, TMB, BRAF, KIT, CPI ORR, neoadjuvant evidence, prognosis.",
        ],
        "bullets": [
            "Sites: H&N, anorectal, vulvovaginal",
            "Molecular: KIT/NRAS > BRAF",
            "Local: surgery ± RT; margins often limited",
            "Systemic: CPI first; imatinib if KIT; BRAF/MEKi if V600",
            "Prognosis worse than cutaneous",
            "NCCN 2026 neoadjuvant CPI = cutaneous nodal story — contrast explicitly",
        ],
        "pearls": [
            "Uveal melanoma is a different disease — do not conflate.",
            "Quote CheckMate/KEYNOTE mucosal subgroup humility (lower ORR).",
            "KIT testing is the targeted-therapy doorway.",
            "Draw site map + molecular pie chart for quick marks.",
            "State MDT site specialty by anatomic primary.",
        ],
        "flowchart": [
            "Confirm MM site",
            "Resect ± RT if localized",
            "NGS",
            "CPI ± targeted",
            "Surveillance / palliation",
        ],
        "flowchart_title": "MM 30-second revision flow",
    },
]

# =============================================================================
# Q385 — Jan 2026 Essay 1: Next-gen targeted therapies — KRAS, PARP, ADCs
# =============================================================================
DEEP["Q385"] = [
    {
        "heading": "1. Introduction — the ‘next-generation targeted’ triad",
        "level": 1,
        "paragraphs": [
            "This January 2026 essay expects an integrated discussion of three transformative classes: (1) direct KRAS inhibitors (finally drugging the ‘undruggable’), (2) PARP inhibitors exploiting synthetic lethality in homologous recombination deficiency, and (3) antibody–drug conjugates as targeted cytotoxics. "
            "Organize by class: biology → drugs/doses → tumor types → pivotal trials → resistance → NCCN 2026 refinements → shared sequencing principles.",
        ],
        "pearls": [
            "Announce a three-part structure in sentence one so the examiner can follow.",
        ],
    },
    {
        "heading": "2. KRAS biology — why G12C was first",
        "level": 1,
        "paragraphs": [
            "KRAS cycles between GTP-on and GDP-off states; oncogenic mutations lock signaling through MAPK/PI3K. Codon 12/13/61 alleles differ by tumor: G12C common in NSCLC (smoking-related), G12D dominant in PDAC and common in CRC, G12V across tumors.",
            "Covalent G12C inhibitors bind the mutant cysteine in the switch-II pocket in the GDP state (inactive), trapping KRASG12C. Allele-specific chemistry explains why G12D needs non-covalent / salt-bridge strategies (emerging inhibitors).",
        ],
        "mechanism": [
            ("KRAS mutant", "Chronic GTP signaling"),
            ("G12C covalent Tx", "Switch-II pocket + Cys12 bond"),
            ("Downstream", "RAF–MEK–ERK / PI3K–AKT"),
            ("Resistance", "RTK feedback, new KRAS mutations, fusions"),
            ("Combos", "Anti-EGFR (CRC), SHP2, MEK, IO, chemo"),
        ],
    },
    {
        "heading": "3. Sotorasib & adagrasib — approved G12C inhibitors",
        "level": 1,
        "paragraphs": [
            "Sotorasib (CodeBreaK program): oral KRASG12C inhibitor approved for previously treated KRAS G12C NSCLC; CRC activity improved when combined with EGFR inhibition (CodeBreaK 101/301 paradigms) because EGFR feedback reactivates wild-type RAS isoforms in CRC.",
            "Adagrasib (KRYSTAL program): alternative G12C inhibitor with CNS activity signals; KRYSTAL-1 NSCLC; KRYSTAL-1/-12 /-10 combinations with cetuximab in CRC. Choose based on access, interactions, and CNS disease — both are subsequent-line standards pending evolving 1L combinations.",
        ],
        "table_doses": [
            ("Sotorasib", "960 mg PO daily (NSCLC label dose; modify for interactions/toxicity)"),
            ("Adagrasib", "600 mg PO BID"),
            ("Adagrasib + cetuximab (CRC)", "Per KRYSTAL combination protocols"),
        ],
        "table_trials": [
            ("CodeBreaK 100/200", "Sotorasib in KRAS G12C NSCLC"),
            ("KRYSTAL-1", "Adagrasib NSCLC ± CNS activity"),
            ("CodeBreaK / KRYSTAL CRC combos", "G12Ci + EGFR mAb improves CRC control"),
        ],
        "bullets": [
            "Toxicities: diarrhea, hepatotoxicity, ILD/pneumonitis rare, QTc (adagrasib monitoring), edema.",
            "Avoid strong CYP inducers/inhibitors per label; acid-reducing caveats as applicable.",
        ],
    },
    {
        "heading": "4. Emerging KRAS G12D and pan-RAS strategies",
        "level": 1,
        "paragraphs": [
            "G12D inhibitors (e.g., investigational allele-selective agents such as MRTX1133-class / newer clinical candidates) and pan-KRAS/RAS approaches are 2026 exam ‘future directions’. PDAC — dominated by G12D — is the unmet-need poster child.",
            "Combination logic: SHP2 inhibitors, SOS1 inhibitors, MEK inhibitors, immunotherapy, and chemotherapy backbones aim to block adaptive feedback. Mention resistance via secondary KRAS alterations, MET/EGFR activation, and histologic transformation analogies.",
        ],
        "bullets": [
            "Always re-profile at progression (tissue/ctDNA) after KRAS G12Ci.",
            "G12C CRC: do not use G12Ci monotherapy as enthusiastically as in NSCLC — pair EGFR blockade.",
        ],
        "flowchart": [
            "NGS detects KRAS allele",
            "G12C NSCLC → sotorasib/adagrasib ≥2L (per indication)",
            "G12C CRC → G12Ci + EGFR mAb strategy",
            "G12D / other → trial / emerging agents",
            "Progression → resistance mapping + combo switch",
        ],
        "flowchart_title": "KRAS allele-directed flow",
    },
    {
        "heading": "5. PARP inhibitors — mechanism of synthetic lethality",
        "level": 1,
        "paragraphs": [
            "PARP enzymes repair single-strand DNA breaks. PARP inhibitors trap PARP on DNA and block BER repair; in homologous recombination–deficient cells (BRCA1/2, other HRR genes), double-strand break repair fails → synthetic lethality. "
            "HRD assays and BRCA status select benefit; platinum sensitivity often correlates.",
        ],
        "mechanism": [
            ("SSB", "PARP recruited"),
            ("PARPi", "Catalytic block + PARP trapping"),
            ("Replication fork collapse", "DSB accumulates"),
            ("HR proficient", "Repair possible → less kill"),
            ("HR deficient", "Synthetic lethality → apoptosis"),
        ],
    },
    {
        "heading": "6. PARPi across tumor types",
        "level": 1,
        "paragraphs": [
            "Ovarian: SOLO1 (olaparib maintenance gBRCA after platinum), PAOLA-1 (olaparib+bevacizumab HRD), PRIMA (niraparib broad 1L maintenance), NOVA historical recurrent — but NCCN 2026 narrows PARPi in recurrent treatment sections toward maintenance/biomarker-defined use.",
            "Breast: OlympiAD (olaparib), EMBRACA (talazoparib) in gBRCA mBC; OlympiA adjuvant olaparib for high-risk gBRCA HER2− early breast cancer.",
            "Pancreas: POLO — olaparib maintenance after platinum in gBRCA metastatic PDAC. Prostate: PROfound (olaparib HRR), MAGNITUDE/PROpel/TALAPRO combinations with ARPIs; NCCN prostate update highlights ADT + niraparib/abiraterone for BRCA2-mutated APMS subsets.",
        ],
        "table_doses": [
            ("Olaparib tablets", "300 mg PO BID"),
            ("Niraparib", "200–300 mg PO daily (individualize by weight/platelets in ovarian)"),
            ("Talazoparib", "1 mg PO daily (breast)"),
            ("Rucaparib", "600 mg PO BID (indication-dependent)"),
            ("Niraparib + abiraterone", "Per prostate combination label with ADT + prednisone"),
        ],
        "table_trials": [
            ("SOLO1 / PAOLA-1 / PRIMA", "1L ovarian maintenance paradigms"),
            ("OlympiA / OlympiAD", "Adjuvant & metastatic gBRCA breast"),
            ("POLO", "PDAC gBRCA maintenance"),
            ("PROfound / MAGNITUDE / PROpel", "Prostate HRR/BRCA PARPi ± ARPI"),
        ],
    },
    {
        "heading": "7. NCCN 2026 PARP refinements — ovarian narrowing & prostate BRCA2",
        "level": 1,
        "paragraphs": [
            "High-yield 2026 points: (1) Ovarian — PARPi removed from many recurrent therapy listings; concentrate on maintenance and biomarker-defined (BRCA/HRD) settings; platinum-resistant non-PARP preferred options include nab-paclitaxel+relacorilant (ROSELLA). "
            "(2) Prostate — ADT + niraparib/abiraterone for BRCA2-mutated high-volume (and Cat 2B low-volume) synchronous/metachronous APMS disease. (3) Breast — continue olaparib/talazoparib pathways including OlympiA.",
        ],
        "nccn": {
            "versions": [
                "Ovarian Cancer 2026 panel updates",
                "Prostate Cancer v1.2027",
                "Breast Cancer v9.2026",
            ],
            "bullets": [
                "Ovarian: PARPi narrowed in recurrent treatment sections; focus maintenance + BRCA/HRD.",
                "Prostate: ADT + niraparib/abiraterone for BRCA2 APMS subsets.",
                "Breast: olaparib/talazoparib metastatic gBRCA; adjuvant olaparib OlympiA population.",
                "Counsel MDS/AML rare risk and hematologic monitoring across indications.",
            ],
        },
        "pearls": [
            "Saying ‘PARPi narrowed in ovarian 2026’ is a discriminator vs outdated answers dumping PARPi on all platinum-resistant disease.",
        ],
    },
    {
        "heading": "8. PARPi toxicities & resistance",
        "level": 1,
        "paragraphs": [
            "Class toxicities: anemia, neutropenia, thrombocytopenia, nausea, fatigue; niraparib — early hypertension/platelet dips (individualized starting dose). Rare MDS/AML — informed consent. Drug interactions via CYP3A for olaparib.",
            "Resistance: BRCA reversion mutations restoring HR, loss of PARP trapping, drug efflux, replication fork protection pathway changes. Reversion detectable on ctDNA — elegant exam pearl.",
        ],
        "bullets": [
            "Do not stack full-dose myelotoxic chemo concurrently without protocol.",
            "Hold PARPi for grade ≥3 hematologic toxicity per label.",
        ],
    },
    {
        "heading": "9. ADC catalogue within the triad essay",
        "level": 1,
        "paragraphs": [
            "Reprise ADCs concisely (full detail was Feb 2025 Q373): T-DXd (HER2), T-DM1, SG & Dato-DXd (TROP2), EV (Nectin-4), mirvetuximab (FRα), heme ADCs (BV, pola, belantamab, loncastuximab). Emphasize bystander biology and NCCN 2026 expansion.",
        ],
        "table_trials": [
            ("DESTINY program", "T-DXd across HER2 spectra"),
            ("ASCENT / TROPiCS", "SG in TNBC & HR+ mBC"),
            ("EV-302", "EV+P 1L urothelial"),
            ("MIRASOL", "Mirvetuximab FRα+ PROC"),
            ("TROPION / NCCN 2026", "Dato-DXd EGFR+ NSCLC subsequent"),
        ],
        "table_doses": [
            ("T-DXd", "5.4 mg/kg Q3W breast (ILD watch)"),
            ("SG", "10 mg/kg D1,8 Q21D"),
            ("EV", "1.25 mg/kg D1,8,15 Q28D ± pembro"),
            ("Dato-DXd", "Q3W per label — preferred post-osi+chemo"),
        ],
        "flowchart": [
            "Biomarker (HER2/TROP2/Nectin-4/FRα)",
            "Pick ADC with OS-proven trial",
            "Monitor class toxicity",
            "On PD → alternate payload / driver drug (KRAS/PARP) if relevant",
        ],
        "flowchart_title": "ADC arm inside the triad",
    },
    {
        "heading": "10. Integrating the triad — shared principles",
        "level": 1,
        "paragraphs": [
            "Biomarker-first oncology: NGS for KRAS allele & HRR/BRCA; IHC/ISH for HER2/FRα/Nectin-4/TROP2 context. Use the agent with proven OS earliest when toxicity allows. Avoid overlapping severe marrow or ILD risks without staggered planning.",
            "Liquid biopsy complements tissue for KRAS resistance and BRCA reversions. Trials remain standard options especially for G12D and post-ADC/post-PARPi resistance.",
        ],
        "bullets": [
            "One page comparison table: Class | Target | Exemplar drug | Trial | NCCN 2026 note.",
            "Indian context: access/cost; prioritize Category 1; molecular testing equity.",
        ],
    },
    {
        "heading": "11. Resistance & sequencing vignettes (examiner favorites)",
        "level": 1,
        "paragraphs": [
            "Vignette A: EGFR NSCLC on osi+chemo → PD → Dato-DXd (ADC), not random chemo. Vignette B: mCRPC BRCA2 → PARPi ± ARPI strategies; consider radioligand later. Vignette C: KRAS G12C CRC progression on sotorasib alone → add/ensure EGFR blockade or switch per evidence. "
            "Vignette D: HER2-low mBC after SG → T-DXd if not used (payload switch + antigen).",
        ],
        "pearls": [
            "Payload switch and allele switch are parallel ideas across ADCs and KRAS.",
        ],
    },
    {
        "heading": "12. Toxicity comparison table for the three classes",
        "level": 1,
        "paragraphs": [
            "KRAS G12Ci: GI, LFT, ILD rare, QTc (adagrasib). PARPi: marrow, nausea, MDS/AML rare, hypertension (niraparib). ADCs: ILD (DXd), neuropathy (MMAE), ocular (mirv/belantamab), diarrhea (SG).",
        ],
        "bullets": [
            "Baseline ECG if adagrasib; CNP exams if EV; eye scores if mirvetuximab; CBC q month on PARPi initially.",
        ],
    },
    {
        "heading": "13. NCCN 2026 master box for the triad",
        "level": 1,
        "paragraphs": [
            "Pull NSCLC (Dato-DXd), ovarian PARP narrowing, prostate niraparib/abi BRCA2, breast ADC/PARP, bladder EV+P into one final box.",
        ],
        "nccn": {
            "versions": [
                "NSCLC v9.2026",
                "Ovarian 2026 updates",
                "Prostate v1.2027",
                "Breast v9.2026",
                "Bladder v3.2026",
            ],
            "bullets": [
                "Dato-DXd preferred subsequent after osi+chemo in EGFR+ NSCLC.",
                "PARPi ovarian use narrowed to maintenance/biomarker-defined contexts.",
                "ADT + niraparib/abiraterone for BRCA2 APMS prostate subsets.",
                "ADC expansions: T-DXd, SG, EV+P, mirvetuximab, belantamab combos.",
                "KRAS G12C inhibitors embedded in NSCLC/CRC subsequent pathways with combo nuance in CRC.",
            ],
        },
    },
    {
        "heading": "14. Summary checklist & pearls",
        "level": 1,
        "paragraphs": [
            "Close: KRAS G12C real (sotorasib/adagrasib), G12D emerging; PARPi across ovary/breast/pancreas/prostate with 2026 ovarian narrowing + prostate BRCA2 combo; ADCs as antigen-directed cytotoxics reshaping NCCN maps.",
        ],
        "bullets": [
            "G12C ≠ G12D pharmacology",
            "CRC G12C needs EGFR mAb partner",
            "OlympiA adjuvant olaparib breast",
            "EV-302 and DESTINY must-quote ADC trials",
            "Reversion mutations → PARPi resistance",
        ],
        "pearls": [
            "Three classes, three mechanisms, three NCCN 2026 bullets — minimum passing skeleton.",
            "Write exact doses for sotorasib 960 mg, adagrasib 600 mg BID, olaparib 300 mg BID.",
            "Mention synthetic lethality and bystander effect by name.",
            "Future: pan-RAS, G12D, ADC+IO and PARPi combos carefully toxicity-managed.",
            "Financial toxicity counseling is fair game in 2026 answers.",
        ],
        "flowchart": [
            "Test biomarkers",
            "Match class (KRAS/PARP/ADC)",
            "Dose + trial citation",
            "Monitor class tox",
            "Sequence with NCCN 2026",
        ],
        "flowchart_title": "Triad answer closer",
    },
]

# =============================================================================
# Q386 — Jan 2026 Essay 2: Real-world evidence & digital oncology tools
# =============================================================================
DEEP["Q386"] = [
    {
        "heading": "1. Introduction — why RWE & digital tools are Paper IV topics",
        "level": 1,
        "paragraphs": [
            "Modern cancer care increasingly complements randomized controlled trials (RCTs) with real-world evidence (RWE) and digital tools: AI clinical decision support, digital biomarkers (including ctDNA), and remote patient monitoring / ePROs. "
            "NCCN’s Guidelines Navigator exemplifies digitization of living guidelines. Structure: definitions → RWE methods/bias → Flatiron-type evidence → digital biomarkers → remote toxicity monitoring → AI CDS → regulatory uses → ethics/limits → NCCN 2026.",
        ],
        "pearls": [
            "Define RWE in the first paragraph: clinical evidence from RWD (EHRs, claims, registries, wearables) not traditional trials.",
        ],
    },
    {
        "heading": "2. Definitions — RWD, RWE, digital oncology",
        "level": 1,
        "paragraphs": [
            "Real-world data (RWD): routinely collected health data — EHRs, insurance claims, cancer registries, patient-generated data, pharmacy dispenses. Real-world evidence (RWE): clinical inference derived from RWD analysis regarding usage, benefits, or risks.",
            "Digital oncology tools: software/AI that supports decisions, passive/active sensors, tele-oncology platforms, guideline navigators, and computational biomarkers (radiomics, pathomics, ctDNA kinetics dashboards).",
        ],
        "bullets": [
            "RWE ≠ anecdotal case series — requires pre-specified questions, quality curation, statistics.",
            "Digital biomarker: objective, quantifiable physiologic/molecular data collected via digital means (incl. assays with digital pipelines).",
        ],
        "mechanism": [
            ("RWD sources", "EHR / claims / registry / devices"),
            ("Curation", "Ontology mapping, abstraction"),
            ("Analysis", "Causal methods / ML"),
            ("RWE output", "Effectiveness, safety, QoL"),
            ("Action", "Label, guideline, care pathway"),
        ],
    },
    {
        "heading": "3. RWE vs RCT — complementary roles & bias",
        "level": 1,
        "paragraphs": [
            "RCTs maximize internal validity (randomization, eligibility, protocol therapy) but may under-represent elderly, comorbid, rare genotypes, and LMIC populations. RWE maximizes external validity — how therapies perform in routine care — but suffers confounding, selection bias, immortal-time bias, misclassification, and missingness.",
            "Exam answer must list biases and mitigation: target trial emulation, propensity scores/IPW, instrumental variables, sensitivity analyses, structured abstraction (not billing codes alone), and pre-registration of protocols.",
        ],
        "bullets": [
            "RCTs answer efficacy under ideal conditions; RWE answers effectiveness in practice.",
            "Never claim RWE ‘replaces’ phase III OS trials for novel mechanisms without caveat.",
            "Hybrid designs: pragmatic trials, EHR-embedded randomization.",
        ],
        "flowchart": [
            "Clinical question",
            "Need internal validity? → RCT/pragmatic trial",
            "Need generalizability/rare subgroup? → curated RWE",
            "Regulatory safety signal? → pharmacovigilance RWD",
            "Feed guidelines & shared decisions",
        ],
        "flowchart_title": "Choosing evidence type",
    },
    {
        "heading": "4. Flatiron-type evidence & oncology learning health systems",
        "level": 1,
        "paragraphs": [
            "Oncology-specific EHR networks (e.g., Flatiron Health-style curated datasets) combine structured fields with trained abstraction of unstructured notes — enabling large cohort studies on sequencing, outcomes by biomarker, and post-marketing effectiveness. "
            "Examples of use: validating trial OS in broader NSCLC/breast populations, describing uptake of ADCs/IO, and identifying disparities.",
            "Limitations: US-centric networks may not mirror Indian NCG realities; immortal time when defining index dates; incomplete ECOG/LDH; residual confounding by indication.",
        ],
        "table_trials": [
            ("Flatiron / EHR cohort studies", "Effectiveness of TKIs/IO/ADCs in routine care"),
            ("Cancer registry linkage", "Population survival & equity analyses"),
            ("Pragmatic/PCORnet-style", "Embedded comparative effectiveness"),
        ],
        "pearls": [
            "Name ‘confounding by indication’ — sicker patients get drug X → biased OS.",
        ],
    },
    {
        "heading": "5. Digital biomarkers — ctDNA and beyond",
        "level": 1,
        "paragraphs": [
            "ctDNA is the flagship molecular digital biomarker: quantitative variant allele fractions, MRD detection after curative therapy (CRC, breast, lymphoma emerging), early relapse lead-time, and resistance mutation detection (EGFR C797X, BRCA reversions, KRAS second hits).",
            "Other digital biomarkers: wearable activity/HRV as frailty proxies, continuous glucose with some regimens, AI pathomics grading, radiomics risk scores. Emphasize analytical validation → clinical validation → clinical utility before care changes.",
        ],
        "bullets": [
            "ctDNA MRD+ → escalate? MRD− → de-escalate? — trial-dependent; do not freelance outside evidence.",
            "False negatives if non-shedding tumors; false positives from CHIP (esp. TP53/DNMT3A).",
            "Preanalytics: tube type, time-to-spin, assay LOD matter.",
        ],
        "flowchart": [
            "Define clinical decision (adjuvant escalation etc.)",
            "Choose validated assay",
            "Serial ctDNA draws",
            "Interpret with CHIP/imaging context",
            "Act only if utility proven / trial",
        ],
        "flowchart_title": "ctDNA digital biomarker loop",
    },
    {
        "heading": "6. Remote monitoring & ePROs for toxicity",
        "level": 1,
        "paragraphs": [
            "Electronic patient-reported outcomes (ePROs) and remote monitoring detect symptomatic toxicities (diarrhea on SG/TKIs, dyspnea suggesting ILD on T-DXd, fever on IO) earlier than clinic visits. Randomized data (e.g., Basch et al. classic ePRO trials) showed improved QoL, fewer ER visits, and in some settings survival signals with proactive outreach.",
            "Implementation: scheduled ePRO questionnaires, alert thresholds to nurses, tele-visits, home vitals. Especially relevant for oral targeted therapy adherence and ADC/IO outpatient models.",
        ],
        "table_doses": [
            ("Operational ‘dose’", "ePRO cadence: e.g., weekly during high-risk cycles; alerts → call within 24 h"),
            ("Staffing", "Nurse navigator FTEs per monitoring panel"),
        ],
        "bullets": [
            "Alert fatigue is real — tune thresholds.",
            "Digital divide: older/rural patients need phone backup pathways.",
            "Document remote grading using CTCAE-aligned ePRO items.",
        ],
        "pearls": [
            "Tie ePRO story to ADC ILD and IO colitis — concrete oncology hooks.",
        ],
    },
    {
        "heading": "7. AI clinical decision support",
        "level": 1,
        "paragraphs": [
            "AI CDS spans: guideline-based pathway engines, NLP extraction of stage/biomarkers from notes, imaging AI (pulmonary nodules, mammography), pathology AI (PD-L1 quantitation assist), and trial-matching algorithms. Large language models can draft education materials but risk hallucinations — must be clinician-supervised.",
            "Evaluation: AUC is insufficient; need prospective silent-mode then interventional trials, calibration across hospitals, and bias audits (skin tone in dermatology AI; sex/ethnicity in risk models).",
        ],
        "bullets": [
            "Keep human-in-the-loop for treatment changes.",
            "Cybersecurity & PHI governance essential.",
            "Explainability vs black-box trade-offs for exams.",
        ],
        "mechanism": [
            ("Inputs", "EHR + imaging + genomics"),
            ("Model", "Rules / ML / LLM"),
            ("CDS output", "Options ranked + citations"),
            ("Clinician", "Accept / modify / reject"),
            ("Outcomes capture", "Learning health system"),
        ],
    },
    {
        "heading": "8. NCCN Guidelines Navigator & digitized pathways",
        "level": 1,
        "paragraphs": [
            "NCCN Guidelines Navigator is a digital navigation layer over NCCN Guidelines — launched/expanded including breast cancer and broadening across diseases (supportive care theme in 2026 summaries). It helps clinicians traverse branched algorithms, categories of evidence, and updates more efficiently than static PDFs.",
            "Exam angle: living guidelines + digital tools reduce lag between evidence and practice but still require local adaptation (NCG resource stratification, CDSCO approvals, cost).",
        ],
        "nccn": {
            "versions": [
                "NCCN Guidelines Navigator (digital; breast launch & expansion)",
                "Disease Guidelines 2026/2027 (various)",
            ],
            "bullets": [
                "Navigator digitizes branching NCCN algorithms for point-of-care use.",
                "Expanding across diseases — cite as supportive/digital oncology 2026 update.",
                "Categories of evidence (1/2A/2B) remain the language to quote in answers.",
                "Pair Navigator mention with a disease example (e.g., breast ADC/endocrine branches).",
            ],
        },
    },
    {
        "heading": "9. Regulatory uses of RWE",
        "level": 1,
        "paragraphs": [
            "Regulators (FDA/EMA frameworks) accept RWE for label expansions, rare disease approvals, post-marketing commitments, external control arms when randomization unethical/infeasible, and safety surveillance. Oncology examples include accelerated approvals with confirmatory evidence and dose optimizations informed by exposure–response plus RWD.",
            "India: CDSCO pharmacovigilance, and institutional ethics for registries. Emphasize transparency, audit trails, and assay companion diagnostic co-validation when RWE supports biomarker claims.",
        ],
        "bullets": [
            "External controls must match eligibility, endpoints, and concomitant care eras.",
            "RWE can refine dosing in frail populations under-represented in RCTs.",
            "Fake precision: large n does not fix bias.",
        ],
        "flowchart": [
            "Evidence gap identified",
            "Fit-for-purpose RWD?",
            "Pre-spec protocol + bias plan",
            "Regulator/HMA review",
            "Label / REMS / guideline update",
        ],
        "flowchart_title": "Regulatory RWE pathway",
    },
    {
        "heading": "10. Equity, ethics, and Indian/NCG context",
        "level": 1,
        "paragraphs": [
            "Digital oncology can widen disparities if smartphones, broadband, and genomic testing are uneven. Design inclusive monitoring (voice calls, vernacular ePROs). RWE from HIC EHRs may mislead LMIC dosing/supportive care capacity — NCG resource-stratified pathways still matter.",
            "Ethics: consent for secondary EHR research, data sovereignty, algorithmic bias, and commercial dataset incentives. Clinicians remain accountable for AI suggestions.",
        ],
        "bullets": [
            "Ayushman Bharat / public sector data could enable India-specific RWE if curated.",
            "Teach trainees critical appraisal of RWE papers (STROBE, TARGET trial emulation).",
        ],
    },
    {
        "heading": "11. Practical clinic workflow integrating tools",
        "level": 1,
        "paragraphs": [
            "Example workflow: new metastatic diagnosis → NGS/IHC → Navigator/NCCN pathway checklist → prescribe oral TKI/ADC → enroll in ePRO remote monitoring → ctDNA at milestones → registry contribution for RWE. MDT dashboards display toxicity alerts and imaging AI flags.",
        ],
        "flowchart": [
            "Diagnose + biomarker",
            "Guideline Navigator pathway",
            "Start therapy",
            "ePRO remote monitor",
            "ctDNA/imaging digital biomarkers",
            "Outcomes → registry RWE",
        ],
        "flowchart_title": "Integrated digital oncology clinic",
    },
    {
        "heading": "12. Limitations & failures to mention",
        "level": 1,
        "paragraphs": [
            "Overfitting AI, guideline digitization without funding for drugs, ctDNA acting without utility evidence, ePRO without nursing backbone, and RWE used to market low-value interventions. State clearly: digital tools amplify good clinical systems; they do not replace consent, examination, or RCTs for practice-changing efficacy claims.",
        ],
        "pearls": [
            "A balanced paragraph on limitations often separates average from excellent answers.",
        ],
    },
    {
        "heading": "13. Comparison table — RCT vs RWE vs digital tools",
        "level": 1,
        "paragraphs": [
            "Draw a 3-column table in the answer book.",
        ],
        "bullets": [
            "RCT: best causality; limited generalizability; slow; expensive",
            "RWE: generalizable; bias-prone; faster safety/uptake insights; Flatiron-type curation helps",
            "Digital tools: operationalize evidence (Navigator, ePRO, AI CDS); need validation & equity plans",
        ],
        "table_trials": [
            ("Basch ePRO RCTs", "Remote symptom monitoring → QoL ± survival signals"),
            ("ctDNA MRD trials (DYNAMIC-class etc.)", "Utility still indication-specific"),
            ("EHR RWE publications", "Post-approval effectiveness / sequencing patterns"),
        ],
    },
    {
        "heading": "14. NCCN 2026 / digital supportive themes + closing pearls",
        "level": 1,
        "paragraphs": [
            "Tie back to concrete 2026 clinical updates enabled by rapid evidence uptake (ATOMIC, EV+P, Dato-DXd, neoadjuvant melanoma) — digital navigators help deploy such changes. Exercise prescriptions and CVD risk pages also show guidelines incorporating non-drug digital/behavioral monitoring themes.",
        ],
        "nccn": {
            "versions": [
                "NCCN Guidelines Navigator",
                "Supportive care / disease guidelines 2026–2027",
            ],
            "bullets": [
                "Navigator expansion = examinable digital oncology fact.",
                "Living guidelines accelerate ADC/IO/KRAS pathway updates into practice.",
                "Remote monitoring aligns with outpatient ADC/oral TKI safety.",
                "RWE informs categories and ‘useful in certain circumstances’ listings over time.",
            ],
        },
        "pearls": [
            "Define RWE vs RCT bias explicitly.",
            "Name Flatiron-style curated EHR evidence.",
            "ctDNA = digital biomarker poster child; mention CHIP pitfall.",
            "ePRO remote monitoring improves symptom control — cite Basch-type evidence.",
            "NCCN Guidelines Navigator + human oversight closing line.",
        ],
        "flowchart": [
            "RCT efficacy",
            "RWE effectiveness",
            "Digital deployment",
            "Monitor equity & bias",
            "Update guidelines",
        ],
        "flowchart_title": "Evidence-to-practice digital loop",
    },
]

__all__ = ["DEEP"]

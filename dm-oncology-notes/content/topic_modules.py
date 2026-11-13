"""Long-form topic modules to expand exam answers to 10–15 pages."""

from __future__ import annotations

import re


def _m(q: str, *pats: str) -> bool:
    return any(re.search(p, q, re.I) for p in pats)


def modules_for(question: str) -> list[dict]:
    q = question
    mods: list[dict] = []

    # Universal deep modules always appended
    mods.append({
        "heading": "A. Epidemiology & burden (write ½–1 page)",
        "level": 1,
        "paragraphs": [
            "Begin with global and Indian epidemiology when known (GLOBOCAN / ICMR / NCRP). State age distribution, sex ratio, "
            "and risk factors (tobacco, infection-related cancers such as HPV/HBV/HCV/H. pylori/HIV, obesity, inherited syndromes).",
            "Explain why incidence or mortality trends matter for screening and resource allocation. For rare diseases, state incidence per 100,000 and referral-center patterns.",
            "Link epidemiology to prevention: vaccination (HPV, HBV), tobacco control, hepatitis treatment, aspirin in selected molecular CRC, and lifestyle (exercise post-adjuvant CRC per NCCN 2026).",
        ],
        "bullets": [
            "One sentence on screening relevance (mammography, LDCT, FIT/colonoscopy, low-dose CT criteria).",
            "Mention hereditary fraction if applicable (Lynch, HBOC, FAP, MEN, VHL, HPRCC).",
            "State stage distribution at diagnosis in LMICs vs HIC if relevant to treatment sequencing.",
        ],
    })

    mods.append({
        "heading": "B. Historical evolution → modern standard (timeline)",
        "level": 1,
        "paragraphs": [
            "Examiners like a short timeline: historical surgery/RT/chemo era → targeted therapy era → immunotherapy/ADC/cellular therapy era.",
            "Highlight inflection trials that changed guidelines (e.g., imatinib IRIS; trastuzumab HERA; checkpoint inhibitors; ADCs; CAR-T approvals).",
            "End timeline with <b>NCCN 2026/2027</b> preferred regimens so the answer feels contemporary for Paper IV.",
        ],
        "flowchart": [
            "Cytotoxic chemotherapy era",
            "Molecular targeted therapy (TKIs/mAbs)",
            "Immunotherapy (CPI)",
            "ADCs / BiTEs / CAR-T / radioligands",
            "NCCN 2026 biomarker-stratified algorithms",
        ],
        "flowchart_title": "Therapeutic eras timeline",
    })

    mods.append({
        "heading": "C. Detailed differential diagnosis & pathology pearls",
        "level": 1,
        "paragraphs": [
            "List 5–7 differentials and the IHC/molecular discriminators. Pathology reports should include grade, LVI, margins, nodes, and required biomarkers.",
            "For hematologic topics: morphology → flow cytometry → cytogenetics → NGS panel → integrated WHO2022/ICC diagnosis.",
            "For CUP/unknown primary style questions: IHC algorithm (CK7/CK20, TTF1, CDX2, GATA3, PAX8, synaptophysin) plus NGS and MSI/HER2.",
        ],
        "bullets": [
            "Always write ‘correlate clinically with radiology and tumor markers’.",
            "State pre-analytical caveats (decalcification, fixation time) affecting HER2/ER assays.",
            "Liquid biopsy complements but does not always replace tissue.",
        ],
        "mechanism": [
            ("Morphology", "Light microscopy pattern"),
            ("IHC panel", "Lineage + predictive markers"),
            ("Cytogenetics", "Karyotype / FISH fusions"),
            ("NGS", "SNVs, indels, CNAs, MSI, TMB"),
            ("Integrated Dx", "WHO/ICC + AJCC stage"),
        ],
    })

    mods.append({
        "heading": "D. Multidisciplinary care pathway & sequencing",
        "level": 1,
        "paragraphs": [
            "Describe roles: medical oncology, surgical oncology, radiation oncology, radiology, pathology, palliative care, genetics, psycho-oncology, rehabilitation, and clinical trials unit.",
            "Sequencing principles: treat drivers first when OS-proven; use neoadjuvant therapy to downstage and guide adjuvant escalation; avoid overlapping severe toxicities; protect future options (e.g., cumulative cardiotoxicity, neuropathy).",
            "For oligometastatic disease discuss local therapy (surgery/SBRT/ablation) plus systemic therapy — prostate NCCN 2026 explicitly incorporates metastasis-directed therapy in selected APMS disease.",
        ],
        "bullets": [
            "Document MDT minutes in the file — also good exam phrase.",
            "Re-staging after neoadjuvant before definitive local therapy.",
            "Early palliative care improves QoL and sometimes survival in metastatic settings.",
        ],
        "flowchart": [
            "Diagnosis confirmed",
            "MDT meeting",
            "Intent: curative / non-curative",
            "Sequence local ↔ systemic",
            "Supportive + survivorship plan",
        ],
    })

    # Disease-specific long modules
    if _m(q, r"her2|breast|trastuzumab|tnbc|emilia|axilla|dcis"):
        mods.append({
            "heading": "E. Breast oncology deep notes (HER2 / subtypes)",
            "level": 1,
            "paragraphs": [
                "ASCO/CAP HER2 testing: IHC 0, 1+, 2+ (equivocal→ISH), 3+. HER2-low (1+ or 2+/ISH−) and ultralow categories matter after DESTINY-Breast04/06.",
                "Early disease: prefer dual HER2 blockade neoadjuvant for ≥T2 or node-positive; residual disease → adjuvant T-DM1 (KATHERINE). Node-positive adjuvant benefit from pertuzumab (APHINITY).",
                "Metastatic: CLEOPATRA 1L; DESTINY-Breast03 establishes T-DXd over T-DM1 in 2L; HER2CLIMB for brain metastases; continue anti-HER2 beyond progression with changing partners.",
                "Endocrine + anti-HER2 strategies exist for HR+/HER2+; NCCN 2026 adds nuances (e.g., abemaciclib+fulvestrant+trastuzumab Cat 2B in selected HR+/HER2+ advanced disease).",
                "TNBC: KEYNOTE-522 perioperative pembrolizumab; metastatic CPS≥10 pembrolizumab+chemo; sacituzumab govitecan (ASCENT); PARPi if gBRCA; ADCs evolving.",
            ],
            "bullets": [
                "Cardiotoxicity monitoring with HER2 agents + anthracyclines sequencing.",
                "Pregnancy: avoid anti-HER2 until after delivery.",
                "NCCN 2026: imlunestrant for ESR1-mutant HR+/HER2−; neratinib options for HER2-mutant MBC; erdafitinib for FGFR alterations.",
            ],
            "table_trials": [
                ("CLEOPATRA", "H+P+docetaxel OS landmark 1L HER2+ mBC"),
                ("DESTINY-Breast03", "T-DXd ≫ T-DM1 2L"),
                ("KATHERINE", "Adjuvant T-DM1 if residual disease"),
                ("HER2CLIMB", "Tucatinib triplet; CNS activity"),
                ("DESTINY-Breast04/06", "HER2-low / ultralow ADC expansion"),
                ("OlympiA", "Adjuvant olaparib gBRCA HER2−"),
            ],
        })
        mods.append({
            "heading": "F. HER2 testing interpretation workshop",
            "level": 1,
            "paragraphs": [
                "Spend almost a full page on testing — common 15-mark theme (Jan 2024 paper).",
                "Preanalytics: cold ischemia, fixation 6–72 h in 10% NBF; avoid decalcified bone for HER2 if possible.",
                "Discordance between core and excision: retest if heterogenous, grade/histology unexpected, or residual disease after NAT.",
                "ISH methods: dual-probe HER2/CEP17; ratios and copy number cutoffs per ASCO/CAP updates; polysomy interpretation pitfalls.",
            ],
            "flowchart": [
                "IHC performed",
                "0 / 1+ → HER2-negative (consider HER2-low reporting)",
                "2+ → reflex ISH",
                "3+ → HER2-positive",
                "Treat per early vs metastatic algorithms + NCCN 2026",
            ],
        })

    if _m(q, r"lung|nsclc|egfr|osimertinib|alk|sclc|dato"):
        mods.append({
            "heading": "E. Thoracic oncology deep notes",
            "level": 1,
            "paragraphs": [
                "Molecular first in advanced nonsquamous NSCLC; consider in squamous with never-smoker/young features. PD-L1 TPS guides IO if driver-negative.",
                "EGFR 1L options 2026: osimertinib alone; osimertinib+platinum/pemetrexed (FLAURA2); amivantamab+lazertinib (MARIPOSA) — NCCN Cat 1 preferred combinations.",
                "Post-progression after osi+chemo: Dato-DXd preferred (NCCN 2026). Resistance testing: tissue/liquid for MET, C797X, fusions, histologic transformation.",
                "Early NSCLC: adjuvant osimertinib (ADAURA); perioperative IO trials; unresectable III durvalumab (PACIFIC) vs osi (LAURA) if EGFR+.",
                "SCLC ES: chemo-IO then consider lurbinectedin+atezolizumab maintenance per NCCN 2026 update in selected patients.",
            ],
            "table_doses": [
                ("Osimertinib", "80 mg PO daily"),
                ("FLAURA2 chemo", "Platinum + pemetrexed with osi"),
                ("Amivantamab + lazertinib", "IV amivantamab + lazertinib 240 mg PO daily"),
                ("Dato-DXd", "TROP2 ADC — preferred subsequent per NCCN 2026 EGFR pathway"),
            ],
            "flowchart": [
                "NGS + PD-L1 + staging (AJCC 9th)",
                "Driver+? → targeted 1L",
                "Driver− → chemo±IO by PD-L1/histology",
                "Progression → resistance map → ADC/TKI/chemo",
            ],
        })

    if _m(q, r"colon|rectal|colorectal|mmr|msi|atomic|hipec"):
        mods.append({
            "heading": "E. Colorectal cancer deep notes",
            "level": 1,
            "paragraphs": [
                "Side and RAS/BRAF/MMR define therapy. Left RAS WT: EGFR mAb+chemo; right-sided less EGFR benefit. BRAF V600E: encorafenib+EGFR mAb ± chemo (BREAKWATER 1L NCCN).",
                "Stage III dMMR: ATOMIC — FOLFOX/CAPOX + atezolizumab preferred NCCN 2026. Neoadjuvant CPI for dMMR rectal — organ preservation possible.",
                "Aspirin 100–162 mg × 3 years if PIK3CA pathway alteration after surgery (stage II–III colon / stage I rectal) — NCCN 2026.",
                "Exercise ≥150 min/week after adjuvant therapy — formal NCCN recommendation.",
                "Metastatic sequencing: MSI-H → CPI; HER2 amplified RAS WT → anti-HER2; KRAS G12C → sotorasib/adagrasib combinations evolving; ctDNA for MRD under study.",
            ],
            "bullets": [
                "IDEA collaboration: 3 months CAPOX sufficient for many low-risk stage III.",
                "Watch-and-wait after TNT in selected rectal complete responders.",
                "HIPEC not routine for CRC peritoneal disease outside trials/selected centers.",
            ],
        })

    if _m(q, r"\bcml\b|imatinib|asciminib|ponatinib"):
        mods.append({
            "heading": "E. CML deep notes",
            "level": 1,
            "paragraphs": [
                "Pathogenesis: BCR::ABL1 constitutive tyrosine kinase. Diagnosis: CBC, peripheral smear, bone marrow, karyotype, quantitative PCR IS.",
                "Risk scores: Sokal/EURO/ELTS. Choose TKI by risk, age, comorbidities (dasatinib pleural effusion/PH; nilotinib vascular/metabolic; imatinib edema/muscle cramps).",
                "ELN milestones: BCR::ABL1 ≤10% at 3 mo, ≤1% at 6 mo, ≤0.1% (MMR) at 12 mo ideal. Failure → mutation analysis + switch.",
                "T315I: ponatinib or asciminib. Advanced phase: optimize TKI ± chemo and consider allograft.",
                "Treatment-free remission: typically ≥3 y TKI, sustained MR4/MR4.5, structured molecular monitoring.",
            ],
            "table_doses": [
                ("Imatinib", "400 mg daily CP"),
                ("Dasatinib", "100 mg daily"),
                ("Nilotinib", "300 mg BID newly diagnosed"),
                ("Ponatinib", "OPTIC response-adapted"),
                ("Asciminib", "80 mg daily or 40 mg BID per label/line"),
            ],
        })

    if _m(q, r"\baml\b|apml|apl|flt3|venetoclax|mds"):
        mods.append({
            "heading": "E. AML / myeloid deep notes",
            "level": 1,
            "paragraphs": [
                "Fit induction: 7+3 ± FLT3 inhibitor (midostaurin/quizartinib per mutation). Unfit: HMA+venetoclax (VIALE-A).",
                "APL separate: ATRA+ATO (±ida) with meticulous coagulopathy management — highest curability.",
                "ELN 2022 risk guides allograft timing. MRD (flow/NGS) increasingly guides consolidation.",
                "NCCN 2026: ziftomenib for R/R NPM1; revumenib for R/R (menin); olutasidenib IDH1 option; intensive chemo+venetoclax combinations Cat 2B.",
            ],
            "flowchart": [
                "Suspect AML → urgent BM + genetics",
                "APL? → ATRA immediately",
                "Fit vs unfit + ELN risk + mutations",
                "Induction → consolidation ± allo-HCT",
                "R/R → targeted options / trial / HCT",
            ],
        })

    if _m(q, r"myeloma|bortezomib|teclistamab|bcma|daratumumab|proteasome"):
        mods.append({
            "heading": "E. Multiple myeloma deep notes",
            "level": 1,
            "paragraphs": [
                "IMWG diagnosis with CRAB/SLiM. Risk: R-ISS / IMS-IMWG high-risk genetics (del17p, t(4;14), t(14;16), 1q, etc.).",
                "Induction quadruplets (Dara-VRd / Isa-VRd) + ASCT in fit patients; maintenance len ± anti-CD38 in selected.",
                "R/R: triplets, anti-CD38, selinexor, belantamab combinations, bispecifics (teclistamab, talquetamab, elranatamab, linvoseltamab), BCMA CAR-T.",
                "NCCN 2026/2027: Tec+Dara Cat 1 early relapse PI/IMiD refractory (MajesTEC-3); belantamab+Vd; linvoseltamab later lines.",
            ],
            "bullets": [
                "Supportive: bone (zoledronic acid/denosumab), VTE prophylaxis with IMiDs, infection vaccines, neuropathy care.",
                "Response including MRD 10^-5.",
            ],
        })

    if _m(q, r"car.?t|adoptive|bite|blinatumomab|icans"):
        mods.append({
            "heading": "E. Cellular therapy & engagers deep notes",
            "level": 1,
            "paragraphs": [
                "CAR structure: scFv + hinge/transmembrane + costim (4-1BB or CD28) + CD3ζ. Manufacturing autologous vs emerging allogeneic/CAR-NK.",
                "BiTEs continuous infusion (blinatumomab) vs newer half-life extended engagers; step-up dosing to mitigate CRS.",
                "ASTCT CRS/ICANS grading mandatory knowledge. Tocilizumab for CRS; steroids for ICANS; anakinra in refractory protocols.",
                "NCCN pathways place CAR-T earlier in LBCL (ZUMA-7) and after BTKi/BCL2i in CLL (liso-cel).",
            ],
            "flowchart": [
                "Eligibility & bridging",
                "Apheresis → manufacture",
                "Lymphodepletion Flu/Cy",
                "Infusion",
                "CRS/ICANS surveillance D0–28",
                "Long-term infection/cytopenia care",
            ],
        })

    if _m(q, r"checkpoint|immuno|pd.?1|ctla|nivolumab|pembrolizumab|melanoma"):
        mods.append({
            "heading": "E. Immunotherapy deep notes",
            "level": 1,
            "paragraphs": [
                "CTLA-4 acts priming phase in lymphoid organs; PD-1/PD-L1 in peripheral effector phase. LAG-3 (relatlimab) additional checkpoint.",
                "Biomarkers: PD-L1, MSI/dMMR, TMB — imperfect. TME, gut microbiome modulation is an exam discussion point (2026 short note theme).",
                "Neoadjuvant IO preferred for resectable nodal melanoma (NCCN 2026). Combinations with VEGF in RCC; with chemo in lung/gastric; with ADC in bladder (EV+P).",
            ],
            "bullets": [
                "irAE timelines: skin/GI early; endocrine anytime; late neuropathies/myocarditis rare but deadly.",
                "Rechallenge decisions individualized after grade 2 resolution; avoid after grade 4 myocarditis/SJS etc.",
            ],
        })

    if _m(q, r"parp|olaparib|niraparib|rucaparib|hrd"):
        mods.append({
            "heading": "E. PARP inhibitor deep notes",
            "level": 1,
            "paragraphs": [
                "Mechanism: PARP trapping + synthetic lethality in HR-deficient cells. Indications span ovarian maintenance, breast (gBRCA), pancreas (POLO), prostate (HRR), and evolving combinations with ARPI.",
                "NCCN 2026 ovarian: PARPi narrowed in recurrent treatment sections; focus maintenance + biomarkers. Prostate: ADT+niraparib/abiraterone for BRCA2 APMS subsets.",
                "Toxicities: hematologic, GI, fatigue; rare MDS/AML — counsel. Resistance: reversion mutations restoring HR.",
            ],
            "table_doses": [
                ("Olaparib", "300 mg BID tablets"),
                ("Niraparib", "200–300 mg daily individualized"),
                ("Talazoparib", "1 mg daily (breast gBRCA)"),
            ],
        })

    if _m(q, r"adc|antibody.?drug|deruxtecan|sacituzumab|enfortumab|mirvetuximab|brentuximab"):
        mods.append({
            "heading": "E. Antibody–drug conjugate deep notes",
            "level": 1,
            "paragraphs": [
                "ADC anatomy: mAb + linker + payload. Cleavable linkers + permeable payloads → bystander effect (T-DXd). Non-cleavable (T-DM1) more intracellularly restricted.",
                "Payloads: microtubule inhibitors (DM1, MMAE) vs topoisomerase-I (DXd, SN-38).",
                "NCCN 2026 expands ADCs across tumors: T-DXd, Dato-DXd, SG, EV, mirvetuximab, belantamab combos, loncastuximab.",
            ],
            "mechanism": [
                ("mAb", "Targets HER2/TROP2/Nectin-4/FRα/BCMA/CD30"),
                ("Linker", "Cleavable vs non-cleavable"),
                ("Payload", "Topo-I or microtubule toxin"),
                ("Bystander", "Kills neighboring low-antigen cells"),
                ("Key toxicity", "ILD / neuropathy / hyperglycemia / ocular"),
            ],
        })

    if _m(q, r"gastric|flot|esophageal|claudin"):
        mods.append({
            "heading": "E. Gastric / EGJ deep notes",
            "level": 1,
            "paragraphs": [
                "Perioperative FLOT standard for fit resectable adenocarcinoma. MATTERHORN: FLOT+durvalumab Cat 1 if PD-L1+ (NCCN 2026).",
                "Metastatic biomarker split: HER2 → KN811 / T-DXd; Claudin18.2 → zolbetuximab; MSI → CPI; PD-L1 → chemo-IO; FGFR2b investigational (bemarituzumab).",
            ],
        })

    if _m(q, r"ovarian|hipec|mirvetuximab|relacorilant"):
        mods.append({
            "heading": "E. Ovarian cancer deep notes",
            "level": 1,
            "paragraphs": [
                "Primary cytoreduction vs NACT-IDS based on resectability. Maintenance bev and/or PARPi by BRCA/HRD and residual disease.",
                "Platinum-sensitive vs resistant definitions guide next therapy. NCCN 2026: nab-paclitaxel+relacorilant; pembro+paclitaxel±bev if CPS≥1; mirvetuximab for FRα+.",
                "HIPEC: OVHIPEC-1 selected newly diagnosed interval debulking context — discuss controversy and center expertise.",
            ],
        })

    if _m(q, r"bladder|urothelial|bcg|enfortumab|intravesical"):
        mods.append({
            "heading": "E. Bladder cancer deep notes",
            "level": 1,
            "paragraphs": [
                "NMIBC risk strata drive BCG vs chemo intravesical. BCG-unresponsive: pembrolizumab, nadofaragene, nogapendekin, gemcitabine system — cystectomy still preferred for many.",
                "MIBC: cisplatin-eligible NIAGARA perioperative; cisplatin-ineligible EV+P perioperative data; metastatic EV+P preferred 1L (EV-302).",
            ],
        })

    if _m(q, r"prostate|abiraterone|psma|nm.?crpc"):
        mods.append({
            "heading": "E. Prostate cancer deep notes",
            "level": 1,
            "paragraphs": [
                "mHSPC: ADT + ARPI ± docetaxel by volume/fitness. nmCRPC: SPARTAN/PROSPER/ARAMIS. mCRPC: sequencing ARPI, chemo, PARPi, radioligand, Sipuleucel-T selected.",
                "NCCN 2026: MDT for metachronous oligometastatic APMS; ADT+niraparib/abi for BRCA2; CVD risk page; PET tracer table.",
            ],
        })

    if _m(q, r"rcc|renal|cabozantinib|vegf"):
        mods.append({
            "heading": "E. RCC deep notes",
            "level": 1,
            "paragraphs": [
                "Clear cell vs non-clear cell. IMDC risk for 1L choice. NCCN 2026: nivo+ipi Cat 1 preferred; post-IO sequencing recalibrated; genomic testing in nccRCC for trials.",
            ],
        })

    if _m(q, r"transplant|gvhd|haplo|engraftment|conditioning"):
        mods.append({
            "heading": "E. Transplant deep notes",
            "level": 1,
            "paragraphs": [
                "Indications by disease/risk. Donor hierarchy. MAC vs RIC (comorbidity index). PTCy haplo platforms. GVHD acute vs chronic NIH criteria.",
                "Engraftment: ANC ≥500 for 3 days; platelet engraftment definitions; engraftment syndrome treatment with steroids.",
            ],
        })

    # Always add supportive + ethics expansion
    mods.append({
        "heading": "G. Supportive care mini-chapter",
        "level": 1,
        "paragraphs": [
            "Antiemetics (olanzapine-containing regimens for HEC), G-CSF primary/secondary prophylaxis, antimicrobial prophylaxis, mucositis care, nutrition (including TPN indications/contraindications), pain ladder + interventional techniques, thrombosis prevention (Khorana), growth factors, transfusion thresholds.",
            "Psychosocial distress screening, fertility preservation referral before gonadotoxic therapy, and survivorship clinics.",
        ],
        "bullets": [
            "Febrile neutropenia: risk assess; anti-pseudomonal beta-lactam; add antifungal if persistent.",
            "Checkpoint diarrhea: rule out infection then steroids promptly.",
            "ADC ILD algorithms — patient education on dyspnea.",
        ],
    })

    mods.append({
        "heading": "H. Model answer skeleton (time plan for 35 minutes)",
        "level": 1,
        "paragraphs": [
            "Minutes 0–3: definition + epidemiology + diagram outline. Minutes 3–12: biology + diagnosis. Minutes 12–25: management algorithm with doses/trials. "
            "Minutes 25–30: toxicities + NCCN 2026. Minutes 30–35: summary pearls + underline Category 1 regimens.",
        ],
        "bullets": [
            "Leave a half page blank early for a neat flowchart drawn once.",
            "Underline drug doses.",
            "Box the NCCN 2026 bullets.",
        ],
        "pearls": [
            "Currency + clarity > exhaustive rare regimens.",
            "Named trial + number beats unnamed claim.",
            "NCCN 2026 phrase is expected in Paper IV recent advances.",
        ],
    })

    mods.append({
        "heading": "K. Pitfalls, contraindications & ‘do not miss’ warnings",
        "level": 1,
        "paragraphs": [
            "List absolute/relative contraindications of key drugs (e.g., baseline ILD caution for T-DXd; severe autoimmune disease caution for CPI; T315I needs ponatinib/asciminib not 1G/2G TKI alone; "
            "ATRA differentiation syndrome in APL; TLS with venetoclax/Blincyto; HBV reactivation with anti-CD20/CPI).",
            "Drug–drug interactions and QT prolongation traps are classic viva points — mention checking concomitant meds (azoles, macrolides, acid suppressants with selected TKIs).",
            "Imaging pitfalls: pseudo-progression on IO; flare on bone scan; PET Deauville interpretation after immunomodulatory therapy.",
        ],
        "bullets": [
            "Always screen hepatitis B before anti-CD20, anthracyclines, and many systemic regimens.",
            "Pregnancy test before teratogenic agents (IMiDs — REMS; MTX; TKI counseling).",
            "Do not combine overlapping QT-prolonging agents without ECG plan.",
            "Document performance status — unfit vs fit changes entire AML/lymphoma pathway.",
        ],
        "flowchart": [
            "Checklist before cycle 1",
            "Infections / viral serology / ejection fraction / PFTs if needed",
            "Drug interaction review",
            "Consent for specific risks (ILD, CRS, infertility)",
            "Proceed / modify / defer",
        ],
    })

    mods.append({
        "heading": "L. Case vignette practice (apply the algorithm)",
        "level": 1,
        "paragraphs": [
            "Invent a short case in the answer: age, stage, biomarkers, comorbidities → your exact regimen with dose → expected monitoring → what you will do at progression. "
            "This shows applied knowledge and often gains examiner goodwill.",
            "Example template: “45-year-old, ECOG 1, biomarker X positive, no contraindication Y → start regimen Z at dose… per trial T / NCCN 2026 preferred. "
            "Assess response at interval N. At progression, re-profile for resistance mutation R and switch to agent S.”",
            "Add one geriatric or organ-dysfunction variant to show nuance (dose reduce, alternate preferred regimen, or best supportive care).",
        ],
        "bullets": [
            "Vignette 1: fit, biomarker-positive — preferred Cat 1 therapy.",
            "Vignette 2: comorbid/unfit — alternative regimen.",
            "Vignette 3: progression with resistance mutation — sequenced next line.",
            "Vignette 4: severe toxicity — hold, treat, rechallenge decision.",
        ],
    })

    mods.append({
        "heading": "M. One-page ‘wall chart’ summary (draw/box this)",
        "level": 1,
        "paragraphs": [
            "Reserve the penultimate page for a wall-chart style summary with four quadrants: (1) Biology (2) Work-up (3) Treatment lines (4) NCCN 2026 bullets. "
            "This mirrors how many toppers present long answers and helps hit the page target with high signal density.",
        ],
        "mechanism": [
            ("Quadrant 1", "Hallmark gene / pathway / figure"),
            ("Quadrant 2", "Must-order tests + staging"),
            ("Quadrant 3", "1L / 2L / 3L with doses"),
            ("Quadrant 4", "Trials + NCCN 2026 + toxicities"),
            ("Center", "MDT + patient goals"),
        ],
        "pearls": [
            "Wall chart + flowchart + trial table = visual completeness.",
            "Write ‘NCCN 2026’ in quadrant 4 explicitly.",
        ],
    })

    return mods

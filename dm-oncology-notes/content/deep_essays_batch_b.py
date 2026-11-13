"""Deep essay section banks — Batch B (Q349, Q350, Q361, Q362).

Exports DEEP = {qid: sections_list} for ReportLab/platypus PDF builder.
Section keys: heading, level, paragraphs, bullets, flowchart, flowchart_title,
mechanism, table_trials, table_doses, nccn{versions,bullets}, pearls.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Q349 — Feb 2023 Essay 1: MMR genes, testing, CPI biomarker
# ---------------------------------------------------------------------------

Q349: list[dict] = [
    {
        "heading": "1. Introduction & exam framing",
        "level": 1,
        "paragraphs": [
            "Mismatch repair (MMR) is a post-replication DNA repair system that corrects base–base "
            "mismatches and insertion–deletion loops arising mainly in microsatellite sequences. "
            "Loss of MMR → microsatellite instability–high (MSI-H) / deficient MMR (dMMR) phenotype → "
            "hypermutation, high neoantigen load, and exceptional sensitivity to PD-1/PD-L1 checkpoint "
            "inhibitors (CPIs) across tumour types (tissue-agnostic approvals).",
            "For a 15-mark answer structure: (1) genes and pathway, (2) cancers and Lynch syndrome, "
            "(3) testing modalities with interpretation pitfalls, (4) mechanistic link to CPI response, "
            "(5) landmark trials with numbers, (6) NCCN 2026 CRC pathways (ATOMIC; neoadjuvant rectal CPI), "
            "(7) exam pearls and a drawn algorithm.",
        ],
        "bullets": [
            "State predictive vs prognostic: dMMR/MSI-H is both prognostic (better stage-for-stage CRC "
            "prognosis historically) and strongly predictive of CPI benefit.",
            "Always contrast germline Lynch vs sporadic (often MLH1 promoter hypermethylation ± BRAF V600E).",
            "Quote KEYNOTE-177, CheckMate-8HW, KEYNOTE-158, and ATOMIC with primary endpoints.",
        ],
        "pearls": [
            "Open with a one-line definition of MMR → MSI-H → neoantigens → CPI — examiners mark this triad.",
            "Draw IHC 4-protein panel + reflex pathway once; it scores heavily.",
        ],
    },
    {
        "heading": "2. MMR genes and molecular pathway",
        "level": 1,
        "paragraphs": [
            "Core MutSα heterodimer = MSH2–MSH6 (recognises single-base mismatches and 1–2 bp loops). "
            "MutSβ = MSH2–MSH3 (larger insertion–deletion loops). MutLα = MLH1–PMS2 (endonuclease that "
            "recruits excision/resynthesis machinery). EPCAM deletions silence MSH2 by transcriptional "
            "read-through and are a recognised Lynch mechanism without MSH2 coding mutation.",
            "Biallelic inactivation (germline + second hit, or two somatic hits, or epigenetic silencing) "
            "abolishes MMR → MSI. Constitutional mismatch repair deficiency (CMMRD) = biallelic germline "
            "MMR mutations → childhood cancers (haematologic, brain, GI).",
        ],
        "mechanism": [
            ("Replication error", "Polymerase slip at microsatellites → mismatch / indel loop"),
            ("Recognition", "MutSα (MSH2–MSH6) or MutSβ (MSH2–MSH3) binds lesion"),
            ("Incision", "MutLα (MLH1–PMS2) endonuclease nick"),
            ("Excision / resynthesis", "EXOI, DNA pol δ, ligase restore correct sequence"),
            ("Failure (dMMR)", "Frameshift peptides → neoantigens; MSI-H genomic signature"),
        ],
        "bullets": [
            "Gene → protein pairs to memorise: MLH1↔PMS2 (co-loss common); MSH2↔MSH6.",
            "Isolated MSH6 or PMS2 loss can be subtle on IHC — do not dismiss without PCR/NGS if clinical suspicion high.",
            "POLE/POLD1 exonuclease mutations cause ultramutation (MSS often) but also CPI-responsive — mention as differential hypermutators.",
        ],
    },
    {
        "heading": "3. Role of MMR genes across cancers",
        "level": 1,
        "paragraphs": [
            "Lynch syndrome (LS) spectrum: colorectal (~lifetime risk 40–80% depending on gene), "
            "endometrial (especially MSH6/MLH1), gastric, ovarian, urothelial (upper tract classic for MSH2), "
            "small bowel, sebaceous tumours (Muir–Torre), brain (Turcot). Gene-specific penetrance matters: "
            "MSH6/PMS2 often later onset / endometrial-skewed; MLH1/MSH2 higher CRC risk.",
            "Sporadic MSI-H CRC (~12–15% of CRC): typically older patients, right-sided, BRAF V600E+, "
            "MLH1 promoter CpG island hypermethylation — not Lynch. Gastric, endometrial, and small subsets "
            "of pancreatic, biliary, prostate, and sarcoma also harbour dMMR/MSI-H. Pan-tumour prevalence "
            "~2–4% but enrichment in CRC/endometrial/gastric.",
        ],
        "bullets": [
            "Stage II CRC: MSI-H historically associated with good prognosis and limited fluoropyrimidine-alone benefit — classic exam line.",
            "Metastatic MSI-H CRC: CPI preferred over chemo first-line (KEYNOTE-177 / CheckMate-8HW).",
            "dMMR rectal cancer: neoadjuvant CPI can enable organ preservation (NCCN 2026 primary consideration).",
        ],
        "table_trials": [
            ("KEYNOTE-177", "1L pembrolizumab vs chemo MSI-H mCRC: mPFS 16.5 vs 8.2 mo; durable OS; chemo crossover"),
            ("CheckMate-8HW", "Nivo+ipi vs chemo (and vs nivo) MSI-H/dMMR mCRC — dual CPI PFS superiority"),
            ("KEYNOTE-158", "Pembro tissue-agnostic MSI-H/dMMR solid tumours — ORR ~34%; basis of agnostic label"),
            ("ATOMIC (NCCN 2026)", "Stage III dMMR colon: FOLFOX/CAPOX + atezolizumab preferred adjuvant pathway"),
        ],
    },
    {
        "heading": "4. Lynch vs sporadic — clinical and molecular distinction",
        "level": 1,
        "paragraphs": [
            "Universal tumour testing (IHC ± MSI) is standard for CRC and endometrial cancer in most guidelines. "
            "If MLH1/PMS2 loss: reflex BRAF V600E and/or MLH1 methylation. BRAF V600E+ or methylated MLH1 → "
            "sporadic pathway (usually stop germline testing unless strong pedigree). Intact BRAF and unmethylated "
            "MLH1 with IHC loss → refer genetics for germline MMR panel (± EPCAM).",
            "Amsterdam/Bethesda criteria are historical triage tools; universal testing catches more LS. "
            "Cascade testing of relatives after pathogenic germline variant is the prevention payoff.",
        ],
        "flowchart": [
            "CRC / endometrial tumour → MMR IHC (± MSI PCR/NGS)",
            "Proficient MMR (pMMR) / MSS → standard oncology pathway",
            "dMMR: MLH1±PMS2 loss? → BRAF V600E ± MLH1 methylation",
            "Methylated / BRAF+ → sporadic MSI-H (usually no germline)",
            "MSH2/MSH6/PMS2 isolated loss or unmethylated MLH1 loss → germline LS panel ± EPCAM",
            "Pathogenic germline variant → cascade testing + intensified surveillance",
        ],
        "flowchart_title": "Lynch triage after tumour MMR testing (draw this)",
        "pearls": [
            "Never call 'Lynch' on IHC alone — IHC shows phenotype; germline confirms syndrome.",
            "EPCAM deletion → MSH2 protein loss on IHC; include EPCAM in LS panels.",
        ],
    },
    {
        "heading": "5. Testing modalities — IHC for MMR proteins",
        "level": 1,
        "paragraphs": [
            "Four-antibody IHC (MLH1, MSH2, MSH6, PMS2) on formalin-fixed paraffin-embedded tumour is the "
            "workhorse. Loss of nuclear staining in tumour with retained internal control (stroma/lymphocytes) "
            "defines dMMR. Paired loss patterns: MLH1+PMS2; MSH2+MSH6; isolated MSH6 or PMS2 possible.",
            "Preanalytics: adequate fixation (typically 6–72 h, 10% NBF), avoid over-decalcification, "
            "report heterogeneity. Neoadjuvant therapy can weaken staining — interpret cautiously; correlate MSI.",
        ],
        "bullets": [
            "IHC = protein expression surrogate; does not directly prove MSI but correlates strongly.",
            "Indeterminate / focal loss → reflex MSI PCR or NGS MSI / MMR sequencing.",
            "Post-treatment rectal specimens: prefer pretreatment biopsy for MMR if possible.",
        ],
        "mechanism": [
            ("MLH1 loss", "Usually ± PMS2 loss; check methylation/BRAF"),
            ("MSH2 loss", "Usually ± MSH6 loss; think LS / EPCAM"),
            ("Isolated MSH6", "LS possible; MSI may be low/subtle"),
            ("Isolated PMS2", "LS possible; confirm with genetics"),
            ("All four retained", "pMMR phenotype — still consider POLE if ultramutated"),
        ],
    },
    {
        "heading": "6. Testing modalities — MSI PCR and NGS",
        "level": 1,
        "paragraphs": [
            "PCR MSI assays compare tumour vs normal at mononucleotide/dinucleotide loci (e.g., Bethesda/NCI "
            "panel or pentaplex mononucleotide panels). MSI-H typically ≥2/5 (or ≥30%) unstable markers; "
            "MSI-L = 1 marker; MSS = stable. Mononucleotide panels are more specific.",
            "NGS-based MSI / tumour mutational burden (TMB) from large panels estimates MSI from indel burden "
            "at homopolymers and reports MMR gene mutations. Advantages: simultaneous RAS/BRAF/POLE and "
            "theranostic genes. Pitfalls: low tumour purity, poor coverage of microsatellites, and "
            "MSH6-mutant tumours sometimes MSI-L/MSS on limited panels.",
        ],
        "bullets": [
            "Concordance IHC ↔ PCR is high (~90–95%); discordances need both modalities + genetics discussion.",
            "Liquid biopsy MSI is emerging but tissue remains gold standard for treatment decisions when available.",
            "For CPI eligibility, FDA labels accept IHC dMMR or PCR/NGS MSI-H per companion diagnostics.",
        ],
        "table_doses": [
            ("IHC MMR panel", "MLH1 / MSH2 / MSH6 / PMS2 nuclear stain; internal control mandatory"),
            ("PCR MSI", "Tumour vs normal; MSI-H if ≥2/5 (panel-dependent)"),
            ("NGS MSI/TMB", "Panel-based; report MMR variants + MSI score + TMB mut/Mb"),
            ("Germline LS panel", "MLH1, MSH2, MSH6, PMS2, EPCAM ± complementary assays for deletions"),
        ],
    },
    {
        "heading": "7. Interpretation workshop — pitfalls and reporting",
        "level": 1,
        "paragraphs": [
            "Common pitfalls: (1) scoring cytoplasmic stain as retained; (2) missing weak MSH6 after "
            "chemotherapy/radiotherapy; (3) calling LS without methylation/BRAF workup; (4) treating "
            "MSI-L as MSI-H; (5) ignoring clonal heterogeneity after neoadjuvant therapy.",
            "Report template should state method, antibodies/panel, result (dMMR vs pMMR or MSI-H/L/MSS), "
            "and recommended reflex tests. For exams, write a mini-algorithm and one sentence on "
            "genetic counselling triggers.",
        ],
        "flowchart": [
            "Obtain adequate tumour block (prefer pretreatment)",
            "Perform MMR IHC (± concurrent MSI)",
            "Discordant / equivocal → add orthogonal test (PCR or NGS)",
            "dMMR CRC/endometrial → BRAF/methylation triage if MLH1-pattern",
            "Counsel genetics if LS suspected; document CPI biomarker status for MDT",
        ],
        "flowchart_title": "MMR testing interpretation loop",
        "pearls": [
            "Exam trap: BRAF V600E in CRC supports sporadic MLH1 methylation — not LS.",
            "Exam trap: IHC loss without MSI-H still may qualify as dMMR for CPI if assay validated.",
        ],
    },
    {
        "heading": "8. Mechanism — why dMMR/MSI-H predicts CPI benefit",
        "level": 1,
        "paragraphs": [
            "Frameshift mutations in coding microsatellites generate mutant neopeptides presented on MHC-I/II. "
            "The inflamed TME of MSI-H tumours shows high CD8+ infiltration, upregulated PD-1/PD-L1, and "
            "interferon-γ signatures — priming for PD-1 blockade. CPIs release exhausted T cells to recognise "
            "these neoantigens → durable responses even in chemo-refractory disease.",
            "Resistance still occurs: antigen presentation defects (B2M, HLA LOH), JAK/STAT IFN-pathway loss, "
            "alternative checkpoints, and immunosuppressive myeloid programs. MSS tumours rarely respond to "
            "PD-1 alone — hence combination and biomarker research.",
        ],
        "mechanism": [
            ("dMMR", "Unrepaired indels at microsatellites"),
            ("Neoantigens", "Frameshift peptides → MHC presentation"),
            ("T-cell priming", "High TILs; IFN-γ inflamed phenotype"),
            ("Checkpoint up", "PD-1/PD-L1 adaptive resistance"),
            ("CPI unlock", "Anti–PD-1/PD-L1 ± CTLA-4 → durable control"),
        ],
        "bullets": [
            "Tissue-agnostic principle: biology > histology when MSI-H/dMMR.",
            "TMB-high overlaps but is not identical to MSI-H — do not conflate casually.",
            "CTLA-4 + PD-1 (nivo+ipi) deepens responses in MSI-H mCRC (CheckMate-8HW).",
        ],
    },
    {
        "heading": "9. Landmark CPI trials (quote numbers)",
        "level": 1,
        "paragraphs": [
            "Memorise phase, population, arms, and primary endpoint for four to six trials. Examiners "
            "expect KEYNOTE-177 medians and the tissue-agnostic KEYNOTE-158 ORR. Add ATOMIC for 2026 "
            "adjuvant CRC relevance and CheckMate-8HW for dual CPI.",
        ],
        "table_trials": [
            ("KEYNOTE-016/164", "Early signal: pembro in dMMR CRC — high ORR; launched MSI-H CPI era"),
            ("KEYNOTE-177 (Ph3)", "1L pembro vs chemo MSI-H mCRC: PFS 16.5 vs 8.2 mo; 5-y OS ~50%+ with crossover"),
            ("CheckMate-142", "Nivo ± ipi in prior-treated MSI-H mCRC — durable ORR; ipi adds depth"),
            ("CheckMate-8HW (Ph3)", "1L nivo+ipi vs chemo MSI-H/dMMR mCRC — superior PFS; dual CPI standard discussion"),
            ("KEYNOTE-158", "Pembro MSI-H non-CRC: ORR ~34%; DoR durable → tissue-agnostic approval"),
            ("ATOMIC / Alliance", "Adjuvant atezo + FOLFOX/CAPOX stage III dMMR colon — NCCN 2026 preferred"),
            ("Neoadjuvant dMMR rectal series", "Dostarlimab / other CPI — clinical CR and organ preservation possible"),
        ],
        "pearls": [
            "Write one HR or median per major trial — vague 'improved PFS' scores less.",
            "Mention chemo crossover in KEYNOTE-177 when discussing OS nuance.",
        ],
    },
    {
        "heading": "10. Therapeutic strategies & doses when MMR is the biomarker",
        "level": 1,
        "paragraphs": [
            "Metastatic MSI-H/dMMR solid tumours: anti–PD-1 monotherapy (pembrolizumab; nivolumab) or "
            "nivo+ipi in CRC per trial/label. Continue until progression/toxicity per protocol; "
            "pseudo-progression uncommon but known — confirm with clinical status ± repeat imaging.",
            "Localised disease shifts (NCCN 2026): stage III dMMR colon — chemo + atezolizumab pathway; "
            "dMMR locally advanced rectal — neoadjuvant CPI as primary consideration aiming for organ "
            "preservation. POLE/POLD1 ultramutated tumours: CPI benefit often extrapolated.",
        ],
        "table_doses": [
            ("Pembrolizumab", "200 mg IV Q3W or 400 mg IV Q6W (CRC and tissue-agnostic MSI-H/dMMR)"),
            ("Nivolumab", "240 mg Q2W or 480 mg Q4W; with ipilimumab per CheckMate CRC regimens"),
            ("Ipilimumab (CRC dual CPI)", "1 mg/kg with nivolumab per CheckMate-8HW/142 schedules — monitor irAE"),
            ("Atezolizumab (ATOMIC context)", "With FOLFOX or CAPOX adjuvant stage III dMMR — per protocol/NCCN"),
            ("Dostarlimab (rectal dMMR)", "Neoadjuvant PD-1 in highly selected organ-preservation pathways"),
        ],
        "flowchart": [
            "Confirm dMMR/MSI-H with validated assay",
            "Stage & primary site → MDT",
            "mCRC MSI-H → CPI ± dual CPI (preferred over chemo 1L)",
            "Other metastatic MSI-H → pembro (agnostic) / trial",
            "Stage III dMMR colon → chemo + atezo (NCCN 2026)",
            "dMMR rectal → neoadjuvant CPI pathway discussion",
        ],
        "flowchart_title": "MMR biomarker → therapy algorithm",
    },
    {
        "heading": "11. Toxicities, monitoring & supportive care",
        "level": 1,
        "paragraphs": [
            "Immune-related AEs (irAEs): dermatitis, colitis, hepatitis, endocrinopathies (thyroid, "
            "hypophysitis, adrenal), pneumonitis, nephritis, rarer myocarditis/neurotoxicity. Dual CPI "
            "increases grade ≥3 irAE rates — counsel and monitor closely.",
            "Management principles: hold CPI for ≥G2; steroids first-line for most; escalate to "
            "infliximab/vedolizumab (colitis), MMF (hepatitis), etc.; permanently discontinue for "
            "severe myocarditis/neurotoxicity. Baseline TSH, LFTs, creatinine; educate patients on red flags.",
        ],
        "bullets": [
            "Endocrine irAEs often need lifelong replacement even after CPI stop — do not 'taper off' thyroxine casually.",
            "Distinguish infection vs immune colitis before infliximab.",
            "Vaccinations and infection workup before intensifying immunosuppression.",
        ],
        "flowchart": [
            "Suspect irAE → grade (CTCAE)",
            "G1 → supportive ± continue",
            "G2 → hold CPI + consider steroids",
            "G3–4 → admit as needed; high-dose steroids ± second-line IS; specialty input",
            "Rechallenge only if benefit ≫ risk and toxicity resolved (never if life-threatening)",
        ],
        "flowchart_title": "irAE management loop",
    },
    {
        "heading": "12. NCCN 2026 updates relevant to MMR / MSI",
        "level": 1,
        "paragraphs": [
            "Weave NCCN Colon v3.2026 and Rectal v2.2026 bullets into the 'recent advances' paragraph. "
            "ATOMIC adjuvant atezolizumab for stage III dMMR and neoadjuvant CPI for dMMR rectal are "
            "the highest-yield 2026 lines. Also note aspirin for PIK3CA-altered resected CRC (orthogonal "
            "molecular point often paired in the same molecular workup discussion).",
        ],
        "nccn": {
            "versions": [
                "Colon Cancer v3.2026",
                "Rectal Cancer v2.2026",
                "NCCN immunotherapy / disease-specific MSI-H pathways",
            ],
            "bullets": [
                "ATOMIC: FOLFOX or CAPOX + atezolizumab preferred for stage III dMMR/MSI-H colon "
                "(benefit assumed to extend to POLE/POLD1 hypermutated in panel discussion).",
                "Checkpoint inhibitor neoadjuvant pathway is a primary consideration for dMMR rectal "
                "tumours — organ preservation possible.",
                "Universal MMR/MSI testing informs both hereditary triage and CPI eligibility.",
                "Metastatic MSI-H CRC: CPI-based 1L preferred; dual CPI (nivo+ipi) per evidence hierarchy.",
                "Aspirin 100–162 mg daily × 3 years after surgery for stage II–III colon (and stage I rectal) "
                "with somatic PIK3CA pathway alterations — triggers broad molecular profiling.",
                "Structured exercise ≥150 min/week after adjuvant CRC therapy — cite as supportive NCCN 2026 item.",
            ],
        },
        "pearls": [
            "Say 'NCCN Colon v3.2026 — ATOMIC preferred for stage III dMMR' verbatim in the closing box.",
        ],
    },
    {
        "heading": "13. Special situations & differentials",
        "level": 1,
        "paragraphs": [
            "CMMRD, Muir–Torre, and Turcot variants expand the syndromic discussion. Immunotherapy in "
            "LS-related non-CRC tumours follows agnostic principles. After CPI failure in MSI-H mCRC, "
            "options include chemo ± targeted therapy by RAS/BRAF/HER2, trials, and local therapies for "
            "oligoprogression while sometimes continuing CPI off-label/trial — acknowledge evidence gaps.",
            "Differentiate MSI-H from TMB-H MSS (e.g., some melanomas, NSCLC) — both may respond to CPI "
            "but mechanisms and labels differ. Polymerase proofreading deficiency (POLE) is the classic "
            "ultramutated MSS CPI-responsive mimic.",
        ],
        "bullets": [
            "Pregnancy and CPI: generally avoid; individualise only in life-threatening disease.",
            "Autoimmune disease: weigh flare risk; often still treat MSI-H metastatic disease with caution.",
            "Transplant recipients: CPI may precipitate rejection — multidisciplinary decision.",
        ],
    },
    {
        "heading": "14. Summary checklist & exam pearls",
        "level": 1,
        "paragraphs": [
            "Close the answer with a boxed pathway: genes → tests → Lynch triage → CPI mechanism → "
            "key trials → NCCN 2026. Underline that MMR is a pan-tumour predictive biomarker with "
            "hereditary implications beyond the index cancer.",
        ],
        "bullets": [
            "Genes: MLH1, MSH2, MSH6, PMS2 (+ EPCAM).",
            "Tests: IHC ± MSI PCR/NGS; methylation/BRAF for MLH1-pattern.",
            "Mechanism: neoantigens + inflamed TME → PD-1 benefit.",
            "Trials: KEYNOTE-177, 8HW, 158, ATOMIC.",
            "NCCN 2026: adjuvant atezo stage III dMMR; neoadjuvant CPI dMMR rectal.",
        ],
        "pearls": [
            "IHC loss patterns predict which gene to sequence — write the pairs.",
            "Sporadic MSI-H CRC = MLH1 methylation ± BRAF; Lynch ≠ MSI alone.",
            "KEYNOTE-177 mPFS 16.5 vs 8.2 mo is the number to memorise.",
            "ATOMIC + rectal neoadjuvant CPI are the 2026 'recent advances' clinchers.",
            "Always offer genetic counselling language when LS is possible.",
        ],
        "flowchart": [
            "Define MMR genes",
            "Show testing algorithm",
            "Explain CPI biomarker biology",
            "Table of trials with numbers",
            "NCCN 2026 box + 5 pearls",
        ],
        "flowchart_title": "35-minute answer time plan",
    },
]


# ---------------------------------------------------------------------------
# Q350 — Feb 2023 Essay 2: WHO 2022 myeloid / AML
# ---------------------------------------------------------------------------

Q350: list[dict] = [
    {
        "heading": "1. Introduction & exam framing",
        "level": 1,
        "paragraphs": [
            "WHO 2022 (5th edition) reorganised myeloid neoplasms around genetics-first definitions, "
            "narrowing morphology-only categories and aligning partly with ICC 2022. AML diagnosis, "
            "ELN 2022 genetic risk, measurable residual disease (MRD), and genomically targeted therapy "
            "(FLT3, IDH1/2, menin pathway) dominate modern management.",
            "15-mark skeleton: WHO myeloid map → AML diagnostic work-up → molecular panel → ELN 2022 "
            "risk table → fit vs unfit algorithms with doses → landmark trials → NCCN AML v5.2026 "
            "(ziftomenib NPM1 R/R, revumenib, HMA+ven, FLT3) → pearls.",
        ],
        "bullets": [
            "Separate APL (PML::RARA) immediately — different emergency pathway (ATRA±ATO).",
            "State blast threshold nuance: defining genetics can diagnose AML with <20% blasts in WHO 2022.",
            "End with allo-HCT indications tied to ELN risk and MRD.",
        ],
        "pearls": [
            "Open with 'genetics-first WHO 2022' — signals updated knowledge vs FAB-only answers.",
        ],
    },
    {
        "heading": "2. WHO 2022 myeloid malignancies — overview map",
        "level": 1,
        "paragraphs": [
            "Major WHO 2022 myeloid groups: clonal haematopoiesis / clonal cytopenia; myeloproliferative "
            "neoplasms (MPN: CML BCR::ABL1+, CNL, PV, ET, PMF, etc.); mastocytosis; myelodysplastic/"
            "myeloproliferative neoplasms (MDS/MPN); myelodysplastic neoplasms (MDS) with genetics-based "
            "entities (e.g., MDS with SF3B1, MDS with del(5q), MDS with biallelic TP53); AML with defining "
            "genetic abnormalities; AML defined by differentiation; secondary myeloid neoplasms; "
            "eosinophilic/TK-fusion disorders.",
            "Key philosophy: integrate morphology, immunophenotype, cytogenetics, and NGS. ICC 2022 is "
            "a parallel system — mention awareness without derailing into a comparison essay unless asked.",
        ],
        "bullets": [
            "CML remains BCR::ABL1-defined MPN — not lumped into AML until blast phase criteria met.",
            "MDS vs AML boundary softened when AML-defining genetics present.",
            "Therapy-related and myelodysplasia-related AML flagged for adverse biology / HCT planning.",
        ],
        "flowchart": [
            "CBC + smear + clinical context",
            "Bone marrow morphology + flow",
            "Karyotype / FISH + NGS myeloid panel",
            "Assign WHO 2022 entity (MDS / MPN / MDS-MPN / AML / other)",
            "Risk stratify (ELN / IPSS-M etc.) → therapy",
        ],
        "flowchart_title": "WHO 2022 myeloid diagnostic pathway",
    },
    {
        "heading": "3. AML — clinical presentation & urgent work-up",
        "level": 1,
        "paragraphs": [
            "AML presents with marrow failure (anaemia, neutropenia, thrombocytopenia), leukocytosis/"
            "leukostasis, DIC (especially APL), infection, or extramedullary disease (gum, skin, CNS). "
            "Urgent priorities: stabilise airway/breathing, treat infection, cytoreduce if leukostasis, "
            "correct coagulopathy, and obtain diagnostic marrow before non-urgent cytoreductive chemo "
            "when feasible — but never delay ATRA if APL suspected.",
        ],
        "bullets": [
            "Labs: CBC, smear, PT/INR, aPTT, fibrinogen, D-dimer, chemistry, TLS labs, viral serologies, HLA typing early if HCT candidate.",
            "Imaging/LP only as indicated (CNS symptoms, monoblastic phenotype, relapse work-up).",
            "Echo/ECG before anthracyclines; PS, comorbidities, geriatric assessment for fit vs unfit.",
        ],
        "flowchart": [
            "Suspect AML / APL",
            "Stabilize + DIC/TLS/leukostasis care",
            "ATRA immediately if APL possible",
            "BM aspirate/biopsy + flow + cytogenetics + NGS",
            "ELN risk + fitness → induction plan",
        ],
        "flowchart_title": "First 48 hours in suspected AML",
    },
    {
        "heading": "4. Diagnostic investigations in detail",
        "level": 1,
        "paragraphs": [
            "Morphology: blast percentage, Auer rods (myeloid), dysplasia. Flow cytometry: myeloid markers "
            "(MPO, CD13, CD33, CD117, CD34) vs monocytic (CD14, CD64) vs megakaryocytic; exclude mixed "
            "phenotype. Cytogenetics: karyotype essential for t(8;21), inv(16)/t(16;16), t(15;17), "
            "t(9;11), complex karyotype, etc.",
            "WHO 2022 AML with defining genetic abnormalities includes (examples): PML::RARA; RUNX1::RUNX1T1; "
            "CBFB::MYH11; KMT2A rearrangements; DEK::NUP214; MECOM; NPM1; CEBPA bZIP; and others — learn "
            "the concept that genetics trump a rigid 20% blast cutoff for several entities.",
        ],
        "table_doses": [
            ("BM aspirate + biopsy", "Morphology, iron stain as needed, trephine architecture"),
            ("Flow immunophenotyping", "Lineage assignment; baseline for MRD assays"),
            ("Conventional karyotype", "≥20 metaphases when possible; reflex FISH panels"),
            ("Molecular NGS panel", "NPM1, FLT3-ITD/TKD, IDH1/2, TP53, RUNX1, ASXL1, KRAS/NRAS, KIT, etc."),
            ("RT-PCR fusions", "Rapid PML::RARA; CBF fusions; KMT2Ar as available"),
        ],
    },
    {
        "heading": "5. Molecular testing — what to order and why",
        "level": 1,
        "paragraphs": [
            "At diagnosis order rapid FLT3 (ITD and TKD) because midostaurin/quizartinib timing matters with "
            "induction. NPM1, IDH1/2, TP53, and karyotype/FISH drive ELN risk and targeted options "
            "(ivosidenib/enasidenib/olutasidenib; menin inhibitors for NPM1/KMT2Ar). CBF AML: add KIT.",
            "MRD tools: NPM1 RT-qPCR, multiparameter flow MRD, NGS MRD — ELN MRD guidance informs "
            "consolidation/HCT. Repeat NGS at relapse for targetable clones (FLT3 acquisition, menin pathway).",
        ],
        "mechanism": [
            ("FLT3-ITD/TKD", "Constitutive FLT3 signalling → proliferation; target with TKI"),
            ("NPM1 mut", "Cytoplasmic NPM1; HOX expression; menin dependence"),
            ("KMT2A-r", "Menin–KMT2A oncogenic transcription → menin inhibitors"),
            ("IDH1/2 mut", "2-HG oncometabolite → differentiation block; IDH inhibitors"),
            ("TP53 / complex KY", "Chemo resistance; adverse ELN; consider HCT / trials"),
        ],
        "pearls": [
            "FLT3 results should return within days — write 'do not delay sending rapid FLT3'.",
            "NPM1+ FLT3-ITD allelic ratio nuances appear in ELN — mention ITD ratio if space.",
        ],
    },
    {
        "heading": "6. ELN 2022 risk stratification",
        "level": 1,
        "paragraphs": [
            "ELN 2022 favourable: t(8;21)/RUNX1::RUNX1T1; inv(16)/CBFB::MYH11; mutated NPM1 without "
            "FLT3-ITD; bZIP in-frame CEBPA mutations. Intermediate: mainly cytogenetic/molecular findings "
            "not favourable or adverse (including FLT3-ITD with NPM1 per updated rules — quote current "
            "ELN table in exam). Adverse: complex karyotype, inv(3)/MECOM, −5/−7, TP53, ASXL1, RUNX1 "
            "(as sole), KMT2Ar (many), myelodysplasia-related genetics, etc.",
            "Use ELN risk + MRD + patient fitness to decide consolidation intensity and allo-HCT in CR1. "
            "Adverse risk → HCT in CR1 if eligible; favourable → chemo consolidation if MRD-negative; "
            "intermediate → individualise with MRD and donor availability.",
        ],
        "bullets": [
            "Always present ELN as favourable / intermediate / adverse with ≥2 example lesions each.",
            "Therapy-related and MRC-AML often behave adverse regardless of some genetics.",
            "Reassess risk at relapse with new genetics.",
        ],
        "flowchart": [
            "Karyotype + NGS complete",
            "Map to ELN 2022 favourable / intermediate / adverse",
            "Integrate age, PS, comorbidities, MRD",
            "Favourable MRD− → chemo consolidation",
            "Adverse / MRD+ / intermediate selected → allo-HCT CR1",
        ],
        "flowchart_title": "ELN 2022 → consolidative intent",
    },
    {
        "heading": "7. Management — fit induction & consolidation",
        "level": 1,
        "paragraphs": [
            "Fit induction standard: cytarabine + anthracycline ('7+3'). Add midostaurin for FLT3-mutated "
            "(RATIFY) or quizartinib for FLT3-ITD (QuANTUM-First) per label/eligibility. CBF AML may "
            "use GO (gemtuzumab ozogamicin) in selected protocols. APL: ATRA+ATO (± chemo) — separate section.",
            "Consolidation: HiDAC cycles for favourable risk; bridge to allo-HCT for adverse/selected "
            "intermediate. Supportive care: antifungals, antibacterial prophylaxis per centre, transfusion, "
            "TLS monitoring, growth factors selectively.",
        ],
        "table_doses": [
            ("7+3 induction", "Cytarabine 100–200 mg/m² CIV D1–7 + daunorubicin 60 mg/m² D1–3 (or idarubicin 12 mg/m²)"),
            ("Midostaurin (FLT3)", "50 mg PO BID D8–21 each induction/consolidation cycle (RATIFY)"),
            ("Quizartinib (FLT3-ITD)", "Per QuANTUM-First with chemo — monitor QTc"),
            ("HiDAC consolidation", "Cytarabine 1–3 g/m² Q12h on D1,3,5 (age/centre-adjusted)"),
            ("GO (selected CBF/CD33)", "Fractionated GO with chemo per protocol — VOD risk counselling"),
        ],
        "pearls": [
            "Write exact 7+3 doses once — free marks.",
            "Anthracycline cardiotoxicity: baseline EF; lifetime dose tracking.",
        ],
    },
    {
        "heading": "8. Unfit / older AML — HMA + venetoclax backbone",
        "level": 1,
        "paragraphs": [
            "VIALE-A established azacitidine + venetoclax vs azacitidine in unfit newly diagnosed AML: "
            "median OS 14.7 vs 9.6 months; higher composite CR rates. Decitabine + venetoclax is an "
            "alternative HMA partner. Ramp venetoclax with TLS prophylaxis; adjust for azole antifungals "
            "(CYP3A).",
            "IDH1-mutated unfit: ivosidenib + azacitidine (AGILE OS benefit) or ivosidenib monotherapy "
            "in selected. NCCN 2026 reinforces HMA+ven after cytarabine-based induction failure and as "
            "frontline unfit standard.",
        ],
        "table_trials": [
            ("VIALE-A", "Aza + ven vs aza: mOS 14.7 vs 9.6 mo — unfit ND-AML standard"),
            ("AGILE", "Ivosidenib + aza vs aza in IDH1 mut — EFS/OS benefit"),
            ("RATIFY", "7+3 + midostaurin FLT3 mut — OS benefit"),
            ("QuANTUM-First", "Quizartinib + chemo FLT3-ITD — OS benefit"),
            ("ADMIRAL", "Gilteritinib vs salvage chemo R/R FLT3 — OS benefit"),
        ],
        "table_doses": [
            ("Azacitidine", "75 mg/m² SC/IV D1–7 (or D1–5/8–9 schedules) Q28D"),
            ("Venetoclax (AML)", "Ramp 100 → 200 → 400 mg daily with HMA; hold for cytopenias per label"),
            ("Ivosidenib", "500 mg PO daily (IDH1); differentiation syndrome watch"),
            ("Enasidenib", "100 mg PO daily (IDH2 R/R context)"),
        ],
    },
    {
        "heading": "9. Targeted agents — FLT3, IDH, menin (NPM1 / KMT2A)",
        "level": 1,
        "paragraphs": [
            "FLT3: midostaurin/quizartinib with induction; gilteritinib in R/R FLT3 (ADMIRAL). Monitor "
            "QTc, differentiation syndrome rare, interactions. IDH inhibitors: differentiation syndrome "
            "(treat like APL DS with steroids), QTc (ivosidenib), bilirubin (enasidenib).",
            "Menin inhibitors: revumenib for KMT2A-rearranged R/R AML (and related indications); "
            "ziftomenib for R/R NPM1-mutated AML — both appear in NCCN AML v5.2026. These exploit "
            "dependence on menin–KMT2A transcriptional complexes driving HOX/MEIS1.",
        ],
        "mechanism": [
            ("Menin–KMT2A complex", "Drives leukemogenic HOX program in KMT2Ar / NPM1"),
            ("Revumenib", "Menin inhibitor — KMT2Ar R/R AML (NCCN listed)"),
            ("Ziftomenib", "Menin inhibitor — R/R NPM1-mut AML (NCCN Cat 2A)"),
            ("Resistance themes", "Menin mutations / pathway reactivation — trial space"),
        ],
        "bullets": [
            "NCCN 2026 also lists intensive chemo + ven combinations (CLIA+ven; FLAG-IDA+ven) as Cat 2B options.",
            "Olutasidenib Cat 2B IDH1 option if not candidate for preferred/ivosidenib.",
            "Always send patients to allo-HCT evaluation in parallel with targeted salvage when curative intent remains.",
        ],
    },
    {
        "heading": "10. Relapsed/refractory AML algorithm",
        "level": 1,
        "paragraphs": [
            "Confirm relapse with marrow ± extramedullary assessment; repeat cytogenetics/NGS. Choose "
            "salvage by prior therapy, fitness, and targets: gilteritinib (FLT3), IDH inhibitors, "
            "menin inhibitors (NPM1/KMT2Ar), HMA+ven if not refractory to it, intensive salvage "
            "(FLAG-IDA ± ven), clinical trials, then HCT if CR2 achievable.",
        ],
        "flowchart": [
            "R/R AML → re-biopsy + rapid FLT3/NPM1/KMT2A/IDH/TP53",
            "Target present? → matched TKI / IDHi / menin inhibitor ± bridge",
            "No target / unfit → HMA+ven or trial",
            "Fit + need bulk reduction → intensive salvage ± ven (Cat 2B)",
            "CR/CRi → allo-HCT if eligible; else maintenance/trial",
        ],
        "flowchart_title": "R/R AML decision tree (include NCCN 2026 agents)",
        "table_trials": [
            ("ADMIRAL", "Gilteritinib R/R FLT3 — mOS ~9.3 vs 5.6 mo vs salvage chemo"),
            ("Menin programs", "Revumenib KMT2Ar responses; ziftomenib NPM1 R/R — NCCN 2026"),
            ("Bridging concept", "Targeted salvage → HCT consolidation whenever feasible"),
        ],
    },
    {
        "heading": "11. APL — do not mix into generic AML",
        "level": 1,
        "paragraphs": [
            "APL is a medical emergency defined by PML::RARA. Start ATRA on suspicion before genetic "
            "confirmation if coagulopathy/compatible morphology. Low/intermediate risk: ATRA+ATO "
            "(Lo-Coco / AML17 paradigms); high-risk: add chemo/GO per protocol. Manage DIC aggressively; "
            "watch differentiation syndrome (dexamethasone).",
        ],
        "table_doses": [
            ("ATRA", "45 mg/m²/day PO divided until CR (protocols vary)"),
            ("ATO", "0.15 mg/kg IV daily per induction/consolidation schedules"),
            ("Supportive", "Aggressive FFP/cryoprecipitate for DIC; platelets keep high thresholds"),
        ],
        "pearls": [
            "Exam killer omission: forgetting immediate ATRA when APL suspected.",
            "ATO toxicity: QTc prolongation — replete K/Mg; serial ECG.",
        ],
    },
    {
        "heading": "12. NCCN AML v5.2026 updates box",
        "level": 1,
        "paragraphs": [
            "Examiners increasingly expect named 2026 agents. Place this box near R/R and unfit sections.",
        ],
        "nccn": {
            "versions": ["Acute Myeloid Leukemia v5.2026"],
            "bullets": [
                "Ziftomenib Category 2A for relapsed/refractory NPM1-mutated AML.",
                "Revumenib listed for R/R AML in menin inhibitor / KMT2A rearrangement context.",
                "HMA (azacitidine/decitabine) + venetoclax pathway reinforced for unfit patients and after "
                "cytarabine-based induction failure.",
                "CLIA + venetoclax and FLAG-IDA + venetoclax Category 2B intensive options.",
                "Olutasidenib Category 2B IDH1 option if not candidate for preferred regimens / ivosidenib.",
                "Continue FLT3 inhibitor integration (midostaurin/quizartinib induction; gilteritinib R/R) per mutation.",
            ],
        },
        "pearls": [
            "Spell ziftomenib ↔ NPM1 and revumenib ↔ KMT2Ar explicitly — easy discriminator marks.",
        ],
    },
    {
        "heading": "13. Supportive care, infections & HCT principles",
        "level": 1,
        "paragraphs": [
            "TLS prevention, transfusion support, menstrual suppression, tumour fever vs infection "
            "work-up, antifungal prophylaxis in induction, and dental/line care matter for OS. "
            "Allo-HCT: matched sibling/unrelated/haplo with PTCY — indicate for adverse ELN, "
            "persistent MRD, secondary AML, and most CR2. Vaccinations and late-effects follow-up post-HCT.",
        ],
        "bullets": [
            "Leukostasis: hydroxyurea ± leukapheresis in selected hyperleukocytosis with symptoms.",
            "Avoid azole–venetoclax interaction errors — dose-adjust ven.",
            "Fertility counselling before induction when feasible.",
        ],
    },
    {
        "heading": "14. Summary — wall-chart answer & pearls",
        "level": 1,
        "paragraphs": [
            "Final page: WHO genetics-first map → AML work-up → ELN 2022 → fit 7+3±FLT3i vs unfit "
            "HMA+ven → targets (FLT3/IDH/menin) → HCT → NCCN 2026 names.",
        ],
        "bullets": [
            "WHO 2022: genetics can define AML without rigid 20% blasts.",
            "ELN 2022 drives HCT timing.",
            "VIALE-A and RATIFY/QuANTUM-First/ADMIRAL are core numbers.",
            "NCCN 2026: ziftomenib NPM1 R/R; revumenib; HMA+ven; FLT3 pathway.",
        ],
        "pearls": [
            "APL out of the gate with ATRA.",
            "Rapid FLT3 at diagnosis every time.",
            "VIALE-A mOS 14.7 vs 9.6 mo.",
            "Menin inhibitors are the 2026 'recent advances' punchline.",
            "MRD-guided consolidation is modern ELN practice — say it aloud in the answer.",
        ],
        "flowchart": [
            "WHO entity",
            "ELN risk",
            "Fit vs unfit induction",
            "Targeted add-ons / salvage",
            "HCT decision",
        ],
        "flowchart_title": "One-page AML wall chart",
    },
]


# ---------------------------------------------------------------------------
# Q361 — Jan 2024 Essay 1: HER2 testing + HER2+ metastatic breast cancer
# ---------------------------------------------------------------------------

Q361: list[dict] = [
    {
        "heading": "1. Introduction & exam framing",
        "level": 1,
        "paragraphs": [
            "HER2 (ERBB2) testing determines eligibility for anti-HER2 antibodies, tyrosine kinase "
            "inhibitors, and antibody–drug conjugates (ADCs). ASCO/CAP guidelines define IHC/ISH "
            "interpretation; DESTINY-Breast04/06 expanded therapy into HER2-low / ultralow disease. "
            "This essay focuses on testing plus therapeutic strategies for HER2-positive metastatic "
            "breast cancer (mBC), with NCCN Breast v9.2026 updates.",
            "Structure: biology → ASCO/CAP methods → interpretation/HER2-low → metastatic sequencing "
            "(CLEOPATRA → DB-03 → HER2CLIMB) → doses → toxicities → NCCN 2026 (note imlunestrant is "
            "HR+/HER2− ESR1 pathway; still discuss HER2 ADCs) → pearls.",
        ],
        "bullets": [
            "Clarify HER2-positive (IHC3+ or ISH-amplified) vs HER2-low (IHC1+ or 2+/ISH−).",
            "Metastatic HER2+ standard: dual blockade + taxane 1L; T-DXd 2L; tucatinib triplet for CNS.",
            "Flag NCCN 2026 imlunestrant as HR+ ESR1-mutant — not a HER2-directed drug.",
        ],
        "pearls": [
            "Examiners love a full-page testing algorithm before drugs — do not rush to CLEOPATRA.",
        ],
    },
    {
        "heading": "2. HER2 pathobiology & drug-target map",
        "level": 1,
        "paragraphs": [
            "HER2 is a ligand-independent receptor tyrosine kinase that heterodimerises (notably with "
            "HER3) to activate PI3K–AKT and MAPK cascades → proliferation and survival. Amplification "
            "of ERBB2 drives protein overexpression. Trastuzumab binds subdomain IV (ADCC + signalling "
            "effects); pertuzumab binds dimerisation domain II; TKIs (lapatinib, neratinib, tucatinib) "
            "block the kinase; ADCs deliver payload after internalisation.",
            "T-DXd (trastuzumab deruxtecan): cleavable linker + membrane-permeable topoisomerase-I "
            "payload → bystander effect, explaining activity in HER2-low. T-DM1: non-cleavable DM1 "
            "payload — less bystander, requires higher HER2 density.",
        ],
        "mechanism": [
            ("HER2 amp / overexpression", "Homodimers & HER2–HER3 → PI3K/MAPK"),
            ("Trastuzumab", "Subdomain IV; ADCC"),
            ("Pertuzumab", "Blocks HER2–HER3 dimerisation"),
            ("T-DXd", "Topo-I ADC; bystander kill; ILD risk"),
            ("Tucatinib", "HER2-selective TKI; CNS penetration"),
            ("Resistance", "PIK3CA, PTEN loss, incomplete blockade, CNS sanctuary"),
        ],
    },
    {
        "heading": "3. ASCO/CAP HER2 testing methods",
        "level": 1,
        "paragraphs": [
            "Primary testing: validated IHC on invasive carcinoma. IHC 0 / 1+ = negative (historically); "
            "2+ = equivocal → reflex ISH; 3+ = positive. ISH (dual-probe HER2/CEP17 preferred): "
            "report HER2 copy number and HER2/CEP17 ratio per ASCO/CAP cutoffs (classic positive: "
            "ratio ≥2.0 with HER2 copies ≥4; additional groups for monosomy/polysomy — quote groups "
            "if marks allow).",
            "Preanalytics: cold ischaemia minimised; fixation 6–72 h in 10% neutral buffered formalin; "
            "avoid strong decalcification for bone mets when possible; use validated assays and "
            "external QA. Repeat testing on metastatic site recommended (discordance ~10%).",
        ],
        "bullets": [
            "Core biopsy vs excision discordance: retest if unexpected histology/grade or residual disease after NAT.",
            "Heterogeneous amplification: score invasive component carefully; may need additional blocks.",
            "NGS ERBB2 mutation ≠ IHC overexpression — neratinib pathways for activating mutations (NCCN).",
        ],
        "table_doses": [
            ("IHC 0", "No staining or ≤10% incomplete faint — historically negative; note ultralow debates"),
            ("IHC 1+", "Incomplete faint >10% — HER2-low eligible if met criteria"),
            ("IHC 2+", "Weak–moderate complete membrane — reflex ISH"),
            ("IHC 3+", "Complete intense membrane >10% — HER2-positive"),
            ("ISH positive", "Per ASCO/CAP ratio/copy number groups — treat as HER2+"),
        ],
    },
    {
        "heading": "4. Interpretation workshop — HER2-low and ultralow",
        "level": 1,
        "paragraphs": [
            "HER2-low = IHC 1+ or IHC 2+ / ISH-negative. DESTINY-Breast04 showed T-DXd superiority "
            "over physician's choice chemo in previously treated HER2-low mBC (HR+ and HR− cohorts). "
            "DESTINY-Breast06 moved T-DXd earlier in chemo-naive HR+ HER2-low/ultralow after endocrine "
            "therapy. Reporting IHC 0 vs ultralow has therapeutic implications — pathology–oncology "
            "communication is mandatory.",
            "For classic HER2-positive metastatic disease, dual HER2 blockade strategies still require "
            "IHC3+ or ISH amplification — do not treat HER2-low with pertuzumab dual blockade as if HER2+.",
        ],
        "flowchart": [
            "Perform IHC on invasive tumour",
            "3+ → HER2-positive pathway",
            "2+ → reflex ISH → amp = HER2+; non-amp = HER2-low candidate",
            "1+ → HER2-low candidate (not HER2+ dual-blockade)",
            "0 → historically negative; consider ultralow reporting / DB06 context in HR+",
            "Metastatic retest when therapy-defining",
        ],
        "flowchart_title": "ASCO/CAP testing → therapy binning",
        "pearls": [
            "Say explicitly: HER2-low is not 'HER2-positive' — different drug algorithms.",
            "DB-04 mPFS ~10 vs 5 mo range (quote exact cohort numbers if memorised) — ADC expansion story.",
        ],
    },
    {
        "heading": "5. Staging work-up before metastatic HER2 therapy",
        "level": 1,
        "paragraphs": [
            "Confirm metastatic histology when feasible; restage with CT C/A/P ± bone scan/PET; brain "
            "MRI if symptoms or before regimens with CNS implications. Document ER/PR, HER2, prior "
            "neoadjuvant/adjuvant anti-HER2 exposure (trastuzumab, pertuzumab, T-DM1), anthracycline "
            "history, and baseline LVEF.",
            "De novo vs recurrent metastatic HER2+ may influence residual endocrine options if HR+ "
            "(continue endocrine ± anti-HER2 in selected maintenance settings).",
        ],
        "bullets": [
            "Echo/MUGA baseline and during trastuzumab/pertuzumab/ADC therapy.",
            "Pregnancy test when relevant — anti-HER2 contraindicated in pregnancy.",
            "gBRCA rarely changes HER2+ 1L choice but matters for later PARPi if HER2− phenotypes evolve.",
        ],
    },
    {
        "heading": "6. First-line HER2+ mBC — CLEOPATRA dual blockade",
        "level": 1,
        "paragraphs": [
            "CLEOPATRA: docetaxel + trastuzumab + pertuzumab vs docetaxel + trastuzumab + placebo in "
            "1L HER2+ mBC. Landmark OS improved to ~56–57 months with dual blockade; PFS benefit "
            "established new global standard. After chemo completion, continue H+P maintenance until "
            "progression/toxicity. Docetaxel typically ≥6 cycles if tolerated; some use paclitaxel backbones.",
            "If HR+/HER2+, endocrine therapy may be combined or sequenced with anti-HER2 maintenance "
            "after chemo — individualise. CNS screening as clinically indicated.",
        ],
        "table_trials": [
            ("CLEOPATRA", "H+P+docetaxel vs H+docetaxel: mOS ~57 vs ~40 mo — 1L standard"),
            ("PERUSE / real-world", "Taxane backbone flexibility with dual blockade"),
            ("PHEREXA / others", "Beyond 1L dual blockade lessons — sequencing context"),
        ],
        "table_doses": [
            ("Trastuzumab", "8 mg/kg IV load → 6 mg/kg Q3W (or SC fixed dose)"),
            ("Pertuzumab", "840 mg IV load → 420 mg Q3W with trastuzumab"),
            ("Docetaxel", "75 mg/m² IV Q3W (CLEOPATRA) × ≥6 cycles if tolerated"),
        ],
        "pearls": [
            "Memorise OS ~57 months — the CLEOPATRA number every examiner knows.",
        ],
    },
    {
        "heading": "7. Second-line and beyond — DESTINY-Breast03 (T-DXd)",
        "level": 1,
        "paragraphs": [
            "DESTINY-Breast03 randomised T-DXd vs T-DM1 after trastuzumab ± pertuzumab in HER2+ mBC. "
            "mPFS 28.8 vs 6.8 months (stunning separation); OS benefit confirmed on updates. T-DXd "
            "is preferred 2L for most patients without contraindications. Monitor interstitial lung "
            "disease/pneumonitis — hold permanently for grade ≥2 ILD per label algorithms; counsel on "
            "dyspnoea/cough.",
            "T-DM1 (EMILIA) remains an option if T-DXd unavailable/contraindicated or later lines. "
            "NCCN sequencing places T-DXd ahead of T-DM1 for eligible 2L patients.",
        ],
        "table_trials": [
            ("DESTINY-Breast03", "T-DXd vs T-DM1: mPFS 28.8 vs 6.8 mo; new 2L standard"),
            ("EMILIA", "T-DM1 vs lapatinib+capecitabine — historical 2L PFS/OS benefit"),
            ("DESTINY-Breast01/02", "Heavily pretreated HER2+ activity; DB02 vs TPC"),
            ("DESTINY-Breast04/06", "HER2-low / ultralow — ADC expansion (mention even in HER2+ essay)"),
        ],
        "table_doses": [
            ("T-DXd (breast)", "5.4 mg/kg IV Q3W — ILD monitoring mandatory"),
            ("T-DM1", "3.6 mg/kg IV Q3W — thrombocytopenia/LFTs/cardiac"),
        ],
    },
    {
        "heading": "8. CNS disease — HER2CLIMB and radiotherapy integration",
        "level": 1,
        "paragraphs": [
            "HER2CLIMB: tucatinib + trastuzumab + capecitabine vs placebo + trastuzumab + capecitabine "
            "in previously treated HER2+ mBC, including active brain metastases. Improved PFS/OS and "
            "intracranial outcomes — preferred systemic option when CNS disease is relevant. Local "
            "therapy (SRS/surgery/WBRT) remains essential for symptomatic lesions; coordinate sequencing.",
            "T-DXd also has intracranial activity signals — choose by disease tempo, prior TKI/ADC "
            "exposure, and toxicity profile (ILD vs diarrhoea/hand-foot from capecitabine/tucatinib).",
        ],
        "table_trials": [
            ("HER2CLIMB", "Tucatinib triplet: PFS/OS benefit; CNS activity practice-changing"),
            ("NALA", "Neratinib + capecitabine vs lapatinib + capecitabine — later-line option"),
            ("TBCRC / ADC CNS data", "T-DXd intracranial responses — evolving sequencing"),
        ],
        "table_doses": [
            ("Tucatinib", "300 mg PO BID with trastuzumab + capecitabine 1000 mg/m² BID D1–14 Q21D"),
            ("Neratinib", "240 mg PO daily (diarrhoea prophylaxis with loperamide mandatory)"),
            ("Lapatinib", "1250 mg daily with capecitabine in older regimens"),
        ],
        "flowchart": [
            "HER2+ mBC progression",
            "Prior H+P ± taxane?",
            "Yes → prefer T-DXd (DB-03) if eligible",
            "Active / progressive CNS? → consider tucatinib triplet (HER2CLIMB) ± local therapy",
            "Later lines → T-DM1 / neratinib / lapatinib regimens / trials / ADCs",
        ],
        "flowchart_title": "Metastatic HER2+ sequencing (exam flowchart)",
    },
    {
        "heading": "9. HR+/HER2+ metastatic nuances & NCCN 2026 adjacent updates",
        "level": 1,
        "paragraphs": [
            "HR+/HER2+ disease may use endocrine therapy with trastuzumab ± pertuzumab after chemo "
            "induction, or in frail patients. NCCN Breast v9.2026 lists abemaciclib + fulvestrant + "
            "trastuzumab as Category 2B in selected HR+/HER2+ unresectable/stage IV settings.",
            "Important clarity for exams: imlunestrant is added in NCCN 2026 for ESR1-mutated "
            "HR+/HER2− metastatic disease (Cat 2A other recommended) — it is not a HER2-targeted "
            "therapy. Mention it under 'NCCN 2026 breast updates' while keeping HER2 ADC pathways "
            "(T-DXd, and sacituzumab in other subtypes) in the ADC discussion.",
        ],
        "bullets": [
            "Neratinib ± trastuzumab or fulvestrant Cat 2A useful in certain circumstances for HER2-activating mutations in stage IV.",
            "Erdafitinib Cat 2A useful in certain circumstances for FGFR alterations in stage IV — molecular housekeeping.",
            "Continue anti-HER2 across lines while changing partners — classic teaching.",
        ],
    },
    {
        "heading": "10. Toxicities & monitoring table",
        "level": 1,
        "paragraphs": [
            "Cardiac dysfunction: risk with trastuzumab/pertuzumab especially after anthracyclines — "
            "hold if LVEF declines per criteria; cardio-oncology input. T-DXd: ILD/pneumonitis, nausea, "
            "cytopenias, alopecia. T-DM1: thrombocytopenia, transaminitis, cardiac. Tucatinib/capecitabine: "
            "diarrhoea, PPE, hepatotoxicity. Neratinib: early diarrhoea — mandatory prophylaxis.",
        ],
        "bullets": [
            "Educate on ILD symptoms before cycle 1 of T-DXd; low threshold for CT chest.",
            "Do not rechallenge T-DXd after symptomatic ILD grade ≥2.",
            "Antidiarrhoeal protocols for neratinib; dose escalate only if using labelled ramp regimens.",
        ],
        "flowchart": [
            "Baseline LVEF + symptom education",
            "On therapy: cardiac q3mo early; LFTs; CBCs",
            "New dyspnoea on T-DXd → hold + CT + steroids per ILD algorithm",
            "LVEF drop → hold HER2 mAb; treat HF; rechallenge case-by-case",
        ],
        "flowchart_title": "Safety monitoring loop",
    },
    {
        "heading": "11. Landmark trial summary table (copy into answer book)",
        "level": 1,
        "paragraphs": [
            "Consolidate the must-quote trials with phase and take-home message.",
        ],
        "table_trials": [
            ("CLEOPATRA", "1L H+P+docetaxel — mOS ~57 mo"),
            ("EMILIA", "T-DM1 beats lapatinib+cape post-trastuzumab"),
            ("DESTINY-Breast03", "T-DXd ≫ T-DM1 — mPFS 28.8 vs 6.8 mo"),
            ("HER2CLIMB", "Tucatinib triplet — OS + CNS benefit"),
            ("NALA", "Neratinib+cape vs lapatinib+cape"),
            ("DESTINY-Breast04", "T-DXd in HER2-low — testing implications"),
            ("DESTINY-Breast06", "Earlier T-DXd in HR+ HER2-low/ultralow"),
            ("KATHERINE (early)", "Mention only if asked residual disease adjuvant contrast"),
        ],
    },
    {
        "heading": "12. NCCN Breast Cancer v9.2026 box",
        "level": 1,
        "paragraphs": [
            "Place near the end. Explicitly separate HR+ endocrine updates from HER2-directed standards.",
        ],
        "nccn": {
            "versions": ["Breast Cancer v9.2026"],
            "bullets": [
                "Metastatic algorithms remain stratified by HR and HER2 status, including HER2-low/ultralow "
                "ADC pathways (T-DXd; sacituzumab govitecan in other indicated subtypes).",
                "Imlunestrant added (Cat 2A other recommended) for ESR1-mutated HR+/HER2− recurrent "
                "unresectable/stage IV disease — note: HR+ pathway, not HER2-targeted.",
                "Abemaciclib + fulvestrant + trastuzumab Cat 2B for selected HR+/HER2+ advanced disease.",
                "Neratinib ± trastuzumab or fulvestrant Cat 2A useful in certain circumstances for "
                "HER2-activating mutations in stage IV.",
                "Erdafitinib Cat 2A useful in certain circumstances for FGFR1/2/3 fusion/mutation in stage IV.",
                "NCCN Guidelines Navigator digital tool launched for breast cancer pathways.",
            ],
        },
        "pearls": [
            "Write one sentence: 'Imlunestrant = ESR1-mutant HR+/HER2−; HER2+ mBC still sequenced CLEOPATRA → T-DXd → tucatinib.'",
        ],
    },
    {
        "heading": "13. Practical sequencing vignette",
        "level": 1,
        "paragraphs": [
            "Model case: 52-year-old, de novo ER+/HER2+ IHC3+ liver metastases, LVEF 62%. Start "
            "docetaxel+H+P (CLEOPATRA). After 6 cycles, maintain H+P ± endocrine. On progression "
            "(no ILD risk factors): T-DXd. Later isolated brain progression: add local SRS and "
            "consider tucatinib triplet if systemic options fit. Throughout: reassess goals, toxicities, "
            "and clinical trial eligibility.",
        ],
        "bullets": [
            "Oligoprogression: local therapy + continue systemic anti-HER2 when appropriate.",
            "Performance status decline: drop chemo, keep antibody/TKI if benefiting.",
            "Indian/NCG context: access to pertuzumab/T-DXd/tucatinib may gate sequence — state alternatives.",
        ],
    },
    {
        "heading": "14. Summary checklist & exam pearls",
        "level": 1,
        "paragraphs": [
            "Testing page + metastatic algorithm page + trial numbers page + NCCN box = complete answer.",
        ],
        "bullets": [
            "ASCO/CAP IHC → ISH; report HER2-low separately.",
            "1L CLEOPATRA; 2L DB-03 T-DXd; CNS HER2CLIMB.",
            "Doses: H 8→6 mg/kg; P 840→420; T-DXd 5.4 mg/kg; tucatinib 300 mg BID.",
            "NCCN v9.2026: imlunestrant is HR+ ESR1; HER2 ADCs still central.",
        ],
        "pearls": [
            "IHC2+ without ISH is incomplete — always reflex.",
            "DB-03 28.8 vs 6.8 mo is the ADC number of the decade.",
            "ILD counselling is part of informed consent for T-DXd.",
            "HER2CLIMB for brain mets — say 'active CNS included'.",
            "Do not misclassify imlunestrant as anti-HER2 in the NCCN paragraph.",
        ],
    },
]


# ---------------------------------------------------------------------------
# Q362 — Jan 2024 Essay 2: Practice-changing advances in early-stage NSCLC
# ---------------------------------------------------------------------------

Q362: list[dict] = [
    {
        "heading": "1. Introduction & exam framing",
        "level": 1,
        "paragraphs": [
            "Early-stage NSCLC (AJCC resectable I–III and unresectable stage III) has been transformed "
            "by adjuvant EGFR TKI (ADAURA), consolidation PD-L1 after CRT (PACIFIC), EGFR TKI after "
            "CRT (LAURA), and perioperative immunotherapy (CheckMate-816, KEYNOTE-671, AEGEAN). "
            "Molecular testing and AJCC 9th staging (NCCN NSCLC v9.2026) are now integral even before "
            "surgery or CRT.",
            "Answer plan: staging/molecular prerequisites → stage-by-stage advances with trial numbers → "
            "perioperative IO comparison → adjuvant IO → unresectable III pathways → doses → NCCN 2026 → pearls.",
        ],
        "bullets": [
            "Always bifurcate EGFR/ALK driver+ vs driver− pathways.",
            "Distinguish adjuvant (post-op) vs neoadjuvant vs perioperative (pre+post) designs.",
            "Quote EFS/DFS/OS endpoints carefully — examiners dock loose language.",
        ],
        "pearls": [
            "Opening line: 'Early NSCLC is no longer surgery ± chemo alone — biomarker-directed adjuvant/perioperative therapy is standard.'",
        ],
    },
    {
        "heading": "2. Staging update — AJCC 9th & work-up",
        "level": 1,
        "paragraphs": [
            "NCCN NSCLC v9.2026 adopts AJCC 9th edition staging. Practical work-up: contrast CT, PET-CT "
            "for staging, brain MRI for stage II–III (and selected IB), invasive mediastinal staging "
            "(EBUS/mediastinoscopy) when it changes therapy, and pulmonary function for resectability.",
            "Pathologic confirmation before systemic therapy. Multidisciplinary tumour board for borderline "
            "resectable IIIA/N2 disease — choose surgery-first vs definitive CRT vs neoadjuvant systemic.",
        ],
        "bullets": [
            "AJCC 9th nuances (updated T/N categories) — state that NCCN pathways now reference 9th edition.",
            "Never skip mediastinal staging in radiographic N2 before trimodality claims.",
            "Document smoking cessation — improves outcomes across modalities.",
        ],
        "flowchart": [
            "Suspect lung nodule / mass",
            "CT + PET + brain MRI (as indicated)",
            "Tissue diagnosis + PD-L1 + NGS (EGFR/ALK/ROS1/others)",
            "Invasive mediastinal staging if needed",
            "MDT: resectable vs borderline vs unresectable",
        ],
        "flowchart_title": "Early NSCLC staging & biomarker pathway",
    },
    {
        "heading": "3. Molecular testing in early-stage disease — why it changed practice",
        "level": 1,
        "paragraphs": [
            "ADAURA and LAURA made EGFR genotyping mandatory for resected and unresectable stage III "
            "consideration of osimertinib. ALK and other drivers increasingly influence perioperative "
            "IO decisions (limited IO benefit / prefer targeted approaches when data mature). Broad "
            "NGS on resection specimen or pretreatment biopsy is best practice.",
            "PD-L1 TPS still informs adjuvant IO discussions (IMpower010 enrichment) but perioperative "
            "trials enrolled broader populations — know each trial's biomarker subgroup.",
        ],
        "mechanism": [
            ("EGFR ex19del / L858R", "Adjuvant / post-CRT osimertinib sensitivity"),
            ("PD-L1 / T-cell inflamed", "IO benefit in perioperative & adjuvant settings"),
            ("Driver+ caution", "Prefer targeted path; IO benefit uncertain / lesser"),
            ("MRD / ctDNA (emerging)", "Risk stratification research — mention as future"),
        ],
        "pearls": [
            "Write: 'Send EGFR before finalising adjuvant plan — ADAURA window.'",
        ],
    },
    {
        "heading": "4. ADAURA — adjuvant osimertinib",
        "level": 1,
        "paragraphs": [
            "ADAURA: stage IB–IIIA EGFR-mutated (ex19del/L858R) NSCLC after complete resection ± "
            "adjuvant chemo, randomised to osimertinib 80 mg daily vs placebo for 3 years. Dramatic "
            "DFS benefit (overall and stage II–IIIA); CNS DFS improved; OS benefit confirmed on longer "
            "follow-up — practice-changing adjuvant targeted therapy. ADAURA2 explores extended "
            "duration questions in selected residual-risk settings.",
            "Practical: start after recovery from surgery/chemo; monitor labs/ECG as indicated; manage "
            "rash/diarrhoea/ILD rare risks; counsel adherence for 3 years.",
        ],
        "table_trials": [
            ("ADAURA", "Adjuvant osi vs placebo EGFR+ IB–IIIA: DFS HR ~0.20–0.27 range in early reports; OS benefit later confirmed"),
            ("ADAURA CNS", "Marked reduction in CNS recurrence — key exam line"),
            ("ADAURA2", "Extended adjuvant osi questions in higher-risk residual disease"),
        ],
        "table_doses": [
            ("Osimertinib adjuvant", "80 mg PO daily × 3 years (ADAURA)"),
        ],
        "pearls": [
            "OS confirmation elevated ADAURA from DFS-only criticism to firm standard.",
        ],
    },
    {
        "heading": "5. PACIFIC — unresectable stage III consolidation durvalumab",
        "level": 1,
        "paragraphs": [
            "PACIFIC: unresectable stage III NSCLC without progression after concurrent platinum CRT "
            "randomised to durvalumab vs placebo consolidation (up to 12 months). PFS and OS benefits "
            "established new standard for driver-negative (and historically all-comers) unresectable III. "
            "PD-L1 subgroup controversies exist for European labelling — discuss nuance: benefit clearest "
            "if PD-L1 ≥1% in some analyses, but practice varies by region.",
            "Start ideally within 42 days of CRT; exclude severe unresolved pneumonitis. Concurrent "
            "IO+CRT regimens are evolving but PACIFIC consolidation remains the classic standard.",
        ],
        "table_trials": [
            ("PACIFIC", "Durvalumab after cCRT: mPFS 16.8 vs 5.6 mo; 5-y OS ~43% vs 33%"),
            ("PACIFIC-2 / others", "Concurrent IO+CRT strategies — evolving, not yet universal replacement"),
        ],
        "table_doses": [
            ("Durvalumab consolidation", "10 mg/kg Q2W or 1500 mg Q4W × 12 months post-CRT (per label/practice)"),
            ("cCRT backbone", "Platinum doublet + 60 Gy-equivalent thoracic RT — centre protocols"),
        ],
    },
    {
        "heading": "6. LAURA — osimertinib after CRT in unresectable EGFR+ stage III",
        "level": 1,
        "paragraphs": [
            "LAURA addressed EGFR-mutated unresectable stage III disease: after definitive CRT, "
            "osimertinib vs placebo markedly improved PFS — establishing targeted consolidation/"
            "maintenance rather than default durvalumab for EGFR+ patients. This pairs with ADAURA "
            "to make EGFR testing essential across early/locally advanced NSCLC.",
            "Exam contrast table: PACIFIC (IO, all-comers/PD-L1) vs LAURA (EGFR TKI). Do not "
            "reflexively give durvalumab to EGFR+ unresectable III without considering LAURA.",
        ],
        "table_trials": [
            ("LAURA", "Osi vs placebo after CRT EGFR+ unresectable III — major PFS win; new standard discussion"),
            ("PACIFIC vs LAURA", "Driver− → durvalumab; EGFR+ → osimertinib pathway"),
        ],
        "table_doses": [
            ("Osimertinib (LAURA)", "80 mg PO daily after CRT until progression/toxicity per protocol"),
        ],
        "flowchart": [
            "Unresectable stage III NSCLC",
            "Complete cCRT without progression",
            "EGFR+ (ex19del/L858R)?",
            "Yes → osimertinib (LAURA)",
            "No / other → durvalumab consolidation (PACIFIC) if eligible",
        ],
        "flowchart_title": "Post-CRT consolidation fork",
    },
    {
        "heading": "7. CheckMate-816 — neoadjuvant chemo-IO",
        "level": 1,
        "paragraphs": [
            "CheckMate-816: resectable stage IB–IIIA NSCLC randomised to neoadjuvant nivolumab + "
            "platinum chemo vs chemo alone. Improved pCR and EFS; surgery feasibility maintained. "
            "Established neoadjuvant chemo-IO as a preferred option for eligible driver-negative "
            "resectable disease, especially nodal-positive.",
            "Practical pearls: restage after neoadjuvant; operate in window; path reports must include "
            "residual viable tumour percentage / pCR; manage irAEs without missing surgical timing.",
        ],
        "table_trials": [
            ("CheckMate-816", "Neoadjuvant nivo+chemo vs chemo: higher pCR; EFS benefit — FDA neoadjuvant approval basis"),
        ],
        "table_doses": [
            ("Nivolumab neoadjuvant", "360 mg Q3W with platinum doublet × 3 cycles (816 schedule)"),
            ("Platinum doublet", "Histology-based (pemetrexed nonsquamous; paclitaxel/gemcitabine squamous variants)"),
        ],
    },
    {
        "heading": "8. KEYNOTE-671 & AEGEAN — perioperative IO platforms",
        "level": 1,
        "paragraphs": [
            "KEYNOTE-671: perioperative pembrolizumab (neoadjuvant pembro+chemo → surgery → adjuvant "
            "pembro) vs perioperative chemo+placebo in resectable stage II–IIIB (N2). EFS and OS "
            "benefits — strong perioperative standard. AEGEAN: perioperative durvalumab + chemo "
            "improved EFS in resectable NSCLC. Together with 816, they redefine multimodality care.",
            "Compare designs on exam: 816 = neoadjuvant only IO; 671/AEGEAN = peri-operative IO "
            "(before and after surgery). Choice may depend on approval, PD-L1, stage, and centre protocol.",
        ],
        "table_trials": [
            ("KEYNOTE-671", "Perioperative pembro+chemo: EFS & OS benefit in resectable II–III"),
            ("AEGEAN", "Perioperative durvalumab+chemo: EFS benefit"),
            ("CheckMate-77T", "Perioperative nivo — additional perioperative evidence (mention if space)"),
            ("Neotorch / other regional", "Toripalimab perioperative data — global landscape awareness"),
        ],
        "table_doses": [
            ("Pembrolizumab perioperative", "200 mg Q3W with chemo neoadjuvant → adjuvant pembro per 671"),
            ("Durvalumab perioperative", "Per AEGEAN with platinum chemo → adjuvant durvalumab"),
        ],
        "pearls": [
            "Say 'OS benefit in KEYNOTE-671' — differentiates from EFS-only trials.",
        ],
    },
    {
        "heading": "9. Adjuvant immunotherapy after resection (IMpower010, KEYNOTE-091)",
        "level": 1,
        "paragraphs": [
            "IMpower010: adjuvant atezolizumab after cisplatin-based chemo improved DFS in PD-L1 "
            "TC ≥1% stage II–IIIA (and stronger in TC ≥50%). KEYNOTE-091 / PEARLS: adjuvant "
            "pembrolizumab improved DFS in stage IB–IIIA after resection (± chemo). These remain "
            "relevant when patients did not receive neoadjuvant IO.",
            "If perioperative IO already given, do not stack redundant adjuvant IO outside protocol. "
            "EGFR+ resected patients: prefer ADAURA osimertinib over adjuvant IO.",
        ],
        "table_trials": [
            ("IMpower010", "Adjuvant atezo after chemo — DFS benefit PD-L1+ II–IIIA"),
            ("KEYNOTE-091 (PEARLS)", "Adjuvant pembro — DFS benefit IB–IIIA"),
            ("ADAURA vs adjuvant IO", "EGFR+ → osi; driver− → IO pathway"),
        ],
        "flowchart": [
            "Completely resected NSCLC",
            "EGFR+ → adjuvant osimertinib (ADAURA) ± prior chemo",
            "Driver− & no perioperative IO → consider adjuvant atezo/pembro per label/PD-L1/stage",
            "Already perioperative IO → complete protocol adjuvant IO only as designed",
        ],
        "flowchart_title": "Post-operative systemic therapy fork",
    },
    {
        "heading": "10. Integrated management by stage (exam flowchart)",
        "level": 1,
        "paragraphs": [
            "Synthesise into a single algorithm examiners can follow. Emphasise MDT, biomarkers first, "
            "then modality sequencing.",
        ],
        "flowchart": [
            "Stage I resectable → surgery (± adjuvant chemo by risk) → EGFR? ADAURA if eligible",
            "Stage II–III resectable → consider neoadjuvant/perioperative chemo-IO (816/671/AEGEAN) if driver−",
            "After surgery driver− without peri-IO → adjuvant IO (IMpower010/PEARLS)",
            "EGFR+ resectable → surgery ± chemo → ADAURA osi",
            "Unresectable III → cCRT → EGFR+ LAURA osi / else PACIFIC durvalumab",
        ],
        "flowchart_title": "Practice-changing early NSCLC master algorithm",
        "bullets": [
            "Borderline N2: neoadjuvant systemic may convert / select biology (pCR).",
            "Incomplete resection: re-resection / RT / systemic per MDT — not covered by adjuvant trial populations cleanly.",
            "Pneumonitis risk: prior IO + thoracic RT needs careful PACIFIC timing.",
        ],
    },
    {
        "heading": "11. Comparison table of practice-changing trials",
        "level": 1,
        "paragraphs": [
            "Use this table as the centrepiece of the answer book.",
        ],
        "table_trials": [
            ("ADAURA", "Adjuvant osi EGFR+ IB–IIIA — DFS + OS; 80 mg × 3 y"),
            ("PACIFIC", "Durvalumab post-cCRT unresectable III — PFS + OS"),
            ("LAURA", "Osi post-CRT EGFR+ unresectable III — PFS practice change"),
            ("CheckMate-816", "Neoadjuvant nivo+chemo — pCR + EFS"),
            ("KEYNOTE-671", "Perioperative pembro — EFS + OS"),
            ("AEGEAN", "Perioperative durvalumab — EFS"),
            ("IMpower010", "Adjuvant atezo after chemo — DFS in PD-L1+"),
            ("KEYNOTE-091", "Adjuvant pembro — DFS"),
        ],
    },
    {
        "heading": "12. Doses & regimens quick sheet",
        "level": 1,
        "paragraphs": [
            "Examiners award marks for writable doses even in a 'advances' essay.",
        ],
        "table_doses": [
            ("Osimertinib", "80 mg PO daily (ADAURA 3 years; LAURA post-CRT)"),
            ("Durvalumab PACIFIC", "10 mg/kg Q2W or 1500 mg Q4W × 12 months"),
            ("Nivolumab 816", "360 mg Q3W × 3 with platinum chemo pre-op"),
            ("Pembrolizumab 671", "200 mg Q3W perioperative schedule with chemo"),
            ("Adjuvant atezolizumab", "1200 mg Q3W after cisplatin chemo (IMpower010)"),
            ("Adjuvant pembrolizumab", "200 mg Q3W or 400 mg Q6W (PEARLS/label)"),
        ],
    },
    {
        "heading": "13. NCCN NSCLC v9.2026 updates (early & related)",
        "level": 1,
        "paragraphs": [
            "Even though many 2026 bullets emphasise metastatic EGFR combinations, cite AJCC 9th "
            "adoption and reinforce biomarker-directed early pathways. Mention metastatic updates "
            "briefly only as 'continuum of EGFR care' if space (FLAURA2/MARIPOSA/Dato-DXd) without "
            "derailing the early-stage focus.",
        ],
        "nccn": {
            "versions": ["Non-Small Cell Lung Cancer v9.2026"],
            "bullets": [
                "AJCC 9th edition staging adopted in NCCN NSCLC pathway.",
                "Early/locally advanced care remains biomarker-stratified: EGFR testing to guide "
                "adjuvant osimertinib (ADAURA) and post-CRT osimertinib (LAURA) vs durvalumab (PACIFIC).",
                "Perioperative and neoadjuvant immunotherapy options incorporated for eligible resectable disease.",
                "Metastatic continuum (for context): osimertinib + platinum/pemetrexed and "
                "amivantamab + lazertinib Category 1 preferred 1L EGFR mut+; Dato-DXd preferred in "
                "selected post-osi+chemo settings — shows EGFR care continuity beyond early stage.",
                "ROS1 subsequent options (repotrectinib/taletrectinib) and HER2-mut ADC notes appear in "
                "advanced disease sections — test broadly on NGS.",
            ],
        },
        "pearls": [
            "Lead NCCN paragraph with AJCC 9th — it is the explicit 2026 staging bullet.",
        ],
    },
    {
        "heading": "14. Toxicities, practical pitfalls & Indian context",
        "level": 1,
        "paragraphs": [
            "IO: irAEs may delay surgery — coordinate tightly. CRT+IO: pneumonitis differential "
            "(radiation vs immune). Osimertinib: rash, diarrhoea, rare ILD, QTc/lab monitoring. "
            "Access and cost of 3-year adjuvant osi and perioperative IO are real-world constraints — "
            "discuss NCG/institutional pathways and prioritisation of EGFR testing where TKI access exists.",
        ],
        "bullets": [
            "Do not give adjuvant IO instead of ADAURA in EGFR+.",
            "Do not skip surgery window after neoadjuvant IO due to unmanaged G1 toxicities.",
            "Document PD-L1 and EGFR on every pathology report for early NSCLC.",
        ],
    },
    {
        "heading": "15. Summary — exam pearls wall chart",
        "level": 1,
        "paragraphs": [
            "Close with a six-line wall chart mapping trial → setting → drug → endpoint.",
        ],
        "bullets": [
            "ADAURA: adjuvant osi EGFR+ — DFS/OS.",
            "PACIFIC: durvalumab post-CRT III — PFS/OS.",
            "LAURA: osi post-CRT EGFR+ III — PFS.",
            "816 / 671 / AEGEAN: neoadjuvant & perioperative IO.",
            "IMpower010 / PEARLS: adjuvant IO if no peri-IO.",
            "AJCC 9th + universal molecular testing.",
        ],
        "pearls": [
            "EGFR first — splits the entire algorithm.",
            "PACIFIC numbers: mPFS 16.8 vs 5.6 mo; quote 5-y OS if remembered.",
            "KEYNOTE-671 has OS — say so.",
            "LAURA prevents wrong default to durvalumab in EGFR+ III.",
            "AJCC 9th is the NCCN 2026 staging soundbite.",
        ],
        "flowchart": [
            "Biomarker",
            "Resectable vs unresectable",
            "Match to ADAURA / 816-671-AEGEAN / PACIFIC-LAURA",
            "Write doses + 1 HR/median each",
            "NCCN AJCC9 box + pearls",
        ],
        "flowchart_title": "35-minute early NSCLC answer plan",
    },
]


# ---------------------------------------------------------------------------
# Public export
# ---------------------------------------------------------------------------

DEEP: dict[str, list[dict]] = {
    "Q349": Q349,
    "Q350": Q350,
    "Q361": Q361,
    "Q362": Q362,
}


def validate_deep(deep: dict[str, list[dict]] | None = None) -> None:
    """Light structural checks for import-time sanity."""
    deep = deep if deep is not None else DEEP
    allowed = {
        "heading",
        "level",
        "paragraphs",
        "bullets",
        "flowchart",
        "flowchart_title",
        "flowchart_caption",
        "mechanism",
        "table_trials",
        "table_doses",
        "nccn",
        "pearls",
    }
    for qid, sections in deep.items():
        if not 12 <= len(sections) <= 16:
            raise ValueError(f"{qid}: expected 12–16 sections, got {len(sections)}")
        for i, sec in enumerate(sections):
            unknown = set(sec) - allowed
            if unknown:
                raise ValueError(f"{qid} section {i}: unknown keys {unknown}")
            if "heading" not in sec:
                raise ValueError(f"{qid} section {i}: missing heading")
            if "nccn" in sec:
                n = sec["nccn"]
                if not isinstance(n, dict) or "versions" not in n or "bullets" not in n:
                    raise ValueError(f"{qid} section {i}: nccn needs versions+bullets")
            if "mechanism" in sec:
                for row in sec["mechanism"]:
                    if not (isinstance(row, (list, tuple)) and len(row) == 2):
                        raise ValueError(f"{qid} section {i}: mechanism rows must be pairs")
            for key in ("table_trials", "table_doses"):
                if key in sec:
                    for row in sec[key]:
                        if not (isinstance(row, (list, tuple)) and len(row) == 2):
                            raise ValueError(f"{qid} section {i}: {key} rows must be pairs")


validate_deep()

__all__ = ["DEEP", "Q349", "Q350", "Q361", "Q362", "validate_deep"]

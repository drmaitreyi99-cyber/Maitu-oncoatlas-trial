DEEP = {
    "Q325": [
        {
            "heading": "1. Introduction & exam framing (Feb 2022 essay)",
            "level": 1,
            "paragraphs": [
                "DNA microarray gene-expression profiling (GEP) measures simultaneous mRNA abundance of thousands of genes on a solid substrate. "
                "In oncology it moved from unsupervised discovery of molecular subtypes to <b>clinically validated prognostic and predictive signatures</b>, especially in early breast cancer.",
                "A high-scoring answer should (1) explain the technology and QC, (2) contrast prognostic vs predictive use, (3) detail Oncotype DX, MammaPrint, PAM50/Prosigna (and related assays), "
                "(4) note GEP in myeloma/ALL/lymphoma with limitations, (5) compare microarray vs RNA-seq/NGS, and (6) close with Indian/NCG practicality and NCCN-aligned breast pathways.",
            ],
            "bullets": [
                "Definition one-liner: simultaneous transcriptome snapshot → risk score or subtype.",
                "Clinical maturity is highest in ER+/HER2− early breast cancer; elsewhere mostly research or specialized centers.",
                "Always state: signature ≠ substitute for stage, grade, receptor status, or germline testing.",
            ],
            "pearls": [
                "Open with: ‘Microarrays classified biology; selected multigene assays now guide adjuvant chemo omission.’",
                "Examiners expect TAILORx and MINDACT numbers — write at least one HR or absolute DMFS/%.",
            ],
        },
        {
            "heading": "2. Technology: platforms, workflow & quality control",
            "level": 1,
            "paragraphs": [
                "Classic platforms: spotted cDNA arrays and high-density oligonucleotide arrays (e.g., Affymetrix GeneChip). Modern clinical assays are often RT-PCR or RNA-based kits derived from microarray discovery cohorts, "
                "run on FFPE with standardized RNA extraction.",
                "Workflow: tissue adequacy → RNA isolation → reverse transcription / labeling → hybridization → scanning → normalization → signature algorithm → clinical report. "
                "Pre-analytics dominate error: ischemic time, fixation, tumor cellularity, and necrosis.",
            ],
            "bullets": [
                "Minimum tumor cellularity thresholds are assay-specific (often ≥10–30% invasive tumor).",
                "Housekeeping-gene normalization and batch-effect correction are mandatory for research arrays.",
                "Clinical assays report a locked algorithm (no ad-hoc re-clustering at the bedside).",
            ],
            "mechanism": [
                ("mRNA from tumor", "Reflects active transcription programs"),
                ("Probe hybridization", "Quantifies relative gene expression"),
                ("Normalization", "Removes technical noise"),
                ("Signature score", "Maps to prognosis / chemo benefit"),
                ("Clinical action", "Escalate or omit adjuvant therapy"),
            ],
            "flowchart": [
                "Adequate invasive tumor (FFPE/fresh)",
                "RNA QC (integrity / yield)",
                "Assay run (RT-PCR or array kit)",
                "Locked signature score / subtype",
                "Integrate with clinicopathologic risk → adjuvant decision",
            ],
            "flowchart_title": "Microarray / multigene assay clinical workflow",
        },
        {
            "heading": "3. Biology captured by expression profiling",
            "level": 1,
            "paragraphs": [
                "GEP recapitulates pathways of proliferation (e.g., Ki-67–related genes), ER signaling, HER2 amplicon activity, immune infiltration, and basal programs. "
                "Unsupervised clustering historically defined intrinsic breast subtypes: Luminal A/B, HER2-enriched, Basal-like, Normal-like.",
                "Important exam nuance: IHC surrogates approximate but do not perfectly match intrinsic subtypes; PAM50 is the gene-expression gold-standard for intrinsic subtype assignment in many studies.",
            ],
            "bullets": [
                "Proliferation modules drive much of the prognostic power in ER+ disease.",
                "Immune gene signatures correlate with CPI benefit in some tumors — still largely investigational for microarray clinical kits.",
                "Expression ≠ mutation: microarray will not replace DNA NGS for EGFR/BRAF/BRCA targets.",
            ],
            "mechanism": [
                ("Proliferation genes", "Higher → higher recurrence risk"),
                ("ER module", "Endocrine sensitivity correlate"),
                ("HER2 module", "HER2-enriched biology"),
                ("Basal / immune modules", "Aggressive / IO-relevant biology"),
            ],
        },
        {
            "heading": "4. Oncotype DX (21-gene RS) — the exam workhorse",
            "level": 1,
            "paragraphs": [
                "Oncotype DX quantifies 16 cancer-related + 5 reference genes by RT-PCR on FFPE, yielding Recurrence Score (RS) 0–100. "
                "It is both <b>prognostic</b> (distant recurrence on endocrine therapy) and <b>predictive</b> of chemotherapy benefit in ER+/HER2− early breast cancer.",
                "Historical cutoffs (NSABP B-14/B-20 era): low <18, intermediate 18–30, high ≥31. Prospective TAILORx redefined clinical bands used today: RS 0–10, 11–25, and ≥26.",
            ],
            "bullets": [
                "Best validated in node-negative and limited node-positive (1–3) HR+/HER2− disease.",
                "Does not replace HER2 testing or staging; HER2+ disease is outside classic RS chemo-sparing paradigms.",
                "Report turnaround and cost matter for Indian practice — discuss affordability and selective use.",
            ],
            "table_trials": [
                ("NSABP B-20 (retrospective)", "High RS derives large chemo benefit; low RS little benefit"),
                ("TAILORx (NEJM 2018)", "N0, RS 11–25: endocrine alone non-inferior to chemo→endocrine for iDFS overall"),
                ("TAILORx age subgroup", "Women ≤50 y with RS 16–25: chemo may reduce distant recurrence"),
                ("RxPONDER (NEJM 2021)", "N1 (1–3 nodes), RS ≤25: postmenopausal — no chemo benefit; premenopausal — chemo benefit"),
            ],
            "pearls": [
                "Memorize: TAILORx = N0; RxPONDER = N1 — menopausal status flips the chemo decision at intermediate RS.",
            ],
        },
        {
            "heading": "5. TAILORx & RxPONDER — numbers to quote",
            "level": 1,
            "paragraphs": [
                "<b>TAILORx</b>: HR+/HER2−, N0, RS 11–25 randomized to endocrine vs chemo + endocrine. Invasive disease-free survival was non-inferior for endocrine alone in the overall intermediate group "
                "(e.g., 9-year iDFS ~83% both arms in primary report). Absolute chemo benefit emerges mainly in younger women with mid-range RS.",
                "<b>RxPONDER</b>: 1–3 positive nodes, RS ≤25. Postmenopausal: 5-year iDFS similar with or without chemo (~91–92%). Premenopausal: chemo improved iDFS (≈ absolute ~3–5%+ depending on follow-up cut) "
                "and distant relapse-free intervals — OFS strategies are discussed as alternative contributors in debates, but trial as reported supports chemo benefit.",
            ],
            "bullets": [
                "RS ≥26 (N0) or high RS with nodes: chemotherapy generally recommended unless contraindicated.",
                "RS ≤10 (N0): endocrine therapy alone — excellent prognosis.",
                "Always integrate anatomic stage, grade, LVI, comorbidity, and patient preference.",
            ],
            "flowchart": [
                "ER+/HER2− early breast cancer",
                "Order RS if result will change chemo decision",
                "N0: use TAILORx bands (≤50 y nuance RS 16–25)",
                "N1 (1–3): use RxPONDER + menopausal status",
                "Document shared decision + offer OFS discussion if premenopausal",
            ],
            "flowchart_title": "Oncotype-guided adjuvant chemo decision",
        },
        {
            "heading": "6. MammaPrint (70-gene) & MINDACT",
            "level": 1,
            "paragraphs": [
                "MammaPrint (Amsterdam 70-gene signature) dichotomizes genomic High vs Low risk. Originally fresh tissue / microarray; FFPE versions exist. "
                "<b>MINDACT</b> (NEJM 2016; long-term updates) used clinical risk (Adjuvant! Online) × genomic risk.",
                "Key practice point: clinically high risk / genomically low risk patients who omitted chemotherapy had 5-year distant metastasis-free survival ≈ 94% — supporting chemo sparing in selected patients. "
                "Absolute chemo benefit in discordant groups is small; shared decision-making is essential.",
            ],
            "table_trials": [
                ("MINDACT primary", "Clinical high / genomic low: chemo omission feasible; 5-y DMFS ~94.7% without chemo (per primary analysis framing)"),
                ("MINDACT long-term", "Confirms limited absolute chemo benefit in genomic-low discordant patients"),
                ("Microarray discovery (van’t Veer / van de Vijver)", "70-gene signature prognostic in early breast cancer"),
            ],
            "bullets": [
                "MammaPrint = binary risk; Oncotype = continuous RS with predictive chemo data in node± settings.",
                "Do not mix cutoffs across assays — they are not interchangeable.",
            ],
        },
        {
            "heading": "7. PAM50 / Prosigna, EndoPredict, BCI & comparisons",
            "level": 1,
            "paragraphs": [
                "<b>PAM50</b> intrinsic subtype + Risk of Recurrence (ROR) score (Prosigna) provides prognostic information in HR+ early breast cancer and is used in some guidelines/centers for late-distant recurrence risk. "
                "<b>EndoPredict</b> (12-gene; EPclin combines clinical factors) and <b>Breast Cancer Index (BCI)</b> help prognosis and, for BCI, decisions on extended endocrine therapy.",
                "Comparative pearl: Oncotype has the strongest prospective predictive evidence for adjuvant chemo benefit (TAILORx/RxPONDER). Others are primarily prognostic or endocrine-duration tools.",
            ],
            "bullets": [
                "Prosigna: intrinsic subtype (LumA/LumB/HER2-E/Basal) + ROR.",
                "BCI: prognostic + predictive for extended AI benefit after 5 years endocrine therapy in selected N0/N1.",
                "IHC4 / clinical models are cheaper alternatives when genomic assays unavailable (NCG resource-stratified thinking).",
            ],
            "table_trials": [
                ("TransATAC / ABCSG cohorts", "PAM50 ROR, EndoPredict, BCI prognostic validation sets"),
                ("BCI extended endocrine analyses", "Identifies who benefits from years 5–10 endocrine therapy"),
            ],
        },
        {
            "heading": "8. Beyond breast: myeloma GEP, ALL, lymphoma COO",
            "level": 1,
            "paragraphs": [
                "<b>Multiple myeloma</b>: GEP70/GEP80 (UAMS) and related signatures stratify high-risk biology (e.g., proliferation, chromosome 1q–linked programs). "
                "They refine prognosis beyond ISS/R-ISS but are not universally mandated; NGS/FISH for del(17p), t(4;14), t(14;16), 1q gain remain standard.",
                "<b>ALL</b>: expression profiling helped define Ph-like ALL and other subtypes historically; contemporary diagnosis leans on NGS fusions, CRLF2, and flow/genomics rather than clinical microarray kits.",
                "<b>DLBCL cell-of-origin</b>: microarray GCB vs ABC (Wright/Alizadeh) → IHC algorithms (Hans) as surrogates; NanoString Lymph2Cx used in trials. COO alone no longer drives most frontline choices after failed subtype-selected trials with R-CHOP ± novel agents in unselected practice — nuance for exams.",
            ],
            "bullets": [
                "Myeloma: quote GEP as research/prognostic adjunct — treatment still driven by IMWG risk + frailty + induction trials (e.g., anti-CD38 quadruplets).",
                "ALL: Ph-like identification matters for TKI/trial options — method is usually NGS/MLPA, not bedside microarray.",
                "Lymphoma: COO is biologic literacy; PET-adapted and molecular subtypes (e.g., MCD, BN2) are evolving.",
            ],
            "pearls": [
                "Say explicitly: ‘GEP in myeloma/ALL informs biology; routine Indian practice still FISH/cytogenetics/NGS-first.’",
            ],
        },
        {
            "heading": "9. Other solid tumors — status check (honest limitations)",
            "level": 1,
            "paragraphs": [
                "Colon Cancer: ColoPrint and similar GEP assays remain less practice-changing than MSI/RAS/BRAF and ctDNA MRD. "
                "Prostate: Decipher genomic classifier (expression-based) has growing role in post-prostatectomy risk and ADT intensification debates. "
                "Lung and others: expression signatures for IO prediction underperform relative to PD-L1, TMB, and driver NGS.",
                "Bottom line for the essay: microarray profiling’s <b>clearest management impact</b> remains adjuvant breast cancer chemo and endocrine-duration decisions.",
            ],
            "bullets": [
                "Do not oversell pan-cancer microarray panels as standards of care.",
                "DNA NGS actionable mutations > expression arrays for targeted drug selection in advanced disease.",
            ],
        },
        {
            "heading": "10. Microarray vs RNA-seq vs DNA NGS — choose the right tool",
            "level": 1,
            "paragraphs": [
                "Microarrays quantify known probe sets; RNA-seq offers wider dynamic range, novel transcripts, and fusion detection. DNA NGS detects mutations, copy number, MSI, TMB. "
                "Clinical multigene ‘recurrence scores’ may use RT-PCR on a fixed gene list — conceptually descendants of microarray discovery.",
            ],
            "mechanism": [
                ("DNA microarray / RT-PCR signature", "Fixed genes → risk score (Oncotype/MammaPrint era)"),
                ("RNA-seq", "Discovery, fusions, broader transcriptome"),
                ("DNA NGS panel", "Actionable mutations / CNAs / MSI"),
                ("IHC / FISH", "Protein/amplification bedside standards"),
            ],
            "bullets": [
                "Predictive targeted therapy → DNA/RNA fusion NGS + IHC.",
                "Adjuvant chemo sparring in ER+ breast → validated expression signatures.",
                "Minimal residual disease → ctDNA, not microarray.",
            ],
        },
        {
            "heading": "11. Limitations, pitfalls & ethics",
            "level": 1,
            "paragraphs": [
                "Limitations: assay discordance, cost, turnaround, limited predictive breadth outside breast, racial/ethnic under-representation in some training sets, and risk of over-reliance ignoring clinical high-risk features. "
                "Heterogeneity and biopsy site bias can misclassify.",
                "Ethics: financial toxicity and equity — offer assay when it materially changes therapy; otherwise use clinicopathologic models.",
            ],
            "bullets": [
                "Never omit chemo solely on genomic low risk if inflammatory breast cancer or other extreme clinical risk without supportive data.",
                "Repeat testing rarely indicated; prefer correct initial indication.",
                "Counsel that intermediate results still need judgment (especially premenopausal).",
            ],
        },
        {
            "heading": "12. NCCN / guideline position (breast-focused) & 2026 framing",
            "level": 1,
            "paragraphs": [
                "NCCN Breast Cancer pathways endorse consideration of validated multigene assays to assess prognosis and potential chemo benefit in HR+/HER2− early disease with specified anatomic stages. "
                "Paper IV answers should cite <b>NCCN Breast Cancer v9.2026</b> currency alongside classic trial evidence.",
            ],
            "nccn": {
                "versions": ["Breast Cancer v9.2026", "NCCN Guidelines Navigator (breast)"],
                "bullets": [
                    "Use 21-gene RS (or other validated assays per NCCN footnotes) to guide adjuvant systemic therapy in appropriate HR+/HER2− patients.",
                    "Integrate menopausal status with RS (TAILORx/RxPONDER logic) when discussing chemo.",
                    "NCCN 2026 metastatic HR+ additions (e.g., imlunestrant for ESR1) are separate from adjuvant GEP — mention only to show guideline literacy.",
                    "Genomic assays complement, never replace, AJCC staging and receptor testing.",
                ],
            },
        },
        {
            "heading": "13. Indian / NCG practical notes",
            "level": 1,
            "paragraphs": [
                "In many Indian centers, selective Oncotype/MammaPrint use is constrained by cost. NCG resource-stratified approaches emphasize accurate ER/PR/HER2/Ki-67, anatomic stage, and MDT discussion. "
                "When assay unavailable: offer chemo for higher anatomic/biological risk; consider omission in unequivocally low clinical risk postmenopausal N0 disease after counseling.",
            ],
            "bullets": [
                "Prioritize funding assays for borderline cases where decision truly hinges on genomic risk.",
                "Ensure receptor re-testing quality (ASCO/CAP) before expensive GEP.",
                "Document financial counseling in the file — exam-friendly phrase.",
            ],
        },
        {
            "heading": "14. Future directions",
            "level": 1,
            "paragraphs": [
                "RNA-seq signatures, spatial transcriptomics, and multimodal AI (pathology + expression + radiology) are research frontiers. "
                "ctDNA MRD may overshadow static GEP for escalation/de-escalation in coming years. Tumor-agnostic DNA biomarkers already dominate metastatic matching.",
            ],
            "bullets": [
                "Watch prospective trials combining MRD + GEP.",
                "Immune GEP for CPI selection — promising, not yet microarray-kit standard across cancers.",
            ],
        },
        {
            "heading": "15. Summary algorithm & exam pearls",
            "level": 1,
            "paragraphs": [
                "DNA microarray profiling established the molecular taxonomy of cancer; clinically, locked multigene expression assays — especially Oncotype DX and MammaPrint — meaningfully guide adjuvant therapy in HR+/HER2− breast cancer. "
                "GEP elsewhere is adjunctive. Pair every score with clinicopathologic context, menopausal status, and patient values.",
            ],
            "flowchart": [
                "Is this ER+/HER2− early breast cancer where chemo is uncertain?",
                "Yes → validated assay (Oncotype preferred for predictive chemo data)",
                "Apply TAILORx / RxPONDER / MINDACT logic",
                "Other tumors → use disease-standard genomics (NGS/FISH); GEP optional/prognostic",
                "Counsel, document, follow NCCN/NCG",
            ],
            "flowchart_title": "When microarray-derived assays change management",
            "pearls": [
                "TAILORx = N0 intermediate RS; RxPONDER = N1 RS≤25 + menopause split.",
                "MINDACT: clinical high / genomic low → chemo omission often acceptable.",
                "Myeloma GEP high-risk ≠ mandatory assay in all Indian clinics — know FISH first.",
                "Microarray discovers; RT-PCR kits deliver; NGS targets drugs.",
                "Write one limitation paragraph — examiners reward maturity.",
            ],
        },
    ],
    "Q326": [
        {
            "heading": "1. Introduction — supportive care as anticancer therapy",
            "level": 1,
            "paragraphs": [
                "Supportive care prevents and treats complications of cancer and its treatment — enabling delivery of full-dose intensive regimens, preserving organ function, and improving quality of life and sometimes survival. "
                "‘Recent advances’ for a 2022-onward Paper IV answer span antiemetics (olanzapine), growth factors, bone-modifying agents, cardio-oncology, immuno-toxicity algorithms, nutrition, VTE prevention, and digital PRO monitoring.",
                "Structure: CINV → FN/G-CSF → anemia/ESA caution → bone health → cardio-oncology → irAEs → mucositis/nutrition → VTE → CIPN/fatigue/fertility → NCCN 2026 supportive bullets → Indian practice.",
            ],
            "bullets": [
                "Supportive care is not optional add-on — it is part of the treatment protocol.",
                "Cite MASCC/ESMO/ASCO antiemetic guidelines and NCCN Supportive Care libraries.",
            ],
            "pearls": [
                "Start essay with: ‘Cure rates rise when toxicity is anticipated and protocolized.’",
            ],
        },
        {
            "heading": "2. CINV — modern risk-adapted antiemesis",
            "level": 1,
            "paragraphs": [
                "Chemotherapy-induced nausea/vomiting is classified as acute (≤24 h), delayed (>24 h), anticipatory, breakthrough, and refractory. Emetogenicity tiers (high/moderate/low/minimal) drive prophylaxis.",
                "Cornerstone classes: 5-HT3 antagonists (ondansetron, granisetron, palonosetron), NK1 receptor antagonists (aprepitant/fosaprepitant/netupitant), dexamethasone, and <b>olanzapine</b> — now a practice-changing addition for HEC and breakthrough.",
            ],
            "bullets": [
                "HEC (e.g., cisplatin, AC): 4-drug prophylaxis often used — 5-HT3 + NK1 + dexamethasone + olanzapine.",
                "Palonosetron: longer half-life; useful for delayed CINV.",
                "Non-pharmacologic: hydration, ginger evidence modest, behavioral therapy for anticipatory CINV.",
            ],
            "mechanism": [
                ("Peripheral 5-HT3", "Acute CINV — enterochromaffin → vagus"),
                ("Central NK1 / substance P", "Delayed CINV"),
                ("Dopamine / multiple receptors", "Olanzapine broad antiemetic cover"),
                ("Cortex / memory", "Anticipatory CINV"),
            ],
        },
        {
            "heading": "3. Olanzapine evidence & practical dosing",
            "level": 1,
            "paragraphs": [
                "Navari et al. and subsequent trials showed olanzapine improves nausea control — the endpoint patients care about most — when added to triple therapy for HEC. "
                "Typical investigational/clinical dose: <b>olanzapine 5–10 mg PO nightly</b> on days 1–4 (5 mg often preferred in elderly to reduce sedation).",
                "Breakthrough: olanzapine is a preferred agent in many guidelines when not already used for prophylaxis.",
            ],
            "table_doses": [
                ("Olanzapine (HEC prophylaxis)", "5–10 mg PO days 1–4 (prefer 5 mg if sedation risk)"),
                ("Aprepitant", "125 mg d1 → 80 mg d2–3 (or fosaprepitant 150 mg IV d1)"),
                ("Ondansetron", "8 mg IV/PO schedule per regimen; watch QT"),
                ("Dexamethasone (with NK1)", "12 mg d1 then tapered per guideline (NK1 interaction)"),
                ("Palonosetron", "0.25 mg IV day 1"),
            ],
            "table_trials": [
                ("Navari NEJM / JCO olanzapine trials", "Olanzapine ↑ no-nausea rates with HEC triple therapy"),
                ("MASCC/ESMO & ASCO antiemetic updates", "Olanzapine incorporated into HEC pathways"),
            ],
            "pearls": [
                "Warn about sedation and metabolic effects; avoid co-administration issues with CNS depressants.",
            ],
        },
        {
            "heading": "4. Febrile neutropenia — prevention & treatment advances",
            "level": 1,
            "paragraphs": [
                "FN remains a medical emergency: temperature ≥38.3°C (or ≥38.0°C sustained) + ANC <500/µL (or <1000 with predicted decline). "
                "Risk tools: ASCO/NCCN regimen risk (≥20% FN → primary G-CSF), MASCC/CISNE scores for outpatient eligibility after careful selection.",
                "Advances: biosimilar filgrastim/pegfilgrastim improving access; same-day vs next-day pegfilgrastim debates; antibiotic stewardship with early de-escalation when cultures negative and recovering.",
            ],
            "flowchart": [
                "Estimate FN risk of regimen + patient factors",
                "≥20% or dose-dense → primary prophylaxis G-CSF",
                "If FN occurs → cultures, risk stratify, empiric antipseudomonal β-lactam",
                "Add MRSA/antifungal coverage per guidelines if indicated",
                "G-CSF therapeutic use if high-risk FN; educate for next cycle prophylaxis",
            ],
            "flowchart_title": "FN prevention and acute management",
            "bullets": [
                "High-risk FN: hypotension, pneumonia, uncontrolled cancer, ANC <100, duration >7 d expected.",
                "Never delay first antibiotic dose for imaging.",
            ],
        },
        {
            "heading": "5. G-CSF / GM-CSF — doses & pearls",
            "level": 1,
            "paragraphs": [
                "Filgrastim 5 µg/kg SC daily until ANC recovery (start 24–72 h post chemo). Pegfilgrastim 6 mg SC once per cycle (≥24 h after chemo; avoid within 14 days before next chemo). "
                "Self-administration and on-body injectors are recent practical advances. Biosimilars are preferred cost-saving options in Indian practice.",
            ],
            "table_doses": [
                ("Filgrastim", "5 µg/kg SC daily; start ≥24 h after myelosuppressive chemo"),
                ("Pegfilgrastim", "6 mg SC once per cycle"),
                ("Trilaciclib (selected ES-SCLC)", "Myelopreservation before chemo — niche advance"),
            ],
            "bullets": [
                "Bone pain: manage with NSAIDs/loratadine as used in practice pathways.",
                "Do not use G-CSF concurrently with chemo/RT in most protocols (except specific regimens).",
            ],
        },
        {
            "heading": "6. Anemia, ESAs & transfusion — caution first",
            "level": 1,
            "paragraphs": [
                "Cancer- and chemo-related anemia: correct iron deficiency (IV iron when appropriate), B12/folate, bleed, hemolysis. Transfuse based on symptoms and comorbidities, not a fixed Hb alone.",
                "<b>ESA caution</b>: erythropoiesis-stimulating agents may shorten survival / promote tumor progression in some settings and ↑ VTE. Restrict to selected chemo-induced anemia with non-curative intent under label/REMS-like caution; avoid in curative pathways when possible.",
            ],
            "bullets": [
                "Target lowest Hb to avoid transfusion — do not normalize Hb with ESA.",
                "IV iron formulations (ferric carboxymaltose etc.) useful if absolute/functional iron deficiency.",
                "Exam phrase: ‘ESA — symptom control in palliative chemo anemia only, after risk discussion.’",
            ],
            "pearls": [
                "FDA boxed warnings on ESAs are classic viva fodder.",
            ],
        },
        {
            "heading": "7. Bone-modifying agents — SRE prevention",
            "level": 1,
            "paragraphs": [
                "Zoledronic acid and denosumab reduce skeletal-related events in bone metastases (breast, prostate, others) and treat hypercalcemia of malignancy. "
                "Denosumab (RANKL mAb) delayed SREs vs zoledronic acid in some solid-tumor trials; choose by renal function, cost, and ONJ risk counseling.",
                "Adjuvant bisphosphonates in postmenopausal early breast cancer reduce bone recurrence and improve OS in meta-analyses — mention as supportive/adjuvant overlap.",
            ],
            "table_doses": [
                ("Zoledronic acid (bone mets)", "4 mg IV q4–12 weeks (extend interval if stable)"),
                ("Denosumab (bone mets)", "120 mg SC q4 weeks"),
                ("Zoledronic acid (hypercalcemia)", "4 mg IV; dental check when feasible"),
                ("Calcium + vitamin D", "Supplement with denosumab/bisphosphonate unless hypercalcemic"),
            ],
            "bullets": [
                "ONJ risk: dental review, avoid invasive dental procedures on therapy when possible.",
                "Hypocalcemia: especially denosumab — monitor Ca/Mg.",
                "Renal dosing: adjust/hold zoledronic acid for CrCl limits; denosumab not renally cleared the same way but watch Ca.",
            ],
        },
        {
            "heading": "8. Cardio-oncology advances",
            "level": 1,
            "paragraphs": [
                "Anthracyclines (cumulative dose, liposomal formulations), HER2 agents, VEGF TKIs/bevacizumab (hypertension, ischemia), ibrutinib (AF), and checkpoint myocarditis define modern cardio-oncology. "
                "Advances: baseline risk stratification, echo/GLS, troponin surveillance in high-risk protocols, aggressive BP control on VEGF inhibitors, and rapid steroid pathways for IO myocarditis.",
            ],
            "bullets": [
                "Hold HER2 therapy for significant LVEF drops per institutional/ASCO rules; cardio referral.",
                "IO myocarditis: rare but high mortality — early ECG/troponin, pulse steroids, discontinue CPI.",
                "Dexrazoxane in selected high cumulative anthracycline settings (guidelines vary).",
            ],
            "flowchart": [
                "Baseline CV risk + echo if anthracycline/HER2/IO high risk",
                "On-treatment BP/ECG/symptoms surveillance",
                "Toxicity → grade → hold drug + treat (ACEi/BB, steroids if myocarditis)",
                "Rechallenge only if benefit ≫ risk",
            ],
            "flowchart_title": "Cardio-oncology loop",
        },
        {
            "heading": "9. Immune-related adverse events (irAEs) — IRIS-adjacent care",
            "level": 1,
            "paragraphs": [
                "Checkpoint inhibitor expansion made irAE management a core supportive-care competency. CTCAE grading drives hold/steroid decisions. "
                "Common: dermatitis, colitis, hepatitis, endocrinopathies (thyroid, hypophysitis, adrenal), pneumonitis; rare: myocarditis, myasthenia, severe neurologic disease.",
                "‘IRIS’ in exam answers may be framed as immune reconstitution-type flares in HIV or as immune-related inflammatory syndromes after CPI — clarify terminology and discuss steroid-responsive inflammation with multidisciplinary care.",
            ],
            "bullets": [
                "Grade 2: usually hold CPI + start corticosteroids (e.g., prednisone 0.5–1 mg/kg).",
                "Grade 3–4: high-dose steroids; infliximab for steroid-refractory colitis; MMF for hepatitis; permanent discontinuation for many grade 4.",
                "Endocrinopathies: hormone replacement; CPI often continued once stable on replacement.",
            ],
            "table_doses": [
                ("Prednisone (gr 2 irAE)", "~0.5–1 mg/kg/day with taper"),
                ("Methylprednisolone (severe)", "1–2 mg/kg/day IV"),
                ("Infliximab (refractory colitis)", "5 mg/kg IV — after excluding infection"),
            ],
            "nccn": {
                "versions": ["NCCN Management of Immunotherapy-Related Toxicities (current 2026 family)", "Kidney Cancer v2.2027 (IO combinations context)"],
                "bullets": [
                    "Follow NCCN immunotherapy toxicity algorithms for hold/discontinue/steroid/infliximab pathways.",
                    "Educate patients with wallet cards — early reporting reduces fatalities from myocarditis/pneumonitis.",
                ],
            },
        },
        {
            "heading": "10. Mucositis, nutrition & cachexia",
            "level": 1,
            "paragraphs": [
                "Oral mucositis: oral cryotherapy for bolus 5-FU, dental prep, magic mouthwash variants, palifermin in selected transplant TBI regimens, photobiomodulation in some centers. "
                "Nutrition: early dietitian referral; treat reversible causes; consider enteral feeding before parenteral. Cachexia: multimodal — exercise, nutrition, treat inflammation; ghrelin mimetics/other agents evolving.",
            ],
            "bullets": [
                "NCCN Distress Thermometer + nutrition screening at key visits.",
                "Avoid alcohol-based mouth rinses that worsen mucositis.",
                "Tube feeding preferred over TPN if gut works.",
            ],
        },
        {
            "heading": "11. VTE prevention & treatment in cancer",
            "level": 1,
            "paragraphs": [
                "Cancer VTE risk: tumor type (pancreas, stomach, brain), stage, chemo (platinum, IMiDs + steroids), central lines. Khorana score guides primary prophylaxis in ambulatory high-risk patients.",
                "Advances: DOACs (apixaban, rivaroxaban, edoxaban) validated vs LMWH in selected cancer VTE (select GI/GU mucosal bleed risk caution). LMWH remains preferred in many GI luminal cancers or very high bleed risk.",
            ],
            "table_doses": [
                ("Enoxaparin (treatment)", "1 mg/kg SC BID or 1.5 mg/kg daily (adjust CrCl)"),
                ("Apixaban (selected cancer VTE)", "10 mg BID ×7 d → 5 mg BID (trial protocols)"),
                ("Rivaroxaban (selected)", "15 mg BID ×21 d → 20 mg daily with food"),
            ],
            "bullets": [
                "Primary prophylaxis: consider in Khorana high-risk ambulatory outpatients after bleed assessment.",
                "IMiDs in myeloma: aspirin/LMWH/DOAC thromboprophylaxis per risk.",
            ],
        },
        {
            "heading": "12. CIPN, fatigue, fertility, survivorship",
            "level": 1,
            "paragraphs": [
                "Chemotherapy-induced peripheral neuropathy (taxanes, platinum, vinca, bortezomib): dose holds/reductions; duloxetine has best evidence for painful CIPN. Cryotherapy/compression for taxanes — supportive data evolving.",
                "Fatigue: treat contributors (anemia, thyroid, depression, sleep); structured exercise is an evidence-based intervention — now even embedded in some NCCN disease guidelines (e.g., post-adjuvant CRC exercise).",
                "Fertility: sperm cryopreservation; oocyte/embryo freezing; GnRH analogs during chemo in selected breast cancer — discuss before gonadotoxic therapy.",
            ],
            "bullets": [
                "Vaccinations: inactivated vaccines timing; COVID/influenza; avoid live vaccines while immunosuppressed.",
                "Psychosocial oncology and palliative integration early in metastatic disease.",
            ],
        },
        {
            "heading": "13. Growth factors for platelets & special agents",
            "level": 1,
            "paragraphs": [
                "Romiplostim/eltrombopag: used in selected chemo-induced thrombocytopenia pathways and bone marrow failure — specialist use. "
                "TPO receptor agonists appear in modern supportive algorithms when dose intensity is critical and plateletdelay is the bottleneck.",
            ],
            "bullets": [
                "Not a substitute for treating underlying marrow disease.",
                "Watch thrombosis risk with TPO-RAs.",
            ],
        },
        {
            "heading": "14. NCCN 2026 supportive-care relevant updates",
            "level": 1,
            "paragraphs": [
                "Even when answering a classic ‘supportive care in chemotherapy’ essay, inject <b>NCCN 2026</b> currency: exercise prescription, CVD risk pages, and digital navigation tools show examiners you are up to date.",
            ],
            "nccn": {
                "versions": [
                    "NCCN Supportive Care guidelines family (antiemesis, myeloid growth factors, anemia, survivorship, immunotherapy toxicity)",
                    "Colon Cancer v3.2026 (exercise)",
                    "Prostate Cancer v1.2027 (CVD risk assessment page)",
                ],
                "bullets": [
                    "Structured exercise ≥150 min moderate–vigorous activity/week after adjuvant CRC therapy — formal NCCN recommendation.",
                    "Prostate NCCN: CVD risk-assessment page added — model for cardio-oncology documentation.",
                    "NCCN Guidelines Navigator digital tool expanding — use for rapid antiemesis/growth-factor look-ups.",
                    "Immunotherapy toxicity NCCN pathways are mandatory knowledge as chemo-IO combinations proliferate.",
                ],
            },
        },
        {
            "heading": "15. Indian / NCG practical supportive care",
            "level": 1,
            "paragraphs": [
                "Biosimilar G-CSF and antiemetics improved access. Challenges: dental ONJ prevention logistics, echo wait times, DOAC cost vs LMWH, and uneven dietitian/palliative staffing. "
                "NCG centers emphasize protocolized FN pathways and antimicrobial stewardship.",
            ],
            "bullets": [
                "Teach patients FN precautions in local language; provide 24h contact number.",
                "Olanzapine is inexpensive and high-value — highlight for Indian exams.",
                "Avoid unnecessary ESA use in curative breast/lymphoma pathways.",
            ],
        },
        {
            "heading": "16. Summary flowchart & pearls",
            "level": 1,
            "paragraphs": [
                "Recent advances make supportive care proactive and evidence-based: olanzapine-containing antiemesis, risk-adapted G-CSF, cautious ESA use, optimized bone agents, cardio-oncology surveillance, irAE algorithms, DOAC options for VTE, and lifestyle prescriptions.",
            ],
            "flowchart": [
                "Before chemo: risk-adapt antiemetics + G-CSF + fertility + vaccines",
                "During: monitor CV, counts, nutrition, VTE risk",
                "Toxicity: CTCAE grade → protocolized intervention",
                "Survivorship: bone health, exercise, psychosocial care",
            ],
            "flowchart_title": "Supportive care across the treatment continuum",
            "pearls": [
                "HEC: remember olanzapine 5–10 mg d1–4.",
                "FN ≥20% risk → primary pegfilgrastim/filgrastim.",
                "ESA: non-curative + informed consent only.",
                "Denosumab 120 mg SC q4w vs zoledronic acid 4 mg IV — ONJ counseling both.",
                "irAE grade 3 colitis: steroids → infliximab if refractory.",
                "Exercise is now a guideline-backed anticancer adjunct.",
            ],
        },
    ],
    "Q337": [
        {
            "heading": "1. Introduction — HIV, immunodeficiency & cancer",
            "level": 1,
            "paragraphs": [
                "HIV-1 infection causes progressive CD4+ T-cell depletion, chronic immune activation, and loss of immune surveillance. "
                "Cancer risk rises from oncogenic co-infections, impaired EBV/HHV8/HPV control, and lifestyle confounders (tobacco). ART has shifted the spectrum from AIDS-defining cancers toward non-AIDS-defining cancers (NADCs) as people live longer.",
                "Essay structure demanded by the question: (A) pathogenesis, (B) cancer list AIDS-defining vs NADC, (C) detailed HIV lymphoma management (DLBCL, BL, PEL, PBL, HL).",
            ],
            "bullets": [
                "AIDS-defining: Kaposi sarcoma, non-Hodgkin lymphoma, invasive cervical cancer.",
                "Always start/continue ART — cornerstone of both prevention and lymphoma outcomes.",
            ],
            "pearls": [
                "Opening line: ‘HIV is both an oncogenic facilitator and a treatable comorbidity — ART plus standard lymphoma regimens.’",
            ],
        },
        {
            "heading": "2. Pathogenesis — mechanisms linking HIV to cancer",
            "level": 1,
            "paragraphs": [
                "Mechanisms: (1) loss of virus-specific CD4/CD8 control of EBV and HHV8; (2) chronic B-cell activation and dysregulation → lymphomagenesis; (3) HIV proteins (Tat, Nef) contributing to angiogenesis/inflammation in KS pathogenesis alongside HHV8; "
                "(4) mucosal HPV persistence → cervical/anal dysplasia; (5) HBV/HCV co-infection → HCC; (6) immune reconstitution later changing KS/lymphoma presentations.",
                "Direct HIV integration into oncogenes is not the dominant solid-tumor mechanism; <b>indirect immunodeficiency + co-infection</b> predominates.",
            ],
            "mechanism": [
                ("CD4 depletion", "Failed immune surveillance"),
                ("Chronic inflammation", "Activation-induced cytidine deaminase / mutagenesis milieu"),
                ("EBV co-infection", "BL, many DLBCL, HL biology"),
                ("HHV8/KSHV", "KS, PEL, some multicentric Castleman"),
                ("HPV / HBV / HCV", "Cervical, anal, HCC"),
            ],
            "bullets": [
                "Nadir CD4 and uncontrolled viremia correlate with lymphoma/KS risk.",
                "ART reduces AIDS-defining cancers dramatically but NADCs persist.",
            ],
        },
        {
            "heading": "3. Cancers associated with HIV — spectrum",
            "level": 1,
            "paragraphs": [
                "<b>AIDS-defining</b>: Kaposi sarcoma; NHL (including BL, DLBCL, PEL, primary CNS lymphoma); invasive cervical carcinoma. "
                "<b>NADCs with elevated SIR</b>: Hodgkin lymphoma, anal cancer, lung cancer, HCC, head-and-neck (HPV), skin cancers; relative risks vary by region and smoking prevalence.",
                "Indian context: suspect HIV in unusual KS, PEL, PBL, primary CNS lymphoma, or aggressive extranodal NHL in young adults; offer testing broadly per NACO counseling norms.",
            ],
            "bullets": [
                "Primary CNS lymphoma in HIV: usually EBV+, CD4 often <50 — distinguish from toxoplasmosis.",
                "PBL: oral/jaw masses in low CD4; MYC; plasmablastic phenotype (CD20 often negative).",
                "PEL: body-cavity effusions; HHV8+; often EBV co-positive; CD20 variable/negative.",
            ],
            "flowchart": [
                "New cancer diagnosis in at-risk patient",
                "Offer HIV test (opt-out where policy allows)",
                "If HIV+: CD4, HIV-RNA, opportunistic infection screen",
                "Start/optimize ART + oncology MDT",
                "Cancer-specific therapy with infection prophylaxis",
            ],
            "flowchart_title": "HIV testing and parallel ART/oncology care",
        },
        {
            "heading": "4. General principles of lymphoma care in HIV-AIDS",
            "level": 1,
            "paragraphs": [
                "Modern paradigm: treat HIV-associated lymphomas with <b>full-dose standard regimens</b> plus concurrent ART, growth-factor support, and opportunistic infection prophylaxis — outcomes approach non-HIV patients when CD4 and performance status allow.",
                "Baseline: CBC, chemistries, LDH, uric acid, viral hepatitis, CMV IgG, Toxoplasma IgG, β2-microglobulin, CT/PET-CT, bone marrow as indicated, ECG/echo, pregnancy test, fertility counseling.",
            ],
            "bullets": [
                "PJP prophylaxis (TMP-SMX) for all on intensive chemo or CD4 <200.",
                "Azole/antiviral choices: watch ART–chemo CYP interactions (especially vinca, midazolam, some TKIs).",
                "Rituximab: use if CD20+; caution historically if CD4 very low — modern practice still favors R if CD20+ with infection vigilance (AMC data nuance).",
            ],
            "table_doses": [
                ("TMP-SMX prophylaxis", "1 DS tablet thrice weekly or daily per protocol"),
                ("Filgrastim support", "As needed to deliver on-time cycles"),
                ("Intrathecal MTX/cytarabine", "CNS prophylaxis per histology risk (BL, extranodal)"),
            ],
        },
        {
            "heading": "5. Diffuse large B-cell lymphoma (HIV-DLBCL)",
            "level": 1,
            "paragraphs": [
                "Most common HIV NHL. Often extranodal, high IPI, EBV±. Regimens: <b>R-CHOP</b> or <b>DA-EPOCH-R</b> (NCI infusional regimen widely used in HIV). "
                "AMC and NCI experience support EPOCH-based therapy with concurrent ART and rituximab in CD20+ disease.",
                "CNS prophylaxis for high-risk features (extranodal sites, elevated LDH, MYC rearrangements). Restage with PET-CT; consolidate with ASCT in chemosensitive relapse if ART-controlled and stem-cell feasible.",
            ],
            "table_doses": [
                ("R-CHOP", "Rituximab 375 mg/m² + CHOP q21d ×6 (HIV: G-CSF liberal)"),
                ("DA-EPOCH-R", "Infusional EPOCH + rituximab; dose-adjust to ANC/platelets nadir"),
                ("IT chemotherapy", "Per protocol days for CNS risk"),
            ],
            "table_trials": [
                ("NCI DA-EPOCH-R HIV cohorts", "High CR rates with concurrent ART"),
                ("AMC rituximab studies", "R improves responses in CD20+ HIV-DLBCL with infection monitoring"),
            ],
            "bullets": [
                "Do not empirically dose-reduce solely because of HIV label — fitness and organ function decide.",
                "If CD20-negative plasmablastic morphology → see PBL section (no rituximab benefit).",
            ],
        },
        {
            "heading": "6. Burkitt lymphoma in HIV",
            "level": 1,
            "paragraphs": [
                "Highly aggressive; MYC translocation; often EBV+. Treat with intensive regimens: CODOX-M/IVAC ± R, or DA-EPOCH-R, with mandatory CNS prophylaxis. "
                "TLS risk extreme — hydrate, rasburicase if high-risk, telemetry labs.",
                "Outcomes excellent if treated intensively with ART; avoid CHOP alone for BL.",
            ],
            "flowchart": [
                "Confirm BL (morphology + MYC + immunophenotype)",
                "TLS prophylaxis + ART + echo/performance check",
                "Intensive chemoimmunotherapy + CNS directed therapy",
                "Count recovery → next cycle on time",
                "PET end-of-treatment → surveillance",
            ],
            "flowchart_title": "HIV-Burkitt management skeleton",
            "pearls": [
                "Exam red flag: CHOP for BL = inadequate.",
            ],
        },
        {
            "heading": "7. Primary effusion lymphoma (PEL)",
            "level": 1,
            "paragraphs": [
                "HHV8-positive effusion-based lymphoma (pleural/peritoneal/pericardial) without solid masses usually; extracavitary PEL variants exist. Immunophenotype often null for B-cell markers (CD20−), CD30±, CD138±, EMA±. EBV frequently co-positive.",
                "Therapy: ART essential; CHOP-like or EPOCH-based regimens used; prognosis historically poor. Rituximab generally not useful if CD20−. Consider extracavitary disease radiotherapy in selected cases; clinical trials preferred.",
            ],
            "bullets": [
                "Send HHV8 LANA IHC / PCR on cytology cell block.",
                "Differentiate from HHV8+ multicentric Castleman disease (MCD) — different treatment (rituximab ± antivirals/ART).",
            ],
            "mechanism": [
                ("HHV8 latent proteins", "Drive PEL survival programs"),
                ("Effusion microenvironment", "IL-6 rich, poor drug penetration challenges"),
                ("ART", "Immune recovery + HHV8 control adjunct"),
            ],
        },
        {
            "heading": "8. Plasmablastic lymphoma (PBL)",
            "level": 1,
            "paragraphs": [
                "Aggressive CD20-negative lymphoma with plasmablastic morphology; frequent oral cavity involvement; MYC rearrangements common; EBV often +. Associated with low CD4.",
                "Treatment: intensive regimens (EPOCH, CODOX-based, or myeloma-like approaches in selected reports) + ART; rituximab usually omitted. Prognosis guarded; CNS prophylaxis individualized.",
            ],
            "bullets": [
                "Do not mistake for myeloma — clinical context + HIV + EBV help.",
                "Supportive care intensive: mucositis, infections, TLS.",
            ],
            "table_trials": [
                ("Retrospective EPOCH series in PBL", "Best available evidence; no large RCT"),
            ],
        },
        {
            "heading": "9. Primary CNS lymphoma (HIV-PCNSL)",
            "level": 1,
            "paragraphs": [
                "Typically EBV-associated DLBCL confined to CNS; CD4 often very low. Differentiate from toxoplasma abscess (multiple ring-enhancing lesions, Toxo IgG+). CSF EBV PCR supportive; biopsy when safe.",
                "Treat with high-dose methotrexate-based regimens ± rituximab as tolerated, concurrent ART, and infection prophylaxis. WBRT historically used but neurotoxicity high — prefer chemo-first when feasible.",
            ],
            "bullets": [
                "Empiric Toxoplasma therapy sometimes started pending diagnosis in unstable patients — center-dependent.",
                "ART can produce IRIS — monitor neurologic status.",
            ],
        },
        {
            "heading": "10. Hodgkin lymphoma in HIV",
            "level": 1,
            "paragraphs": [
                "HL is a NADC with markedly increased incidence; often mixed-cellularity, advanced stage, EBV+. ABVD remains a standard backbone with ART and G-CSF as needed; brentuximab vedotin combinations and PD-1 inhibitors enter R/R settings with careful infection/IRIS awareness.",
                "PET-adapted strategies as in non-HIV HL when logistics allow; avoid bleomycin lung toxicity with growth-factor caution (bleomycin + G-CSF interaction debated — follow protocol).",
            ],
            "table_doses": [
                ("ABVD", "Standard doses q14d × up to 6 cycles with ART"),
                ("Brentuximab vedotin", "1.8 mg/kg q3w in BV-based regimens / R/R"),
                ("Nivolumab / pembrolizumab", "R/R HL — monitor irAE + HIV control"),
            ],
            "bullets": [
                "Outcomes approach HIV-negative HL with modern ART.",
                "Screen for TB before IO if endemic risk.",
            ],
        },
        {
            "heading": "11. Kaposi sarcoma & MCD (brief, for completeness)",
            "level": 1,
            "paragraphs": [
                "KS: HHV8-driven; ART is first-line for limited disease; liposomal doxorubicin or paclitaxel for advanced. Pomalidomide is a modern systemic option in some labels/guidelines. "
                "HHV8-MCD: rituximab-based therapy + ART; watch for concurrent lymphoma.",
            ],
            "bullets": [
                "Pulmonary KS: treat promptly — high morbidity.",
                "IRIS-KS after ART initiation — continue ART, treat KS.",
            ],
        },
        {
            "heading": "12. ART interactions & infection prophylaxis checklist",
            "level": 1,
            "paragraphs": [
                "Prefer ART regimens with fewer CYP3A interactions when combining with vincristine/vinblastine (avoid boosting conflicts when possible — involve HIV pharmacist). "
                "Integrase inhibitor–based ART commonly used. Never interrupt ART casually during chemo.",
            ],
            "bullets": [
                "PJP prophylaxis; MAC prophylaxis if CD4 <50 (azithromycin) per guidelines.",
                "HBV co-infection: entecavir/tenofovir backbone to prevent reactivation.",
                "Fungal prophylaxis individualized for prolonged neutropenia.",
            ],
            "flowchart": [
                "HIV pharmacist review of ART ↔ chemo",
                "Start prophylaxis bundle",
                "Deliver full-dose lymphoma therapy",
                "Monitor HIV-RNA / CD4 during treatment",
                "Vaccinate when counts recover (inactivated)",
            ],
            "flowchart_title": "ART–chemo safety pathway",
        },
        {
            "heading": "13. Relapsed disease, transplant & cellular therapy",
            "level": 1,
            "paragraphs": [
                "Salvage chemo + ASCT is appropriate for chemosensitive relapsed HIV-DLBCL/HL with controlled HIV at experienced centers. "
                "CAR-T and bispecifics: emerging case series in HIV+ lymphoma if viral control adequate — discuss trials; not yet universal standard in all Indian centers.",
            ],
            "bullets": [
                "Exclude opportunistic infection before intensive salvage.",
                "Donor/registry issues historically limited allo-SCT; selected cases possible.",
            ],
        },
        {
            "heading": "14. NCCN / guideline bullets (lymphoma & HIV practice)",
            "level": 1,
            "paragraphs": [
                "Cite NCCN B-Cell Lymphomas / Hodgkin guidelines for regimen selection and note HIV-specific principles: concurrent ART, prophylaxis, and preference for standard intensive therapy. "
                "NCCN 2026 B-cell updates (bispecifics, CAR-T sequencing) apply to R/R pathways when HIV controlled.",
            ],
            "nccn": {
                "versions": ["B-Cell Lymphomas v4.2026", "Hodgkin Lymphoma v2.2026"],
                "bullets": [
                    "Treat HIV-associated B-cell lymphomas with standard NCCN regimens plus ART rather than attenuated ‘AIDS-era’ palliative chemo when fitness allows.",
                    "R/R B-cell: consider bispecifics/CAR-T pathways per NCCN 2026 when accessible and HIV controlled.",
                    "HL: ABVD/BV-based and PD-1 pathways as indicated; integrate infection risk assessment.",
                    "Document CD4/HIV-RNA alongside Lugano response assessments.",
                ],
            },
        },
        {
            "heading": "15. Indian / NACO / NCG practical notes",
            "level": 1,
            "paragraphs": [
                "Coordinate with NACO ART centers for uninterrupted antiretrovirals. Generic chemo and biosimilar rituximab improve access. "
                "TB co-infection endemic — screen before steroids/IO. PCR for EBV/HHV8 and PET may be limited peripherally — refer tertiary centers for PEL/PBL/PCNSL.",
            ],
            "bullets": [
                "Offer HIV testing in aggressive extranodal NHL and oral PBL presentations.",
                "Counsel stigma-sensitive care; involve counselors.",
            ],
        },
        {
            "heading": "16. Summary & exam pearls",
            "level": 1,
            "paragraphs": [
                "HIV promotes cancer via immunodeficiency and oncogenic viruses. AIDS-defining cancers and NADCs both matter. Lymphoma care = ART + full-dose histology-specific therapy (R-CHOP/DA-EPOCH-R, intensive BL regimens, specialized PEL/PBL/PCNSL approaches, ABVD for HL) with rigorous infection prophylaxis.",
            ],
            "pearls": [
                "ART concurrent — non-negotiable.",
                "BL ≠ CHOP; use intensive regimens + CNS prophylaxis.",
                "PEL = HHV8 effusion lymphoma, often CD20−.",
                "PBL = oral, CD20−, MYC, EBV — no rituximab.",
                "PCNSL: HD-MTX ± R + ART; rule out Toxo.",
                "Rituximab if CD20+ with infection vigilance.",
            ],
        },
    ],
    "Q338": [
        {
            "heading": "1. Introduction — dual targeting in metastatic RCC",
            "level": 1,
            "paragraphs": [
                "Clear-cell RCC is a VEGF-driven, immunogenic cancer. Front-line standards shifted from TKI monotherapy (sunitinib/pazopanib era) to <b>checkpoint inhibitor (CPI) + VEGF-targeted therapy</b> doublets and to dual CPI (nivolumab + ipilimumab). "
                "This essay covers biologic rationale, landmark combinations with numbers, dosing, toxicity trade-offs, COSMIC-313 nuance, subsequent therapy, and <b>NCCN Kidney Cancer v2.2027</b> (ipi+nivo Cat 1).",
            ],
            "bullets": [
                "Risk-stratify with IMDC (Heng) criteria before choosing 1L.",
                "Confirm histology (clear-cell vs nccRCC) — most phase III doublets enrolled predominantly ccRCC.",
            ],
            "pearls": [
                "Examiners want: rationale paragraph + 4 trial names with PFS/OS + 2L algorithm.",
            ],
        },
        {
            "heading": "2. Biologic rationale — why CPI + VEGF",
            "level": 1,
            "paragraphs": [
                "VHL loss → HIF accumulation → VEGF/PDGF-driven angiogenesis creates an abnormal immunosuppressive tumor microenvironment (TME): MDSCs, regulatory T cells, endothelial barriers to T-cell trafficking, and high VEGF itself impairing dendritic cell function.",
                "VEGF/VEGFR blockade normalizes vessels, reduces MDSCs/Tregs, and can enhance CPI efficacy. PD-1/PD-L1 or CTLA-4 blockade restores antitumor T-cell activity. Combination aims for higher ORR/CR and deeper durable responses than TKI alone.",
            ],
            "mechanism": [
                ("VHL loss / HIF", "VEGF-driven angiogenesis"),
                ("VEGF high TME", "MDSC/Treg recruitment; DC dysfunction"),
                ("Anti-VEGF/TKI", "Vessel normalization; ↓ immunosuppression"),
                ("Anti-PD-1 / CTLA-4", "Reinvigorate T-cell cytotoxicity"),
                ("Clinical result", "Higher ORR, longer PFS/OS vs sunitinib"),
            ],
            "bullets": [
                "Rationale also explains overlapping toxicities (hypertension + immune hepatitis rare but serious).",
                "HIF-2α inhibitor belzutifan exploits the same VHL–HIF axis downstream — relevant for later lines.",
            ],
        },
        {
            "heading": "3. IMDC risk & choosing among 1L options",
            "level": 1,
            "paragraphs": [
                "IMDC factors: time from diagnosis to systemic therapy <1 year, KPS <80, Hb <LLN, corrected Ca >ULN, neutrophils >ULN, platelets >ULN. Favorable (0), intermediate (1–2), poor (≥3).",
                "Dual CPI (nivo+ipi) historically shone in intermediate/poor risk with durable CR; IO+TKI doublets show high ORR/PFS across risks including favorable. Individualize by need for rapid cytoreduction (IO+TKI), autoimmune history, and preference for treatment-free intervals after limited ipi doses.",
            ],
            "flowchart": [
                "Metastatic ccRCC confirmed + IMDC scored",
                "Need rapid response / high burden? → IO+TKI doublet",
                "Intermediate/poor + desire durable IO-only? → nivo+ipi (Cat 1)",
                "Favorable risk: IO+TKI preferred in many pathways; nivo+ipi less favored historically",
                "Progression → subsequent TKI / HIF-2α / clinical trial",
            ],
            "flowchart_title": "1L metastatic ccRCC decision skeleton",
        },
        {
            "heading": "4. CheckMate 214 — nivolumab + ipilimumab",
            "level": 1,
            "paragraphs": [
                "Phase III: nivo 3 mg/kg + ipi 1 mg/kg q3w ×4 → nivolumab maintenance vs sunitinib 50 mg (4/2). Primary focus intermediate/poor IMDC: OS benefit (updated mOS ~47 vs ~27 months range in long follow-up reports; HR ~0.68), ORR ~42% vs ~27%, CR ~10–12% vs ~2%.",
                "Favorable-risk subgroup initially favored sunitinib for ORR/PFS; longer follow-up softens OS differences — still, many guidelines preferred IO+TKI for favorable risk. "
                "<b>NCCN 2026/2027</b>: ipi+nivo upgraded to <b>Category 1 preferred</b> 1L clear-cell RCC — must quote.",
            ],
            "table_trials": [
                ("CheckMate 214", "Nivo+ipi vs sunitinib — OS benefit IMDC int/poor; durable CRs"),
                ("CheckMate 214 long FU", "Sustained OS; plateau suggests cure-like subset"),
            ],
            "table_doses": [
                ("Nivolumab + ipilimumab induction", "Nivo 3 mg/kg + ipi 1 mg/kg IV q3w ×4"),
                ("Nivolumab maintenance", "240 mg q2w or 480 mg q4w (label-aligned)"),
                ("Sunitinib (control)", "50 mg PO daily 4 weeks on / 2 off"),
            ],
            "pearls": [
                "Ipi dose in RCC is 1 mg/kg (lower than melanoma 3 mg/kg combo) — fewer grade 3–4 irAEs than melanoma dosing but still significant.",
            ],
        },
        {
            "heading": "5. KEYNOTE-426 — pembrolizumab + axitinib",
            "level": 1,
            "paragraphs": [
                "Pembro 200 mg q3w + axitinib 5 mg BID vs sunitinib. Landmark: improved OS and PFS across IMDC groups. Illustrative numbers: mPFS ~15.4 vs 11.1 months; ORR ~60% vs ~40%; OS HR ~0.73 with mOS ~45–47 vs ~40 months in updates.",
                "Axitinib is a selective VEGFR TKI — hypertension and diarrhea common; hold axi for immune hepatitis workup overlap.",
            ],
            "table_trials": [
                ("KEYNOTE-426", "Pembro+axi vs sunitinib — OS/PFS/ORR superiority"),
            ],
            "table_doses": [
                ("Pembrolizumab", "200 mg IV q3w or 400 mg q6w"),
                ("Axitinib", "Start 5 mg PO BID; titrate 2.5–10 mg BID per BP/toxicity"),
            ],
        },
        {
            "heading": "6. CLEAR — lenvatinib + pembrolizumab",
            "level": 1,
            "paragraphs": [
                "Lenvatinib 20 mg daily + pembrolizumab vs sunitinib. Among the highest ORR/PFS of IO+TKI triplets-in-spirit doublets: mPFS ~23.9 vs 9.2 months; ORR ~71% vs ~36%; OS HR ~0.66 in primary/updated analyses.",
                "Toxicity: hypertension, diarrhea, proteinuria, dysphonia, weight loss — proactive dose reduction of lenvatinib common and acceptable.",
            ],
            "table_trials": [
                ("CLEAR (KEYNOTE-581)", "Len+pembro vs sunitinib — mPFS 23.9 vs 9.2 mo; high ORR"),
            ],
            "table_doses": [
                ("Lenvatinib (with pembro)", "20 mg PO daily"),
                ("Pembrolizumab", "200 mg q3w"),
                ("Lenvatinib dose reductions", "14 → 10 → 8 mg daily per label toxicity path"),
            ],
            "pearls": [
                "Quote 23.9 vs 9.2 months PFS — highest-yield CLEAR number.",
            ],
        },
        {
            "heading": "7. CheckMate 9ER — cabozantinib + nivolumab",
            "level": 1,
            "paragraphs": [
                "Cabozantinib 40 mg daily + nivolumab vs sunitinib. Cabo hits VEGFR/MET/AXL — useful biology after VEGF resistance. mPFS ~16.6 vs 8.3 months; ORR ~56% vs 27%; OS HR ~0.70.",
                "Cabo toxicity: diarrhea, PPE, hypertension, mucositis; start 40 mg (not 60 mg monotherapy dose) in the IO combo.",
            ],
            "table_trials": [
                ("CheckMate 9ER", "Cabo 40 mg + nivo vs sunitinib — PFS/OS/ORR benefit"),
            ],
            "table_doses": [
                ("Cabozantinib (with nivo)", "40 mg PO daily empty stomach"),
                ("Nivolumab", "240 mg q2w or 480 mg q4w"),
            ],
        },
        {
            "heading": "8. Other IO+VEGF / dual IO references",
            "level": 1,
            "paragraphs": [
                "JAVELIN Renal 101 (avelumab+axitinib) improved PFS; OS maturity less compelling than pembro-based doublets — NCCN demotions occurred over time. "
                "NCCN 2026 notes axitinib + avelumab removed and some post-IO TKI+IO combinations downgraded — show currency.",
            ],
            "table_trials": [
                ("JAVELIN Renal 101", "Avelumab+axi — PFS benefit; OS less practice-defining"),
                ("KEYNOTE-564", "Adjuvant pembrolizumab post-nephrectomy high-risk — separate from metastatic but cite literacy"),
            ],
            "bullets": [
                "Do not conflate adjuvant pembro with metastatic doublets.",
                "PD-L1 is not required to select 1L IO in ccRCC.",
            ],
        },
        {
            "heading": "9. COSMIC-313 nuance — triplet not automatic standard",
            "level": 1,
            "paragraphs": [
                "COSMIC-313: cabozantinib + nivo + ipi vs nivo + ipi in IMDC intermediate/poor. Added cabo improved PFS but with substantially more grade 3–4 toxicity (ALT/AST, diarrhea, PPE). "
                "OS advantage not established as practice-changing at key analyses — therefore triplet is <b>not</b> default 1L for all; discuss only in selected high-risk patients or trials.",
            ],
            "bullets": [
                "Exam maturity: ‘PFS≠adopt triplet blindly; toxicity and OS matter.’",
                "Know why doublet remains standard.",
            ],
            "table_trials": [
                ("COSMIC-313", "Cabo+nivo+ipi vs nivo+ipi — PFS↑, toxicity↑, OS unclear/not standard for all"),
            ],
        },
        {
            "heading": "10. Toxicity management of CPI + VEGF doublets",
            "level": 1,
            "paragraphs": [
                "VEGF side effects: hypertension, proteinuria, bleeding/clotting, wound-healing delay (hold perioperatively), PPE, dysphonia, diarrhea. "
                "CPI: irAEs as usual. Overlap: hepatitis, diarrhea — hold both agents, diagnose immune vs TKI etiology (timing, enzyme pattern), use steroids if immune.",
            ],
            "flowchart": [
                "New AE on IO+TKI",
                "Grade severity (CTCAE)",
                "Hold TKI ± CPI per grade",
                "Immune workup vs TKI toxicity",
                "Steroids if irAE; antihypertensives/dose-reduce TKI if VEGF-type",
                "Restart sequentially when grade ≤1",
            ],
            "flowchart_title": "Toxicity triage on IO+TKI",
            "bullets": [
                "Home BP monitoring mandatory on axi/len/cabo.",
                "Educate for colitis/pneumonitis red flags.",
            ],
        },
        {
            "heading": "11. Second-line and subsequent therapy after IO ± VEGF",
            "level": 1,
            "paragraphs": [
                "After IO+TKI progression: cabozantinib (if not used), lenvatinib + everolimus, tivozanib (TIVO-3), other VEGF TKIs (axitinib, sorafenib historically), belzutifan (HIF-2α) for VHL-associated and selected sporadic ccRCC after prior PD-1 and VEGF therapy.",
                "After nivo+ipi progression: VEGF TKI monotherapy or IO+TKI if not given — sequencing evidence evolving. Rechallenge with CPI alone less established. Cytoreductive nephrectomy selectively in IMDC favorable synchronous disease (CARMENA caution).",
            ],
            "table_trials": [
                ("METEOR", "Cabozantinib vs everolimus post-VEGF — OS/PFS benefit"),
                ("CheckMate 025", "Nivo vs everolimus — historical 2L IO"),
                ("TIVO-3", "Tivozanib vs sorafenib — PFS in highly pretreated"),
                ("LEN+EVE (Study 205 / approvals)", "Len 18 mg + everolimus 5 mg after VEGF"),
                ("Belzutifan trials (LITESPARK program)", "HIF-2α inhibitor activity post IO/VEGF"),
            ],
            "table_doses": [
                ("Cabozantinib monotherapy", "60 mg PO daily (empty stomach)"),
                ("Lenvatinib + everolimus", "18 mg + 5 mg PO daily"),
                ("Tivozanib", "1.34 mg daily 21/7 schedule per label"),
                ("Belzutifan", "120 mg PO daily (monitor Hb — anemia)"),
            ],
            "flowchart": [
                "Progression after 1L",
                "Prior nivo+ipi? → VEGF TKI (cabo preferred often)",
                "Prior IO+TKI? → alternate TKI / len+eve / belzutifan / trial",
                "Oligoprogression? → consider local therapy + continue systemic if otherwise controlled",
                "MDT + NCG/NCCN subsequent lists",
            ],
            "flowchart_title": "Subsequent-line mRCC after modern 1L",
        },
        {
            "heading": "12. Non–clear cell & special populations",
            "level": 1,
            "paragraphs": [
                "nccRCC: heterogeneous (papillary, chromophobe, translocation, collecting duct). Evidence thinner; cabo, immuno-oncology, and genomic matching (MET, FH, SWI/SNF) matter. NCCN 2026: consider tumor genomic testing for trial eligibility.",
                "Brain mets: local therapy + systemic with CNS activity considerations. Poor PS: prefer manageable TKI or best supportive care.",
            ],
            "bullets": [
                "Sarcomatoid features: IO-containing regimens preferred (CheckMate 214 sarcomatoid benefit notable).",
                "Pregnancy: avoid TKI/IO — counsel.",
            ],
        },
        {
            "heading": "13. NCCN Kidney Cancer v2.2027 / 2026 updates (must-box)",
            "level": 1,
            "paragraphs": [
                "Paper IV marks for explicitly writing NCCN category changes.",
            ],
            "nccn": {
                "versions": ["Kidney Cancer v2.2027", "NCCN Immunotherapy toxicity guidelines (supportive)"],
                "bullets": [
                    "Ipilimumab + nivolumab upgraded to Category 1 preferred 1L clear-cell RCC.",
                    "Lenvatinib Cat 2A useful in certain circumstances subsequent (IO-naive or post-IO).",
                    "Several post-IO TKI+IO combinations downgraded Cat 2A→2B; axitinib + avelumab removed.",
                    "Non–clear cell: consider tumor genomic testing for trial eligibility.",
                    "Subsequent therapy: prefer agents with OS/PFS data not previously used (cabo, len+eve, tivozanib, belzutifan as indicated).",
                ],
            },
        },
        {
            "heading": "14. Indian / NCG practical notes",
            "level": 1,
            "paragraphs": [
                "Cost and access: sunitinib/pazopanib generics still used when IO unavailable — disclose resource-stratified care. "
                "IO+TKI and nivo+ipi available at tertiary/NCG centers via schemes; biosimilars limited for CPI. Monitor BP in clinic networks; educate on irAE in local language.",
            ],
            "bullets": [
                "If only TKI accessible: sunitinib/pazopanib/cabo still valid — plan IO referral when feasible.",
                "Cytoreductive nephrectomy not routine for poor-risk IMDC (CARMENA).",
            ],
        },
        {
            "heading": "15. Comparison table for the answer book",
            "level": 1,
            "paragraphs": [
                "Draw a 4-row table in the hall: regimen | key trial | mPFS highlight | OS/ORR pearl | top toxicity.",
            ],
            "table_trials": [
                ("Nivo+ipi", "CM-214 — OS int/poor; CR ~10%+; Cat 1 preferred"),
                ("Pembro+axi", "KN-426 — OS benefit; ORR ~60%"),
                ("Len+pembro", "CLEAR — mPFS 23.9 vs 9.2; ORR ~71%"),
                ("Cabo+nivo", "9ER — mPFS 16.6 vs 8.3; cabo 40 mg"),
                ("Cabo+nivo+ipi", "COSMIC-313 — PFS↑ only; not default"),
            ],
            "bullets": [
                "Column for IMDC applicability.",
                "Column for whether CTLA-4 included (irAE burden).",
            ],
        },
        {
            "heading": "16. Closing summary & exam pearls",
            "level": 1,
            "paragraphs": [
                "CPI + VEGF combinations exploit angiogenesis–immune crosstalk in ccRCC and outperform sunitinib on ORR/PFS/OS. Choose among pembro+axi, len+pembro, cabo+nivo, and nivo+ipi using IMDC, disease tempo, and toxicity. "
                "COSMIC-313 shows more is not always better. Subsequent therapy relies on unused VEGF TKIs, len+everolimus, tivozanib, and HIF-2α inhibition per NCCN 2026/2027.",
            ],
            "pearls": [
                "Rationale: VEGF shapes immunosuppressive TME — dual blockade synergistic.",
                "CLEAR PFS 23.9 vs 9.2; 9ER 16.6 vs 8.3; KN-426 OS HR ~0.73.",
                "CM-214: nivo 3 + ipi 1 ×4 → nivo; Cat 1 preferred NCCN.",
                "Cabo with nivo is 40 mg — not 60 mg.",
                "COSMIC-313: PFS without clear OS mandate for triplet.",
                "2L: cabo / len+eve / belzutifan / tivozanib — avoid recycling identical mechanisms blindly.",
            ],
        },
    ],
}

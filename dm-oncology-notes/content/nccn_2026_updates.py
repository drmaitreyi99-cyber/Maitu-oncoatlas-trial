"""NCCN 2026 / early-2027 guideline updates for DM Medical Oncology exam notes.

Sources: NCCN Guidelines versions posted 2025–2026; ASCO Post NCCN 2026 Annual
Conference roundup (May 2026); OncLive summary of notable NCCN changes heading
into 2026. Cite as 'NCCN Guidelines® Version X.2026/2027' in answers.
Always remind: verify latest NCCN PDF before clinical use.
"""

from __future__ import annotations

# Keyword → list of update bullets for injection into answers
NCCN_VERSIONS = {
    "breast": "Breast Cancer v9.2026",
    "nsclc": "Non-Small Cell Lung Cancer v9.2026",
    "sclc": "Small Cell Lung Cancer v1.2027 / updates from v2.2026",
    "aml": "Acute Myeloid Leukemia v5.2026",
    "cll": "CLL/SLL v2.2027",
    "cml": "Chronic Myeloid Leukemia v2.2027",
    "myeloma": "Multiple Myeloma v2.2027",
    "mds": "Myelodysplastic Syndromes v3.2026",
    "colon": "Colon Cancer v3.2026",
    "rectal": "Rectal Cancer v2.2026",
    "gastric": "Gastric Cancer v4.2026",
    "esophageal": "Esophageal and EGJ Cancers v4.2026",
    "hcc": "Hepatocellular Carcinoma v2.2026",
    "ovarian": "Ovarian Cancer (latest 2026 panel updates)",
    "bladder": "Bladder Cancer v3.2026",
    "prostate": "Prostate Cancer v1.2027",
    "rcc": "Kidney Cancer v2.2027",
    "melanoma": "Melanoma: Cutaneous v3.2026",
    "hodgkin": "Hodgkin Lymphoma v2.2026",
    "bcell": "B-Cell Lymphomas v4.2026",
    "gist": "GIST v1.2026",
    "hnscc": "Head and Neck Cancers v2.2026",
    "cns": "CNS Cancers v4.2026",
    "neuroblastoma": "Neuroblastoma v2.2026",
    "pancreas": "Pancreatic Adenocarcinoma v4.2026",
    "uterine": "Uterine Neoplasms v3.2026",
    "testicular": "Testicular Cancer v1.2027",
    "mesothelioma": "Mesothelioma Pleural/Peritoneal v1.2027",
    "mpn": "Myeloproliferative Neoplasms v3.2026",
    "all": "ALL v3.2026",
}

UPDATES: dict[str, list[str]] = {
    "nsclc": [
        "AJCC 9th edition staging adopted in NCCN NSCLC pathway.",
        "Osimertinib + platinum/pemetrexed AND amivantamab + lazertinib elevated to Category 1 preferred 1L for EGFR mut+ (detected before 1L systemic therapy).",
        "Datopotamab deruxtecan (Dato-DXd) preferred 2L after progression on osimertinib + chemotherapy; also preferred 3L after other preferred 1L regimens; listed for EGFR ex19del/L858R, uncommon EGFR, and EGFR ex20ins subsequent therapy.",
        "Amivantamab + lazertinib useful in certain circumstances after osimertinib progression (multiple lesions) if not previously given.",
        "Repotrectinib or taletrectinib preferred subsequent for ROS1+ with brain metastases.",
        "Ado-trastuzumab emtansine useful in certain circumstances for ERBB2/HER2-mutated NSCLC after frontline progression.",
    ],
    "sclc": [
        "Carboplatin + etoposide + atezolizumab → maintenance lurbinectedin + atezolizumab added for extensive-stage SCLC.",
        "Consider adding lurbinectedin to maintenance atezolizumab if ≥SD after 4 cycles induction, ECOG 0–1, no prior brain metastases.",
    ],
    "breast": [
        "NCCN Guidelines Navigator launched for breast cancer (digital navigation of guidelines).",
        "Imlunestrant added (Cat 2A other recommended) for ESR1-mutated HR+/HER2− recurrent unresectable/stage IV disease (1L or subsequent).",
        "Abemaciclib + fulvestrant + trastuzumab Cat 2B for HR+/HER2+ recurrent unresectable/stage IV.",
        "Neratinib ± trastuzumab or fulvestrant Cat 2A useful in certain circumstances for HER2-activating mutations in stage IV.",
        "Erdafitinib Cat 2A useful in certain circumstances for FGFR1/2/3 fusion or mutation in stage IV.",
        "Metastatic algorithms remain stratified by HR and HER2 status (including HER2-low / ultralow pathways with ADCs such as T-DXd, sacituzumab govitecan).",
    ],
    "colon": [
        "Aspirin 100–162 mg daily × 3 years after recovery from surgery for stage II–III colon (and stage I rectal) with somatic PIK3CA pathway alterations; triggers molecular profiling of all stage II–III tumors.",
        "ATOMIC: FOLFOX or CAPOX + atezolizumab preferred for stage III dMMR/MSI-H colon cancer (benefit assumed to extend to POLE/POLD1 hypermutated).",
        "Checkpoint inhibitor neoadjuvant pathway primary consideration for dMMR rectal tumors (organ preservation possible).",
        "Structured exercise ≥150 min moderate–vigorous activity/week after adjuvant therapy (≈28% relative reduction in deaths/recurrences).",
        "FOLFOX + encorafenib + cetuximab/panitumumab as 1L systemic option for BRAF V600E mCRC (BREAKWATER).",
    ],
    "rectal": [
        "Neoadjuvant immunotherapy preferred pathway for dMMR/MSI-H locally advanced rectal cancer.",
        "FOLFIRINOX neoadjuvant option for pMMR/MSS resectable disease with liver-only and/or lung-only metastases.",
        "Aspirin recommendation as in colon for PIK3CA-altered stage I rectal after surgery.",
    ],
    "gastric": [
        "Universal biomarker workup: HER2 IHC/ISH, PD-L1, MMR/MSI, Claudin 18.2, BRAF, NTRK as indicated — regardless of stage.",
        "Perioperative FLOT remains preferred backbone; FLOT + durvalumab (MATTERHORN) Cat 1 preferred when PD-L1 CPS/TAP ≥1.",
        "KEYNOTE-811: pembrolizumab + trastuzumab + chemo 1L for HER2+ PD-L1+; T-DXd 2L after trastuzumab progression (DESTINY-Gastric04 OS benefit).",
        "Zolbetuximab + fluoropyrimidine/platinum for Claudin 18.2–high HER2-negative disease.",
        "Tislelizumab + fluoropyrimidine/oxaliplatin Cat 1 1L for HER2-negative metastatic adenocarcinoma.",
        "Emphasize limited CPI benefit if PD-L1 negative.",
    ],
    "esophageal": [
        "Same biomarker panel as gastric/EGJ; histology-directed pathways (adeno vs squamous).",
        "Perioperative FLOT preferred for adenocarcinoma; CROSS + adjuvant nivolumab (CheckMate 577) mainly for residual disease after nCRT (often squamous).",
        "Updated OS for CheckMate 577 did not reach significance — discuss nuance in exams.",
    ],
    "myeloma": [
        "Isa-VRd Cat 1 preferred induction for transplant-eligible newly diagnosed MM; Dara-VRd Cat 1 preferred for transplant-deferred/<80 y pathways.",
        "Maintenance daratumumab useful in certain circumstances post-transplant.",
        "Early relapse: teclistamab + daratumumab Cat 1 preferred for PI/IMiD-refractory after ≥1 prior line including len + PI (MajesTEC-3: 36-mo PFS 83.4% vs 29.7%).",
        "Belantamab mafodotin + Vd Cat 1 other recommended after ≥2 prior (PI + IMiD) — DREAMM-7.",
        "Later lines: linvoseltamab preferred after ≥4 prior lines including anti-CD38, PI, IMiD; talquetamab may bridge to BCMA CAR-T.",
    ],
    "aml": [
        "Ziftomenib Cat 2A for R/R NPM1-mutated AML.",
        "CLIA + venetoclax and FLAG-IDA + venetoclax Cat 2B intensive options.",
        "HMA (aza/decitabine) + venetoclax pathway reinforced for unfit / after cytarabine-based induction failure.",
        "Olutasidenib Cat 2B IDH1 option if not candidate for preferred / ivosidenib.",
        "Revumenib listed for R/R (menin inhibitor / KMT2A rearrangements context).",
    ],
    "cll": [
        "Time-limited BCL2i regimens favored for higher uMRD rates vs continuous BTKi or CIT.",
        "Pirtobrutinib (noncovalent BTKi) and lisocabtagene maraleucel after prior BTKi + BCL2i.",
        "Richter transformation: venetoclax + atezolizumab + obinutuzumab; epcoritamab; glofitamab; axi-cel; tisa-cel (Cat 2A options).",
        "Molecular analysis for clonal relatedness in Richter transformation guides therapy.",
    ],
    "ovarian": [
        "PARPi narrowed: removed from many recurrent therapy sections; concentrate on maintenance + biomarker-defined (BRCA/HRD).",
        "Platinum-resistant: nab-paclitaxel + relacorilant preferred (ROSELLA) after ≤3 lines + prior bevacizumab.",
        "Paclitaxel + pembrolizumab ± bevacizumab useful if PD-L1 CPS ≥1 (KEYNOTE-B96 OS signal).",
        "Mirvetuximab in FRα+ platinum-sensitive/resistant pathways; T-DXd for HER2-expressing; avutometinib + defactinib for KRAS-mutated LGSC.",
    ],
    "bladder": [
        "EV + pembrolizumab sole preferred 1L for locally advanced/metastatic urothelial carcinoma.",
        "Perioperative EV+P for cisplatin-ineligible MIBC (KEYNOTE-905/EV-303); NIAGARA (durvalumab + GC) preferred perioperative for cisplatin-eligible.",
        "BCG-unresponsive NMIBC: nadofaragene firadenovec, nogapendekin alfa inbakicept among other recommended; gemcitabine intravesical system for select BCG-unresponsive/intolerant.",
        "2L after EV+P: platinum chemo; genomic testing for T-DXd (HER2) and erdafitinib (FGFR3).",
    ],
    "prostate": [
        "Metastasis-directed therapy incorporated for metachronous oligometastatic APMS (castration-sensitive) disease; new Principles of MDT section.",
        "ADT + niraparib/abiraterone for BRCA2-mutated high-volume (and Cat 2B low-volume) synchronous/metachronous disease.",
        "Terminology: 'ARPIs' replaces 'other hormonal agents'; CVD risk-assessment page; FDA-cleared PET tracer table.",
        "PSMA-PET integration evolving — most level-1 data still based on conventional imaging.",
    ],
    "rcc": [
        "Ipilimumab + nivolumab upgraded to Cat 1 preferred 1L clear-cell RCC.",
        "Lenvatinib Cat 2A useful in certain circumstances subsequent (IO-naive or post-IO).",
        "Several post-IO TKI+IO combinations downgraded Cat 2A→2B; axitinib + avelumab removed.",
        "Non–clear cell: consider tumor genomic testing for trial eligibility.",
    ],
    "melanoma": [
        "Neoadjuvant systemic therapy now preferred initial approach for resectable nodal disease (vs surgery-first historically).",
        "Preferred neoadjuvant: pembrolizumab; ipilimumab + nivolumab (Cat 1). Other: nivo alone; nivo + relatlimab. BRAF/MEKi useful in certain circumstances for BRAF V600.",
    ],
    "hcc": [
        "Nivolumab + ipilimumab Cat 2A other recommended 1L systemic option.",
        "Lenvatinib/sorafenib removed from subsequent-line lists in updated algorithms; refine 2L choices after IO/TKI.",
        "NTRK: entrectinib, larotrectinib, repotrectinib Cat 2A useful in certain circumstances.",
    ],
    "mantle": [
        "TRIANGLE / EA4151: ASCT not for CR with uMRD6 after induction; may consider if dMRD6.",
        "TP53-mutated MCL: BOVen (zanubrutinib/obinutuzumab/venetoclax); acalabrutinib + rituximab if unfit for aggressive induction.",
        "R/R stratified by covalent BTKi-naive/late relapse vs progression/early relapse after cBTKi; mosunetuzumab + polatuzumab; glofitamab listed.",
    ],
    "adc": [
        "Expanding ADC footprint across NCCN 2026: T-DXd (HER2 breast/gastric/NSCLC/urothelial), Dato-DXd (EGFR+ NSCLC), sacituzumab govitecan (breast/urothelial), mirvetuximab (ovarian FRα), enfortumab vedotin (urothelial), belantamab combinations (myeloma), loncastuximab (B-cell).",
    ],
    "parp": [
        "Prostate: ADT + niraparib/abiraterone for BRCA2 APMS subsets.",
        "Ovarian: PARPi focused on maintenance/biomarker-defined; removed from many recurrent treatment sections.",
        "Breast: continue olaparib/talazoparib pathways per germline BRCA and OlympiA adjuvant context.",
    ],
    "immunotherapy": [
        "Earlier-line CPI expansion: ATOMIC stage III dMMR colon; neoadjuvant CPI for dMMR rectal; neoadjuvant melanoma; EV+P bladder; FLOT+durvalumab gastric.",
        "PD-L1 testing emphasized for gastric/EGJ; limited benefit if PD-L1 negative.",
    ],
    "supportive": [
        "Structured exercise formally recommended after adjuvant CRC therapy.",
        "Prostate CVD risk assessment page added.",
        "NCCN Guidelines Navigator digital tool expanding across diseases.",
    ],
}


KEYWORD_MAP: list[tuple[str, list[str]]] = [
    (r"breast|her2|trastuzumab|pertuzumab|tnbc|imlunestrant|sacituzumab|olympia|emilia|destiny|alpelisib|neratinib|dcis|axilla|sentinel", ["breast", "adc", "parp"]),
    (r"lung|nsclc|egfr|osimertinib|alk|ros1|dato|amivantamab|lazertinib|kras|sclc|lurbinectedin", ["nsclc", "sclc", "adc"]),
    (r"colon|colorectal|rectal|msi|mmr|atomic|encorafenib|braf|aspirin|pik3ca|ctdna", ["colon", "rectal", "immunotherapy", "parp"]),
    (r"gastric|stomach|flot|claudin|zolbetuximab|egj|esophageal|matterhorn|checkmate.?577", ["gastric", "esophageal", "adc", "immunotherapy"]),
    (r"myeloma|bortezomib|car.?t|teclistamab|belantamab|linvoseltamab|daratumumab|isatuximab|bcma|proteasome", ["myeloma", "adc"]),
    (r"\baml\b|acute myeloid|flt3|npm1|venetoclax|ziftomenib|revumenib|apml|apl|mds|myelodysplas", ["aml"]),
    (r"\bcll\b|chronic lymphocytic|btk|pirtobrutinib|richter|obinutuzumab", ["cll"]),
    (r"\bcml\b|imatinib|dasatinib|nilotinib|ponatinib|asciminib|tki", ["cml"]),
    (r"ovarian|parp|olaparib|niraparib|rucaparib|hipec|mirvetuximab|relacorilant|fr.?α", ["ovarian", "parp", "adc"]),
    (r"bladder|urothelial|bcg|enfortumab|intravesical|nadofaragene", ["bladder", "adc", "immunotherapy"]),
    (r"prostate|abiraterone|enzalutamide|psma|nm.?crpc|arpi|androgen", ["prostate", "parp"]),
    (r"renal|rcc|kidney|cabozantinib|lenvatinib|axitinib|vegf.*checkpoint|checkpoint.*vegf", ["rcc", "immunotherapy"]),
    (r"melanoma|mucosal melanoma|relatlimab|dabrafenib|trametinib", ["melanoma", "immunotherapy"]),
    (r"hepatocellular|\bhcc\b|liver cancer|sorafenib|atezolizumab.*bevacizumab", ["hcc"]),
    (r"mantle|mcl|triangle|tp53.*lymphoma", ["mantle", "bcell"]),
    (r"hodgkin|brentuximab|nlphl|beacopp|deauville", ["hodgkin"]),
    (r"lymphoma|bite|blinatumomab|car.?t|icans|gvhd|transplant|haplo", ["bcell", "immunotherapy"]),
    (r"adc|antibody.?drug|trastuzumab deruxtecan|enfortumab|mirvetuximab|datopotamab", ["adc"]),
    (r"parp|olaparib|talazoparib|niraparib|rucaparib|hrd", ["parp"]),
    (r"checkpoint|pd.?1|pd.?l1|ctla|nivolumab|pembrolizumab|immunotherapy", ["immunotherapy"]),
    (r"neuroblastoma", ["neuroblastoma"]),
    (r"gist|imatinib.*gist|sunitinib|regorafenib|avapritinib", ["gist"]),
    (r"head and neck|hnscc|cetuximab.*head", ["hnscc"]),
    (r"glioma|glioblastoma|tumor treating fields|ttfields", ["cns"]),
    (r"mesothelioma", ["mesothelioma"]),
    (r"testicular|germ cell", ["testicular"]),
    (r"uterine|endometrial|leiomyosarcoma|carcinosarcoma", ["uterine"]),
    (r"myelofibrosis|jak2|mpn|polycythemia|essential thrombocythemia", ["mpn"]),
    (r"\ball\b|acute lymphoblastic|cns leukemia|blinatumomab", ["all"]),
]


def match_nccn_topics(question: str) -> list[str]:
    import re

    q = question.lower()
    topics: list[str] = []
    for pattern, keys in KEYWORD_MAP:
        if re.search(pattern, q, re.I):
            for k in keys:
                if k not in topics:
                    topics.append(k)
    return topics


def get_nccn_block(question: str) -> dict:
    topics = match_nccn_topics(question)
    bullets: list[str] = []
    versions: list[str] = []
    for t in topics:
        if t in NCCN_VERSIONS and NCCN_VERSIONS[t] not in versions:
            versions.append(NCCN_VERSIONS[t])
        for b in UPDATES.get(t, []):
            if b not in bullets:
                bullets.append(b)
    if not bullets:
        bullets = [
            "Cite the latest disease-specific NCCN Guidelines® (2026/2027 versions) and NCCN Drugs & Biologics Compendium for category ratings.",
            "Mention Category 1 vs 2A/2B and preferred vs other recommended vs useful in certain circumstances.",
            "Cross-check FDA label, institutional availability (India), and National Cancer Grid pathways where relevant.",
        ]
        versions = ["NCCN Guidelines® (latest 2026/2027 disease-specific version)"]
    return {"topics": topics, "versions": versions, "bullets": bullets[:12]}

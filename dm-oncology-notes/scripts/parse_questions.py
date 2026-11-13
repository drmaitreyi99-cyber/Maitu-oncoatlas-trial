#!/usr/bin/env python3
"""Parse all DM Medical Oncology Paper IV questions into structured JSON."""
import json
import re
from pathlib import Path

PAPERS = [
    {
        "exam": "August 2008",
        "code": "KT 020",
        "marks_essay": 20,
        "marks_short": 6,
        "essays": [
            "Discuss the pathophysiology of hemopoiesis and the current status of colony stimulating factors in the management of infectious complications in subjects with febrile neutropenia following myelosuppressive chemotherapy.",
            "Elaborate the role of molecular targeted therapy in the treatment of squamous cell cancer of the head and neck.",
        ],
        "shorts": [
            "Directed donation",
            "Osteoarticular allograft",
            "Thrombopoietin",
            "Mammalian target of rapamycin inhibitors (mTOR)",
            "Graft versus myeloma effect",
            "Proteasome inhibitor",
            "Thallium-201 (Imaging)",
            "Terminally ill children – issue of support",
            "Neurocognitive sequelae of children treated with radiation",
            "Central venous catheter infection",
        ],
    },
    {
        "exam": "February 2009",
        "code": "KU 020",
        "marks_essay": 20,
        "marks_short": 6,
        "essays": [
            "Write a short essay on Epigenetics.",
            "‘Cancer is a multistep process’ – Explain with the example of colon cancer. What could be possible interventions at each step?",
        ],
        "shorts": [
            "Bortezomib",
            "Treatment of CNS leukemia",
            "T-cell non-Hodgkin’s lymphoma",
            "Allogeneic stem cell transplantation for immunodeficiency diseases",
            "Role of immunohistochemistry in the diagnosis of unknown primary",
            "Management of invasive aspergillosis",
            "Treatment of superior vena cava obstruction",
            "Differential diagnosis of ovarian mass in a 15-year-old girl",
            "Communication skills in oncology care",
            "Merits and demerits of treatment in asymptomatic early-stage prostate cancer",
        ],
    },
    {
        "exam": "August 2009",
        "code": "KV 020",
        "marks_essay": 20,
        "marks_short": 6,
        "essays": [
            "Discuss briefly the recent developments in pathology, molecular biology and management of glioblastoma multiforme.",
            "Management of imatinib-resistant chronic myeloid leukemia.",
        ],
        "shorts": [
            "KRAS",
            "RECIST / PD criteria",
            "Lapatinib",
            "IGRT (Image Guided Radiotherapy)",
            "Multikinase inhibitors",
            "Chemoport",
            "GVHD",
            "Molecular targeted therapy in renal cell carcinoma",
            "Chemoprevention",
            "Management of mesothelioma",
        ],
    },
    {
        "exam": "August 2011",
        "code": "KZ 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss in detail Adoptive cell therapy in treatment of Cancer.",
            "Discuss the current status of individualized treatment for Cancer (Tailored Therapy) in Medical Oncology.",
        ],
        "shorts": [
            "Electronic Medical Records",
            "Robotic Surgery in Oncology",
            "Bendamustine",
            "Radiation induced Cardiotoxicity",
            "Olaparib",
            "Image Guided Radiotherapy (IGRT)",
            "Genitourinary Rhabdomyosarcoma",
            "Carcinosarcoma of uterus",
            "Thalidomide",
            "Myelofibrosis",
        ],
    },
    {
        "exam": "August 2012",
        "code": "LB 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss in detail the role of Targeted therapy and recent advances in the Systemic Management of Colorectal Cancers.",
            "Critically analyse the role and issues regarding Intraperitoneal Chemotherapy in Epithelial Ovarian Cancer.",
        ],
        "shorts": [
            "Indications and contraindications of Total Parenteral Nutrition in Cancer Patients",
            "Algorithm for Cancer Pain Management",
            "Utility of Erlotinib in Solid Tumour Oncology",
            "Definition and Indications of Haploidentical Stem cell Transplantation",
            "Recent advances in Systemic therapy in Non Small Cell Lung Cancer",
            "Accelerated Approval of Cancer Drugs",
            "Definition and issues involved in Euthanasia and Physician Assisted Suicide",
            "Clinical Indications and Toxicity of Trastuzumab",
            "Recent Advances in the management of Hormone Refractory Prostate Cancer",
            "Current role of PET Scan in patients with Lymphomas",
        ],
    },
    {
        "exam": "August 2013",
        "code": "LD 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss in detail the role of Targeted therapy in Oncology.",
            "Indications, contraindications, methodology and side effects of Allogeneic bone marrow transplant.",
        ],
        "shorts": [
            "Nanotechnology in oncology",
            "Active specific immunotherapy for cancer",
            "3rd generation Pgp (P-glycoprotein) inhibitors",
            "Differentiating agents in the treatment of cancer",
            "HNPCC prevention",
            "Sorafenib",
            "Radiofrequency ablation",
            "Vandetanib",
            "Metronomic chemotherapy",
            "Predictive molecular tests in cancer management",
        ],
    },
    {
        "exam": "August 2014",
        "code": "LF 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Recent advances in treatment of HER2 Positive Breast cancer.",
            "Discuss in detail about cytogenetics, molecular abnormalities, prognostic factors and newer therapies in Acute Myeloid Leukemia.",
        ],
        "shorts": [
            "Eribulin",
            "Targeted therapy in Hodgkin’s Lymphoma",
            "Ramucirumab in colorectal cancer",
            "Nutritional assessment and intervention in cancer patients",
            "Role of Androgen receptor in breast cancer management",
            "Immunotherapy in malignant melanoma",
            "Surgery vs Observation following Neoadjuvant chemoradiation in locally advanced rectal cancer",
            "Charged particle beams in radiation – advantages and disadvantages of Proton and Carbon beam therapy",
            "Granulosa cell tumours of the ovary",
            "How do you assess cost-effectiveness and use it in decision making?",
        ],
    },
    {
        "exam": "August 2015",
        "code": "LH 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Unique biology of Triple negative breast cancer and targeted agents in the treatment of advanced triple negative breast cancer.",
            "Perioperative and Neoadjuvant chemotherapy in Gastric cancer.",
        ],
        "shorts": [
            "Role of radiation therapy in organ preservation",
            "Second malignancies after treatment of Hodgkin lymphoma",
            "Role of chemotherapy in Retinoblastoma",
            "NFkB signalling in Drug resistance – explain with examples",
            "Myeloid sarcoma and its management",
            "Mechanisms of resistance to antiangiogenic therapy",
            "Stereotactic radiosurgery",
            "EMILIA trial",
            "Management of ductal carcinoma in situ",
            "Chemotherapy in soft tissue sarcoma",
        ],
    },
    {
        "exam": "February 2016",
        "code": "LI 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss the pathology, pathogenesis, risk assessment and treatment of myelodysplastic syndrome.",
            "Discuss the role of chemotherapy in early breast cancer.",
        ],
        "shorts": [
            "Targeted therapy in colon cancer",
            "Plerixafor",
            "Chemoradiotherapy in rectal cancer",
            "Stopping TKI in CML",
            "Advances in treatment of anaplastic large cell lymphoma",
            "Accelerated drug approval",
            "Management of TKI rash",
            "Empiric therapy of carcinoma of unknown primary",
            "Management of intraocular retinoblastoma",
            "Management of malignant pleural effusion",
        ],
    },
    {
        "exam": "August 2016",
        "code": "LJ 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Describe the role of PET scan in early stage Hodgkin lymphoma and optimal management.",
            "Describe the etiology and molecular profile in the development of gastric cancer and role of targeted therapy.",
        ],
        "shorts": [
            "Recent development in the management of malignant Melanoma",
            "Role of Medical Oncologist in the management of operable early Breast cancer",
            "Late Sequelae of Radiotherapy in Hodgkin’s lymphoma",
            "Cytotoxic T–Lymphocyte Associated Antigen-4 (CTLA-4)",
            "Vorinostat",
            "Oligometastasis",
            "Tositumomab",
            "Recent advances in managing bone pain",
            "Targeted therapy of FLT3 positive acute myeloid leukemia",
            "Pazopanib",
        ],
    },
    {
        "exam": "February 2017",
        "code": "LK 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss the checkpoint inhibitors and their clinical application.",
            "Discuss the recent advances in management of chronic myeloid leukemia.",
        ],
        "shorts": [
            "Proton beam therapy",
            "Maintenance rituximab in lymphoma",
            "PI3 kinase and mTOR pathway in breast cancer",
            "Next generation sequencing",
            "Upfront chemotherapy in prostate cancer",
            "Liquid biopsy in cancer",
            "Management of hand foot syndrome",
            "Abiraterone",
            "Recent advances in management of primary CNS lymphoma",
            "Newer drugs in myeloma",
        ],
    },
    {
        "exam": "August 2017",
        "code": "LL 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Pathogenesis, Diagnosis and management of CML and Newer drugs in the treatment of CML.",
            "Management of axilla – Role of axillary Lymph Node Dissection vs Sentinel Lymph Node Biopsy.",
        ],
        "shorts": [
            "Neoadjuvant HER2 targeted therapy in breast cancer",
            "Early intensification treatment approach in advanced Hodgkin Lymphoma",
            "Rasburicase",
            "Preservation of fertility during chemotherapy for breast cancer",
            "Autologous Bone Marrow Transplant in Multiple Myeloma",
            "Maintenance Therapy in Lung cancer",
            "Comprehensive Geriatric assessment in cancer patients",
            "Cancer related fatigue and its management",
            "Stereotactic Body Radiation in treatment of solid tumours",
            "Deauville criteria for PET",
        ],
    },
    {
        "exam": "February 2018",
        "code": "LM 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Pathologic evaluation of carcinoma of unknown primary and management of favourable subsets.",
            "Molecular subtypes of Breast cancer and management of endocrine resistant breast cancer.",
        ],
        "shorts": [
            "Limb salvage and recent options available for bone sarcomas",
            "Nivolumab",
            "Accelerated partial breast irradiation",
            "NeoSphere trial",
            "NCCN evidence blocks – explain with one example",
            "Escalated BEACOPP",
            "Idelalisib",
            "Molecular diagnostic studies in lung cancer",
            "Recommendations for vaccination after Autologous and Allogeneic Hematopoietic cell transplant (HCT)",
            "CheckMate-057 trial",
        ],
    },
    {
        "exam": "August 2018",
        "code": "LN 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss the Diagnostic criteria of Multiple myeloma and Recent developments in the management of Refractory multiple myeloma.",
            "Malignant Melanoma – Diagnosis and Recent Therapeutic Advances.",
        ],
        "shorts": [
            "Role of Androgen Deprivation in Prostate Cancer",
            "Role of JAK2 inhibitors in myeloproliferative disorders",
            "Molecular pathways in Head and Neck cancer",
            "Immunotherapy in lung cancers",
            "Pediatric RMS Risk stratification",
            "Metastatic soft tissue Sarcoma treatment options",
            "Ibritumomab",
            "Stereotactic Radio Surgery",
            "Late effects in cancer survivors",
            "Pertuzumab",
        ],
    },
    {
        "exam": "August 2019",
        "code": "LP 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss CAR-T cells and its therapeutic implications.",
            "Management of locally advanced rectal cancer.",
        ],
        "shorts": [
            "Stopping TKI in CML",
            "ALK positive lung cancer",
            "Maintenance therapy in ovarian cancer",
            "Metformin in cancer",
            "Therapy induced AML",
            "Juvenile myelomonocytic leukemia",
            "Cancer related haemolytic uremic syndrome",
            "Revised staging and response assessment in lymphoma",
            "NUT midline carcinoma",
            "Recent advances in management of metastatic colon cancer",
        ],
    },
    {
        "exam": "February 2020",
        "code": "LQ 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss fertility preservation strategies in cancer.",
            "Discuss thromboembolism in cancer, its prevention and treatment.",
        ],
        "shorts": [
            "Robotic surgery in oncology",
            "Brentuximab",
            "Management of biochemical relapse in ovarian cancer",
            "Olanzapine",
            "Chemotherapy induced cardiac dysfunction",
            "Checkpoint inhibitor toxicity and its management",
            "Merkel cell tumour",
            "Phase IV trials",
            "PI3K inhibitors",
            "Chemotherapy in stage II colon cancer",
        ],
    },
    {
        "exam": "November 2020",
        "code": "LR 020",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss the role of PARP inhibitors in cancer.",
            "Discuss the staging, prognostic factors and management of chronic lymphocytic leukemia.",
        ],
        "shorts": [
            "Management of stage 1 testicular germ cell tumor",
            "Advantages and disadvantages of second and third generation tyrosine kinase inhibitors over imatinib in newly diagnosed chronic myeloid leukemia",
            "Pregnancy associated breast cancer",
            "Intra-arterial chemotherapy in retinoblastoma",
            "Management of metastatic gastrointestinal stromal tumor (GIST)",
            "Venetoclax",
            "Management of acute promyelocytic Leukemia (APML)",
            "Non-pharmacological management of pain",
            "Chemotherapy in gastric cancer",
            "National cancer grid of India",
        ],
    },
    {
        "exam": "August 2021",
        "code": "DM 0821",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss the management of high-risk neuroblastoma.",
            "Discuss the recent advances in management of HER2/neu positive breast cancer.",
        ],
        "shorts": [
            "Total body irradiation",
            "Sequencing of treatment in epidermal growth factor receptor (EGFR) positive metastatic lung cancer",
            "Role of autologous stem cell transplantation in multiple myeloma",
            "Management of nodular lymphocyte predominant Hodgkin lymphoma (NLPHL)",
            "Lung cancer screening",
            "Role of adjuvant chemotherapy in endometrial cancer",
            "Role of hyperthermic intraperitoneal chemotherapy (HIPEC) in ovarian cancer",
            "Discuss whether progression free survival is a surrogate marker for overall survival in clinical trials",
            "Recent advances in management of hepatocellular carcinoma",
            "Intravesical immunotherapy and chemotherapy",
        ],
    },
    {
        "exam": "February 2022",
        "code": "DM 0222",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss the current status of DNA microarray profiling in management of malignant tumour.",
            "Recent advances in supportive care in cancer chemotherapy.",
        ],
        "shorts": [
            "Diet and breast cancer",
            "Newer cancer chemotherapy agents for ovarian cancer",
            "Tumor suppressor gene",
            "CNS directed therapy in ALL – current status",
            "Tumor vaccines",
            "Heavy particle beam Radiation therapy",
            "Gene manipulation in Radiotherapy",
            "Vorinostat",
            "Molecular biology of colon cancer",
            "Myeloma response criteria",
        ],
    },
    {
        "exam": "August 2022",
        "code": "DM 0822",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss the role of HIV in the pathogenesis of Cancer. Discuss the cancers associated with HIV infection. Discuss in detail the management of various lymphomas arising in a patient with HIV-AIDS.",
            "Discuss the rationale of combining checkpoint inhibitor (CPI) and VEGF inhibitors in metastatic renal cell carcinoma. Discuss the various CPI with VEGF inhibitor combinations and the evidence. Discuss 2nd line treatment of metastatic renal cell carcinoma.",
        ],
        "shorts": [
            "Blinatumomab – class of drug and various uses",
            "E-Cigarettes – Merits and Demerits",
            "Various types of intraperitoneal chemotherapy",
            "Adverse events in CAR-T cell therapy",
            "Capmatinib – its target and evidence to use",
            "Pharmacogenomics in Cancer Therapeutics",
            "Antibody Drug conjugates used in Cancer therapeutics",
            "CRISPR–Cas9",
            "Nanoparticle formulation of chemotherapeutic agents and its advantages",
            "Digital Droplet PCR",
        ],
    },
    {
        "exam": "February 2023",
        "code": "DM 0223",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss the role of genes involved in mismatch repair (MMR) mechanisms in various cancers. Discuss testing modalities of MMR genes and their interpretation. Describe the mechanism of MMR as a biomarker for checkpoint inhibitors.",
            "WHO 2022 classification of Myeloid malignancies and describe in detail diagnostic investigations, molecular testing, ELN 2022 risk stratification and management of Acute Myeloid Leukemia (AML).",
        ],
        "shorts": [
            "BiTE (Bi-specific T-cell engager) – describe and discuss the drugs",
            "ENDS (Electronic Nicotine Delivery Systems) – Merits and Demerits",
            "Local Ablative therapies in inoperable Hepatocellular Carcinoma",
            "ICANS (Immune effector cell-associated Neurotoxicity Syndrome)",
            "Brentuximab vedotin",
            "Define NM-CRPC (Non-Metastatic Castrate-Resistant Prostate Cancer) and describe its treatment",
            "Use of PARP inhibitors in various cancers",
            "Various modalities of T cell depletion in Haploidentical transplantation",
            "Tumor treating fields",
            "Adjuvant therapies in Melanoma",
        ],
    },
    {
        "exam": "January 2024",
        "code": "DM 0124",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Methods of HER2 testing and interpretation, therapeutic strategies for HER2+ve Metastatic Breast Cancer.",
            "Practice changing advances in early stage NSCLC.",
        ],
        "shorts": [
            "Multifocal ground glass and Lepidic adenocarcinoma of lung",
            "Engraftment and engraftment syndrome",
            "Screening for colorectal cancer",
            "Hürthle cell carcinoma",
            "Hereditary papillary renal cell carcinoma",
            "Bispecific T-Cell engagers",
            "Clinicopathologic features of breast cancer with intrinsic subtypes",
            "Systemic therapy in medullary thyroid carcinoma",
            "Alpelisib",
            "Uterine leiomyosarcoma",
        ],
    },
    {
        "exam": "February 2025",
        "code": "DM 0225",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Antibody drug conjugates in medical oncology practice.",
            "Mucosal melanoma.",
        ],
        "shorts": [
            "Innovative approaches in treatment of glioma",
            "HIPEC",
            "Immune checkpoint inhibitors in Hodgkin’s lymphoma management",
            "Venetoclax",
            "Reduced intensity conditioning regimen in stem cell transplantation",
            "PI3 Kinase pathway inhibitors",
            "SBRT (Stereotactic Body Radiotherapy)",
            "Osimertinib",
            "Vaccine preventable cancers",
            "Chemotherapy associated peripheral neuropathy",
        ],
    },
    {
        "exam": "January 2026",
        "code": "DM 0126",
        "marks_essay": 15,
        "marks_short": 7,
        "essays": [
            "Discuss the development and clinical application of next-generation targeted therapies, including KRAS inhibitors, PARP inhibitors, and antibody–drug conjugates.",
            "Explain the role of real-world evidence and digital oncology tools (AI decision support, digital biomarkers, remote monitoring) in modern cancer care.",
        ],
        "shorts": [
            "Sacituzumab govitecan",
            "Tumour-agnostic approvals—current indications",
            "Role of precision radiation (SBRT, FLASH therapy)",
            "Novel markers predicting immunotherapy response",
            "CAR-NK and off-the-shelf cellular therapies",
            "Targeted therapies for hematologic malignancies—BTK inhibitors, FLT3 inhibitors",
            "Radioligand therapy—recent clinical applications",
            "Vaccines in oncology—therapeutic vs preventive",
            "ctDNA monitoring in colorectal cancer",
            "Role of microbiome modulation in enhancing immunotherapy effects",
        ],
    },
]


def slugify(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80]


def build_bank():
    questions = []
    qid = 1
    for paper in PAPERS:
        for i, q in enumerate(paper["essays"], 1):
            marks = paper["marks_essay"]
            target_pages = 15 if marks >= 15 else 12
            questions.append(
                {
                    "id": f"Q{qid:03d}",
                    "exam": paper["exam"],
                    "code": paper["code"],
                    "type": "essay",
                    "number": i,
                    "marks": marks,
                    "target_pages": target_pages,
                    "question": q,
                    "slug": slugify(f"{paper['exam']}-essay-{i}-{q}"),
                }
            )
            qid += 1
        for i, q in enumerate(paper["shorts"], 1):
            marks = paper["marks_short"]
            target_pages = 11 if marks >= 7 else 8
            questions.append(
                {
                    "id": f"Q{qid:03d}",
                    "exam": paper["exam"],
                    "code": paper["code"],
                    "type": "short",
                    "number": i,
                    "marks": marks,
                    "target_pages": target_pages,
                    "question": q,
                    "slug": slugify(f"{paper['exam']}-short-{i}-{q}"),
                }
            )
            qid += 1
    return questions


def main():
    out = Path(__file__).resolve().parents[1] / "questions" / "question_bank.json"
    qs = build_bank()
    out.write_text(json.dumps({"count": len(qs), "questions": qs}, indent=2))
    essays = sum(1 for q in qs if q["type"] == "essay")
    shorts = sum(1 for q in qs if q["type"] == "short")
    print(f"Wrote {len(qs)} questions ({essays} essays, {shorts} shorts) -> {out}")


if __name__ == "__main__":
    main()

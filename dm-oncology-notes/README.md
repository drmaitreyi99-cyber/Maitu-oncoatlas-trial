# DM Medical Oncology — Paper IV Exam Answer Notes

Exam-oriented answer PDFs for **all extractable questions** from the Tamil Nadu Dr MGR Medical University D.M. Medical Oncology Paper IV (*Recent Advances*) question compilation (2008–2026).

## What you get

| Item | Details |
|------|---------|
| Question PDFs | **288** individual PDFs (`pdfs/by_question/`) |
| Essays / Elaborate | **48** answers · typically **14–16 pages** · 15–20 marks |
| Short notes | **240** answers · typically **11–13 pages** · 6–7 marks |
| NCCN cheat sheet | `pdfs/NCCN_2026_Updates_CheatSheet.pdf` |
| Master index | `pdfs/00_Master_Index.pdf` |
| Zip bundle | `/opt/cursor/artifacts/dm-oncology-exam-notes/DM_Oncology_PaperIV_All_Answers.zip` |

Each answer includes:

- Mechanisms / hallmark biology  
- Diagnostic & biomarker work-up  
- Management algorithms (flowcharts)  
- **Doses & regimens**  
- **Landmark clinical trials** tables  
- Toxicities & supportive care  
- **NCCN Guidelines® 2026 / 2027 updates** (boxed for quick copy into the answer sheet)  
- Exam pearls, vignettes, and revision flash-card structure  

## NCCN 2026

Answers inject disease-matched updates (examples):

- **NSCLC v9.2026** — osi+chemo & amivantamab+lazertinib Cat 1 preferred; **Dato-DXd** preferred after osi+chemo  
- **Breast v9.2026** — imlunestrant (ESR1), HER2-mut/FGFR options  
- **Myeloma v2.2027** — Tec+Dara (MajesTEC-3), belantamab+Vd, linvoseltamab  
- **AML v5.2026** — ziftomenib (NPM1 R/R), menin inhibitor pathways  
- **Colon v3.2026** — ATOMIC atezolizumab adjuvant dMMR; aspirin in PIK3CA; exercise  
- **Gastric v4.2026** — FLOT+durvalumab; Claudin18.2; T-DXd 2L HER2+  
- Plus bladder EV+P, melanoma neoadjuvant IO, RCC ipi+nivo Cat 1, prostate MDT/PARPi, ovarian ROSELLA, etc.

## Regenerate

```bash
python3 dm-oncology-notes/scripts/parse_questions.py
python3 dm-oncology-notes/scripts/generate_all.py
# samples only:
python3 dm-oncology-notes/scripts/generate_all.py --ids Q277 Q278
```

## Disclaimer

For **university exam revision**. Verify the current full NCCN PDF, FDA/CDSCO labels, and institutional protocols before clinical use. Early image-only papers (≈2001–2007) in the source scan were not text-extractable; coverage starts August 2008.

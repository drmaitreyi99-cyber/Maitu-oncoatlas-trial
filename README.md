# MAITU ONCOTRIAL ATLAS

From Landmark Trials to Latest Breakthroughs.  
Master Oncology Trials. Master Your Exams.

A local study application for DM/DNB Medical Oncology residents, ESMO candidates, fellows, and teachers. It opens in the browser. You do not need to write code to use it.

This is an educational atlas, not a prescribing guide. It does not replace a protocol or a current guideline.

## Open the app on Windows

1. Install Node.js from [https://nodejs.org](https://nodejs.org) (the LTS version).
2. Open this folder.
3. In the address bar of the folder, type `powershell` and press Enter.
4. Run:

```powershell
npm install
npm run dev
```

5. Open [http://localhost:3000](http://localhost:3000).

Other checks:

```powershell
npm test
npm run typecheck
npm run lint
```

## Demo sign-in

Supabase is optional. Without it, the app runs in local demo mode. Bookmarks, reviews, and revision scores stay in this browser.

| Role | Email | Password |
| --- | --- | --- |
| Resident | resident@maitu.demo | atlas |
| Evidence reviewer | reviewer@maitu.demo | review |

The reviewer account can approve or reject citation queue items. Approval does not create survival numbers.

## What is verified

Breast, lung, ovarian, and cervical landmark trials are seeded from cited papers. A figure is shown only when its analysis is marked peer-reviewed and linked to a publication, endpoint definition, and, when available, a cutoff date.

If a dose, hazard ratio, or follow-up result was not confirmed for this seed, the screen says **Verification pending**. The app does not guess it.

Primary results and later overall-survival or progression-free survival updates are stored as separate rows. An update does not overwrite the first analysis.

Questions, flashcards, and viva answers are generated from those stored records. They are original items for this atlas. They are not copies of ESMO or university papers.

## Literature search

The Updates page can query:

- PubMed E-utilities
- ClinicalTrials.gov API version 2
- Crossref

Those routes return citations only. They do not extract efficacy. Conference feeds for ESMO, ASCO, ASH, ELCC, WCLC, EHA, and SABCS stay off unless you have a licensed source (`ENABLE_CONFERENCE_ADAPTERS` in `.env.example`).

### Daily automatic discovery

`/api/cron/discover` checks PubMed, Crossref, and ClinicalTrials.gov every day when the app is deployed on Vercel. `vercel.json` contains the 02:15 UTC schedule. Add `CRON_SECRET` and Supabase credentials to the deployment.

The job:

1. searches recent oncology trial publications and registry changes;
2. deduplicates by NCT, PMID, and DOI;
3. suggests organ, subtype, stage, biomarker, setting, and line of therapy;
4. writes metadata to the protected evidence-review queue.

It never publishes extracted efficacy automatically. A medical reviewer must verify the publication, endpoint definition, analysis cutoff, and numerical results first. Conference adapters remain disabled without licensed access.

The **Benefits in Months** page calculates a descriptive difference only when both published medians are numeric. If a median was not reached, it shows a verified landmark-rate difference when available, or “Not estimable.” A difference between medians is not an individual patient’s expected survival gain.

Copy `.env.example` to `.env.local` if you later add Supabase or an NCBI email address.

## Database

`supabase/migrations/001_initial_schema.sql` is the normalized PostgreSQL schema for organs, trials, arms, regimens, publications, endpoint analyses, adverse events, reviews, questions, flashcards, progress, bookmarks, and audit logs. The local demo reads the TypeScript seed instead of a live database.

## Where to read next

- Trial cards: Organ library, then a trial name
- Timeline: Historical Trial Timeline
- Comparison: Trial Comparison, with the cross-trial warning
- Practice: Flashcards, MCQ bank, Viva, Mock examinations, Revision planner, Error notebook

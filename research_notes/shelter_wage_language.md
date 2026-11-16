# Open-source AI/ML tools for shelter, living wage and endangered languages: what was released and whether it is used (as of 16 Nov 2026)

Verification labels used on every claim:
- **[V]** = verified in a page I fetched, or in a repository I cloned on 2026-11-16 (last-commit date = last commit on the default branch; licence = text of the LICENSE file at the repo root).
- **[S]** = seen only as a search-result title/link; the page itself was not read.
- **[U]** = UNVERIFIED background knowledge (model memory, cutoff mid-2026). Treat as a lead, not a fact.
- "not found" = I looked and found no evidence; it does not mean the thing does not exist.

Tooling limits that shaped these notes: the GitHub API and web UI were blocked, so "archived" flags could not be read directly (only last-commit dates and licence files via `git clone`); Hugging Face model pages were fetchable only where a search result linked to them; search results returned titles without snippets. Roughly 60 tools are covered; depth is uneven and is flagged per item.

Status vocabulary (the distinction the user asked for):
- **DEPLOYED** = a named agency/union/community uses it, with a source.
- **RESEARCH-ONLY** = published, evaluated retrospectively or in shadow mode, never run on live decisions.
- **OPEN-BUT-UNUSED** = code/weights/data public, no deployment evidence found, repo dormant.
- **OPEN-BUT-RESTRICTED** = public but licence blocks practical use (non-commercial, no-scrape, custom terms).
- **CLOSED-BUT-DEPLOYED** = in use, but the model/code is not public.
- **DEPLOYED-THEN-ABANDONED** = was used, then shut down or sunsetted.
- **DELIBERATELY-NOT-OPEN** = community chose a restrictive licence on sovereignty grounds.

---

## Key question 1 (shelter): which housing/homelessness ML tools are deployed, which were pilots, which repos are dormant?

### Takeaway
The housing tools that are actually running in agencies (LA County's Homelessness Prevention Unit model, Allegheny County's AHA) are **closed**: built on restricted linked administrative data with no public code found. The tools that are **open** are either research artefacts whose data cannot be shared (Kube/Das/Fowler; CMU/Allegheny rental-assistance model, shadow-mode only) or data/advocacy tools that are open and genuinely used (JustFix Who Owns What, Eviction Lab tracking data, HOT fAIr). The clearest "open, published, dormant" items are the Ramp building-footprint code (last commit Sept 2022), the Eviction Lab ETL repo (2019), the AEMP COVID map (2021) and older DSSG repos (2017-2019, several under custom non-OSI terms).

### Cited Findings

**LA County / California Policy Lab homelessness-risk model: CLOSED-BUT-DEPLOYED**
- The Homelessness Prevention Unit (HPU) is a partnership of California Policy Lab (UCLA), LA County Department of Health Services and the LA County Chief Information Office; CPL built the predictive model that identifies residents at highest risk. Program launched 2021; pilot phase May 2022 to Feb 2023. [V] — [CPL news, 10 Jul 2025](https://capolicylab.org/news/new-report-early-signs-of-success-from-la-countys-homelessness-prevention-pilot/)
- 1,498 people served to date; 86% retained housing on program exit; average assistance $6,469 per household; enrollment rate rose from 21% to 35%. [V] — [same source](https://capolicylab.org/news/new-report-early-signs-of-success-from-la-countys-homelessness-prevention-pilot/)
- Early (non-randomized) comparison of 335 enrollees vs 1,285 eligible non-enrollees: enrollees "71% less likely to enter a homeless shelter or have contact with street outreach teams within 18 months". The randomized trial result is expected in 2027, so there is no causal estimate yet. [V] — [same source](https://capolicylab.org/news/new-report-early-signs-of-success-from-la-countys-homelessness-prevention-pilot/)
- Whether model code or weights are public: **not found**; the CPL page does not mention a release. [V that the page is silent] — [same source](https://capolicylab.org/news/new-report-early-signs-of-success-from-la-countys-homelessness-prevention-pilot/)

**Allegheny Housing Assessment (AHA), VI-SPDAT replacement: CLOSED-BUT-DEPLOYED, audited**
- Allegheny County deployed AHA in 2020; it replaced the VI-SPDAT in coordinated-entry intake in August 2020. Built by Allegheny County DHS with the Centre for Social Data Analytics (Auckland University of Technology), model development from 2018. [V] — [Cheng, Drayton, Chouldechova, Vaithianathan, arXiv 2407.21209 (ar5iv)](https://ar5iv.labs.arxiv.org/html/2407.21209)
- VI-SPDAT was used in 39 states/countries by 2015; its maintainers announced a phase-out by Dec 2020 after criticism of poor validation and racial bias. [V] — [same paper](https://ar5iv.labs.arxiv.org/html/2407.21209)
- Audit finding: VI-SPDAT tended to score white clients higher and Black clients lower; after AHA, decisions tracked AHA scores better and score distributions were similar across races, **but service-rate disparities did not clearly shrink**, which the authors attribute to the survey-based fallback (Alt-AHA) and eligibility rules (chronic homelessness, veteran status). [V] — [arXiv abstract 2407.21209v3](https://arxiv.org/abs/2407.21209v3)
- Public model/code: **not found**; the paper mentions only a public methodology report. [V that the paper is silent] — [ar5iv](https://ar5iv.labs.arxiv.org/html/2407.21209)

**CMU DSSG / Allegheny County rental-assistance prioritization (dssg/acdhs_housing_public): RESEARCH-ONLY to PILOT; code open, data closed**
- Vajiac, Frey, Baumann, Smith, Amarasinghe, Lai, Rodolfa, Ghani: model ranks people facing eviction by predicted homelessness risk. Ran in **shadow mode** Sept 2022 to Aug 2023 (live data, no effect on decisions); RCT "planned but not yet conducted" at time of writing. [V] — [arXiv 2403.12599](https://arxiv.org/pdf/2403.12599)
- Results: precision@100 about 0.20 (about 20% better than the best heuristic, about 10x the first-come-first-served approximation); in shadow deployment 22 of the top 100 used homelessness services within 12 months, 17 of whom the current process missed. Recall for first-time homelessness only about 4%; slightly under-serves women. [V] — [arXiv 2403.12599](https://arxiv.org/pdf/2403.12599)
- Repo: MIT licence, 12 commits, 4 stars; README: "This data is not publicly available; researchers interested in collaborating with ACDHS should contact them directly." Last-commit date not readable. [V via mirror] — [repo mirror](https://github-users.yhajoa.workers.dev/dssg/acdhs_housing_public)
- A March 2025 Harvard Data-Smart article describes the same Allegheny/CMU effort as in "piloting and refinement", "initial pilot results show success", no permanent rollout described. Note it dates the project start to 2023, which conflicts with the paper's Sept 2022 shadow start. [V] — [Data-Smart City Solutions, 18 Mar 2025](https://datasmart.hks.harvard.edu/data-driven-models-eviction-prevention)

**Kube, Das, Fowler allocation model: RESEARCH-ONLY (proof of concept)**
- "Fair and Efficient Allocation of Scarce Resources Based on Predicted Outcomes: Implications for Homeless Service Delivery", JAIR 76 (2023); preliminary version AAAI 2019. Uses HMIS records 2007-2014 from an unnamed "major metropolitan area" plus hotline calls. **Not deployed**: "a proof of concept through a case study", evaluated retrospectively. [V] — [NSF PAR copy](https://par.nsf.gov/servlets/purl/10415667)
- Documented barrier is ethical, not technical: the optimized allocation is not Pareto-improving; about 21% of households (2,133 of 13,940) would be assigned a service with a *higher* predicted re-entry probability. [V] — [same](https://par.nsf.gov/servlets/purl/10415667)
- Released: a GitHub repo with counterfactual predictions for 13,940 households; no licence stated in the paper; underlying data under data-sharing agreements. [V] — [same](https://par.nsf.gov/servlets/purl/10415667)
- That the metro area is St. Louis: [U] (search-result titles associate the work with St. Louis; the paper anonymizes it).
- Fowler and Das now have a J-PAL "Project AI Evidence" pilot (Spring 2025 RFP) evaluating an ML model that predicts court eviction within three months to drive community outreach with unnamed local housing advocates. Status: pilot, no dates or results. [V] — [J-PAL](https://www.povertyactionlab.org/initiative-project/evaluating-ai-enabled-eviction-prevention-low-income-tenants)

**New York eviction prediction: RESEARCH-ONLY**
- Rodriguez, Dohler et al. (arXiv 2512.12919, Dec 2025), Bronx County: forecasting eviction filings from open data (Housing Data Coalition filings, ACS, DeepMaps). "Proof-of-concept", checked retrospectively against 2020-21; all models over-predicted filings 2.6 to 3.3x (moratoria); one input series (DeepMaps) ended Dec 2020. Read only through a third-party summary, not the paper. [V of the summary only] — [summary page](https://www.themoonlight.io/review/open-source-software-and-data-for-human-service-development-a-case-study-on-predicting-housing-instability)

**JustFix "Who Owns What": DEPLOYED, open, active**
- Repo JustFixNYC/who-owns-what: GPL-3.0, last commit 2026-09-24. [V, cloned] — [repo](https://github.com/JustFixNYC/who-owns-what)
- Use by tenants/organizers: a June 2025 Shelterforce feature on tenant tech exists but the page could not be fetched (redirect loop). User numbers: **not found**. [S] — [Shelterforce](https://shelterforce.org/2025/06/17/tech-tools-help-tenants-push-back-against-problematic-landlords/)

**Eviction Lab: DEPLOYED as data infrastructure, active; older code dormant**
- Eviction Tracking System v4.0 (2026): weekly/monthly filing CSVs at tract/ZIP level for 43 cities and 11-13 states/regions, page updated 7 Oct 2026, most files current to 10/2026. No licence stated; citation requested. [V] — [Eviction Lab, Get the Data](https://evictionlab.org/eviction-tracking/get-the-data/)
- Repo EvictionLab/eviction-lab-etl (the original national-map pipeline): MIT, last commit 2019-11-03. [V, cloned] — [repo](https://github.com/EvictionLab/eviction-lab-etl)

**Anti-Eviction Mapping Project: one repo checked, dormant**
- antievictionmappingproject/covid-19-map: MIT, last commit 2021-01-18 (the COVID tenant-protections map; an event-bound project). [V, cloned] — [repo](https://github.com/antievictionmappingproject/covid-19-map)
- AEMP's other tools (Evictorbook etc.): not checked.

**HOT fAIr: DEPLOYED (open, active), with measured usability limits**
- Repos hotosm/fAIr (AGPL-3.0, last commit 2026-11-15) and hotosm/fAIr-utilities (AGPL-3.0, 2026-08-21). [V, cloned] — [fAIr](https://github.com/hotosm/fAIr)
- User test (Nov 2024, 26 mappers, presented at State of the Map 3 Oct 2025): fAIr reached 78.22% accuracy at 1.97 buildings/min vs 86.08% at 4.23 buildings/min in JOSM; participants said fAIr "was not their preferred tool for humanitarian mapping"; more than half would return; outputs usually needed manual correction and merged adjacent buildings. [V] — [SotM 2025 talk](https://pretalx.com/sotm2025-osm-science/talk/WJDTBX)
- Study of AI-generated buildings in OSM (Fila, Štampach, Herfort, Int. J. Digital Earth 18(1), 2025): 75% are concentrated in five countries (USA, Nigeria, Algeria, India, Kenya); they are edited less often afterwards; AI-assisted mapping correlates with population, not with HDI or local mapper community size. [V] — [HeiGIT, 12 Mar 2025](https://heigit.org/?p=38589)

**Ramp (Replicable AI for Microplanning): OPEN-BUT-DORMANT as a standalone repo**
- devglobalpartners/ramp-code: Apache-2.0, **last commit 2022-09-15**. [V, cloned] — [repo](https://github.com/devglobalpartners/ramp-code)
- Training data and baseline model are hosted on Source Cooperative and by Radiant Earth. [S] — [source.coop/ramp](https://source.coop/ramp), [model_ramp_baseline](https://www.github.com/radiantearth/model_ramp_baseline)
- DevGlobal/WHO launch coverage could not be fetched; that fAIr uses Ramp as its base model is [U].

**Older DSSG repos (dormant; several not OSI-licensed)**
- dssg/johnson-county-ddj-public: last commit 2017-05-05, custom "BY DOWNLOADING this PROGRAM YOU AGREE TO THE FOLLOWING TERMS OF USE" licence. dssg/police-eis: 2018-11-29, same custom terms. dssg/syracuse_public: 2019-02-06, same. dssg/cincinnati2015-public (blight inspections): MIT, 2017-04-20. dssg/barefoot-winnie-public: MIT, 2019-10-26. [V, cloned] — [dssg org](https://github.com/dssg)
- The DSSG *toolkits* are alive: dssg/triage (MIT, last commit 2026-10-28), dssg/aequitas (MIT, 2026-05-12). [V, cloned] — [triage](https://github.com/dssg/triage), [aequitas](https://github.com/dssg/aequitas)
- Guessed housing repo names (dssg/tulsa-public, dssg/bank-eviction, dssg/sf-housing, dssg/hitachi-public, DataKind-SG/slum-mapping) do not exist or are private: clone failed. This is "not found", not evidence of deletion.

### Inferences
- In housing, "open" and "deployed" are close to mutually exclusive for *predictive models*, because the feature set is linked county administrative data that cannot leave the agency. What gets open-sourced is code that cannot run without the data (acdhs_housing_public says so in its README). So the open artefact is unusable by any other jurisdiction by construction, which is a different barrier from "nobody maintained it".
- The open tools that are used in shelter work are not predictive: they are data products (Eviction Lab), lookup tools on public records (Who Owns What) or human-in-the-loop mapping (fAIr).
- For allocation models, the binding barrier documented by the authors themselves is fairness/legitimacy (a fifth of households made worse off in expectation), not engineering.
- Project-specific DSSG repos typically stop receiving commits within about two years of the fellowship; the reusable infrastructure (triage, aequitas) is what survives. This is from five repos, not an audit.

### Gaps
- "CTA homelessness prevention work": I could not identify what this refers to and did not find it. Not found.
- Open Buildings (Google) and Overture Maps for informal settlements, slum-mapping models, xView2/building-damage models, DataKind housing projects: not researched in fetched sources. Background only: Open Buildings is released as data under CC BY 4.0 / ODbL and Overture under CDLA-Permissive 2.0 / ODbL [U]; the google-research/open-buildings repo clone failed.
- JustFix user counts, AEMP tool status, and whether NYC agencies use any eviction-prediction model: not found.
- Whether LA County or Allegheny have published model code anywhere: not found.

---

## Key question 2: quantified evidence that civic tech / "AI for social good" projects fail to reach deployment

### Takeaway
There is no rigorous published survival-rate audit of DSSG fellowship projects or Code for America brigade projects that I could find. The most-quoted number ("72% of AI-for-social-impact projects never leave R&D") is a **misreading**: McKinsey's 2024 report says 72% of about 60 surveyed *experts* believe most efforts focus on research rather than scaling. The solid evidence is qualitative (interviews, case studies) plus one small survey in language documentation (see Key question 4).

### Cited Findings
- McKinsey, "AI for social good: Improving lives and protecting the planet" (10 May 2024): library of about 600 AI use cases for the SDGs (up from about 170 in 2018); "72% of expert survey respondents said most efforts 'have focused on research and innovation rather than adoption and scaling'"; survey of about 60 experts from 17 countries; 55% of foundation grants for AI-for-SDG work are $250,000 or smaller; only 10% of such grants went to organizations headquartered in low- or middle-income countries. The report does **not** give a deployed-vs-R&D share of projects. [V] — [McKinsey](https://www.mckinsey.com/no/our-insights/ai-for-social-good)
- Majumdar, Zhang, Prawal, Yadav (Penn State), "The Hardness of Achieving Impact in AI for Social Impact Research" (2025, AAAI copyright): cites McKinsey (Bankhwal et al. 2024) as finding that "72% of AI4SI projects never make it out of the research and development phase". This restates an opinion-survey figure as a project-outcome figure. [V] — [arXiv 2506.14829](https://arxiv.org/html/2506.14829v1); contradicted by the primary source [McKinsey](https://www.mckinsey.com/no/our-insights/ai-for-social-good)
- Same paper, own data: interviews with 6 senior AI4SI researchers (Mar-Apr 2025) covering 19 projects: 12 deployed, 3 not deployed, 2 pilot/advocacy use, 2 R&D. This is a sample of senior, successful researchers and is not a field estimate. Named barriers: publication incentives ("maintenance is even harder, because you cannot get publications out of it"), partner buy-in, funding ("If funding is not figured out, it may not fail immediately, but it will fail eventually"), data access and data-use agreements, missing engineering skills, partner distrust ("you just come and get a paper, and then you're gone"), partner staff turnover. [V] — [arXiv 2506.14829](https://arxiv.org/html/2506.14829v1)
- Hamm, Shibuya, Cerratto Pargman, Bendor, Raetzsch, Hendawy, Rehak, Klerks, Schouten, Hansen, "What does 'failure' mean in civic tech?" (ACM Interactions, Mar-Apr 2024): "Only a few of the many civic tech prototypes developed around the world last"; no rate given. Discontinuation is framed as "an outcome of misaligned temporalities": research-led projects end after a few years; projects "could not be functionally integrated into governmental structures or receive stable (public) funding". Points to the Civic Tech Graveyard as the field's failure record. [V] — [ACM Interactions](https://interactions.acm.org/archive/view/march-april-2024/what-does-failure-mean-in-civic-tech-we-need-continued-conversations-about-discontinuation)
- Civic Tech Field Guide timeline (data as of 1 Mar 2019): about 2,000 projects with start dates; the authors state they record launch dates not end dates and are "not exploring project longevity". So the largest civic-tech directory did not, at that date, support a survival-rate calculation. [V] — [Civic Tech Field Guide](https://civictech.guide/a-timeline-of-civic-tech-tells-a-data-driven-story-of-the-field)
- Code for America Brigades: open letter of 13 Jul 2016 (Neditch, Pahlka) confirms stipends to brigades were discontinued in 2015 because funding was not sustainable; network had grown from 16 cities (2012) to 80 US cities. [V] — [Code for America](https://codeforamerica.org/news/an-open-letter-to-the-code-for-america-brigades/)
- Shi, Wang, Fang, "Artificial Intelligence for Social Good: A Survey" (arXiv 2001.01818) surfaced in search but was not read. [S] — [arXiv](https://arxiv.org/pdf/2001.01818)
- "'Come to us first': Centering Community Organizations in AI for Social Good Partnerships" (arXiv 2409.06814) surfaced but was not read. [S] — [arXiv](https://arxiv.org/html/2409.06814v1)

### Inferences
- Any report that repeats "72% never leave R&D" should be corrected to "72% of surveyed experts say the field is research-heavy". A defensible project-level failure rate does not exist in the sources I read.
- The recurring mechanism across independent sources is temporal: grants, fellowships and paper cycles last months to two or three years; agency adoption and maintenance need indefinite ownership. The Gessler et al. language-documentation survey (Key question 4) finds the same thing in a different field, which makes it more credible than any one paper.

### Gaps
- Tomašev et al. 2020 (Nature Communications, "AI for social good: unlocking the opportunity for positive impact"): not fetched; I cannot quote it. [U] that it proposes partnership guidelines rather than a deployment rate.
- No audit of DSSG fellowship project survival found (a 2026 dssgfellowship.org post "What makes a good DSSG project" surfaced [S] but was not read: https://dssgfellowship.org/2026/02/26/what-makes-a-good-dssg-project/).
- Code for America's later decision to end the Brigade program (my recollection: announced 2023): [U], not fetched. Brigade project abandonment rates: not found.
- Civic Tech Graveyard current count: not found.

---

## Key question 3 (living wage): which open labor/wage/benefits tools are used by workers, unions or agencies, and which stalled or shut down?

### Takeaway
The pattern differs from housing: the tools with real users are **rules-based or crowdsourced-data tools tied to an organization that operates them** (MyFriendBen with 211 and state partners; FairFare with a Colorado drivers' union), not ML models. The casualties are organizational: Driver's Seat was sunsetted, Gigbox is self-declared unmaintained, and Benefits Data Trust closed in Aug 2024 with the fate of its tools undocumented. Wage-theft ML is still at pilot/"in development" stage eight years after the first Stanford report. The MIT Living Wage Calculator is public to view but not open: no scraping or export, licence required beyond 10 locations.

### Cited Findings

**MIT Living Wage Calculator: OPEN-TO-VIEW, NOT OPEN DATA**
- "Do not scrape, extract, or export the data available on the site." Up to 10 locations may be used off the web with citation; more requires a licensing request to the Living Wage Institute, which now produces the data. Fees: not stated. [V] — [LWC FAQ](https://livingwage.mit.edu/pages/faqs)

**FairFare (Workers' Algorithm Observatory): DEPLOYED with a union**
- Web tool for rideshare drivers to donate trip/pay data so organizers can estimate platform take rates; built by Calacci (Penn State), Rao, Di, Pua, Monroy-Hernández (Princeton), Dalal (CU Boulder), Schwartz, Spitzberg with a Colorado rideshare union; collaboration from June 2023. Main deployment: 45 drivers, 76,625 rides. By Nov 2024: over 500 drivers, more than 800,000 rides. [V] — [arXiv 2502.11273](https://arxiv.org/html/2502.11273v1)
- Partner named as Colorado Independent Drivers United (CIDU); "Today, FairFare has collected data on four million rides from over one thousand accounts" (Dec 2025). Colorado SB24-075 signed 5 Jun 2024 requires per-trip disclosure of rider price and driver pay; in Seattle the pay reports support wrongful-deactivation compensation claims. [V] — [Princeton Engineering, 8 Dec 2025](https://engineering.princeton.edu/news/2025/12/08/new-tool-drives-gig-workers-toward-wage-transparency)
- Caveats from the authors: Uber only (Lyft data via Argyle lacked rider prices); depends on a third-party data broker (Argyle); evaluation rests on interviews with two organizers; influence on the bill's specific provisions "hard to trace". The paper calls FairFare "an open source web-based application" but gives no licence or repo link in the portion read. [V] — [arXiv 2502.11273](https://arxiv.org/html/2502.11273v1)
- WAO's site lists partners CIDU and Drivers Union (Washington) and projects FairFare, FareShare (lost-wage estimates for deactivated drivers) and Handlebar ("coming soon"); no code links on the page. [V] — [WAO](https://wao.cs.princeton.edu/)

**Driver's Seat: DEPLOYED-THEN-ABANDONED**
- WAO's site states Driver's Seat has been sunsetted and that its mission carries forward through FairFare. [V] — [WAO](https://wao.cs.princeton.edu/)
- A Sept 2024 paper describes Driver's Seat as "now under the Worker's Algorithm Observatory". [V] — [arXiv 2409.00737](https://arxiv.org/html/2409.00737v1)
- An App Store listing titled "WAO Driver's Seat" exists. [S] — [App Store](https://apps.apple.com/us/app/drivers-seat/id6478721051)
- Date and stated reason for the cooperative's wind-down: **not found** (searches returned nothing; the Mozilla Foundation article failed to load).

**Gigbox: OPEN-BUT-UNUSED (self-declared unmaintained)**
- dcalacci/gigbox: "open-source tracker for gig workers"; README says the project is "currently unmaintained"; licence MIT with Commons Clause (bars selling it as a product). [V via index] — [ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2Fdcalacci%2Fgigbox)
- Any worker or union deployment of Gigbox: not found.

**Wage-theft detection ML: RESEARCH/PILOT only**
- Stanford CIFE TR229 (Johnson, Peterson, Myers, Silver Taube, Fischer; created Oct 2018, published Feb 2019), "Predicting, Analyzing, and Educating on Wage Theft with Machine Learning Tools": described as pilot work reviewed by a wage-theft investigator; "pilot implementations with partner organizations can proceed"; no named agency, no deployment, no code release mentioned. [V] — [Stanford Digital Repository](https://purl.stanford.edu/mx396wr3611)
- Harvard Impact Labs Strategic Enforcement Lab (start-up funding 2025): co-designing and testing ML models to target enforcement with the New Jersey Department of Labor; building complaint-triage models with Maine DOL; a sick-leave compliance measure with NYC DCWP. Nothing described as released; no results; quasi-experimental field tests planned. [V] — [Harvard Impact Labs](https://impactlabs.harvard.edu/strategic-enforcement-lab)
- UT Austin work on reinforcement learning for day-laborer exploitation surfaced but was not read. [S] — [IC2 Institute](https://ic2.utexas.edu/news/new-research-uses-ai-reinforcement-learning-to-address-exploitation-of-day-workers/)

**Benefits screeners**
- MyFriendBen: DEPLOYED, open, active. Repos MyFriendBen/benefits-api and Gary-Community-Ventures/benefits-api: MPL-2.0, last commit 2026-11-13. [V, cloned] — [repo](https://github.com/MyFriendBen/benefits-api)
- Urban Institute evaluation (25 Aug 2026, Coffey and Chambers; commissioned by the MyFriendBen team): nearly 100,000 screeners started 2023-2025 in Colorado and North Carolina; launched Colorado 2023, expanded to North Carolina and four other states in 2025-26. Only 6% of Colorado users were in non-metro counties. Follow-up survey only 117 of 301. No evaluation of eligibility accuracy reported. [V] — [Urban Institute](https://www.urban.org/research/publication/myfriendben-benefits-screener)
- Kansas/Missouri launch 22 Oct 2026 with United Way of Greater Kansas City 211, funded by the Kauffman Foundation; article repeats Urban figures (64% learned of a new benefit; 86% of follow-up respondents applied; 85% of those approved; these rest on the 117-person follow-up). [V] — [KCTV5](https://www.kctv5.com/2026/10/22/free-tool-unlock-tax-credits-public-benefits-ks-mo/)
- PolicyEngine US: open (AGPL-3.0), very active (last commit 2026-11-16). [V, cloned] — [repo](https://github.com/PolicyEngine/policyengine-us). Described as an open-source microsimulation usable as a Python package, API or web app; the directory page names no agency users. [V] — [Digital Government Hub](https://digitalgovernmenthub.org/ecosystem/directory/policyengine/). That MyFriendBen and other navigators call the PolicyEngine API: [U].
- Amplifi (formerly Imagine LA) Benefit Navigator: SaaS (open-source status not stated), launched Oct 2025; earlier testing with more than 60 agencies; over 500 case managers piloted the chatbot Sept 2023 to Nov 2024. CLOSED-BUT-DEPLOYED by this taxonomy. [V] — [Route Fifty, 6 Nov 2025](https://www.route-fifty.com/digital-government/2025/11/nonprofit-launches-tool-help-agencies-field-medicaid-snap-rule-changes/409368)
- Benefits Data Trust: DEPLOYED-THEN-ABANDONED. Closed 24 Aug 2024 after failing to find an acquirer ("had exhausted all avenues"); about 270 jobs lost. [V] — [Philadelphia Inquirer, 30 Jul 2024](https://www.inquirer.com/health/benefits-data-trust-bdt-failed-acquirer-closing-august-24-20240730.html)
- BDT served more than 120,000 people in 2023; seven states had SNAP signature collaborations left "up in the air" (IL, IA, MN, NV, OK, TN, VT); about 120 former staff alleged "gross financial and organizational mismanagement and negligence" and asked what would happen to "toolkits, projects, initiatives and chatbots, as well as its custom-built benefits screening applications". [V] — [Route Fifty, Jul 2024](https://route-fifty.com/management/2024/07/nonprofits-abrupt-closure-puts-access-public-benefits-risk/397968)
- Whether any BDT software was open-sourced or handed over: **not found**.

**Open skills / job-matching models: used in research; worker- or agency-facing deployment not found**
- kris927b/SkillSpan (skill-extraction dataset and code): MIT, last commit 2025-02-13. [V, cloned] — [repo](https://github.com/kris927b/SkillSpan)
- JobBERT, ESCOXLM-R: repo/licence could not be verified (clone of the guessed JobBERT path failed). Licence and deployment: not found. That these are academic models evaluated on benchmarks with no documented public-employment-service deployment: [U].
- O*NET (US DOL, CC BY 4.0), ESCO (European Commission, free reuse), Lightcast Open Skills (free tier under Lightcast terms): [U], not fetched. These taxonomies are infrastructure widely embedded in other products rather than "unused".
- DOL Wage and Hour Division enforcement data is public for download (enforcedata.dol.gov): [U], not fetched.
- Fairwork (platform ratings, Oxford) and Turkopticon (worker-run requester reviews for Mechanical Turk): [U] both believed active; not researched.
- Open labor-market agent-based models: not researched; not found.

### Inferences
- In labor, the survival variable is the operator, not the licence. FairFare has a union that needs the output for bargaining and legislation; MyFriendBen has a funded nonprofit plus 211 partners; Gigbox and Driver's Seat were open or semi-open but had no durable operator, and went quiet.
- BDT is the cautionary case for "deployed but not open": when the organization failed, staff themselves did not know what would happen to the screening applications. Open-source release would have at least left the artefacts recoverable. This is an inference; no source says BDT's code was lost.
- Gig-pay tools share a structural dependency on getting data out of the platforms (Argyle scraping, screenshots). The FairFare authors flag this as the main fragility.
- Benefits screeners being used is not the same as benefits being received: the Urban evaluation has no accuracy audit and a 39% follow-up rate.

### Gaps
- Reason and date for Driver's Seat Cooperative's closure; FairFare's licence and repo URL; current status of the Shipt pay calculator.
- Any deployed open job-matching model at a public employment service; any open wage-theft model with code.
- Fairwork, Turkopticon, WeClock status in 2026.

---

## Key question 4 (languages): which open models, corpora and documentation tools are actually used by language communities or documentary linguists?

### Takeaway
This is the best-evidenced "published but unused" domain. A 2025 ACL survey found 29 of 30 documentary linguists knew of relevant NLP systems but only 11 had used one, and 4 of those 11 reported a net productivity loss; 7 of 8 NLP researchers whose system was used said it could not have run without them personally. The dedicated documentation ASR tools are stale (Persephone: last commit 2020, README "not actively maintained"; Elpis: last commit June 2024), while the big multilingual models linguists now fine-tune (MMS, NLLB) are **non-commercial** and, for NLLB, explicitly "not released for production deployment". Separately, some communities (Te Hiku Media) have deliberately refused open release.

### Cited Findings

**Uptake studies**
- Gessler, Palmer, von der Wense, "Understanding the Gap: an Analysis of Research Collaborations in NLP and Language Documentation" (Findings of ACL 2025): "tools are rarely used in practice" despite two decades of NLP-for-documentation work. [V] — [ACL Anthology](https://preview.aclanthology.org/setup/2025.findings-acl.48)
- Survey numbers (49 respondents: 30 documentary linguists, 19 NLP researchers; 17 interviews): 29/30 linguists aware of NLP systems that could help; **11/30 (37%) had used one**; 6/30 had done so with an NLP collaborator. Of the 11 users: 3 said expectations were met; 6 reported real labor savings (4 of those had an NLP researcher's help); **4 reported a net productivity loss**; 8 found workflow integration somewhat or very difficult. [V] — [paper PDF](https://preview.aclanthology.org/evt-to-venues/2025.findings-acl.48.pdf)
- Reasons among the 19 non-users: 13 (68%) "unsure of how to set them up and integrate them into their workflows"; 6 lacked hardware; 6 doubted it was worth the effort; in free responses 4 of 10 doubted they had enough data. [V] — [same PDF](https://preview.aclanthology.org/evt-to-venues/2025.findings-acl.48.pdf)
- NLP-researcher side: 9/19 had a system applied in a documentation setting; of 8 deployed systems, **7 were operated personally by the researcher, and all 7 said it could not have been deployed without them**; 6 of 8 needed manual data transfer. 9/19 rated past impact "limited". [V] — [same PDF](https://preview.aclanthology.org/evt-to-venues/2025.findings-acl.48.pdf)
- Software and incentives: ELAN and FLEx "were by far the most commonly used apps"; interviewee: "I need FLEx to not suck"; "NLP researchers are incentivized to work on many projects" that end after publication, whereas documentation "spans years and even careers". Authors caution the sample is small. [V] — [same PDF](https://preview.aclanthology.org/evt-to-venues/2025.findings-acl.48.pdf)
- Gessler and von der Wense (AmericasNLP 2024): of 93 computer-science departments surveyed, none offered a language-documentation course; of 56 linguistics departments, 10 offered both NLP and documentation courses (9 in the US); in a Semantic Scholar sample as few as 13% of NLP-for-documentation papers had interdisciplinary author teams. [V] — [ACL Anthology](https://aclanthology.org/2024.americasnlp-1.1.pdf)
- Liang and Levow (Field Matters 2025): ASR "use in linguistic fieldwork remains limited"; benchmarks MMS vs XLS-R on five languages (MMS better with very little data; comparable above one hour). [V] — [ACL Anthology](https://aclanthology.org/2025.fieldmatters-1.3)
- Billings and McDonnell (ComputEL 2025): identify two beliefs that keep documentary linguists from ASR (not enough data; correcting is slower than transcribing). With 25 hours of Nasal (Indonesia) speech, a fine-tuned model at 44% WER still "can significantly speed up the transcription process" in timed tests. [V] — [ACL Anthology](https://aclanthology.org/2025.computel-main.14)
- Le Ferrand, Jiang, Hartshorne, Prud'hommeaux (ACL 2025 short) say ASR is "increasingly common" in field workflows (asserted, no data), and that inconsistent field transcriptions harm ASR training. This partly cuts against the "unused" framing. [V] — [ACL Anthology](https://aclanthology.org/2025.acl-short.49)
- Bird, "Decolonising Speech and Language Technology" (COLING 2020): "Indigenous people often respond negatively to the idea that their languages are data ready for the taking"; treating languages as data risks "reenacting the causes of language endangerment". Abstract only. [V] — [ACL Anthology](https://aclanthology.org/2020.coling-main.313)

**Documentation ASR tools**
- Persephone (phoneme transcription): Apache-2.0; last commit on default branch 2020-11-04 [V, cloned]; an index reports last push 18 Apr 2023 and a README stating the project is "not actively maintained", v0.4.2 beta, 157 stars. Status: OPEN-BUT-UNSUPPORTED. — [repo](https://github.com/persephone-tools/persephone), [ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2Fpersephone-tools%2Fpersephone)
- Elpis (CoEDL): Apache-2.0, 163 stars, no archive banner visible, last commit 2024-06-03 (about 29 months before this note). [V] — [repo](https://www.github.com/CoEDL/elpis)
- Mahmudi, Dang, Vylomova, Thieberger (Univ. of Melbourne; arXiv 2608.11629, 2026): "Elpis requires local GPU infrastructure and lacks support for fine-tuning modern language models"; fine-tuning "requires technical expertise, specialised corpus formatting, and GPU management that fall outside the typical linguist's toolkit". They propose Easper, a no-code cloud workflow from ELAN annotations, tested on three Vanuatu languages. Easper's own uptake: none reported (new). [V] — [arXiv](https://arxiv.org/pdf/2608.11629)

**Large multilingual models and their licences**
- Meta MMS: "License: CC-BY-NC 4.0 license". [V] — [HF model card](https://huggingface.co/facebook/mms-300m/blob/main/README.md)
- Meta NLLB-200: CC-BY-NC-4.0; "NLLB-200 is a research model and is not released for production deployment"; not intended for medical/legal text or document translation; translations "can not be used as certified translations". [V] — [HF model card](https://huggingface.co/facebook/nllb-200-distilled-600M/blob/main/README.md)
- fairseq (the code both ship in): MIT, last commit 2025-09-30, i.e. more than a year without commits. [V, cloned] — [repo](https://github.com/facebookresearch/fairseq)
- OpenAI Whisper: MIT, last commit 2026-08-31. [V, cloned] — [repo](https://github.com/openai/whisper). Whisper's training data included 1,381 hours of Māori audio, per Thomson Reuters Foundation (6 Apr 2023). [V] — [Eco-Business reprint](https://www.eco-business.com/id/news/indigenous-groups-in-nz-us-fear-colonisation-as-ai-learns-their-languages/)
- AI4Bharat IndicTrans2: MIT, last commit 2025-10-03. [V, cloned] — [repo](https://github.com/AI4Bharat/IndicTrans2). Deployment (e.g. in Indian government translation services): [U], not fetched.

**Community corpora and platforms**
- Mozilla Common Voice: platform repo MPL-2.0, last commit 2026-11-16 [V, cloned] — [repo](https://github.com/common-voice/common-voice). Scripted Speech 24.0 released 17 Dec 2025: 289 languages, 38,932 hours (25,886 validated); now distributed through the Mozilla Data Collective. [V] — [Mozilla Discourse](https://discourse.mozilla.org/t/release-live-mcv-scripted-speech-24-0-and-spontaneous-speech-2-0/146740)
- Common Voice remains CC0 and "continues unchanged", but Mozilla launched the Data Collective for communities who want "different terms than full openness" (own licences, optional charging). The same release shows the split: the standard Dholuo set is CC0 while the separate DhoNam Dholuo set is under the NOODL licence. [V] — [OSI webinar page, 7 Oct 2025](https://opensource.org/ai/webinars/beyond-extraction-building-community-centered-speech-data), [Mozilla Discourse](https://discourse.mozilla.org/t/release-live-mcv-scripted-speech-24-0-and-spontaneous-speech-2-0/146740)
- Masakhane: masakhane-io/masakhane-mt MIT, last commit 2022-06-14; masakhane-io/masakhane-ner last commit 2025-10-15. [V, cloned] — [masakhane-mt](https://github.com/masakhane-io/masakhane-mt). A Sept 2026 workshop abstract by Masakhane African Languages Hub authors (Gwadabe, Taban) frames "moving from technological capability to real-world outcomes" as still to be demonstrated and gives no deployment figures. [V] — [STIAS workshop abstract](https://fmadore.github.io/stias-dh-ai-workshop-2026/papers/masakhane-4d-framework)
- AmericasNLP 2021 shared-task repo: last commit 2022-07-05, no licence file at repo root. [V, cloned] — [repo](https://github.com/AmericasNLP/americasnlp2021)
- Glottolog: CC BY 4.0, last commit 2026-11-12 (actively maintained reference catalogue). [V, cloned] — [repo](https://github.com/glottolog/glottolog)
- FirstVoices (First Peoples' Cultural Council / Foundation, British Columbia): described as open source and free for B.C. communities; "Communities own their data" and the language team controls access; keyboards for "100+ First Nations languages". Number of language sites: not stated on the page. DEPLOYED, community-controlled. [V] — [FPCC](https://fpcc.ca/firstvoices/)
- Mozilla DeepSpeech: MPL-2.0, last commit 2025-06-19; Coqui STT (its successor fork): MPL-2.0, last commit 2023-03-28. [V, cloned] — [DeepSpeech](https://github.com/mozilla/DeepSpeech), [Coqui STT](https://github.com/coqui-ai/STT). That DeepSpeech is archived, that Coqui the company closed in early 2024, and that Te Hiku's first Māori ASR was built on DeepSpeech: [U].

**Deliberate non-open release (data sovereignty)**
- The Kaitiakitanga licence was originally written by Te Hiku Media: "Data may be freely used and distributed with the licence attached but may not be sold or used for commercial purposes"; guardianship stays with the whānau/hapū/iwi; "a living licence". The publishing page argues that open-sourcing or Creative Commons licensing would "further allow ourselves to be colonised digitally". [V] — [Taiuru, Māori Data Sovereignty Licences](https://www.taiuru.maori.nz/maori-data-sovereignty-licences/)
- Te Hiku CEO Peter-Lucas Jones called it "concerning" that a non-Māori organisation released a Māori speech model; Te Hiku has built its own Māori ASR, has turned down several companies seeking to commercialise its data, and is in talks to share its technology with other Indigenous communities. [V] — [Thomson Reuters Foundation via Eco-Business, 6 Apr 2023](https://www.eco-business.com/id/news/indigenous-groups-in-nz-us-fear-colonisation-as-ai-learns-their-languages/)
- TeHikuMedia/corpora repo: clone failed (path guessed); not found.

### Inferences
- Three distinct "open but unused" mechanisms appear in language technology, and they should not be merged:
  1. **Abandoned bespoke tools** (Persephone, arguably Elpis): built for linguists by short-funded research teams, overtaken by pretrained models, no maintainer.
  2. **Usable-in-principle foundation models that the intended users cannot operate** (MMS, XLS-R, Whisper fine-tuning): the barrier is setup, hardware and workflow integration with ELAN/FLEx (68% of non-users), and the "researcher must run it personally" finding (7 of 8).
  3. **Licence-blocked for the community's own purposes**: MMS and NLLB are CC-BY-NC and NLLB disclaims production use, so a community organization or small business wanting to ship a product cannot rely on them without legal risk.
- Te Hiku is the inverse case: closed by choice and in use by its community. "Not open" is not a failure category here; counting it as one would repeat the framing Bird criticizes.
- Common Voice's 2025 move to add a non-CC0 channel is evidence that full openness itself was a participation barrier for some communities.
- Evidence conflict worth carrying forward: Liang and Levow say fieldwork ASR use "remains limited"; Le Ferrand et al. say it is "increasingly common". Only Gessler et al. measure it (37% of 30 linguists had ever used any NLP system), and that sample is small and self-selected.

### Gaps
- Not researched in fetched sources (background only, [U]): FLORES-200 (CC BY-SA 4.0), Aya dataset (Apache 2.0), Universal Dependencies (per-treebank licences, many CC BY-SA or non-commercial), Ethnologue (subscription), Endangered Languages Project, ELAR, PARADISEC and AILLA (archives with tiered, often restricted access set by depositors and communities), Living Tongues talking dictionaries, Wav2Vec2 fine-tunes on Hugging Face. No download or usage statistics were obtained for any of these.
- No count of how many community-language Wav2Vec2/Whisper fine-tunes on Hugging Face have any downloads or users. This would be a tractable original measurement.
- Hugging Face download counts for MMS/NLLB (a research-use proxy): the pages that carry them were blocked.
- Liu et al. (the user mentioned this; I could not identify which paper) and specific ComputEL papers on non-adoption beyond Billings and McDonnell: not found.
- Number of FirstVoices language sites; current Te Hiku model performance and licensing of their models.

---

## Inventory table

Abbreviations: V = verified in fetched page or cloned repo (2026-11-16); S = search-result title only; U = unverified background. "Last commit" is the default branch. Archived flags could not be read for any repo.

| Tool | Problem | Type | Released (code/weights/data) | License | Deployment evidence | Maintenance status | Barrier if unused | Source URL | Verification status |
|---|---|---|---|---|---|---|---|---|---|
| LA County Homelessness Prevention Unit model (California Policy Lab) | shelter | Predictive risk model | None found | n/a | LA County DHS + CIO; 1,498 served; RCT due 2027 | Active program (report Jul 2025) | Not unused; closed (restricted linked county data) | https://capolicylab.org/news/new-report-early-signs-of-success-from-la-countys-homelessness-prevention-pilot/ | V (release status: not found) |
| Allegheny Housing Assessment (AHA) | shelter | Predictive prioritization (VI-SPDAT replacement) | None found; public methodology report only | n/a | Allegheny County DHS, in intake since Aug 2020 | Active; audited 2024 | Not unused; closed. Audit: disparities in service rates persisted | https://ar5iv.labs.arxiv.org/html/2407.21209 | V |
| dssg/acdhs_housing_public (CMU + Allegheny rental assistance) | shelter | Predictive prioritization | Code open; data closed | MIT | Shadow mode Sep 2022 to Aug 2023; "piloting" per Mar 2025 article; RCT planned | 12 commits; date not readable | Restricted microdata; needs RCT; low recall for first-time homelessness | https://arxiv.org/pdf/2403.12599 | V |
| Kube, Das, Fowler allocation model | shelter | Counterfactual allocation optimizer | Counterfactual predictions on GitHub; data closed | not stated | None; "proof of concept" | Paper 2023; repo status not checked | Fairness: about 21% of households made worse off; restricted HMIS data | https://par.nsf.gov/servlets/purl/10415667 | V |
| Fowler/Das eviction-outreach model (J-PAL PAIE) | shelter | Eviction prediction for outreach | None found | n/a | Pilot with unnamed housing advocates (Spring 2025 RFP) | Pilot | Too early | https://www.povertyactionlab.org/initiative-project/evaluating-ai-enabled-eviction-prevention-low-income-tenants | V |
| Bronx eviction-filing forecast (Rodriguez et al.) | shelter | Time-series forecast on open data | Release not confirmed | not found | None; proof of concept | Paper Dec 2025 | Academic prototype; over-predicted 2.6 to 3.3x; an input dataset ended 2020 | https://www.themoonlight.io/review/open-source-software-and-data-for-human-service-development-a-case-study-on-predicting-housing-instability | V (secondary summary only) |
| JustFix Who Owns What | shelter | Landlord-portfolio lookup on public records | Code open | GPL-3.0 | NYC tenants/organizers (numbers not found) | Active; last commit 2026-09-24 | n/a (used) | https://github.com/JustFixNYC/who-owns-what | V (repo); S (usage) |
| Eviction Lab Eviction Tracking System v4.0 | shelter | Dataset | Data open (CSV) | none stated; citation requested | Widely used data source; 43 cities, 11+ states | Active; updated Oct 2026 | n/a | https://evictionlab.org/eviction-tracking/get-the-data/ | V |
| EvictionLab/eviction-lab-etl | shelter | Data pipeline code | Code open | MIT | Internal to Eviction Lab's 2018 map | Dormant; last commit 2019-11-03 | Superseded | https://github.com/EvictionLab/eviction-lab-etl | V |
| AEMP covid-19-map | shelter | Advocacy map | Code open | MIT | Used during COVID moratoria (not verified) | Dormant; last commit 2021-01-18 | Event-bound project ended | https://github.com/antievictionmappingproject/covid-19-map | V (repo) |
| HOT fAIr | shelter (informal settlements, mapping) | AI-assisted building mapping | Code open | AGPL-3.0 | HOT/OSM mappers; user test n=26 | Active; last commit 2026-11-15 | Slower and less accurate than JOSM in test; not preferred tool | https://pretalx.com/sotm2025-osm-science/talk/WJDTBX | V |
| Ramp (ramp-code) | shelter (building footprints) | Segmentation model + training code | Code, baseline model, data open | Apache-2.0 (code) | Not found directly (fAIr reuse is U) | Dormant; last commit 2022-09-15 | Funding/project ended (inferred); no maintainer | https://github.com/devglobalpartners/ramp-code | V (repo); U (reuse) |
| Google Open Buildings | shelter | Dataset | Data open | CC BY 4.0 / ODbL (U) | not found | not found | not researched | https://sites.research.google/open-buildings/ | U |
| dssg/johnson-county-ddj-public | shelter-adjacent (jail/mental health diversion) | Predictive model code | Code public | Custom "terms of use", not OSI | not found | Dormant; last commit 2017-05-05 | Fellowship project; custom licence; restricted data | https://github.com/dssg/johnson-county-ddj-public | V |
| dssg/cincinnati2015-public | shelter (blight inspections) | Predictive model code | Code open | MIT | not found | Dormant; last commit 2017-04-20 | Fellowship prototype | https://github.com/dssg/cincinnati2015-public | V |
| dssg/triage, dssg/aequitas | cross-cutting | ML pipeline / bias-audit toolkits | Code open | MIT | Used in DSSG/CMU projects (e.g. Allegheny) | Active; 2026-10-28 / 2026-05-12 | n/a | https://github.com/dssg/triage | V |
| MIT Living Wage Calculator | wage | Reference data | Viewable; no bulk export | Proprietary; licence needed beyond 10 locations | Widely cited (not measured here) | Active (Living Wage Institute) | No scraping/export; licensing | https://livingwage.mit.edu/pages/faqs | V |
| FairFare (WAO) | wage | Crowdsourced pay-data tool | Described as open source; repo not found | not found | CIDU (Colorado); Drivers Union (WA); 4M rides, 1,000+ accounts | Active (Dec 2025) | n/a; fragile dependence on Argyle and platform data | https://engineering.princeton.edu/news/2025/12/08/new-tool-drives-gig-workers-toward-wage-transparency | V |
| Driver's Seat (Cooperative, later WAO) | wage | Gig-driver data app | not found | not found | Was used by drivers; moved under WAO by Sep 2024 | Sunsetted | Reason/date not found | https://wao.cs.princeton.edu/ | V (sunset); not found (why) |
| Gigbox | wage | Gig-worker tracker | Code open | MIT + Commons Clause | None found | README: "currently unmaintained" | Academic prototype; no maintainer | https://awesome.ecosyste.ms/projects/github.com%2Fdcalacci%2Fgigbox | V (via index) |
| Stanford TR229 wage-theft ML | wage | Predictive/analytic prototype | No code mentioned | n/a | None; pilot reviewed by one investigator | Report 2018-19 | Academic prototype; pilots "can proceed" | https://purl.stanford.edu/mx396wr3611 | V |
| Harvard Strategic Enforcement Lab models | wage | Enforcement-targeting ML | None yet | n/a | In development with NJ DOL, Maine DOL, NYC DCWP | Active (funded 2025) | Too early; nothing released | https://impactlabs.harvard.edu/strategic-enforcement-lab | V |
| MyFriendBen | wage (benefits access) | Rules-based benefits screener | Code open | MPL-2.0 | CO, NC + 4 states; KS/MO with United Way 211 (Oct 2026); about 100k screeners | Active; last commit 2026-11-13 | n/a; no accuracy audit; rural reach 6% | https://www.urban.org/research/publication/myfriendben-benefits-screener | V |
| PolicyEngine US | wage (benefits/tax) | Microsimulation / rules engine | Code open | AGPL-3.0 | Named agency users not found | Very active; last commit 2026-11-16 | n/a | https://github.com/PolicyEngine/policyengine-us | V (repo); users not found |
| Amplifi Benefit Navigator | wage (benefits access) | SaaS screener + chatbot | Not stated | not stated | 60+ agencies tested; 500+ case managers piloted | Active (launched Oct 2025) | Closed | https://www.route-fifty.com/digital-government/2025/11/nonprofit-launches-tool-help-agencies-field-medicaid-snap-rule-changes/409368 | V |
| Benefits Data Trust tools | wage (benefits access) | Screeners, outreach, chatbots | not found | not found | 120k+ served in 2023; 7 state SNAP collaborations | Organization closed 24 Aug 2024 | Organizational/financial collapse; fate of tools unknown | https://www.inquirer.com/health/benefits-data-trust-bdt-failed-acquirer-closing-august-24-20240730.html | V |
| SkillSpan | wage (skills/job matching) | Dataset + extraction code | Code + data open | MIT | Research only (none found) | Last commit 2025-02-13 | Academic benchmark | https://github.com/kris927b/SkillSpan | V (repo) |
| JobBERT / ESCOXLM-R | wage (job matching) | Language models | Weights believed public | not found | not found | not found | not found | not found | U |
| O*NET / ESCO / Lightcast Open Skills | wage | Taxonomies | Data open | CC BY 4.0 / EU reuse / Lightcast terms | Embedded widely | Active | n/a | https://www.onetcenter.org/ | U |
| Persephone | language | Phoneme ASR for documentation | Code open | Apache-2.0 | Na and Chatino research projects (U); no current use found | Unsupported; README "not actively maintained"; last commit 2020-11-04 | No maintainer; overtaken by pretrained models | https://awesome.ecosyste.ms/projects/github.com%2Fpersephone-tools%2Fpersephone | V |
| Elpis (CoEDL) | language | ASR pipeline for documentation | Code open | Apache-2.0 | not found | Stale; last commit 2024-06-03 | Needs local GPU; no modern fine-tuning (per 2026 paper) | https://arxiv.org/pdf/2608.11629 | V |
| Easper | language | No-code ASR fine-tuning from ELAN | Described as open source | not found | 3 Vanuatu languages (authors' tests) | New (2026) | Too early | https://arxiv.org/pdf/2608.11629 | V |
| Meta MMS | language | Multilingual speech models (1,100+ languages) | Weights + code open | CC-BY-NC 4.0 | Research fine-tuning (e.g. Liang and Levow) | fairseq last commit 2025-09-30 | Non-commercial licence; expertise/hardware | https://huggingface.co/facebook/mms-300m/blob/main/README.md | V |
| Meta NLLB-200 | language | MT model (200 languages) | Weights open | CC-BY-NC 4.0 | "not released for production deployment" | Same repo, stale | Non-commercial; research-only by its own card | https://huggingface.co/facebook/nllb-200-distilled-600M/blob/main/README.md | V |
| OpenAI Whisper | language | Multilingual ASR | Weights + code open | MIT | Fine-tuned by linguists (Easper); objected to by Te Hiku | Active; last commit 2026-08-31 | Community objection to training data (1,381 h Māori); expertise | https://www.eco-business.com/id/news/indigenous-groups-in-nz-us-fear-colonisation-as-ai-learns-their-languages/ | V |
| Mozilla Common Voice | language | Crowdsourced speech corpus | Data + platform open | CC0 (data), MPL-2.0 (code) | 289 languages, 38,932 h (v24, Dec 2025) | Active | n/a; some communities want non-CC0 terms (Data Collective, NOODL) | https://discourse.mozilla.org/t/release-live-mcv-scripted-speech-24-0-and-spontaneous-speech-2-0/146740 | V |
| Masakhane MT / NER | language | Community MT and NER datasets/models | Code + data open | MIT (masakhane-mt) | Research; real-world outcomes "to be demonstrated" per Hub abstract | masakhane-mt dormant (2022-06-14); NER 2025-10-15 | Research-to-deployment gap acknowledged | https://fmadore.github.io/stias-dh-ai-workshop-2026/papers/masakhane-4d-framework | V |
| AmericasNLP 2021 data | language | Shared-task MT data (Indigenous languages of the Americas) | Data + baselines public | no licence file at root | Research only | Dormant; last commit 2022-07-05 | Shared-task artefact; unclear licence | https://github.com/AmericasNLP/americasnlp2021 | V (repo) |
| AI4Bharat IndicTrans2 | language | MT for 22 Indian languages | Code + weights open | MIT | not verified | Last commit 2025-10-03 | not found | https://github.com/AI4Bharat/IndicTrans2 | V (repo); U (use) |
| Glottolog | language | Language catalogue | Data open | CC BY 4.0 | Standard reference | Active; last commit 2026-11-12 | n/a | https://github.com/glottolog/glottolog | V |
| FirstVoices | language | Community language-archive platform | Code open (per FPCC) | not found | B.C. First Nations communities; 100+ languages (keyboards) | Active (page updated Sep 2025) | n/a; community-controlled data | https://fpcc.ca/firstvoices/ | V |
| Te Hiku Media Māori ASR + Kaitiakitanga licence | language | ASR + data licence | Deliberately not open | Kaitiakitanga licence (no commercial use; guardianship retained) | Te Hiku Media's own use; sharing talks with other Indigenous groups | Active (as of 2023 source) | Not unused: deliberate non-open choice | https://www.taiuru.maori.nz/maori-data-sovereignty-licences/ | V |
| Mozilla DeepSpeech / Coqui STT | language | Open ASR engines | Code + weights open | MPL-2.0 | Past use by Te Hiku (U) | Dormant: last commits 2025-06-19 / 2023-03-28 | Sponsor withdrew (U) | https://github.com/coqui-ai/STT | V (repo dates); U (history) |
| FLORES-200, Aya, Universal Dependencies, ELAR, PARADISEC, AILLA, Ethnologue, Living Tongues | language | Benchmarks / archives | Mixed | Mixed (see Gaps) | not researched | not researched | not researched | not found | U |

---

## Open datasets a student could download and study

Only the first group was confirmed in this session. Check each licence page before redistribution.

Confirmed (V):
- **Eviction Lab Eviction Tracking System v4.0**: weekly and monthly eviction filings by tract/ZIP for 43 cities and 11+ states, CSV. No formal licence stated; citation requested. https://evictionlab.org/eviction-tracking/get-the-data/
- **Mozilla Common Voice Scripted Speech 24.0**: 289 languages, 38,932 hours; CC0 for the standard sets (per-dataset exceptions such as NOODL exist). Via Mozilla Data Collective. https://discourse.mozilla.org/t/release-live-mcv-scripted-speech-24-0-and-spontaneous-speech-2-0/146740
- **Glottolog**: catalogue of the world's languages, families and references; CC BY 4.0. https://github.com/glottolog/glottolog
- **SkillSpan**: annotated skill spans in job postings; MIT. https://github.com/kris927b/SkillSpan
- **Kube/Das/Fowler counterfactual predictions**: predicted re-entry probabilities under each service for 13,940 households (the linked paper gives the GitHub location); no licence stated. https://par.nsf.gov/servlets/purl/10415667
- **Ramp training data**: building-footprint labels and imagery chips on Source Cooperative (existence seen in search only; licence not read). https://source.coop/ramp
- **AmericasNLP 2021**: parallel text for Indigenous languages of the Americas; no licence file at repo root, so treat as research-use and check per-language terms. https://github.com/AmericasNLP/americasnlp2021
- **Repositories themselves as data**: the cloned DSSG, Persephone, Elpis and Ramp repos give commit histories that could be mined for a survival analysis, which is the audit this research could not find.

Unverified leads (U; confirm licence at the source):
- US DOL Wage and Hour Division enforcement data (public domain, enforcedata.dol.gov)
- O*NET database (CC BY 4.0) and ESCO (European Commission)
- Google Open Buildings (CC BY 4.0 / ODbL) and Overture Maps buildings (ODbL / CDLA-Permissive 2.0)
- FLORES-200 (CC BY-SA 4.0), Aya dataset (Apache 2.0), Universal Dependencies (per-treebank)
- NYC Housing Data Coalition "nycdb" (open NYC housing records used by Who Owns What)
- MMS and NLLB weights are downloadable for study under CC-BY-NC 4.0 (V for licence), which is fine for coursework but not for a product.

Not downloadable in bulk: MIT Living Wage Calculator (scraping and export prohibited; licence needed beyond 10 locations) [V].

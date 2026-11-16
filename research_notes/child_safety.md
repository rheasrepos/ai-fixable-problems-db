# Open-source / openly published AI tools for child online safety, and whether they are used (state as of 16 Nov 2026)

Verification labels used throughout:
- **[V]** = verified in a page I fetched this session (the fetch returns a model-generated reading of the page, so exact quotations should be re-checked before being printed as verbatim quotes).
- **[S]** = seen only in a search-result title/snippet, page not fetched.
- **[U]** = UNVERIFIED background knowledge (from training data, not checked this session). Treat as leads, not facts.

Access note: github.com was not fetchable in this session (allowlist block), so NO GitHub star counts, last-commit dates or "archived" flags were checked directly. Where repo status is stated, it comes from project documentation pages, not from the repo UI. This is the single largest gap in these notes.

No abusive content, file-name examples, keyword lists or evasion techniques are reproduced anywhere below; only tool metadata.

---

## Q1. Which genuinely open-source tools exist, and what exactly was released?

### Takeaway
The genuinely open (code under a permissive licence) layer in this field is almost entirely *infrastructure for known-content matching and moderation workflow* (Meta's PDQ/TMK+PDQF/vPDQ/HMA under BSD; ROOST's Osprey under Apache-2.0 and Coop) plus *text grooming-detection research artefacts* built on PAN12. The detection models for novel CSAM (Thorn, Google, Microsoft PhotoDNA, the León/4NSEEK classifiers, Microsoft's metadata classifier, iCOP, DeepPatrol) are published as papers or services but not as open code/weights, because the positive-class training data is illegal to hold or share.

### Cited Findings

**Open code, permissive licence**
- [V] Meta's ThreatExchange repository contains PDQ (image hashing), TMK+PDQF (video hashing), vPDQ (video hashing), Hasher-Matcher-Actioner (HMA) and python-threatexchange (on PyPI as `threatexchange`); repository-wide licence is BSD, with one file exception (pdq/cpp/CImg.h). — [ThreatExchange README mirror](https://cdn.jsdelivr.net/gh/facebook/ThreatExchange@main/README.md)
- [V] HMA 1.0 was AWS-only; it was archived in March 2024 and replaced by a full rewrite, HMA 2.0 / "Open Media Match", BSD-licensed, API-only, no GUI, runs as a Docker image. — [HMA history page](https://facebook.github.io/ThreatExchange/hma/history.html)
- [S] PDQ and TMK+PDQF were open-sourced by Facebook in August 2019 (headline dated 2 Aug 2019). — [Engadget](https://www.engadget.com/2019/08/02/facebook-open-source-harmful-content-algorithm/)
- [S] HMA was announced by Meta as an open-source tool in December 2022 (headline). — [Engadget](https://www.engadget.com/meta-open-source-tool-scan-terrorist-content-130952284.html)
- [V] ROOST Osprey v1.0 was announced 28 Jan 2026 under Apache 2.0; it is a rules engine and investigation tool originally built by Discord and now maintained through ROOST. — [ROOST Osprey v1.0](https://roost.tools/blog/introducing-osprey-v1-0-open-source-infrastructure-for-real-time-abuse-mitigation/)
- [V] ROOST Coop 1.0 was announced 9 June 2026 as free, open-source, self-hostable (source and Docker images) review/enforcement tooling that files reports directly to NCMEC and "integrates with leading child safety detection tools out of the box"; the announcement does not name the licence or the specific detection integrations. — [ROOST Coop 1.0](https://roost.tools/blog/coop-1-0-world-s-first-free-open-source-child-safety-infrastructure-for-every-platform/)
- [V] ROOST's 2025 review lists: Osprey (donated by Discord), Coop (acquired from Cove; extended to NCMEC-compliant CSAM reporting), gpt-oss-safeguard (open-weight bring-your-own-policy reasoning model released with OpenAI), the ROOST Model Community, and the `awesome-safety-tools` directory. — [ROOST in review 2025](https://roost.tools/blog/roost-in-review-a-look-back-on-2025/)

**Open research artefacts for grooming detection (text)**
- [V] PAN12 Sexual Predator Identification corpus (Inches & Crestani) is on Zenodo with access type "Open", a 91.2 MB zip, DOI 10.5281/zenodo.3713280; the record shows no explicit licence. — [Zenodo record](https://zenodo.org/record/3713280)
- [V] Vogt et al. (ACL 2021, "Early Detection of Sexual Predators in Chats") released on GitLab: training/eval code, preprocessing code that builds the PANC dataset from PAN12 + ChatCoder2, a chat visualiser, an Android demo (BERT-base and MobileBERT on device), and trained models via a Mega folder. No licence stated. The page states the trained models are "not ready for real-world use". — [Supplementary material site](https://early-sexual-predator-detection.gitlab.io)
- [V] `chatcompanion/compAnIonv1` on Hugging Face: MIT-licensed ~110M-parameter grooming classifier for gaming chat, a UC Berkeley MIDS capstone, trained on PAN12 and PJZC (1,104 Perverted-Justice conversations) plus IRC/Omegle/Chit-Chats negatives; README last touched "over 2 years ago", 1 like, described as "not to be considered a source of truth". — [HF model card](https://huggingface.co/chatcompanion/compAnIonv1/blob/main/README.md)

**Open data release in the AI-training-data hygiene niche**
- [V] Re-LAION-5B was released 30 Aug 2024 (Apache-2.0 metadata, gated on Hugging Face with affiliation + consent) in two variants (research; research-safe). 2,236 links matching partner hash lists were removed (upper bound; includes the 1,008 from the Stanford report). Partners: IWF, Canadian Centre for Child Protection (C3P), Stanford Internet Observatory, plus Human Rights Watch link reports. LAION-5B had been taken down on 19 Dec 2023. — [LAION blog](https://laion.ai/blog/relaion-5b/)

**Published but closed (contrast set)**
- [V] Thorn Safer Predict (launched 22 Jul 2024): image/video CSAM classifier trained partly on NCMEC CyberTipline data, and text CSE classifiers; the press release makes no open-source claim and names only X as a beta tester of the text model. — [Thorn press release](https://www.thorn.org/press-releases/thorn-launches-safer-predict-a-proactive-ai-detection-solution-to-scale-child-safety-on-content-hosting-platforms/)
- [V] Pereira, Dodhia, Anderson, Brown, "Metadata-Based Detection of Child Sexual Abuse Material" (arXiv 2010.02387): CNN on file paths, reported accuracy 0.97; the arXiv abstract page mentions no code, model or data release. — [arXiv](https://arxiv.org/abs/2010.02387)
- [V] Al-Nabki et al. (arXiv 2011.01113; the Scientific Reports 2023 paper is the journal version [U]): no code/model/data link; positive-class data was supplied by Spanish law enforcement via INCIBE; negative class from NIST's NSRL; funded under 4NSEEK. — [ar5iv full text](https://ar5iv.labs.arxiv.org/html/2011.01113)
- [V] 4NSEEK tool modules listed by INCIBE as delivered software libraries: file name/path detection (Univ. León), face detection + gender/age estimation, adult-pornography detection, sexual-organ detection, video summarisation, camera noise-pattern matching, carving, pre-diagnosis. No licence is stated; distribution was via INCIBE's own install/update platform. — [INCIBE 4NSEEK tool page](https://www.incibe.es/en/incibe/corporate-information/who-we-work-with/european-projects/4nseek/tool)
- [V] iCOP (Peersman, Schulze, Rashid, Brennan, Fischer; Digital Investigation 18, Sept 2016): live-forensics P2P toolkit; publication page mentions no code availability. — [Bristol research portal](https://research-information.bris.ac.uk/en/publications/icop-live-forensics-to-reveal-previously-unknown-criminal-media-o/)
- [V] Cloudflare CSAM Scanning Tool: free service for Cloudflare customers; the Sept 2025 update post does not state it is open source. — [Cloudflare blog](https://blog.cloudflare.com/a-simpler-path-to-a-safer-internet-an-update-to-our-csam-scanning-tool/)
- [V] Apple's CSAM detection (NeuralHash-based) was announced Aug 2021, delayed late 2021, and abandoned on 7 Dec 2022 ("We have further decided to not move forward with our previously proposed CSAM detection tool for iCloud Photos"). — [MacRumors](https://www.macrumors.com/2022/12/07/apple-abandons-icloud-csam-detection/)
- [S] Google offers Content Safety API (classifier) and CSAI Match (video hash matching) to qualifying partners via its "tools for partners" programme (page not fetched). — [Google](https://protectingchildren.google/tools-for-partners/)
- [U] Microsoft PhotoDNA is proprietary; licensed free to qualified organisations and offered as a cloud service; the algorithm is not published.
- [V] Tech Coalition Lantern is a signal-sharing programme (not software) open only to "qualifying technology companies and financial institutions". — [Lantern 2025 transparency report](https://technologycoalition.org/resources/lantern-2025-transparency-report/)

### Inferences
- A three-way taxonomy fits the evidence: (1) open code + open algorithm, usable by anyone (PDQ, TMK+PDQF, vPDQ, HMA, Osprey, Coop, PAN12-derived models); (2) published method, closed artefact (Pereira et al., Al-Nabki et al., iCOP, DeepPatrol, Thorn, Google, PhotoDNA); (3) open algorithm but closed hash *lists* (PDQ is open, but the NCMEC/IWF/StopNCII hash databases that make it useful are access-controlled). Category 3 is the main reason "open source" does not translate into "anyone can deploy" here.
- The open tools are concentrated where no illegal data is needed to build or test (hashing maths, rules engines, review queues, text models trained on decoy chat logs). There is no evidence in these notes of any open-weight classifier for novel CSAM imagery.

### Gaps
- GitHub could not be fetched: licence files, star counts, last-commit dates and archived flags for facebook/ThreatExchange, roostorg/osprey, roostorg/coop, LAION-AI/CLIP-based-NSFW-Detector, yahoo/open_nsfw, bhky/opennsfw2 are NOT verified. Coop's licence: not found.
- Thorn open releases: not found. Searches surfaced only proprietary Safer products; I found no Thorn GitHub repo or open model. Absence in two searches is weak evidence, not proof.
- Whether Microsoft released code/weights for Pereira et al.: not found (abstract page silent; full text not read).
- Open age-estimation models (e.g. MiVOLO, FairFace, UTKFace/IMDB-WIKI-trained models) and NIST's age-estimation evaluation: [U], not researched this session.
- Yahoo open_nsfw archived status, LAION CLIP-based NSFW detector, Falconsai/nsfw_image_detection licence and download counts: only search-result titles seen ([S]); not verified. — [LAION detector](https://www.github.com/LAION-AI/CLIP-based-NSFW-Detector), [opennsfw2](https://github.com/bhky/opennsfw2)
- StopNCII / NCMEC Take It Down hashing algorithm (commonly reported as PDQ for images, MD5 for video [U]) was not confirmed in a fetched source.

---

## Q2. For each tool: real adoption, or evidence of non-use?

### Takeaway
Adoption evidence is strong for closed or membership-gated hash-matching (87-89% of surveyed companies) and now exists by name for ROOST's open tools (Bluesky, Discord, Matrix.org, Kyodo), while the academic/EU/NIJ-funded detection tools show the opposite pattern: 4NSEEK is explicitly "no longer supported", FileTSAR failed independent verification, DeepPatrol was never reported as available, and the open grooming models carry their authors' own "not ready for real-world use" labels.

### Cited Findings

**Deployed and maintained**
- [V] Osprey: Bluesky runs it in production (>50 million events/day); Discord re-adopted the open-source version; the Matrix.org Foundation is an active user (as of 28 Jan 2026). — [ROOST Osprey v1.0](https://roost.tools/blog/introducing-osprey-v1-0-open-source-infrastructure-for-real-time-abuse-mitigation/)
- [V] Coop: Kyodo (messaging platform, >150M messages sent) is a named adopter; an unnamed adopter "serving tens of millions of users" estimates ~95% reduction in annual safety-tooling cost after self-hosting (ROOST's own announcement, 9 June 2026; self-reported, not independently audited). — [ROOST Coop 1.0](https://roost.tools/blog/coop-1-0-world-s-first-free-open-source-child-safety-infrastructure-for-every-platform/)
- [V] StopNCII.org (as of 28 Nov 2024): >1,000,000 image hashes created; 14 partners after Bitly and Resolver joined (Facebook, Instagram, Threads, TikTok, Reddit, OnlyFans, Pornhub, Snap, Niantic, Playhouse, RedGIFS, Microsoft Bing). — [UK Safer Internet Centre](https://saferinternet.org.uk/?p=107230); [S] later headline says 2,000,000 images — [SWGfL](https://swgfl.org.uk/magazine/stopncii-org-being-used-to-protect-2-000-000-images-online-in-the-fight-against-intimate-image-abuse/)
- [V] Lantern (2025 figures, report dated 28 Apr 2026): 31 participants (28 tech companies, 3 financial institutions), 23 meeting engagement criteria; nearly 1 million signals shared in 2025 (>2 million since launch); 31,504 accounts actioned in 2025. — [Lantern 2025 transparency report](https://technologycoalition.org/resources/lantern-2025-transparency-report/)
- [V] Cloudflare CSAM Scanning Tool: after Cloudflare removed the requirement for site operators to supply their own NCMEC credentials (Feb 2025), monthly adoption rose 1,600% (relative figure only; no absolute count). — [Cloudflare blog, 24 Sep 2025](https://blog.cloudflare.com/a-simpler-path-to-a-safer-internet-an-update-to-our-csam-scanning-tool/)
- [V] Thorn Safer Predict: X beta-tested the text model (2024). — [Thorn](https://www.thorn.org/press-releases/thorn-launches-safer-predict-a-proactive-ai-detection-solution-to-scale-child-safety-on-content-hosting-platforms/)
- [V] Re-LAION-5B: produced with IWF, C3P and Stanford hash lists; downstream usage numbers not found. — [LAION](https://laion.ai/blog/relaion-5b/)

**Deployed, then abandoned / unsupported**
- [V] 4NSEEK: INCIBE's project page states "The 4NSEEK forensic analysis tool is no longer supported." Project ran Jan 2019 to June 2021 (EU Internal Security Fund - Police, call ISFP-2017-AG-CYBER); tool was provided free to participating LEAs and other interested police. Partners: INCIBE (coordinator), Univ. León, Univ. Malta, Univ. Groningen, Malta Police, Policía Nacional, Guardia Civil, APAV. — [INCIBE 4NSEEK project page](https://www.incibe.es/en/incibe/corporate-information/who-we-work-with/european-projects/4nseek)
- [V] The separate 4NSEEK tool page still lists LEAs in 28 countries with access and 25 more "in application processes", with no date and no support notice, i.e. the two INCIBE pages are inconsistent and the tool page looks stale. — [INCIBE tool page](https://www.incibe.es/en/incibe/corporate-information/who-we-work-with/european-projects/4nseek/tool)
- [V] HMA 1.0: archived March 2024. Documented reason: hard AWS dependencies and lack of flexibility "kept some potential users from deploying it", and the dependency count became a maintenance burden. It had been built to hit 4,000 QPS for one initial AWS-based industry partner (unnamed). — [HMA history](https://facebook.github.io/ThreatExchange/hma/history.html)
- [V] Apple CSAM detection: announced, never shipped, cancelled 7 Dec 2022. — [MacRumors](https://www.macrumors.com/2022/12/07/apple-abandons-icloud-csam-detection/)

**Published / funded, with evidence against real use**
- [V] FileTSAR (Purdue, NIJ-funded): NIJ's article (16 Dec 2021) says it was licensed free to 120 agencies worldwide, at least 30 had implemented it, and usage by the other 90 was unknown. NIJ's Criminal Justice Testing and Evaluation Consortium (O'Leary, Parsons, Planty, Ropero-Miller; NCJ 306446, July 2022) could not install or test it, could not confirm it performs as reported, and concluded "in its current state, FileTSAR is not a deliverable that should be released for use by the criminal justice community" and that it "does not meet the requirements of the National Institute of Justice solicitation". Note: FileTSAR is a general network-forensics toolkit, not a child-safety classifier. — [NIJ article](https://nij.ojp.gov/topics/articles/improving-collection-digital-evidence); [NIJ verification report](https://nij.ojp.gov/library/publications/verification-report-toolkit-selective-analyses-reconstruction-files-filetsar)
- [V] DeepPatrol (Univ. Rhode Island, NIJ-funded): NIJ (Dec 2021) says more research is needed before it can become a commercially viable tool; runtime cited as 39 hours for a ~1M-file case; under Daubert-standard evaluation by the Defense Cybercrime Institute, no results reported; no agencies listed as users. — [NIJ article](https://nij.ojp.gov/topics/articles/improving-collection-digital-evidence)
- [V] GRACE (H2020 grant 883341; 1 Jun 2020 to 30 Nov 2023; total cost EUR 6,824,012.50; coordinator Vicomtech): CORDIS lists 18 deliverables (mostly ethical/legal reports, architecture documents, one federated-learning report) and publications (age estimation, text classification, speech age/gender, federated learning). The CORDIS results page names no released tool, no open-source release and no deployment at Europol or LEAs. — [CORDIS](https://cordis.europa.eu/project/id/883341/results)
- [V] iCOP: evaluated on real case data and in hands-on trials with law-enforcement officers; the 2016 publication page does not state operational deployment. — [Bristol](https://research-information.bris.ac.uk/en/publications/icop-live-forensics-to-reveal-previously-unknown-criminal-media-o/). Conflicting signal: a 2019 practitioner survey (n=106) reported "ICOP" as used by 50% of respondents, but this very likely refers to ICAC-COPS, a different US law-enforcement system with a near-identical acronym, not the Lancaster iCOP toolkit; I could not resolve this from the transcript. — [Forensic Focus](https://www.forensicfocus.com/webinars/a-practitioner-survey-exploring-forensic-tools-for-investigating-child-sexual-abuse-material/)
- [V] Vogt et al. grooming models: authors' own page says "not ready for real-world use"; no deployment found. — [GitLab pages](https://early-sexual-predator-detection.gitlab.io)
- [V] compAnIonv1: student capstone, 1 like, no update in 2+ years, no deployment evidence. — [HF](https://huggingface.co/chatcompanion/compAnIonv1/blob/main/README.md)
- [V] Pereira et al. (Microsoft) metadata classifier: no deployment statement on the arXiv page. — [arXiv](https://arxiv.org/abs/2010.02387)
- [V] UK Safety Tech Challenge Fund proofs-of-concept (GalaxKey/Yoti, SafeToWatch, Cyacomb, T3K, DragonflAI): REPHRAIN evaluators had no access to code or testing and could not assess effectiveness, robustness or scalability; "none of the projects is in a position to claim it could reliably deal with new CSAM" (Ross Anderson-group blog summary of the REPHRAIN report, 23 Mar 2023). These were not open source. — [Bentham's Gaze](https://www.benthamsgaze.org/2023/03/23/a-well-executed-exercise-in-snake-oil-evaluation/); REPHRAIN describes its work as "the first independent, public evaluation of automated industry tools developed for online child protection" — [REPHRAIN](https://www.rephrain.ac.uk/?p=1593)

### Inferences
- Best-supported examples for "open and published but NOT used": the PAN12-derived grooming models (Vogt et al. GitLab release; compAnIonv1 on HF). Both are openly downloadable, and both show zero documented deployments plus an author disclaimer.
- Best-supported example of "deployed then abandoned": 4NSEEK (LEA-gated, EU-funded, unsupported after project end in June 2021) and HMA 1.0 (open, archived March 2024, with the unusual feature that the maintainers documented *why* adopters walked away).
- Best-supported examples of "published but closed": Al-Nabki et al. file-name classifier, Pereira et al., iCOP, DeepPatrol, GRACE outputs. None of these is an "open-source tool going unused"; they were never open.
- 4NSEEK's file-name classifier therefore does not belong in the "open source but unused" bucket. It is "closed, LEA-gated, deployed, then unsupported". The user's starting framing should be corrected on this point.
- FileTSAR's "licensed to 120, implemented by at least 30, unknown for 90" is the only hard licensed-vs-implemented ratio found (roughly 25% confirmed implementation), and it is for a general forensics tool.
- PDQ's real-world adoption is plausible (StopNCII, NCMEC Take It Down, GIFCT are commonly reported users [U]) but I did not verify any named PDQ deployer in a fetched source this session.

### Gaps
- No direct evidence of who runs HMA 2.0 / Open Media Match in production. [S] A Tech Against Terrorism/JustPaste.it GIFCT hash-sharing case study exists but was not fetched — [PDF](https://counterextremism.com/sites/default/files/TAT%20--%20JustPaste.it%20GIFCT%20hash-sharing%20Case%20study.pdf) (URL as returned by search contained spaces; treat as unverified).
- Whether any LEA still runs 4NSEEK after support ended: not found. Date on which INCIBE added the "no longer supported" notice: not found.
- ASASEC (4NSEEK's predecessor) status: an INCIBE page exists [S] but was not fetched — [INCIBE ASASEC](https://www.incibe.es/incibe/informacion-corporativa/con-quien-trabajamos/proyectos-europeos/asasec).
- GRACE "Results in Brief" and final periodic report were not read; a platform may have been handed to Europol without CORDIS saying so. Absence on CORDIS is not proof of non-deployment.
- DeepPatrol status after Dec 2021: not found.
- NCMEC Take It Down participating platforms and hash counts: not verified ([S] headline only, Feb 2023 launch — [Gizmodo](https://gizmodo.com/facebook-instagram-child-porn-removal-take-it-down-1850163343)).
- Cyberbullying classifiers and age-estimation models: no deployment evidence gathered either way.

---

## Q3. What surveys or reports quantify the research-to-deployment gap?

### Takeaway
I found no source that gives a count or percentage of academic child-safety systems that reach deployment; that number appears not to exist in the sources checked. What exists are industry-side uptake surveys (hash matching near-universal among surveyed firms, classifiers around half, grooming detection about a third) and one practitioner survey showing investigators rely on commercial suites.

### Cited Findings
- [V] WeProtect Global Alliance / Tech Coalition survey of 32 technology companies (Feb-Mar 2021): 87% use image hash-based detection; 76% video hash-based detection; classifiers: text 56%, image 56%, video 30%, livestream 22%; grooming/predatory-behaviour detection 37%. — [WeProtect survey PDF](https://www.weprotect.org/wp-content/uploads/Survey-of-technology-companies-2021.pdf)
- [V] Same survey, stated barriers to using technical resources: time/bandwidth constraints 46%; technical limitations 32%; unfamiliar with or don't know how to access tools 18%; financial limitations 14%; inconsistent with company policy 7%; lack of leadership buy-in 0%; other 29%. — [WeProtect survey PDF](https://www.weprotect.org/wp-content/uploads/Survey-of-technology-companies-2021.pdf)
- [V] Tech Coalition 2023 member survey (published 11 Apr 2024): 89% of members use at least one image hash-matcher; 59% at least one video hash-matcher; 57% at least one classifier for previously unhashed CSAM. No per-tool (PhotoDNA vs PDQ vs CSAI Match) breakdown is given. — [Tech Coalition](https://technologycoalition.org/resources/update-on-voluntary-detection-of-csam/)
- [V] Sanchez et al. (Univ. New Haven), practitioner survey presented at DFRWS US 2019, 106 respondents: commercial tools (Cellebrite, Magnet, FTK) most used; hash-database tools popular but limited to known content; skin-tone and face detection were the most commonly used filtering technologies; respondents unanimously wanted age-estimation tools; 69% had formal CSAM-investigation training; 41% said they were not competent in data science; concerns about false positives/negatives, time cost, and lack of money, equipment and staff. — [Forensic Focus transcript](https://www.forensicfocus.com/webinars/a-practitioner-survey-exploring-forensic-tools-for-investigating-child-sexual-abuse-material/)
- [V] NIJ's own grant portfolio: of two NIJ-funded tools profiled in Dec 2021, one (DeepPatrol) was not yet viable and the other (FileTSAR) failed independent verification. — [NIJ](https://nij.ojp.gov/topics/articles/improving-collection-digital-evidence)
- [V] REPHRAIN's evaluation of five UK-government-funded proofs of concept could not establish false-positive or false-negative rates for any of them because evaluators had documents only, not code or test access. — [Bentham's Gaze](https://www.benthamsgaze.org/2023/03/23/a-well-executed-exercise-in-snake-oil-evaluation/)
- [V] Barbrook & May-Chahal (Lancaster, 2023), "A Rapid Evidence Assessment of Technical Tools for the Detection and Disruption of CSAM and CSAM Offenders in the ASEAN Region", assesses effectiveness of automated tools; only the abstract was accessible, so no figures. — [Lancaster eprints](https://eprints.lancs.ac.uk/id/eprint/199945)
- [S] Lee, Ermakova, Ververis, Fabian, "Detecting child sexual abuse material: A comprehensive survey" (Forensic Science International: Digital Investigation, 2020) exists and is indexed at Fraunhofer; not fetched, no numbers extracted. — [Fraunhofer Publica](https://publica.fraunhofer.de/handle/publica/265608)
- [S] Stanford Internet Observatory, "How to Fix the Online Child Exploitation Reporting System" (22 Apr 2024) on the NCMEC CyberTipline; not fetched. — [Stanford Cyber Policy Center](https://cyber.fsi.stanford.edu/node/36158)
- [S] Bristol/REPHRAIN paper "Towards a framework for evaluating CSAM prevention and detection tools..." exists; not fetched. — [Bristol](https://research-information.bris.ac.uk/en/publications/towards-a-framework-for-evaluating-csam-prevention-and-detection-/)

### Inferences
- The uptake gradient in the industry surveys (image hashing ~87-89% > video hashing 59-76% > classifiers ~56-57% > grooming detection 37%) tracks tool maturity and inversely tracks the amount of sensitive training data needed. Grooming detection is the area with the most open academic artefacts (PAN12 line of work) and the lowest industry uptake.
- The WeProtect/Tech Coalition samples are members of industry coalitions, so they overstate adoption across the long tail of small platforms; that long tail is exactly what Cloudflare's tool and ROOST Coop target.
- A defensible statement for the report: "no published source quantifies how many academic child-safety detection systems reach deployment; the available evidence is anecdotal and negative (NIJ, REPHRAIN, INCIBE)". Any specific percentage would be invented.

### Gaps
- Number/percentage of academic systems reaching deployment: not found in any source.
- Lee et al. 2020 content (their taxonomy and any statement on deployment) not read.
- WeProtect Global Threat Assessment (2023/2025), Thorn research reports, EU CSA Regulation impact assessment (2022), and Stanford CyberTipline report specifics: not fetched; no figures recorded.
- UK DSIT/DCMS official Safety Tech Challenge Fund evaluation text: only a secondary summary was read.

---

## Q4. Documented reasons open (and published) tools are not adopted

### Takeaway
The documented barriers are mostly not about model quality. They are: illegal-to-share training data, access-gated hash lists and reporting credentials, infrastructure lock-in, funding that ends with the project, inability of third parties to evaluate, and operator capacity.

### Cited Findings
- **Training data cannot legally be collected or shared.** [V] Al-Nabki et al.: "there are no publicly available datasets" of the CSEM class; "crawling samples from a P2P network or the Darknet is illegal"; only material "provided by LEAs, could be used". Consequence: the model and data stayed inside the INCIBE/LEA channel. — [ar5iv 2011.01113](https://ar5iv.labs.arxiv.org/html/2011.01113)
- **Law-enforcement-only gating.** [V] 4NSEEK was provided free, but to LEAs. — [INCIBE](https://www.incibe.es/en/incibe/corporate-information/who-we-work-with/european-projects/4nseek)
- **Project funding ends, support ends.** [V] 4NSEEK project window Jan 2019 to June 2021; tool now "no longer supported". — [INCIBE](https://www.incibe.es/en/incibe/corporate-information/who-we-work-with/european-projects/4nseek)
- **Infrastructure lock-in / no integration path.** [V] HMA 1.0's hard AWS dependency kept potential users from deploying it; maintenance burden led to archive and rewrite. — [HMA history](https://facebook.github.io/ThreatExchange/hma/history.html)
- **Credential / reporting-pipeline friction.** [V] Cloudflare: creating and sharing NCMEC credentials "was too confusing or too much work for small site owners"; removing that step produced a 1,600% rise in monthly adoption. — [Cloudflare](https://blog.cloudflare.com/a-simpler-path-to-a-safer-internet-an-update-to-our-csam-scanning-tool/)
- **Cannot be installed or independently verified; legal exposure for users.** [V] FileTSAR: evaluators could not install it; requires Ubuntu 16.04; capture of data in motion is an intercept "subject to court authorization" and the materials did not warn users; "not practical for most state and local agencies". — [NIJ report](https://nij.ojp.gov/library/publications/verification-report-toolkit-selective-analyses-reconstruction-files-filetsar); [NIJ article](https://nij.ojp.gov/topics/articles/improving-collection-digital-evidence)
- **Performance / evidentiary standard.** [V] DeepPatrol: 39 hours per ~1M-file case; needs Daubert-standard reliability evaluation before courtroom use. — [NIJ article](https://nij.ojp.gov/topics/articles/improving-collection-digital-evidence)
- **Evaluation concerns and false positives.** [V] REPHRAIN: developers "generally unprepared to mitigate against false positives", no consideration of auditability or appeals; evaluators had no code access. — [Bentham's Gaze](https://www.benthamsgaze.org/2023/03/23/a-well-executed-exercise-in-snake-oil-evaluation/). [V] Practitioners cite false positive/negative worries and time cost of AI tools. — [Forensic Focus](https://www.forensicfocus.com/webinars/a-practitioner-survey-exploring-forensic-tools-for-investigating-child-sexual-abuse-material/)
- **Authors' own readiness disclaimers; harm from misclassification.** [V] Vogt et al.: models "not ready for real-world use". — [GitLab pages](https://early-sexual-predator-detection.gitlab.io). [V] compAnIonv1: misclassification could harm parent-child relationships and people wrongly accused; English-only; 400-token window; language drift. — [HF](https://huggingface.co/chatcompanion/compAnIonv1/blob/main/README.md)
- **Privacy / civil-liberties opposition.** [V] Apple dropped its system after feedback from customers, advocacy groups and researchers. — [MacRumors](https://www.macrumors.com/2022/12/07/apple-abandons-icloud-csam-detection/). [V] Four of five UK Challenge Fund projects appeared to rely on client-side scanning, criticised as undermining E2EE. — [Bentham's Gaze](https://www.benthamsgaze.org/2023/03/23/a-well-executed-exercise-in-snake-oil-evaluation/)
- **Operator capacity, not leadership will.** [V] Top barrier among 32 surveyed companies was time/bandwidth (46%), then technical limitations (32%), not knowing how to access tools (18%), cost (14%); leadership buy-in 0%. — [WeProtect](https://www.weprotect.org/wp-content/uploads/Survey-of-technology-companies-2021.pdf)
- **Packaging, licensing and maintenance of open projects.** [V] ROOST: small teams are overloaded; "policy is moving faster than tooling"; projects must be effectively licensed, packaged, maintained and interoperable; "some urgently needed open building blocks, especially for child safety, remain unavailable"; ROOST says it "revived orphaned projects" in 2025 (projects not named). — [ROOST 2025 review](https://roost.tools/blog/roost-in-review-a-look-back-on-2025/)

### Inferences
- The barriers split cleanly by tool type. For *novel-content classifiers*: illegal data means no open weights, no third-party evaluation and LEA-only distribution, so the tool dies with its grant. For *open matching/workflow infrastructure*: the code is free but the hash lists, NCMEC reporting credentials and ops burden are not, so adoption depends on someone packaging the full pipeline (which is what Cloudflare's Feb 2025 change and ROOST Coop 1.0 did). For *open text models*: data is decoy-based and a decade-plus old, authors disclaim readiness, and nobody owns maintenance.
- The Cloudflare 1,600% figure is the cleanest natural experiment found: removing a single non-technical integration step changed adoption by more than an order of magnitude.

### Gaps
- No source found that ranks these barriers quantitatively for academic tools specifically.
- Legal analysis (e.g. 18 U.S.C. 2258A reporting duties, EU interim ePrivacy derogation and its expiry/extension status in 2026, UK Online Safety Act duties) was not researched; current status of the EU CSA Regulation as of Nov 2026: not found.
- Which "orphaned projects" ROOST revived: not found.

---

## Q5. Open datasets a student could legally study alone

### Takeaway
Text and hashing are the legally safe areas: PAN12 is openly downloadable (licence unstated), PAN12-derived corpora can be rebuilt from public code, and perceptual-hash algorithms can be tested on any benign image set. No legitimate open dataset of the positive image class exists, and none should be sought.

### Cited Findings
- [V] PAN12 Sexual Predator Identification corpus: Zenodo, access "Open", 91.2 MB, DOI 10.5281/zenodo.3713280, MD5 listed, no licence shown on the record. — [Zenodo](https://zenodo.org/record/3713280); task description — [S] [PAN at CLEF 2012](https://pan.webis.de/clef12/pan12-web/sexual-predator-identification.html)
- [V] PAN12 composition, per a downstream model card: Perverted-Justice decoy transcripts as positives, IRC logs and Omegle chats as negatives; about 3% positive. PJZC is a newer set of 1,104 Perverted-Justice conversations. — [HF compAnIonv1](https://huggingface.co/chatcompanion/compAnIonv1/blob/main/README.md)
- [V] PANC and VTPAN can be rebuilt with public preprocessing scripts from PAN12 (+ ChatCoder2 for PANC); licence not stated. — [GitLab pages](https://early-sexual-predator-detection.gitlab.io)
- [V] NIST NSRL was used as the public benign-class source for file-name research. — [ar5iv 2011.01113](https://ar5iv.labs.arxiv.org/html/2011.01113)
- [V] PDQ, TMK+PDQF, vPDQ reference implementations are BSD-licensed and can be run on any benign media. — [ThreatExchange README](https://cdn.jsdelivr.net/gh/facebook/ThreatExchange@main/README.md)
- [V] Re-LAION-5B metadata (links + captions, Apache-2.0) is gated behind an affiliation/consent form on Hugging Face. — [LAION](https://laion.ai/blog/relaion-5b/)
- [S] Related grooming-analysis work on modern platforms exists ("Large-scale analysis of grooming in modern social networks", arXiv 2004.08205); not fetched. — [arXiv](https://arxiv.org/pdf/2004.08205)

### Inferences
- A student project that is both legal and informative about the research-to-deployment gap: reproduce a PAN12 grooming classifier, then measure how it degrades out of distribution, since the main open corpus dates from 2012 and its positives are adult decoys, not real minors. That limitation is itself a plausible unstated reason the open models are not deployed.
- Perverted-Justice-derived data involves real people convicted of or accused of offences, and Omegle/IRC negatives were collected without consent; "open on Zenodo" does not settle the ethics, and the missing licence means redistribution rights are unclear. An IRB/ethics check is prudent even for solo study.

### Gaps
- Cyberbullying corpora were not researched this session. Leads, all [U]: Jigsaw Toxic Comment Classification (Kaggle), Davidson et al. hate/offensive tweets, the Formspring cyberbullying set, ChatCoder2, and the Instagram/Vine session datasets from CU Boulder. Licences and access terms: not found.
- NSRL RDS licence terms (believed US-government public domain [U]) not verified.
- Age-estimation datasets (UTKFace, IMDB-WIKI, FairFace, APPA-REAL; all [U]) and their research-only licence terms not verified.
- ChatCoder2 access terms (believed request-only [U]): not found.
- Hash-algorithm benchmark sets (e.g. for PDQ robustness testing): none identified.

---

## Inventory table

Abbreviations: V = verified in fetched source; S = search snippet only; U = unverified background. "not found" = searched or fetched, no evidence.

| Tool | Type | Released (code/weights/data) | License | Deployment evidence | Maintenance status | Barrier if unused | Source URL | Verification status |
|---|---|---|---|---|---|---|---|---|
| Meta PDQ | Image perceptual hash | Code open; hash lists not included | BSD | Named deployers not verified this session (StopNCII, Take It Down, GIFCT commonly cited: U) | In active repo per README; commit dates not checked | n/a (used); hash lists are access-controlled | https://cdn.jsdelivr.net/gh/facebook/ThreatExchange@main/README.md | V (release, licence); U (deployers) |
| Meta TMK+PDQF | Video hash | Code open | BSD | not found | Listed in README; status not stated | not found | https://cdn.jsdelivr.net/gh/facebook/ThreatExchange@main/README.md | V (release); adoption not found |
| Meta vPDQ | Video hash | Code open | BSD | not found | Listed in README; status not stated | not found | https://cdn.jsdelivr.net/gh/facebook/ThreatExchange@main/README.md | V (release); adoption not found |
| HMA 1.0 | Hash-match-action pipeline (AWS) | Code open | BSD | One unnamed AWS-based industry partner (design target 4,000 QPS) | Archived March 2024 | Hard AWS dependency, inflexible, maintenance burden | https://facebook.github.io/ThreatExchange/hma/history.html | V |
| HMA 2.0 / Open Media Match | Hash-match pipeline (Docker, API-only) | Code open | BSD | not found | Successor to 1.0; README says "under construction" (README date unknown) | No GUI; needs external hash-list access | https://facebook.github.io/ThreatExchange/hma/history.html | V (existence); adoption not found |
| ROOST Osprey | Rules engine / investigation | Code open | Apache-2.0 | Bluesky (>50M events/day), Discord, Matrix.org Foundation | Active; v1.0 on 28 Jan 2026 | n/a (used) | https://roost.tools/blog/introducing-osprey-v1-0-open-source-infrastructure-for-real-time-abuse-mitigation/ | V |
| ROOST Coop | Review queue + NCMEC reporting | Code + Docker images open | not found | Kyodo; one unnamed adopter (tens of millions of users), self-reported | Active; v1.0 on 9 Jun 2026 | n/a (used) | https://roost.tools/blog/coop-1-0-world-s-first-free-open-source-child-safety-infrastructure-for-every-platform/ | V (vendor-reported) |
| gpt-oss-safeguard (OpenAI + ROOST) | Policy-conditioned safety reasoning model | Open weights (per ROOST) | not found | not found | Released 2025 | not found | https://roost.tools/blog/roost-in-review-a-look-back-on-2025/ | V (existence only) |
| PAN12 Sexual Predator ID corpus | Grooming text dataset | Data open (Zenodo) | None stated | Widely used in research; no production use found | Static (2012) | Decoy-based, dated, licence unclear | https://zenodo.org/record/3713280 | V |
| Vogt et al. eSPD models + PANC | Grooming detection models/code | Code (GitLab), weights (Mega), dataset-build scripts | None stated | None; authors: "not ready for real-world use" | No maintenance info; 2021 | Author disclaimer; eval limits; no integration path | https://early-sexual-predator-detection.gitlab.io | V |
| chatcompanion/compAnIonv1 | Grooming classifier (BERT-size) | Weights open (HF) | MIT | None found; 1 like | Stale (README untouched 2+ years) | Student capstone; false-positive harm; English-only; no owner | https://huggingface.co/chatcompanion/compAnIonv1/blob/main/README.md | V |
| Re-LAION-5B | Cleaned image-link dataset | Metadata open, gated form | Apache-2.0 | Built with IWF, C3P, Stanford hash lists; downstream use not found | Released 30 Aug 2024 | n/a | https://laion.ai/blog/relaion-5b/ | V |
| 4NSEEK forensic tool (incl. Univ. León file-name classifier) | LEA forensic triage suite | Binary to LEAs via INCIBE platform; no public code/weights/data | None stated | LEAs in 28 countries had access (undated page) | "No longer supported" (project ended June 2021) | LEA-only gating; LEA-supplied illegal training data; project funding ended | https://www.incibe.es/en/incibe/corporate-information/who-we-work-with/european-projects/4nseek | V |
| Al-Nabki et al. file-name/path CSEM classifier | Text classifier on metadata | Paper only | n/a | Delivered as 4NSEEK module | Follows 4NSEEK (unsupported) | No public positive-class data; collection illegal | https://ar5iv.labs.arxiv.org/html/2011.01113 | V (preprint); Sci. Reports 2023 version U |
| Pereira et al. (Microsoft) metadata CSAM detector | CNN on file paths | Paper only (no release mentioned in abstract) | n/a | not found | not found | not found (likely data restrictions: U) | https://arxiv.org/abs/2010.02387 | V (abstract only) |
| iCOP (Peersman et al.) | P2P live-forensics toolkit | Paper only; code availability not stated | n/a (article CC BY) | Trials with LE officers (2016); operational deployment not stated | not found | not found | https://research-information.bris.ac.uk/en/publications/icop-live-forensics-to-reveal-previously-unknown-criminal-media-o/ | V |
| EU GRACE (883341) | LEA analytics platform research (federated learning, age estimation, NLP) | Reports + papers; no tool named on CORDIS | not found | None stated on CORDIS | Project closed 30 Nov 2023 | not found (results-in-brief not read) | https://cordis.europa.eu/project/id/883341/results | V |
| DeepPatrol (URI, NIJ) | Video CSAM triage + age estimation | None public | n/a | None stated | Status after Dec 2021 not found | Too slow (39 h per ~1M files); Daubert evaluation pending; not commercially viable | https://nij.ojp.gov/topics/articles/improving-collection-digital-evidence | V |
| FileTSAR (Purdue, NIJ) | Network forensics toolkit (not child-safety specific) | Free licensed distribution to LEAs | Free licence to agencies | Licensed to 120 agencies; at least 30 implemented; 90 unknown (Dec 2021) | Failed NIJ verification (Jul 2022); current status not found | Could not be installed/verified; Ubuntu 16.04; intercept-law exposure; impractical for local agencies | https://nij.ojp.gov/library/publications/verification-report-toolkit-selective-analyses-reconstruction-files-filetsar | V |
| UK Safety Tech Challenge Fund PoCs (GalaxKey, SafeToWatch, Cyacomb, T3K, DragonflAI) | CSAM detection in E2EE prototypes | Closed; evaluators got documents only | Proprietary | None as E2EE deployments | PoC stage (2021-2023) | Unverifiable; false-positive handling absent; client-side scanning objections | https://www.benthamsgaze.org/2023/03/23/a-well-executed-exercise-in-snake-oil-evaluation/ | V (secondary source) |
| Thorn Safer / Safer Predict | Hash matching + CSAM/CSE classifiers | Closed service | Proprietary (no open claim) | X beta-tested text model | Active (launched Jul 2024) | n/a | https://www.thorn.org/press-releases/thorn-launches-safer-predict-a-proactive-ai-detection-solution-to-scale-child-safety-on-content-hosting-platforms/ | V |
| Thorn open-source releases | n/a | not found | not found | not found | not found | not found | https://www.thorn.org/blog/how-thorns-csam-classifier-uses-artificial-intelligence-to-build-a-safer-internet/ | not found (S link only) |
| Cloudflare CSAM Scanning Tool | Fuzzy-hash matching service | Closed, free to customers | Proprietary | Monthly adoption +1,600% after Feb 2025 change (no absolute number) | Active (update 24 Sep 2025) | Earlier: NCMEC credential step too hard for small sites | https://blog.cloudflare.com/a-simpler-path-to-a-safer-internet-an-update-to-our-csam-scanning-tool/ | V |
| Apple CSAM detection (NeuralHash) | On-device perceptual hash + matching | Never released | Proprietary | Never deployed | Cancelled 7 Dec 2022 | Privacy/security backlash | https://www.macrumors.com/2022/12/07/apple-abandons-icloud-csam-detection/ | V |
| Google Content Safety API / CSAI Match | Classifier API / video hash match | Closed, free to qualifying partners | Proprietary | not fetched | Active (assumed) | n/a | https://protectingchildren.google/tools-for-partners/ | S |
| Microsoft PhotoDNA | Image perceptual hash | Closed | Proprietary, free to qualified orgs | Industry standard (87-89% of surveyed firms use some image hash-matcher; not PhotoDNA-specific) | Active (assumed) | n/a | https://technologycoalition.org/resources/update-on-voluntary-detection-of-csam/ | U (PhotoDNA facts); V (survey %) |
| Tech Coalition Lantern | Cross-platform signal sharing programme | Not software; eligibility-gated | n/a | 31 participants; ~1M signals in 2025; 31,504 accounts actioned | Active (report 28 Apr 2026) | n/a | https://technologycoalition.org/resources/lantern-2025-transparency-report/ | V |
| StopNCII.org | On-device NCII hashing + hash sharing | Service; algorithm not named in source (PDQ: U) | n/a | >1M hashes, 14 partner platforms (Nov 2024); 2M headline later | Active | n/a | https://saferinternet.org.uk/?p=107230 | V (2024 figures); S (2M) |
| NCMEC Take It Down | Hashing service for minors' images | Service | n/a | Meta platforms at launch (headline, Feb 2023) | not verified | n/a | https://gizmodo.com/facebook-instagram-child-porn-removal-take-it-down-1850163343 | S |
| LAION CLIP-based NSFW Detector | NSFW proxy classifier | Code/weights (repo exists) | not found | Used to compute p_unsafe scores in Re-LAION filtering | not found | n/a | https://www.github.com/LAION-AI/CLIP-based-NSFW-Detector | S (repo); V (p_unsafe use, via LAION blog) |
| Yahoo open_nsfw / opennsfw2 | NSFW proxy classifier | Code/weights (repos exist) | not found | not found | not found (original believed archived: U) | not found | https://github.com/bhky/opennsfw2 | S / U |
| Open age-estimation models (MiVOLO, FairFace etc.) | Age estimation | not researched | not found | not found | not found | not found | n/a | U |
| Cyberbullying datasets/classifiers | Text datasets/models | not researched | not found | not found | not found | not found | n/a | U |

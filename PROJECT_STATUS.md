# Project Status

_Last updated: 2026-07-29 (backfill complete: 63,827 papers)_

## Completed

- [x] Codebase adapted from the hardened PhotocatalysisPapers architecture
      (stdlib-only pipeline, 8 collectors, JSON storage, static site, daily
      automation, committed fetch-side backfill checkpoint, INCOMPLETE-year
      flagging, peer-review-artifact + corrupt-OSTI collector guards)
- [x] Mechanochemistry classifier: PRIMARY terms (mechanochem…, ball mill…,
      liquid-assisted grinding, twin-screw extrusion, mechanoredox,
      mechanophore, tribochemistry, mechanical alloying) required; SUPPORT
      terms (mills, techniques, materials, reactions, in-situ monitoring, DFT,
      ML) refine score and categories; NEGATIVE terms reject mechanobiology /
      mechanotransduction / machining / engine tribology
- [x] 17 mechanochemistry categories, alphabetical in all UI dropdowns
- [x] Collector + backfill queries rewritten for mechanochemistry
- [x] Pioneers list (config/pioneers.json): Friscic, James, Mack, Bolm,
      Hanusa, Suslick, Kubota, Ito, Borchardt, Colacino, Crawford, Jones,
      Emmerling, Halasz, Boldyreva, Boldyrev, Balaz, Hernandez, Garcia,
      Stolle, Wang, Browne, Porcheddu
- [x] Unit tests adapted to the domain and passing (40 tests)
- [x] First live pipeline run + relevance inspection (caught/fixed a
      mechanobiology false positive: single incidental "mechanochemical
      sensor" in glycocalyx/virology abstracts now penalised out)
- [x] Published: repo `GuruprakashMP/mechanochemistry-papers`, GitHub Pages
      live at https://guruprakashmp.github.io/mechanochemistry-papers/
- [x] Daily workflow at 05:00 UTC collects, classifies, rebuilds, commits
      (verified green end-to-end in CI)
- [x] **Historical backfill 1960→2026 COMPLETE (2026-07-29): 63,827 papers**
      across ~20 year-batched workflow runs driven by a local monitor, plus
      the full pioneer sweep (+838). Every year confirmed clean (INCOMPLETE
      years auto-re-run from the committed fetch-side checkpoint).

## Ongoing (automatic, no maintenance)

- Daily GitHub Actions run keeps the index growing from 8 sources.

## Known issues (inherited environment quirks)

- Local machine: arXiv fails (missing SSL certs) and ChemRxiv 403s
  (Cloudflare) — both work/degrade gracefully in GitHub Actions.
- Semantic Scholar keyless tier rate-limits; collector skips gracefully.
- OpenAlex throttles in long daily windows (~11:00–05:00 UTC) regardless of
  runner IP; only ~05:00–11:00 UTC is reliable. Each run has a ~15k-record
  fetch budget — the committed fetch-side checkpoint
  (data/state/backfill_progress.json) makes retries spend it only on missing
  queries. The pioneer sweep alone costs ~15k fetches — never bundle it with
  a topic-year range in one run.
- OpenAlex serves occasional corrupted merges (OSTI repository records with a
  foreign publisher's DOI + abstract). Detection: OSTI journal/publisher with
  a DOI not starting 10.2172 — dropped at ingestion by the collector guard.

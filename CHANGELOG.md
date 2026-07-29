# Changelog

All notable changes to MechanochemistryPapers.

## [1.0.1] — 2026-07-29

### Fixed
- **One researcher is now one author page.** Publisher metadata carries
  Unicode dashes and honorifics, so the same person fragmented across
  several pages — the U+2010 spelling of a hyphenated name and the ASCII
  spelling everyone types were different keys. 5,013 stored names were
  rewritten (Guan-Wu Wang, Thomas-Xavier Métro, Jong-Beom Baek and more).
  New `models.normalize_author` (NFC, Unicode dashes -> ASCII `-`,
  invisible-space cleanup, leading honorifics dropped) is applied in
  `pipeline.process_records`, the single path shared by the daily run and
  the backfill. `tools/normalize_authors.py` migrates already-stored
  shards; it is idempotent, dry-run by default, and self-converging.
  `app.js` normalizes the incoming `?a=` value so pre-existing links and
  bookmarks still resolve.
- Deliberately not merged: initials vs full given names, and hyphen-less
  spellings — those would fuse distinct researchers, since surnames like
  "Li", "Hu" and "Wu" occur as complete names in this data. A trailing
  period is preserved because many names legitimately end in an initial.
- Paper ids and `data/state/seen.json` are byte-identical before and after
  the migration: author names never feed identity or dedupe keys.

## [1.0.0] — 2026-07-27

Initial release, adapted from the proven
[PhotocatalysisPapers](https://github.com/GuruprakashMP/photocatalysis-papers)
codebase (its hardened v1.2 architecture: stdlib-only pipeline, 8 metadata
collectors, resumable OpenAlex backfill with a committed fetch-side
checkpoint, INCOMPLETE-year flagging, peer-review-artifact and corrupt-OSTI
collector guards, static site with progressive loading).

### Changed from the parent project
- Scope: ALL mechanochemistry research (experimental, DFT, ML) — ball milling
  & grinding, liquid-assisted grinding, twin-screw extrusion, mechanocatalysis
  & mechanoredox, cocrystals & pharmaceutical solids, MOF & framework
  mechanosynthesis, polymer mechanochemistry & mechanophores, piezo- &
  tribocatalysis, sonochemistry, mechanical alloying and in-situ monitoring.
- Classifier: PRIMARY mechanochemistry vocabulary required (mechanochem…,
  ball mill…, liquid-assisted grinding, twin-screw extrusion, mechanoredox,
  mechanophore, tribochemistry, mechanical alloying); SUPPORT vocabulary
  (mills, techniques, materials, target reactions, in-situ monitoring,
  computational and data-driven methods) refines score/categories; NEGATIVE
  vocabulary rejects the neighbours that share the "mechano-" root
  (mechanobiology, mechanotransduction, cell/tissue/bone mechanics) or the
  word "grinding" (machining, grinding wheels, engine tribology).
  Deliberate scope calls: mechanical alloying of materials is IN scope;
  "mechanical properties" is never penalised.
- 17 mechanochemistry-specific categories.
- All collector and backfill queries rewritten for mechanochemistry.
- Pioneers list: Friscic, James, Mack, Bolm, Hanusa, Suslick, Kubota, Ito,
  Borchardt, Colacino, Crawford, Jones, Emmerling, Halasz, Boldyreva,
  Boldyrev, Balaz, Hernandez, Garcia, Stolle, Wang, Browne, Porcheddu
  (ASCII-normalized in config/pioneers.json).
- Backfill default start year: 1960 (modern era; the field has deep roots).
- Site branding: MechanochemistryPapers.

### Inherited operational notes
- OpenAlex throttles in long daily windows (~11:00–05:00 UTC) regardless of
  runner IP; schedule backfills for the ~05:00–11:00 UTC window. Each run has
  a ~15k-record fetch budget; the committed fetch-side checkpoint
  (`data/state/backfill_progress.json`) makes retries spend it only on missing
  queries. The pioneer sweep alone costs ~15k fetches — run it as its own run.
- Local machine: arXiv fails (missing SSL certs) and ChemRxiv 403s
  (Cloudflare) — both work/degrade gracefully in GitHub Actions. Semantic
  Scholar keyless tier rate-limits and skips gracefully.

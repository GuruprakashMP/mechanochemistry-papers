# Changelog

All notable changes to MechanochemistryPapers.

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

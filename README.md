# MechanochemistryPapers

A fully automated, continuously updated public index of **mechanochemistry
research papers** — ball milling & grinding, liquid-assisted grinding,
twin-screw extrusion, mechanocatalysis & mechanoredox, cocrystals &
pharmaceutical solids, MOF & framework mechanosynthesis, polymer
mechanochemistry & mechanophores, piezo- & tribocatalysis, mechanical alloying
and in-situ reaction monitoring. Experimental, computational (DFT) and
machine-learning studies are all in scope; neighbouring fields that merely
share the "mechano-" root or the word "grinding" (mechanobiology,
mechanotransduction, machining, engine tribology) are filtered out.

Sister project of
[DataDrivenChemistryPapers](https://github.com/GuruprakashMP/ddc-papers) and
[PhotocatalysisPapers](https://github.com/GuruprakashMP/photocatalysis-papers)
— same architecture, different scientific scope.

* **No papers are hosted.** Only bibliographic metadata (title, authors,
  journal, date, DOI, link); every card links to the original publisher.
* **Zero dependencies.** Standard-library Python; JSON + static HTML,
  perfect for GitHub Pages.
* **Fully automatic.** A GitHub Actions workflow collects, deduplicates,
  classifies, rebuilds the site and commits — every day.

## Quick start (local)

```bash
cd mechanochemistry_papers
# Windows:  set PYTHONPATH=src        PowerShell:  $env:PYTHONPATH="src"
export PYTHONPATH=src

python -m ddc run            # collect + rebuild the website
python -m ddc run --days 7   # look further back
python -m ddc backfill --from 1960   # historical harvest (year batches!)
python -m ddc build          # rebuild website only
python -m ddc stats          # index statistics
python -m unittest discover -s tests

python -m http.server 8761   # then open http://localhost:8761
```

The backfill starts at **1960** — the modern era of mechanochemistry, though
the field has deep roots (Faraday, Carey Lea, Ostwald). Run it in year-sized
ranges via the "Mechanochemistry historical backfill" GitHub Actions workflow:
OpenAlex allows roughly 15–20k record fetches per runner per day, and every
workflow run gets a fresh runner. Each run checkpoints, so interrupting and
re-running is safe.

## How papers are selected

A paper is indexed only when **mechanochemistry is its primary subject**,
evidenced by unambiguous vocabulary (mechanochem…, ball mill…, liquid-assisted
grinding, twin-screw extrusion, mechanoredox, mechanophore, tribochemistry,
mechanical alloying, ...). Supporting terms (mills, techniques, materials,
target reactions, in-situ monitoring, DFT, ML) refine the 0–100 relevance
score and assign multiple categories. Papers from neighbouring fields that
share the "mechano-" root (mechanobiology, mechanotransduction, cell/tissue
mechanics) or the word "grinding" (machining, grinding wheels) are penalised
out. Tune the vocabulary in `src/ddc/keywords.py`.

## Sources

Direct: **arXiv**, **ChemRxiv**. Aggregators: **Crossref**, **OpenAlex**,
**PubMed**, **Europe PMC**, **Semantic Scholar**, **DOAJ** — which legally
carry the metadata of every DOI-issuing publisher (ACS, RSC, Wiley, Springer
Nature, Elsevier, MDPI, ...).

## Deploying

1. Push this folder's contents to a public GitHub repository
   (e.g. `mechanochemistry-papers`).
2. **Settings → Pages → Deploy from a branch → `main` / root → Save.**
3. Live at `https://<user>.github.io/<repo>/` a minute later; the daily
   workflow keeps it growing with no maintenance.

See [ARCHITECTURE.md](ARCHITECTURE.md) for design decisions,
[PROJECT_STATUS.md](PROJECT_STATUS.md) for current state, and
[CHANGELOG.md](CHANGELOG.md) for history.

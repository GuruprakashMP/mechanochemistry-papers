"""Keyword knowledge base for classification.

Three vocabularies drive the relevance decision:

* ``PRIMARY_TERMS`` — mechanochemistry-specific vocabulary. A paper must show
  strong evidence here to be indexed at all: this is the project's core rule,
  *mechanochemistry as the primary subject* (ball milling, grinding, extrusion,
  mechanocatalysis, polymer mechanochemistry, tribochemistry...).
* ``SUPPORT_TERMS`` — mills, techniques, materials, reactions, monitoring,
  computational and data-driven methods that refine the score and assign
  categories.
* ``NEGATIVE_TERMS`` — signals the paper belongs to a neighbouring field that
  merely shares the "mechano-" root or the word "grinding": mechanobiology,
  mechanotransduction, cell/tissue/bone mechanics, machining and engine
  tribology.  ``penalty`` points.

Weights: 4 = unambiguous ("mechanochem…", "ball mill…", "mechanoredox"),
3 = strong, 2 = supportive, 1 = weak/generic.  Tags become the visible chips
on paper cards; categories group papers for browsing.

Note on scope calls (deliberate, see NEGATIVE_TERMS):
* "mechanical alloying" is IN scope (mechanochemical synthesis of alloys,
  high-entropy/amorphous/nanocrystalline materials by milling), so it is a
  PRIMARY term — only pure biology/machining neighbours are penalised.
* "mechanical properties" is NOT penalised: mechanochemically made materials
  routinely report them.
"""

from __future__ import annotations

from typing import Dict, Tuple

# ---------------------------------------------------------------------------
# Primary mechanochemistry terms — required evidence
# ---------------------------------------------------------------------------
PRIMARY_TERMS: Dict[str, Tuple[int, str, str]] = {
    # phrase: (weight, tag, category)
    # -- the core vocabulary ------------------------------------------------
    "mechanochem": (4, "Mechanochemistry", "General Mechanochemistry"),
    "mechano-chem": (4, "Mechanochemistry", "General Mechanochemistry"),
    "mechanosynthesis": (4, "Mechanosynthesis", "General Mechanochemistry"),
    "mechanosynthes": (4, "Mechanosynthesis", "General Mechanochemistry"),
    "mechanically induced": (4, "Mechanically Induced", "General Mechanochemistry"),
    "mechanically-induced": (4, "Mechanically Induced", "General Mechanochemistry"),
    "mechanically activated": (3, "Mechanical Activation", "Mechanism & Kinetics"),
    "mechanical activation": (3, "Mechanical Activation", "Mechanism & Kinetics"),
    # -- ball milling / grinding -------------------------------------------
    "ball mill": (4, "Ball Milling", "Ball Milling & Grinding"),
    "ball-mill": (4, "Ball Milling", "Ball Milling & Grinding"),
    "planetary ball mill": (4, "Planetary Ball Mill", "Ball Milling & Grinding"),
    "neat grinding": (4, "Neat Grinding", "Ball Milling & Grinding"),
    "solvent-free grinding": (4, "Solvent-Free Grinding", "Ball Milling & Grinding"),
    "solvent free grinding": (4, "Solvent-Free Grinding", "Ball Milling & Grinding"),
    "grinding synthesis": (4, "Grinding Synthesis", "Ball Milling & Grinding"),
    "grinding-induced": (4, "Grinding-Induced", "Ball Milling & Grinding"),
    "grinding induced": (4, "Grinding-Induced", "Ball Milling & Grinding"),
    "manual grinding": (3, "Manual Grinding", "Ball Milling & Grinding"),
    "mortar and pestle": (3, "Mortar & Pestle", "Ball Milling & Grinding"),
    # -- liquid-assisted grinding ------------------------------------------
    "liquid-assisted grinding": (4, "Liquid-Assisted Grinding", "Liquid-Assisted Grinding"),
    "liquid assisted grinding": (4, "Liquid-Assisted Grinding", "Liquid-Assisted Grinding"),
    "ion-and-liquid-assisted grinding": (4, "ILAG", "Liquid-Assisted Grinding"),
    "polymer-assisted grinding": (4, "POLAG", "Liquid-Assisted Grinding"),
    "seeding-assisted grinding": (4, "SEAG", "Liquid-Assisted Grinding"),
    # -- extrusion ----------------------------------------------------------
    "twin-screw extrusion": (4, "Twin-Screw Extrusion", "Twin-Screw Extrusion"),
    "twin screw extrusion": (4, "Twin-Screw Extrusion", "Twin-Screw Extrusion"),
    "reactive extrusion": (4, "Reactive Extrusion", "Twin-Screw Extrusion"),
    "single-screw extrusion": (3, "Screw Extrusion", "Twin-Screw Extrusion"),
    # -- catalysis / redox --------------------------------------------------
    "mechanocataly": (4, "Mechanocatalysis", "Mechanocatalysis & Mechanoredox"),
    "mechano-cataly": (4, "Mechanocatalysis", "Mechanocatalysis & Mechanoredox"),
    "mechanoredox": (4, "Mechanoredox", "Mechanocatalysis & Mechanoredox"),
    "mechano-redox": (4, "Mechanoredox", "Mechanocatalysis & Mechanoredox"),
    "piezocataly": (4, "Piezocatalysis", "Piezo- & Tribocatalysis"),
    "piezo-cataly": (4, "Piezocatalysis", "Piezo- & Tribocatalysis"),
    "piezoelectric cataly": (4, "Piezocatalysis", "Piezo- & Tribocatalysis"),
    "tribocataly": (4, "Tribocatalysis", "Piezo- & Tribocatalysis"),
    "triboelectrocataly": (4, "Triboelectrocatalysis", "Piezo- & Tribocatalysis"),
    "tribochem": (4, "Tribochemistry", "General Mechanochemistry"),
    # -- polymer mechanochemistry ------------------------------------------
    "mechanophore": (4, "Mechanophores", "Polymer Mechanochemistry & Mechanophores"),
    "mechanophor": (4, "Mechanophores", "Polymer Mechanochemistry & Mechanophores"),
    "polymer mechanochem": (4, "Polymer Mechanochemistry", "Polymer Mechanochemistry & Mechanophores"),
    "force-induced": (3, "Force-Induced", "Polymer Mechanochemistry & Mechanophores"),
    "mechanically triggered": (3, "Mechanically Triggered", "Polymer Mechanochemistry & Mechanophores"),
    "mechanoresponsive": (3, "Mechanoresponsive", "Polymer Mechanochemistry & Mechanophores"),
    "mechanofluorescen": (4, "Mechanofluorescence", "Polymer Mechanochemistry & Mechanophores"),
    "mechanoluminescen": (4, "Mechanoluminescence", "Polymer Mechanochemistry & Mechanophores"),
    # -- sonomechanochemistry ----------------------------------------------
    "sonomechanochem": (4, "Sonomechanochemistry", "Sonochemistry"),
    "sono-mechanochem": (4, "Sonomechanochemistry", "Sonochemistry"),
    # -- mechanical alloying (materials, in scope) -------------------------
    "mechanical alloying": (4, "Mechanical Alloying", "Mechanical Alloying & Materials"),
    "mechanically alloyed": (4, "Mechanical Alloying", "Mechanical Alloying & Materials"),
    "high-energy ball mill": (4, "High-Energy Milling", "Mechanical Alloying & Materials"),
    "high energy ball mill": (4, "High-Energy Milling", "Mechanical Alloying & Materials"),
}

# ---------------------------------------------------------------------------
# Support terms — mills, techniques, materials, reactions, monitoring, methods
# ---------------------------------------------------------------------------
SUPPORT_TERMS: Dict[str, Tuple[int, str, str]] = {
    # mills & equipment
    "planetary mill": (3, "Planetary Mill", "Ball Milling & Grinding"),
    "vibratory mill": (3, "Vibratory Mill", "Ball Milling & Grinding"),
    "vibration mill": (3, "Vibratory Mill", "Ball Milling & Grinding"),
    "vibratory ball mill": (3, "Vibratory Mill", "Ball Milling & Grinding"),
    "mixer mill": (3, "Mixer Mill", "Ball Milling & Grinding"),
    "shaker mill": (3, "Shaker Mill", "Ball Milling & Grinding"),
    "attritor": (3, "Attritor Mill", "Ball Milling & Grinding"),
    "milling frequency": (3, "Milling Parameters", "Ball Milling & Grinding"),
    "milling time": (2, "Milling Parameters", "Ball Milling & Grinding"),
    "milling speed": (2, "Milling Parameters", "Ball Milling & Grinding"),
    "rotation speed": (1, "Milling Parameters", "Ball Milling & Grinding"),
    "ball-to-powder": (3, "Ball-to-Powder Ratio", "Ball Milling & Grinding"),
    "grinding jar": (2, "Grinding Jar", "Ball Milling & Grinding"),
    "milling jar": (2, "Grinding Jar", "Ball Milling & Grinding"),
    "milling media": (2, "Milling Media", "Ball Milling & Grinding"),
    "grinding auxiliary": (3, "Grinding Auxiliary", "Liquid-Assisted Grinding"),
    "grinding": (2, "Grinding", "Ball Milling & Grinding"),
    "milling": (1, "Milling", "Ball Milling & Grinding"),
    "resonant acoustic mixing": (3, "Resonant Acoustic Mixing", "Reactor Engineering & Scale-up"),
    "resonance acoustic mixing": (3, "Resonant Acoustic Mixing", "Reactor Engineering & Scale-up"),
    # green / solvent-free
    "solvent-free": (3, "Solvent-Free", "Green & Solvent-Free Chemistry"),
    "solvent free synthesis": (3, "Solvent-Free", "Green & Solvent-Free Chemistry"),
    "solventless": (3, "Solvent-Free", "Green & Solvent-Free Chemistry"),
    "solid-state synthesis": (2, "Solid-State Synthesis", "General Mechanochemistry"),
    "solid state reaction": (2, "Solid-State Reaction", "General Mechanochemistry"),
    "green chemistry": (2, "Green Chemistry", "Green & Solvent-Free Chemistry"),
    "sustainable synthesis": (2, "Sustainable Synthesis", "Green & Solvent-Free Chemistry"),
    "green synthesis": (2, "Green Synthesis", "Green & Solvent-Free Chemistry"),
    "atom economy": (2, "Atom Economy", "Green & Solvent-Free Chemistry"),
    "e-factor": (2, "E-Factor", "Green & Solvent-Free Chemistry"),
    # cocrystals & pharmaceutical solids
    "cocrystal": (3, "Cocrystals", "Cocrystals & Pharmaceutical Solids"),
    "co-crystal": (3, "Cocrystals", "Cocrystals & Pharmaceutical Solids"),
    "cocrystallization": (3, "Cocrystallization", "Cocrystals & Pharmaceutical Solids"),
    "co-crystallization": (3, "Cocrystallization", "Cocrystals & Pharmaceutical Solids"),
    "pharmaceutical cocrystal": (3, "Pharmaceutical Cocrystals", "Cocrystals & Pharmaceutical Solids"),
    "crystal engineering": (2, "Crystal Engineering", "Cocrystals & Pharmaceutical Solids"),
    "polymorph": (2, "Polymorphism", "Cocrystals & Pharmaceutical Solids"),
    "amorphization": (2, "Amorphization", "Cocrystals & Pharmaceutical Solids"),
    "amorphisation": (2, "Amorphization", "Cocrystals & Pharmaceutical Solids"),
    "salt formation": (2, "Salt Formation", "Cocrystals & Pharmaceutical Solids"),
    "supramolecular": (1, "Supramolecular", "Cocrystals & Pharmaceutical Solids"),
    # frameworks
    "metal-organic framework": (3, "MOFs", "MOF & Framework Mechanosynthesis"),
    "metal organic framework": (3, "MOFs", "MOF & Framework Mechanosynthesis"),
    "coordination polymer": (2, "Coordination Polymers", "MOF & Framework Mechanosynthesis"),
    "covalent organic framework": (3, "COFs", "MOF & Framework Mechanosynthesis"),
    "zeolitic imidazolate framework": (3, "ZIFs", "MOF & Framework Mechanosynthesis"),
    "porous material": (1, "Porous Materials", "MOF & Framework Mechanosynthesis"),
    # organic mechanosynthesis
    "organic synthesis": (2, "Organic Synthesis", "Organic Mechanosynthesis"),
    "c-h functionalization": (2, "C-H Functionalization", "Organic Mechanosynthesis"),
    "cross-coupling": (2, "Cross-Coupling", "Organic Mechanosynthesis"),
    "suzuki": (2, "Suzuki Coupling", "Organic Mechanosynthesis"),
    "sonogashira": (2, "Sonogashira Coupling", "Organic Mechanosynthesis"),
    "knoevenagel": (2, "Knoevenagel", "Organic Mechanosynthesis"),
    "aldol": (2, "Aldol Reaction", "Organic Mechanosynthesis"),
    "amide bond": (2, "Amide Bond Formation", "Organic Mechanosynthesis"),
    "amide coupling": (2, "Amide Bond Formation", "Organic Mechanosynthesis"),
    "peptide synthesis": (2, "Peptide Synthesis", "Organic Mechanosynthesis"),
    "organocataly": (2, "Organocatalysis", "Organic Mechanosynthesis"),
    "asymmetric synthesis": (2, "Asymmetric Synthesis", "Organic Mechanosynthesis"),
    "click chemistry": (2, "Click Chemistry", "Organic Mechanosynthesis"),
    "heterocycle": (1, "Heterocycle Synthesis", "Organic Mechanosynthesis"),
    # catalysis
    "heterogeneous cataly": (2, "Heterogeneous Catalysis", "Mechanocatalysis & Mechanoredox"),
    "catalyst": (1, "Catalyst", "Mechanocatalysis & Mechanoredox"),
    "depolymerization": (2, "Depolymerization", "Mechanocatalysis & Mechanoredox"),
    "hydrogen storage": (2, "Hydrogen Storage", "Mechanical Alloying & Materials"),
    # piezo / tribo
    "piezoelectric": (2, "Piezoelectric", "Piezo- & Tribocatalysis"),
    "piezoelectric material": (2, "Piezoelectric", "Piezo- & Tribocatalysis"),
    "triboelectric": (2, "Triboelectric", "Piezo- & Tribocatalysis"),
    "contact electrification": (2, "Contact Electrification", "Piezo- & Tribocatalysis"),
    # sonochemistry
    "sonochem": (2, "Sonochemistry", "Sonochemistry"),
    "ultrasound": (2, "Ultrasound", "Sonochemistry"),
    "ultrasonic": (2, "Ultrasonic", "Sonochemistry"),
    "sonication": (2, "Sonication", "Sonochemistry"),
    "cavitation": (2, "Cavitation", "Sonochemistry"),
    # mechanical alloying & materials
    "high-entropy alloy": (2, "High-Entropy Alloys", "Mechanical Alloying & Materials"),
    "amorphous alloy": (2, "Amorphous Alloys", "Mechanical Alloying & Materials"),
    "nanocrystalline": (2, "Nanocrystalline", "Mechanical Alloying & Materials"),
    "nanostructured": (1, "Nanostructured", "Mechanical Alloying & Materials"),
    "nanoparticle": (1, "Nanoparticles", "Mechanical Alloying & Materials"),
    "metal powder": (2, "Metal Powders", "Mechanical Alloying & Materials"),
    "powder metallurgy": (2, "Powder Metallurgy", "Mechanical Alloying & Materials"),
    "perovskite": (1, "Perovskites", "Mechanical Alloying & Materials"),
    "battery material": (1, "Battery Materials", "Mechanical Alloying & Materials"),
    # in-situ monitoring
    "in situ": (1, "In-Situ", "In-Situ Monitoring"),
    "in-situ": (1, "In-Situ", "In-Situ Monitoring"),
    "in situ pxrd": (3, "In-Situ PXRD", "In-Situ Monitoring"),
    "in-situ pxrd": (3, "In-Situ PXRD", "In-Situ Monitoring"),
    "in situ x-ray diffraction": (3, "In-Situ PXRD", "In-Situ Monitoring"),
    "in-situ raman": (3, "In-Situ Raman", "In-Situ Monitoring"),
    "in situ raman": (3, "In-Situ Raman", "In-Situ Monitoring"),
    "time-resolved": (2, "Time-Resolved", "In-Situ Monitoring"),
    "synchrotron": (2, "Synchrotron", "In-Situ Monitoring"),
    "powder x-ray diffraction": (2, "PXRD", "In-Situ Monitoring"),
    "pxrd": (2, "PXRD", "In-Situ Monitoring"),
    "raman spectroscopy": (1, "Raman", "In-Situ Monitoring"),
    "real-time monitoring": (2, "Real-Time Monitoring", "In-Situ Monitoring"),
    # mechanism & kinetics
    "milling-induced": (3, "Milling-Induced", "Mechanism & Kinetics"),
    "milling induced": (3, "Milling-Induced", "Mechanism & Kinetics"),
    "reaction kinetics": (1, "Reaction Kinetics", "Mechanism & Kinetics"),
    "shear force": (2, "Shear Force", "Mechanism & Kinetics"),
    "impact energy": (2, "Impact Energy", "Mechanism & Kinetics"),
    "hot spot": (1, "Hot Spots", "Mechanism & Kinetics"),
    "reaction mechanism": (1, "Reaction Mechanism", "Mechanism & Kinetics"),
    "phase transformation": (1, "Phase Transformation", "Mechanism & Kinetics"),
    # engineering / scale-up
    "scale-up": (2, "Scale-up", "Reactor Engineering & Scale-up"),
    "continuous manufacturing": (2, "Continuous Manufacturing", "Reactor Engineering & Scale-up"),
    "extrusion": (2, "Extrusion", "Twin-Screw Extrusion"),
    "process intensification": (2, "Process Intensification", "Reactor Engineering & Scale-up"),
    "kilogram scale": (2, "Kilogram Scale", "Reactor Engineering & Scale-up"),
    # computational & data-driven
    "dft": (2, "DFT", "Computational & Data-Driven"),
    "density functional": (2, "DFT", "Computational & Data-Driven"),
    "first-principles": (2, "First-Principles", "Computational & Data-Driven"),
    "ab initio": (2, "Ab Initio", "Computational & Data-Driven"),
    "molecular dynamics": (2, "Molecular Dynamics", "Computational & Data-Driven"),
    "reaxff": (2, "ReaxFF", "Computational & Data-Driven"),
    "discrete element": (2, "Discrete Element Method", "Computational & Data-Driven"),
    "machine learning": (2, "Machine Learning", "Computational & Data-Driven"),
    "deep learning": (2, "Deep Learning", "Computational & Data-Driven"),
    "high-throughput": (2, "High-Throughput", "Computational & Data-Driven"),
}

# ---------------------------------------------------------------------------
# Negative signals — neighbouring fields that merely share the "mechano-"
# root or the word "grinding".  Kept deliberately narrow: mechanical alloying
# and mechanical properties of materials are IN scope and never penalised.
# ---------------------------------------------------------------------------
NEGATIVE_TERMS: Dict[str, int] = {
    # biology / physiology
    "mechanobiolog": 12,
    "mechanotransduction": 12,
    "mechanoreceptor": 12,
    "mechanosensitive": 10,
    "mechanosensing": 10,
    "mechanosensor": 10,
    "biomechanic": 12,
    "cell mechanic": 10,
    "cellular mechanic": 10,
    "tissue mechanic": 10,
    "bone mechanic": 8,
    "cardiac mechanic": 10,
    "cytoskeleton": 8,
    "extracellular matrix": 6,
    "muscle contraction": 8,
    # the "mechanochemical sensor/signalling" of mechanobiology (a single
    # incidental "mechanochemical" in an otherwise biological abstract)
    "mechanochemical sensor": 8,
    "mechanochemical signal": 8,
    "glycocalyx": 10,
    "viral entry": 10,
    "viral infection": 8,
    "virus infection": 8,
    "immune synapse": 10,
    "tissue homeostasis": 8,
    # engineering machining / engine tribology (not chemistry)
    "machining": 8,
    "metal cutting": 8,
    "grinding wheel": 10,
    "surface grinding": 8,
    "combustion engine": 8,
    "engine wear": 8,
    "gear box": 8,
    "fracture mechanics": 6,
    # food / mineral comminution only (size reduction, no reaction)
    "flour milling": 8,
    "wind mill": 8,
}

# Journal-name fragments indicating a relevant venue (score bonus).
CHEM_VENUE_HINTS = (
    "chem", "cryst", "mater", "catal", "green", "powder", "metall",
    "solid", "nano", "molecul", "sustain", "react", "polym", "faraday",
    "beilstein", "milling", "alloy",
)

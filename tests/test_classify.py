"""Tests for the core filtering rule: mechanochemistry as the primary subject."""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from ddc.classify import classify  # noqa: E402
from ddc.models import RawRecord  # noqa: E402


def record(title: str, abstract: str = "", journal: str = "") -> RawRecord:
    return RawRecord(title=title, abstract=abstract, journal=journal, source="test")


class TestClassify(unittest.TestCase):
    def test_accepts_experimental_ball_milling(self):
        r = record(
            "Mechanochemical synthesis of a metal-organic framework by ball milling",
            "Solvent-free ball milling in a planetary mill yields the MOF; "
            "in-situ PXRD monitors the reaction.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertGreaterEqual(verdict.score, 80)
        self.assertIn("Ball Milling & Grinding", verdict.categories)
        self.assertIn("MOF & Framework Mechanosynthesis", verdict.categories)

    def test_accepts_liquid_assisted_grinding_cocrystal(self):
        r = record(
            "Liquid-assisted grinding synthesis of pharmaceutical cocrystals",
            "Neat grinding and liquid-assisted grinding in a mixer mill afford "
            "the cocrystal; polymorph screening by PXRD.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Liquid-Assisted Grinding", verdict.categories)
        self.assertIn("Cocrystals & Pharmaceutical Solids", verdict.categories)

    def test_accepts_twin_screw_extrusion(self):
        r = record(
            "Continuous mechanochemical synthesis by twin-screw extrusion",
            "Reactive extrusion enables solvent-free, kilogram-scale production "
            "of the coordination polymer.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Twin-Screw Extrusion", verdict.categories)

    def test_accepts_mechanoredox(self):
        r = record(
            "Mechanoredox catalysis via piezoelectric activation",
            "Ball milling with a piezoelectric material drives single-electron "
            "transfer for arylation reactions.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Mechanocatalysis & Mechanoredox", verdict.categories)

    def test_accepts_polymer_mechanophore(self):
        r = record(
            "A force-responsive mechanophore for polymer mechanochemistry",
            "Mechanically triggered ring-opening reports on stress in the "
            "polymer network.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Polymer Mechanochemistry & Mechanophores", verdict.categories)

    def test_accepts_mechanical_alloying_in_scope(self):
        # Deliberate scope call: mechanical alloying of materials is IN scope.
        r = record(
            "Mechanical alloying of high-entropy alloys by high-energy ball milling",
            "Nanocrystalline high-entropy alloys form during high-energy ball "
            "milling; phase transformation studied by XRD.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Mechanical Alloying & Materials", verdict.categories)

    def test_accepts_dft_mechanochemistry(self):
        r = record(
            "Molecular dynamics of mechanochemical bond scission",
            "ReaxFF simulations reveal force-induced C-C bond cleavage during "
            "ball milling.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Computational & Data-Driven", verdict.categories)

    def test_accepts_sonomechanochemistry(self):
        r = record(
            "Sonomechanochemistry of polymer solutions",
            "Ultrasound-induced cavitation drives mechanochemical chain "
            "scission of polymers.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Sonochemistry", verdict.categories)

    def test_rejects_mechanobiology(self):
        r = record(
            "Mechanotransduction and mechanobiology of stem cells",
            "Cellular mechanics and cytoskeleton dynamics govern "
            "mechanosensitive signaling in tissue.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_mechanobiology_incidental_mechanochemical(self):
        # A biology abstract that says "mechanochemical sensor" once must not
        # clear the bar on that single incidental mention.
        r = record(
            "Glycocalyx at the host-virus interface in viral infection",
            "The glycocalyx acts as a mechanochemical sensor integrating cues "
            "to coordinate tissue homeostasis during viral entry and immune "
            "synapse formation.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_machining(self):
        r = record(
            "Surface grinding and machining of hardened steel",
            "Grinding wheel wear during metal cutting and surface grinding of "
            "engine components.")
        self.assertFalse(classify(r).accepted)

    def test_rejects_thermal_solid_state(self):
        # Solid-state synthesis alone (thermal, no milling) is not mechanochemistry.
        r = record(
            "Thermal solid-state synthesis of oxide ceramics",
            "High-temperature calcination produces the perovskite oxide.")
        self.assertFalse(classify(r).accepted)

    def test_rejects_generic_organic_synthesis(self):
        r = record(
            "Palladium-catalyzed Suzuki cross-coupling in solution",
            "Aryl halides couple with boronic acids in refluxing THF.")
        self.assertFalse(classify(r).accepted)

    def test_venue_boosts_score(self):
        base = record("Ball milling synthesis of a cocrystal",
                      "Solvent-free ball milling affords the cocrystal.")
        boosted = record("Ball milling synthesis of a cocrystal",
                         "Solvent-free ball milling affords the cocrystal.",
                         journal="CrystEngComm")
        self.assertGreater(classify(boosted).score, classify(base).score)

    def test_empty_title_rejected(self):
        self.assertFalse(classify(record("")).accepted)

    def test_score_bounds(self):
        r = record(
            "Mechanochemical liquid-assisted grinding synthesis of a framework "
            "by twin-screw extrusion",
            "solvent-free ball milling planetary mill in-situ pxrd cocrystal "
            "mechanoredox mechanophore piezocatalysis metal-organic framework")
        verdict = classify(r)
        self.assertLessEqual(verdict.score, 100)
        self.assertGreaterEqual(verdict.score, 90)


if __name__ == "__main__":
    unittest.main()

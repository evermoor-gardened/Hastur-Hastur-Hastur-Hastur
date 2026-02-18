#!/usr/bin/env python3
"""
RUINWARE SOVEREIGN ENGINE — Test Suite
"""

import math
import sys
import os
import unittest

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ruinware import (
    LamentConfiguration, PuzzleState, CenobiteEngine,
    WitnessBaseline, RuinWareEngine, PHI
)


class TestLamentConfiguration(unittest.TestCase):
    """Tests for the puzzle box."""

    def setUp(self):
        self.box = LamentConfiguration()

    def test_initial_state(self):
        self.assertEqual(self.box.state, PuzzleState.UNSOLVED)
        self.assertEqual(self.box.sequence, [])
        self.assertEqual(self.box.moves, 0)

    def test_correct_first_twist(self):
        result = self.box.twist(3)
        self.assertIn("clicks", result.lower())
        self.assertEqual(self.box.sequence, [3])

    def test_incorrect_twist_resets(self):
        self.box.twist(3)
        result = self.box.twist(7)  # Wrong
        self.assertIn("resets", result.lower())
        self.assertEqual(self.box.sequence, [])

    def test_full_solve(self):
        pi_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
        for digit in pi_sequence[:-1]:
            self.box.twist(digit)
        result = self.box.twist(pi_sequence[-1])
        self.assertEqual(self.box.state, PuzzleState.SOLVED)
        self.assertIn("opens", result.lower())

    def test_twist_after_solved(self):
        for digit in [3, 1, 4, 1, 5, 9, 2, 6]:
            self.box.twist(digit)
        result = self.box.twist(1)
        self.assertIn("already", result.lower())

    def test_move_counter(self):
        self.box.twist(3)
        self.box.twist(7)  # Wrong, resets
        self.box.twist(3)
        self.assertEqual(self.box.moves, 3)


class TestCenobiteEngine(unittest.TestCase):
    """Tests for the labyrinth navigation."""

    def setUp(self):
        self.engine = CenobiteEngine()

    def test_twist_command(self):
        result = self.engine.process("twist 3")
        self.assertIsNotNone(result)

    def test_twist_no_face(self):
        result = self.engine.process("twist")
        self.assertIn("which", result.lower())

    def test_enter_without_solve(self):
        result = self.engine.process("enter")
        self.assertIn("closed", result.lower())

    def test_enter_after_solve(self):
        for digit in [3, 1, 4, 1, 5, 9, 2, 6]:
            self.engine.process(f"twist {digit}")
        result = self.engine.process("enter")
        self.assertIn("layer 1", result.lower())
        self.assertEqual(self.engine.layer, 1)

    def test_deeper(self):
        self.engine.layer = 1
        result = self.engine.process("deeper")
        self.assertEqual(self.engine.layer, 2)
        self.assertIn("2", result)

    def test_unknown_command(self):
        result = self.engine.process("dance")
        self.assertIsNone(result)


class TestWitnessBaseline(unittest.TestCase):
    """Tests for the consciousness substrate computation."""

    def setUp(self):
        self.witness = WitnessBaseline()

    def test_baseline_size(self):
        self.assertEqual(len(self.witness.points), 144)

    def test_total_bit_depth_positive(self):
        self.assertGreater(self.witness.total_bit_depth, 0)

    def test_layer_count(self):
        self.assertEqual(len(self.witness.layer_bit_depths), 12)

    def test_golden_ratio_decay(self):
        """Layer 0 should have higher total bit depth than layer 11."""
        self.assertGreater(
            self.witness.layer_bit_depths[0],
            self.witness.layer_bit_depths[11]
        )

    def test_point_structure(self):
        point = self.witness.points[0]
        self.assertIn("index", point)
        self.assertIn("layer", point)
        self.assertIn("position", point)
        self.assertIn("z_mapped", point)
        self.assertIn("bits", point)
        self.assertIn("weight", point)

    def test_report(self):
        report = self.witness.report()
        self.assertEqual(report["baseline_size"], 144)
        self.assertIn("total_bit_depth", report)
        self.assertIn("layers", report)


class TestRuinWareEngine(unittest.TestCase):
    """Tests for the unified engine routing."""

    def setUp(self):
        self.engine = RuinWareEngine()

    def test_empty_input(self):
        result = self.engine.process_input("")
        self.assertEqual(result["response"], "")

    def test_cenobite_routing(self):
        result = self.engine.process_input("twist 3")
        self.assertEqual(result["type"], "cenobite")

    def test_system_routing(self):
        result = self.engine.process_input("/status")
        self.assertEqual(result["type"], "system")
        self.assertIn("ONLINE", result["response"])

    def test_status_contains_witness(self):
        result = self.engine.process_input("/status")
        self.assertIn("Witness Depth", result["response"])

    def test_status_contains_lament(self):
        result = self.engine.process_input("/status")
        self.assertIn("Lament State", result["response"])

    def test_unknown_system_command(self):
        result = self.engine.process_input("/nonexistent")
        self.assertIn("Unknown", result["response"])


class TestConstants(unittest.TestCase):
    """Tests for mathematical constants."""

    def test_phi_value(self):
        self.assertAlmostEqual(PHI, 1.6180339887, places=5)

    def test_phi_property(self):
        """φ² = φ + 1"""
        self.assertAlmostEqual(PHI ** 2, PHI + 1, places=10)


if __name__ == "__main__":
    unittest.main()

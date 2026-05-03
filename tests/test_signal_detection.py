import unittest
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from signal_detection import SignalDetection


class TestSignalDetectionMath(unittest.TestCase):
    def test_hit_rate_normal_case(self):
        sd = SignalDetection(8, 2, 1, 9)
        self.assertAlmostEqual(sd.hit_rate(), 0.8, places=7)


class TestSignalDetectionValidation(unittest.TestCase):
    def test_invalid_negative_counts(self):
        with self.assertRaises(Exception):
            SignalDetection(-1, 2, 1, 9)


class TestSignalDetectionOperators(unittest.TestCase):
    def test_add_returns_combined_counts(self):
        sd1 = SignalDetection(8, 2, 1, 9)
        sd2 = SignalDetection(1, 3, 4, 2)
        result = sd1 + sd2
        self.assertEqual(result.hits, 9)
        self.assertEqual(result.misses, 5)
        self.assertEqual(result.false_alarms, 5)
        self.assertEqual(result.correct_rejections, 11)


class TestSignalDetectionPlotting(unittest.TestCase):
    def test_plot_roc_runs_without_error(self):
        sd = SignalDetection(8, 2, 1, 9)
        SignalDetection.plot_roc([sd])
        plt.close("all")


if __name__ == "__main__":
    unittest.main()


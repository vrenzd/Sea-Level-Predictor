import unittest
import sea_level_predictor
import numpy as np


class LinePlotTestCase(unittest.TestCase):

    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        self.assertEqual(self.ax.get_title(), "Rise in Sea Level")

    def test_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Year")
        self.assertEqual(self.ax.get_ylabel(), "Sea Level (inches)")

    def test_xticks(self):
        expected = [
            1850.0, 1875.0, 1900.0, 1925.0, 1950.0,
            1975.0, 2000.0, 2025.0, 2050.0, 2075.0
        ]
        self.assertEqual(self.ax.get_xticks().tolist(), expected)

    def test_first_best_fit_line_length(self):
        actual = len(self.ax.get_lines()[0].get_ydata())
        expected = 171
        self.assertEqual(actual, expected)

    def test_second_best_fit_line_length(self):
        actual = len(self.ax.get_lines()[1].get_ydata())
        expected = 51
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

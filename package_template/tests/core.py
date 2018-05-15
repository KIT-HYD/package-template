import unittest

import numpy as np
import pandas as pd
from numpy.testing import assert_almost_equal

from package_template import mymodel

KDE_DENSITY = np.array(
    [0.002, 0.01, 0.049, 0.11, 0.191, 0.213, 0.184, 0.121, 0.068,
     0.035, 0.013, 0.003, 0., 0., 0.002])

H_DENSITY = np.array([0.004, 0.016, 0.064, 0.12, 0.184, 0.21, 0.166, 0.124,
                      0.06, 0.032, 0.014, 0.004, 0., 0., 0.002])


class TestMyModel(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.array = np.random.gamma(40, 3, 500)

    def test_kde_from_array(self):
        assert_almost_equal(
            mymodel(self.array),
            KDE_DENSITY,
            decimal=3
        )

    def test_hist_from_array(self):
        assert_almost_equal(
            mymodel(self.array, kind='hist'),
            H_DENSITY,
            decimal=3
        )

    def test_series(self):
        series = pd.Series(data=self.array)
        assert_almost_equal(
            mymodel(series),
            KDE_DENSITY,
            decimal=3
        )

    def test_non_array_input(self):
        with self.assertRaises(ValueError) as error:
            mymodel(['list', 'is', 'not', 'allowed'])
        self.assertEqual(
            str(error.exception),
            'Please use a numpy array or pandas Series as input'
        )

    def test_with_negative_bin(self):
        with self.assertRaises(ValueError) as error:
            mymodel(self.array, bins=-5)
        self.assertEqual(
            str(error.exception),
            'bins has to be a positive integer'
        )

    def test_use_unkonwn_kind(self):
        with self.assertRaises(ValueError) as error:
            mymodel(self.array, kind='not known')
        self.assertEqual(
            str(error.exception),
            "kind has to be one of 'kde', 'hist'"
        )


if __name__ == '__main__':
    unittest.main()

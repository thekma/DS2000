import unittest
import sys

from textwrap import dedent
from subprocess import run as run_process, PIPE

from importlib import import_module
from contextlib import redirect_stdout
from io import StringIO

def input_output_test(f_name, in_str):
    completed = run_process(
        [sys.executable, '-B', f_name], input=in_str, stdout=PIPE, stderr=PIPE, universal_newlines=True
    )
    return completed.returncode, completed.stdout

_imported = {}

def load_module(mod_name):
    global _imported

    if mod_name in _imported:
        return _imported[mod_name]

    stdout = StringIO()
    m = None
    with redirect_stdout(stdout):
        m = import_module(mod_name)
    actual_output = stdout.getvalue()

    _imported[mod_name] = (m, actual_output=='')
    return _imported[mod_name]


class TestAssignment(unittest.TestCase):

    def test_myabs(self):
        nn,clean = load_module('nn')
        self.assertIsNotNone(nn, 'Cannot find module :(')

        self.assertEqual(nn.myabs(-5), 5)
        self.assertAlmostEqual(nn.myabs(-100.1), 100.1, delta=0.0001)
        self.assertEqual(nn.myabs(0), 0)

        self.assertEqual(nn.myabs(11), 11)
        self.assertAlmostEqual(nn.myabs(200.4), 200.4, delta=0.0001)

    def test_mymanhattan(self):
        nn,clean = load_module('nn')
        self.assertIsNotNone(nn, 'Cannot find module :(')

        self.assertEqual(nn.mymanhattan([0, 0], [0, 0]), 0)
        self.assertEqual(nn.mymanhattan([1, 1], [1, 1]), 0)
        self.assertEqual(nn.mymanhattan([2, 2, 2], [2, 2, 2]), 0)
        self.assertEqual(nn.mymanhattan([1, -2, 3, -4, 6], [1, -2, 3, -4, 6]), 0)

        self.assertEqual(nn.mymanhattan([0, 0], [3, 4]), 7)
        self.assertEqual(nn.mymanhattan([0, 0, 0], [1, 2, 3]), 6)
        self.assertEqual(nn.mymanhattan([0, 0, 0], [-1, -2, -3]), 6)
        self.assertEqual(nn.mymanhattan([1, 4, 7, 0], [-3, 4, 20, 1]), 18)
        self.assertEqual(nn.mymanhattan([1, 4, 7, 1], [-3, 4, 20, 1]), 17)

    def test_myhamming(self):
        nn,clean = load_module('nn')
        self.assertIsNotNone(nn, 'Cannot find module :(')

        self.assertEqual(nn.myhamming([0, 0], [0, 0]), 0)
        self.assertEqual(nn.myhamming([1, 1], [1, 1]), 0)
        self.assertEqual(nn.myhamming([2, 2, 2], [2, 2, 2]), 0)
        self.assertEqual(nn.myhamming([1, -2, 3, -4, 6], [1, -2, 3, -4, 6]), 0)

        self.assertEqual(nn.myhamming([0, 0], [3, 4]), 2)
        self.assertEqual(nn.myhamming([0, 0, 0], [1, 2, 3]), 3)
        self.assertEqual(nn.myhamming([0, 0, 0], [-1, -2, -3]), 3)
        self.assertEqual(nn.myhamming([1, 4, 7, 0], [-3, 4, 20, 1]), 3)
        self.assertEqual(nn.myhamming([1, 4, 7, 1], [-3, 4, 20, 1]), 2)

    def test_myeuclidean(self):
        nn,clean = load_module('nn')
        self.assertIsNotNone(nn, 'Cannot find module :(')

        self.assertEqual(nn.myeuclidean([0, 0], [0, 0]), 0)
        self.assertEqual(nn.myeuclidean([1, 1], [1, 1]), 0)
        self.assertEqual(nn.myeuclidean([2, 2, 2], [2, 2, 2]), 0)
        self.assertEqual(nn.myeuclidean([1, -2, 3, -4, 6], [1, -2, 3, -4, 6]), 0)

        self.assertAlmostEqual(nn.myeuclidean([0, 0], [3, 4]), 5, delta=0.0001)
        self.assertAlmostEqual(nn.myeuclidean([0, 0, 0], [1, 2, 3]), 3.741657, delta=0.0001)
        self.assertAlmostEqual(nn.myeuclidean([0, 0, 0], [-1, -2, -3]), 3.741657, delta=0.0001)
        self.assertAlmostEqual(nn.myeuclidean([1, 4, 7, 0], [-3, 4, 20, 1]), 13.638182, delta=0.0001)
        self.assertAlmostEqual(nn.myeuclidean([1, 4, 7, 1], [-3, 4, 20, 1]), 13.601471, delta=0.0001)

    def test_nearestneighbor(self):
        nn,clean = load_module('nn')
        self.assertIsNotNone(nn, 'Cannot find module :(')

        lonely = [
            ["me", [0, 1]],
        ]

        triangle = [
            ["top", [0, 1]],
            ["bottom-left", [0, 0]],
            ["bottom-right", [2, 0]],
        ]

        # [takes-reservations, has-veg, wifi, delivery, takeout]
        restaurants = [
            ["Toscanini's", [0, 1, 1, 0, 1]],
            ["McDonald's",  [0, 1, 0, 0, 1]],
            ["B.GOOD",      [0, 1, 1, 1, 1]],
            ["Uno",         [1, 1, 1, 0, 1]],
        ]

        # https://en.wikipedia.org/wiki/Iris_flower_data_set
        # sepal-length, sepal-width, petal-length, petal-width
        iris = [
            ["setosa", [4.9, 3.0, 1.4, 0.2]],
            ["setosa", [5.1, 3.5, 1.4, 0.2]],
            ["versicolor", [7.0, 3.2, 4.7, 1.4]],
            ["versicolor", [6.4, 3.2, 4.5, 1.5]],
            ["virginica", [6.3, 3.3, 6.0, 2.5]],
            ["virginica", [5.8, 2.7, 5.1, 1.9]],
        ]

        self.assertEqual(nn.nearestneighbor([0, 0], lonely, nn.myhamming), "me")
        self.assertEqual(nn.nearestneighbor([0, 0], lonely, nn.mymanhattan), "me")
        self.assertEqual(nn.nearestneighbor([0, 0], lonely, nn.myeuclidean), "me")

        self.assertEqual(nn.nearestneighbor([0, 0.6], triangle, nn.myhamming), "top")
        self.assertEqual(nn.nearestneighbor([0, 0.6], triangle, nn.mymanhattan), "top")
        self.assertEqual(nn.nearestneighbor([0, 0.6], triangle, nn.myeuclidean), "top")

        self.assertEqual(nn.nearestneighbor([0, 0.4], triangle, nn.myhamming), "top")
        self.assertEqual(nn.nearestneighbor([0, 0.4], triangle, nn.mymanhattan), "bottom-left")
        self.assertEqual(nn.nearestneighbor([0, 0.4], triangle, nn.myeuclidean), "bottom-left")

        self.assertEqual(nn.nearestneighbor([1.9, 1], triangle, nn.myhamming), "top")
        self.assertEqual(nn.nearestneighbor([1.9, 1], triangle, nn.mymanhattan), "bottom-right")
        self.assertEqual(nn.nearestneighbor([1.9, 1], triangle, nn.myeuclidean), "bottom-right")

        self.assertEqual(nn.nearestneighbor([1, 0, 1, 0, 0], restaurants, nn.myhamming), "Uno")

        self.assertEqual(nn.nearestneighbor([5.0, 3.3, 1.4, 0.2], iris, nn.myeuclidean), "setosa")
        self.assertEqual(nn.nearestneighbor([5.7, 2.8, 4.1, 1.3], iris, nn.myeuclidean), "versicolor")
        self.assertEqual(nn.nearestneighbor([5.9, 3.0, 5.1, 1.8], iris, nn.myeuclidean), "virginica")

if __name__ == '__main__':
    unittest.main(verbosity=2)

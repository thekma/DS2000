import unittest
import sys
import random

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

    def test_data_generate_center(self):
        kd,clean = load_module('kmeans_data')
        self.assertIsNotNone(kd, 'Cannot find module :(')

        centers1 = [[1, 1],]
        centers2 = [[1, 1],[2,2],]
        centers3 = [[1, 1],[2,2],[3,3],]
        centers4 = [[1, 1],[2,2],[3,3],[4,4],]

        random.seed(8675)
        self.assertEqual(kd.generate_center(centers1), 0)
        self.assertEqual(kd.generate_center(centers1), 0)
        self.assertEqual(kd.generate_center(centers1), 0)
        self.assertEqual(kd.generate_center(centers1), 0)
        self.assertEqual(kd.generate_center(centers1), 0)

        random.seed(309)
        self.assertEqual(kd.generate_center(centers1), 0)
        self.assertEqual(kd.generate_center(centers1), 0)
        self.assertEqual(kd.generate_center(centers1), 0)
        self.assertEqual(kd.generate_center(centers1), 0)
        self.assertEqual(kd.generate_center(centers1), 0)

        #

        random.seed(8675)
        self.assertEqual(kd.generate_center(centers2), 0)
        self.assertEqual(kd.generate_center(centers2), 0)
        self.assertEqual(kd.generate_center(centers2), 1)
        self.assertEqual(kd.generate_center(centers2), 1)
        self.assertEqual(kd.generate_center(centers2), 0)

        random.seed(309)
        self.assertEqual(kd.generate_center(centers2), 0)
        self.assertEqual(kd.generate_center(centers2), 1)
        self.assertEqual(kd.generate_center(centers2), 0)
        self.assertEqual(kd.generate_center(centers2), 0)
        self.assertEqual(kd.generate_center(centers2), 0)

        #

        random.seed(8675)
        self.assertEqual(kd.generate_center(centers3), 2)
        self.assertEqual(kd.generate_center(centers3), 0)
        self.assertEqual(kd.generate_center(centers3), 2)
        self.assertEqual(kd.generate_center(centers3), 0)
        self.assertEqual(kd.generate_center(centers3), 2)

        random.seed(309)
        self.assertEqual(kd.generate_center(centers3), 0)
        self.assertEqual(kd.generate_center(centers3), 1)
        self.assertEqual(kd.generate_center(centers3), 0)
        self.assertEqual(kd.generate_center(centers3), 0)
        self.assertEqual(kd.generate_center(centers3), 0)

        #

        random.seed(8675)
        self.assertEqual(kd.generate_center(centers4), 1)
        self.assertEqual(kd.generate_center(centers4), 1)
        self.assertEqual(kd.generate_center(centers4), 3)
        self.assertEqual(kd.generate_center(centers4), 3)
        self.assertEqual(kd.generate_center(centers4), 0)

        random.seed(309)
        self.assertEqual(kd.generate_center(centers4), 0)
        self.assertEqual(kd.generate_center(centers4), 2)
        self.assertEqual(kd.generate_center(centers4), 0)
        self.assertEqual(kd.generate_center(centers4), 1)
        self.assertEqual(kd.generate_center(centers4), 1)

    def _test_coordinate(self, result, expected):
        self.assertEqual(type(result), float)
        self.assertEqual(str(result), expected)

    def test_data_generate_coordinate(self):
        kd,clean = load_module('kmeans_data')
        self.assertIsNotNone(kd, 'Cannot find module :(')

        m1 = -18
        m2 = 0.1

        stdev1 = 1
        stdev2 = 3.2

        p1 = 2
        p2 = 3

        #

        random.seed(8675)
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p1), "-18.69")
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p1), "-19.05")
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p1), "-16.41")

        random.seed(8675)
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p2), "-18.695")
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p2), "-19.052")
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p2), "-16.41")

        random.seed(309)
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p1), "-17.97")
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p1), "-17.99")
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p1), "-17.31")

        random.seed(309)
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p2), "-17.973")
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p2), "-17.989")
        self._test_coordinate(kd.generate_coordinate(m1, stdev1, p2), "-17.309")

        random.seed(8675)
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p1), "-20.22")
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p1), "-21.37")
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p1), "-12.91")

        random.seed(8675)
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p2), "-20.223")
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p2), "-21.368")
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p2), "-12.911")

        random.seed(309)
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p1), "-17.91")
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p1), "-17.96")
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p1), "-15.79")

        random.seed(309)
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p2), "-17.914")
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p2), "-17.964")
        self._test_coordinate(kd.generate_coordinate(m1, stdev2, p2), "-15.789")

        #

        random.seed(8675)
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p1), "-0.59")
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p1), "-0.95")
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p1), "1.69")

        random.seed(8675)
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p2), "-0.595")
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p2), "-0.952")
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p2), "1.69")

        random.seed(309)
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p1), "0.13")
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p1), "0.11")
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p1), "0.79")

        random.seed(309)
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p2), "0.127")
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p2), "0.111")
        self._test_coordinate(kd.generate_coordinate(m2, stdev1, p2), "0.791")

        random.seed(8675)
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p1), "-2.12")
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p1), "-3.27")
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p1), "5.19")

        random.seed(8675)
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p2), "-2.123")
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p2), "-3.268")
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p2), "5.189")

        random.seed(309)
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p1), "0.19")
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p1), "0.14")
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p1), "2.31")

        random.seed(309)
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p2), "0.186")
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p2), "0.136")
        self._test_coordinate(kd.generate_coordinate(m2, stdev2, p2), "2.311")

    def test_data_biggestsmallest(self):
        kd,clean = load_module('kmeans_data')
        self.assertIsNotNone(kd, 'Cannot find module :(')

        dataset1 = [
            [1, 2, 3],
        ]

        dataset2 = [
            [1, 2, 3, 5],
            [-1, 2, 4, 4],
        ]

        dataset4 = [
            [100, 200],
            [300, 0],
            [300, -1],
            [400, 100],
        ]

        self.assertEqual(kd.biggestsmallest(dataset1, 0, False), 1)
        self.assertEqual(kd.biggestsmallest(dataset1, 0, True), 1)
        self.assertEqual(kd.biggestsmallest(dataset1, 1, False), 2)
        self.assertEqual(kd.biggestsmallest(dataset1, 1, True), 2)
        self.assertEqual(kd.biggestsmallest(dataset1, 2, False), 3)
        self.assertEqual(kd.biggestsmallest(dataset1, 2, True), 3)

        self.assertEqual(kd.biggestsmallest(dataset2, 0, False), -1)
        self.assertEqual(kd.biggestsmallest(dataset2, 0, True), 1)
        self.assertEqual(kd.biggestsmallest(dataset2, 1, False), 2)
        self.assertEqual(kd.biggestsmallest(dataset2, 1, True), 2)
        self.assertEqual(kd.biggestsmallest(dataset2, 2, False), 3)
        self.assertEqual(kd.biggestsmallest(dataset2, 2, True), 4)
        self.assertEqual(kd.biggestsmallest(dataset2, 3, False), 4)
        self.assertEqual(kd.biggestsmallest(dataset2, 3, True), 5)

        self.assertEqual(kd.biggestsmallest(dataset4, 0, False), 100)
        self.assertEqual(kd.biggestsmallest(dataset4, 0, True), 400)
        self.assertEqual(kd.biggestsmallest(dataset4, 1, False), -1)
        self.assertEqual(kd.biggestsmallest(dataset4, 1, True), 200)

    def test_data_numstring_to_lol(self):
        kd,clean = load_module('kmeans_data')
        self.assertIsNotNone(kd, 'Cannot find module :(')

        str4 = "1 2.2 3 4.0"
        str6 = "-1 202 303 40.4 5.05 6"

        self.assertEqual(kd.numstring_to_lol(str4, 1), [[1], [2.2], [3], [4.0]])
        self.assertEqual(kd.numstring_to_lol(str4, 2), [[1, 2.2], [3, 4.0]])
        self.assertEqual(kd.numstring_to_lol(str4, 4), [[1, 2.2, 3, 4.0]])

        self.assertEqual(kd.numstring_to_lol(str6, 1), [[-1], [202], [303], [40.4], [5.05], [6]])
        self.assertEqual(kd.numstring_to_lol(str6, 2), [[-1, 202], [303, 40.4], [5.05, 6]])
        self.assertEqual(kd.numstring_to_lol(str6, 3), [[-1, 202, 303], [40.4, 5.05, 6]])
        self.assertEqual(kd.numstring_to_lol(str6, 6), [[-1, 202, 303, 40.4, 5.05, 6]])

    def test_distinct_random_assignment(self):
        k,clean = load_module('kmeans')
        self.assertIsNotNone(k, 'Cannot find module :(')

        random.seed(8675)
        self.assertEqual(k.distinct_random_assignment(3, 3), [2, 0, 1])
        self.assertEqual(k.distinct_random_assignment(3, 3), [1, 0, 2])
        self.assertEqual(k.distinct_random_assignment(3, 3), [0, 2, 1])

        random.seed(309)
        self.assertEqual(k.distinct_random_assignment(3, 3), [0, 1, 2])
        self.assertEqual(k.distinct_random_assignment(3, 3), [2, 1, 0])
        self.assertEqual(k.distinct_random_assignment(3, 3), [0, 2, 1])

        random.seed(8675)
        self.assertEqual(k.distinct_random_assignment(3, 100), [84, 31, 70])
        self.assertEqual(k.distinct_random_assignment(3, 100), [23, 92, 99])
        self.assertEqual(k.distinct_random_assignment(3, 100), [64, 53, 58])

        random.seed(309)
        self.assertEqual(k.distinct_random_assignment(3, 100), [8, 38, 0])
        self.assertEqual(k.distinct_random_assignment(3, 100), [17, 25, 30])
        self.assertEqual(k.distinct_random_assignment(3, 100), [26, 29, 93])


    def test_dist(self):
        k,clean = load_module('kmeans')
        self.assertIsNotNone(k, 'Cannot find module :(')

        self.assertEqual(k.dist([0, 0], [0, 0]), 0)
        self.assertEqual(k.dist([1, 1], [1, 1]), 0)
        self.assertEqual(k.dist([2, 2, 2], [2, 2, 2]), 0)
        self.assertEqual(k.dist([1, -2, 3, -4, 6], [1, -2, 3, -4, 6]), 0)

        self.assertAlmostEqual(k.dist([0, 0], [3, 4]), 5, delta=0.0001)
        self.assertAlmostEqual(k.dist([0, 0, 0], [1, 2, 3]), 3.741657, delta=0.0001)
        self.assertAlmostEqual(k.dist([0, 0, 0], [-1, -2, -3]), 3.741657, delta=0.0001)
        self.assertAlmostEqual(k.dist([1, 4, 7, 0], [-3, 4, 20, 1]), 13.638182, delta=0.0001)
        self.assertAlmostEqual(k.dist([1, 4, 7, 1], [-3, 4, 20, 1]), 13.601471, delta=0.0001)

        self.assertAlmostEqual(k.dist([-32.97, -21.06], [9.01, -31.63]), 43.2902448596, delta=0.0001)

    def test_find_closest(self):
        k,clean = load_module('kmeans')
        self.assertIsNotNone(k, 'Cannot find module :(')

        lonely = [
            [0, 1],
        ]

        triangle = [
            [0, 1],
            [0, 0],
            [2, 0],
        ]

        # https://en.wikipedia.org/wiki/Iris_flower_data_set
        # sepal-length, sepal-width, petal-length, petal-width
        iris = [
            [4.9, 3.0, 1.4, 0.2],
            [5.1, 3.5, 1.4, 0.2],
            [7.0, 3.2, 4.7, 1.4],
            [6.4, 3.2, 4.5, 1.5],
            [6.3, 3.3, 6.0, 2.5],
            [5.8, 2.7, 5.1, 1.9],
        ]

        self.assertEqual(k.find_closest([0, 0], lonely, k.dist), 0)
        self.assertEqual(k.find_closest([0, 0.6], triangle, k.dist), 0)
        self.assertEqual(k.find_closest([0, 0.4], triangle, k.dist), 1)
        self.assertEqual(k.find_closest([1.9, 1], triangle, k.dist), 2)
        self.assertEqual(k.find_closest([4.8, 3.2, 1.4, 0.2], iris, k.dist), 0)
        self.assertEqual(k.find_closest([5.0, 3.3, 1.4, 0.2], iris, k.dist), 1)
        self.assertEqual(k.find_closest([6.9, 2.8, 4.8, 1.3], iris, k.dist), 2)
        self.assertEqual(k.find_closest([5.7, 2.8, 4.1, 1.3], iris, k.dist), 3)
        self.assertEqual(k.find_closest([6.2, 3.2, 5.9, 2.4], iris, k.dist), 4)
        self.assertEqual(k.find_closest([5.9, 3.0, 5.1, 1.8], iris, k.dist), 5)

    def test_avg_point(self):
        k,clean = load_module('kmeans')
        self.assertIsNotNone(k, 'Cannot find module :(')

        self.assertEqual(k.avg_point([[0],]), [0])
        self.assertEqual(k.avg_point([[0, 1],]), [0, 1])
        self.assertEqual(k.avg_point([[0, 1, 2],]), [0, 1, 2])

        self.assertEqual(k.avg_point([[0], [1], [2]]), [1])
        self.assertEqual(k.avg_point([[2], [0], [1]]), [1])
        self.assertEqual(k.avg_point([[0], [100], [25], [75]]), [50])

        avgs = k.avg_point([[0.1], [0.2], [0.3], [0.4]])
        self.assertEqual(len(avgs), 1)
        self.assertAlmostEqual(avgs[0], 0.25, delta=0.0001)

        self.assertEqual(k.avg_point([[25, 50, 1, 10], [100, 50, 1, 20], [75, 100, 1, 30], [0, 100, 1, 40]]), [50, 75, 1, 25])



if __name__ == '__main__':
    unittest.main(verbosity=2)

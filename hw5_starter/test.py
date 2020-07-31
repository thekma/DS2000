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

    def test_precisions(self):
        code,clean = load_module('hw5')
        self.assertIsNotNone(code, 'Cannot find module :(')

        import math

        self.assertEqual(code.precisions(101, []), [])
        self.assertEqual(code.precisions(101, [0]), ["Value with precision 0 is 101."])
        self.assertEqual(code.precisions(101, [1]), ["Value with precision 1 is 101.0."])
        self.assertEqual(code.precisions(101, [2]), ["Value with precision 2 is 101.00."])
        self.assertEqual(code.precisions(101, [0, 1, 10]), ["Value with precision 0 is 101.",
                                                            "Value with precision 1 is 101.0.",
                                                            "Value with precision 10 is 101.0000000000."])

        self.assertEqual(code.precisions(42.1, []), [])
        self.assertEqual(code.precisions(42.1, [0]), ["Value with precision 0 is 42."])
        self.assertEqual(code.precisions(42.1, [1]), ["Value with precision 1 is 42.1."])
        self.assertEqual(code.precisions(42.1, [2]), ["Value with precision 2 is 42.10."])
        self.assertEqual(code.precisions(42.1, [0, 1, 10]), ["Value with precision 0 is 42.",
                                                            "Value with precision 1 is 42.1.",
                                                            "Value with precision 10 is 42.1000000000."])

        self.assertEqual(code.precisions(99.9, []), [])
        self.assertEqual(code.precisions(99.9, [0]), ["Value with precision 0 is 100."])
        self.assertEqual(code.precisions(99.9, [1]), ["Value with precision 1 is 99.9."])
        self.assertEqual(code.precisions(99.9, [2]), ["Value with precision 2 is 99.90."])
        self.assertEqual(code.precisions(99.9, [0, 1, 10]), ["Value with precision 0 is 100.",
                                                            "Value with precision 1 is 99.9.",
                                                            "Value with precision 10 is 99.9000000000."])

        self.assertEqual(code.precisions(math.pi, []), [])
        self.assertEqual(code.precisions(math.pi, [0]), ["Value with precision 0 is 3."])
        self.assertEqual(code.precisions(math.pi, [1]), ["Value with precision 1 is 3.1."])
        self.assertEqual(code.precisions(math.pi, [2]), ["Value with precision 2 is 3.14."])
        self.assertEqual(code.precisions(math.pi, [3]), ["Value with precision 3 is 3.142."])
        self.assertEqual(code.precisions(math.pi, [0, 3]), ["Value with precision 0 is 3.",
                                                            "Value with precision 3 is 3.142."])
        self.assertEqual(code.precisions(math.pi, [1, 2, 3]), ["Value with precision 1 is 3.1.",
                                                               "Value with precision 2 is 3.14.",
                                                               "Value with precision 3 is 3.142."])
        self.assertEqual(code.precisions(math.pi, [1, 2, 3, 10]), ["Value with precision 1 is 3.1.",
                                                                   "Value with precision 2 is 3.14.",
                                                                   "Value with precision 3 is 3.142.",
                                                                   "Value with precision 10 is 3.1415926536."])


    def test_values_at_index(self):
        code,clean = load_module('hw5')
        self.assertIsNotNone(code, 'Cannot find module :(')

        dataset1 = [[-1, 7],]
        self.assertEqual(code.values_at_index(dataset1, 0), [-1,])
        self.assertEqual(code.values_at_index(dataset1, 1), [7,])

        dataset2 = [[-5.1, -5.1], [-1, -1], [0, 0], [1, 1], [3, 3]]
        self.assertEqual(code.values_at_index(dataset2, 0), [-5.1, -1, 0, 1, 3])
        self.assertEqual(code.values_at_index(dataset2, 1), [-5.1, -1, 0, 1, 3])

        dataset3 = [[0, 1, 2], [9, 8, 7], [3, 6, 12]]
        self.assertEqual(code.values_at_index(dataset3, 0), [0, 9, 3])
        self.assertEqual(code.values_at_index(dataset3, 1), [1, 8, 6])
        self.assertEqual(code.values_at_index(dataset3, 2), [2, 7, 12])


    def _test_stats_within(self, code, dataset, index, emin, emax, emean, estdev, tolerance):
        vmin, vmax, vmean, vstdev = code.index_stats(dataset, index)
        self.assertAlmostEqual(vmin, emin, delta=tolerance)
        self.assertAlmostEqual(vmax, emax, delta=tolerance)
        self.assertAlmostEqual(vmean, emean, delta=tolerance)
        self.assertAlmostEqual(vstdev, estdev, delta=tolerance)


    def test_index_stats(self):
        code,clean = load_module('hw5')
        self.assertIsNotNone(code, 'Cannot find module :(')

        dataset2 = [[-5.1, -5.1], [-1, -1], [0, 0], [1, 1], [3, 3]]
        self._test_stats_within(code, dataset2, 0, -5.1, 3, -0.42, 3.0053286, 0.01)
        self._test_stats_within(code, dataset2, 1, -5.1, 3, -0.42, 3.0053286, 0.01)

        dataset3 = [[0, 1, 2], [9, 8, 7], [3, 6, 12]]
        self._test_stats_within(code, dataset3, 0, 0, 9, 4, 4.582575695, 0.01)
        self._test_stats_within(code, dataset3, 1, 1, 8, 5, 3.605551275, 0.01)
        self._test_stats_within(code, dataset3, 2, 2, 12, 7, 5, 0.01)


    def test_quick_summary(self):
        code,clean = load_module('hw5')
        self.assertIsNotNone(code, 'Cannot find module :(')

        dataset2 = [[-5.1, -5.1], [-1, -1], [0, 0], [1, 1], [3, 3]]
        self.assertEqual(code.quick_summary(dataset2, ['lat', 'lon'], 2),
            "Dataset has 5 rows" + "\n" +
            "Dimension analysis..." + "\n" +
            " Dimension 0 (lat): min=-5.10, max=3.00, mean=-0.42, stdev=3.01" + "\n" +
            " Dimension 1 (lon): min=-5.10, max=3.00, mean=-0.42, stdev=3.01"
        )

        self.assertEqual(code.quick_summary(dataset2, ['a', 'b'], 4),
            "Dataset has 5 rows" + "\n" +
            "Dimension analysis..." + "\n" +
            " Dimension 0 (a): min=-5.1000, max=3.0000, mean=-0.4200, stdev=3.0053" + "\n" +
            " Dimension 1 (b): min=-5.1000, max=3.0000, mean=-0.4200, stdev=3.0053"
        )

        dataset3 = [[0, 1, 2], [9, 8, 7], [3, 6, 12]]
        self.assertEqual(code.quick_summary(dataset3, ['x', 'y', 'z'], 2),
            "Dataset has 3 rows" + "\n" +
            "Dimension analysis..." + "\n" +
            " Dimension 0 (x): min=0.00, max=9.00, mean=4.00, stdev=4.58" + "\n" +
            " Dimension 1 (y): min=1.00, max=8.00, mean=5.00, stdev=3.61" + "\n" +
            " Dimension 2 (z): min=2.00, max=12.00, mean=7.00, stdev=5.00"
        )

        self.assertEqual(code.quick_summary(dataset3, ['one', 'two', 'three'], 0),
            "Dataset has 3 rows" + "\n" +
            "Dimension analysis..." + "\n" +
            " Dimension 0 (one): min=0, max=9, mean=4, stdev=5" + "\n" +
            " Dimension 1 (two): min=1, max=8, mean=5, stdev=4" + "\n" +
            " Dimension 2 (three): min=2, max=12, mean=7, stdev=5"
        )

    def test_censor(self):
        code,clean = load_module('hw5')
        self.assertIsNotNone(code, 'Cannot find module :(')

        badwords1 = ['Badword1', 'Badword2']

        script1 = ['hi', 'there', 'my', 'name', 'is', 'BadWord1', 'where', 'badword1', 'means', 'BADWORD2']
        code.censor(script1, badwords1, '***')
        self.assertEqual(script1, ['hi', 'there', 'my', 'name', 'is', '***', 'where', '***', 'means', '***'])

        script1 = ['hi', 'there', 'my', 'name', 'is', 'BadWord1', 'where', 'badword1', 'means', 'BADWORD2']
        code.censor(script1, badwords1, '')
        self.assertEqual(script1, ['hi', 'there', 'my', 'name', 'is', 'where', 'means'])

        #

        badwords2 = ['frack']

        script2 = ['polite', 'people', 'really', 'shouldn\'t', 'say', 'FRACK']
        code.censor(script2, [], 'beep')
        self.assertEqual(script2, ['polite', 'people', 'really', 'shouldn\'t', 'say', 'FRACK'])

        script2 = ['polite', 'people', 'really', 'shouldn\'t', 'say', 'FRACK']
        code.censor(script2, badwords2, 'beep')
        self.assertEqual(script2, ['polite', 'people', 'really', 'shouldn\'t', 'say', 'beep'])

        script2 = ['polite', 'people', 'really', 'shouldn\'t', 'say', 'FRACK']
        code.censor(script2, badwords2, '')
        self.assertEqual(script2, ['polite', 'people', 'really', 'shouldn\'t', 'say'])

        #

        badwords3 = ['BB', 'CRIMETHINK', 'DOUBLETHINK', 'JOYCAMP', 'BOOK', 'THINKPOL', 'PLUSGOOD']

        script3a = ['book', 'is', 'plusgood']
        code.censor(script3a, badwords3, '')
        self.assertEqual(script3a, ['is'])

        script3b = ['THINKPOL', 'doublethink', 'book', 'PlusGood']
        code.censor(script3b, badwords3, '')
        self.assertEqual(script3b, [])

    def test_is_vowel(self):
        code,clean = load_module('hw5')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.is_vowel('a', False), True)
        self.assertEqual(code.is_vowel('a', True), True)
        self.assertEqual(code.is_vowel('b', False), False)
        self.assertEqual(code.is_vowel('b', True), False)
        self.assertEqual(code.is_vowel('c', False), False)
        self.assertEqual(code.is_vowel('c', True), False)
        self.assertEqual(code.is_vowel('d', False), False)
        self.assertEqual(code.is_vowel('d', True), False)
        self.assertEqual(code.is_vowel('e', False), True)
        self.assertEqual(code.is_vowel('e', True), True)
        self.assertEqual(code.is_vowel('f', False), False)
        self.assertEqual(code.is_vowel('f', True), False)
        self.assertEqual(code.is_vowel('g', False), False)
        self.assertEqual(code.is_vowel('g', True), False)
        self.assertEqual(code.is_vowel('h', False), False)
        self.assertEqual(code.is_vowel('h', True), False)
        self.assertEqual(code.is_vowel('i', False), True)
        self.assertEqual(code.is_vowel('i', True), True)
        self.assertEqual(code.is_vowel('j', False), False)
        self.assertEqual(code.is_vowel('j', True), False)
        self.assertEqual(code.is_vowel('k', False), False)
        self.assertEqual(code.is_vowel('k', True), False)
        self.assertEqual(code.is_vowel('l', True), False)
        self.assertEqual(code.is_vowel('l', False), False)
        self.assertEqual(code.is_vowel('m', True), False)
        self.assertEqual(code.is_vowel('m', False), False)
        self.assertEqual(code.is_vowel('n', True), False)
        self.assertEqual(code.is_vowel('n', False), False)
        self.assertEqual(code.is_vowel('o', True), True)
        self.assertEqual(code.is_vowel('o', False), True)
        self.assertEqual(code.is_vowel('p', True), False)
        self.assertEqual(code.is_vowel('p', False), False)
        self.assertEqual(code.is_vowel('q', True), False)
        self.assertEqual(code.is_vowel('q', False), False)
        self.assertEqual(code.is_vowel('r', True), False)
        self.assertEqual(code.is_vowel('r', False), False)
        self.assertEqual(code.is_vowel('s', True), False)
        self.assertEqual(code.is_vowel('s', False), False)
        self.assertEqual(code.is_vowel('t', True), False)
        self.assertEqual(code.is_vowel('t', False), False)
        self.assertEqual(code.is_vowel('u', True), True)
        self.assertEqual(code.is_vowel('u', False), True)
        self.assertEqual(code.is_vowel('v', True), False)
        self.assertEqual(code.is_vowel('v', False), False)
        self.assertEqual(code.is_vowel('w', True), False)
        self.assertEqual(code.is_vowel('w', False), False)
        self.assertEqual(code.is_vowel('x', True), False)
        self.assertEqual(code.is_vowel('x', False), False)
        self.assertEqual(code.is_vowel('y', True), True)
        self.assertEqual(code.is_vowel('y', False), False)
        self.assertEqual(code.is_vowel('z', True), False)
        self.assertEqual(code.is_vowel('z', False), False)

    def test_pig_latin_word(self):
        code,clean = load_module('hw5')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.pig_latin_word('alpha'), 'alphaway')
        self.assertEqual(code.pig_latin_word('bravo'), 'avobray')
        self.assertEqual(code.pig_latin_word('charlie'), 'arliechay')
        self.assertEqual(code.pig_latin_word('delta'), 'eltaday')
        self.assertEqual(code.pig_latin_word('echo'), 'echoway')
        self.assertEqual(code.pig_latin_word('foxtrot'), 'oxtrotfay')
        self.assertEqual(code.pig_latin_word('golf'), 'olfgay')
        self.assertEqual(code.pig_latin_word('hotel'), 'otelhay')
        self.assertEqual(code.pig_latin_word('india'), 'indiaway')
        self.assertEqual(code.pig_latin_word('juliet'), 'ulietjay')
        self.assertEqual(code.pig_latin_word('kilo'), 'ilokay')
        self.assertEqual(code.pig_latin_word('lima'), 'imalay')
        self.assertEqual(code.pig_latin_word('mike'), 'ikemay')
        self.assertEqual(code.pig_latin_word('november'), 'ovembernay')
        self.assertEqual(code.pig_latin_word('oscar'), 'oscarway')
        self.assertEqual(code.pig_latin_word('papa'), 'apapay')
        self.assertEqual(code.pig_latin_word('quebec'), 'uebecqay')
        self.assertEqual(code.pig_latin_word('romeo'), 'omeoray')
        self.assertEqual(code.pig_latin_word('sierra'), 'ierrasay')
        self.assertEqual(code.pig_latin_word('tango'), 'angotay')
        self.assertEqual(code.pig_latin_word('uniform'), 'uniformway')
        self.assertEqual(code.pig_latin_word('victor'), 'ictorvay')
        self.assertEqual(code.pig_latin_word('whiskey'), 'iskeywhay')
        self.assertEqual(code.pig_latin_word('xray'), 'ayxray')
        self.assertEqual(code.pig_latin_word('yankee'), 'ankeeyay')
        self.assertEqual(code.pig_latin_word('zulu'), 'uluzay')

        self.assertEqual(code.pig_latin_word('byline'), 'ylinebay')

    def test_pig_latin_phrase(self):
        code,clean = load_module('hw5')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.pig_latin_phrase(''), '')

        self.assertEqual(code.pig_latin_phrase('hello'), 'ellohay')
        self.assertEqual(code.pig_latin_phrase('yello'), 'elloyay')
        self.assertEqual(code.pig_latin_phrase('odo'), 'odoway')

        self.assertEqual(code.pig_latin_phrase('going to make him an offer he cannot refuse'), 'oinggay otay akemay imhay anway offerway ehay annotcay efuseray')
        self.assertEqual(code.pig_latin_phrase('may the force be with you'), 'aymay ethay orcefay ebay ithway ouyay')
        self.assertEqual(code.pig_latin_phrase('show me the money'), 'owshay emay ethay oneymay')
        self.assertEqual(code.pig_latin_phrase('i see dead people'), 'iway eesay eadday eoplepay')
        self.assertEqual(code.pig_latin_phrase('my precious'), 'ymay eciouspray')


if __name__ == '__main__':
    unittest.main(verbosity=2)

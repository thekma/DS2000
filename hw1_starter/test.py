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

    def _d1(self, d1in, d1out):
        self.assertEqual(input_output_test("distance1.py", "{}\n".format(d1in))[1], "Please enter number of meters: The full number of yards is {}\n".format(d1out))

    def test_distance1(self):
        self._d1("0", "0")
        self._d1("0.5", "0")
        self._d1("1", "1")
        self._d1("11", "12")

    ##

    def _d2(self, d2in, d2out_y, d2out_f, d2out_i):
        self.assertEqual(input_output_test("distance2.py", "{}\n".format(d2in))[1], "Please enter full number of inches: {}in = {}yd {}ft {}in\n".format(d2in, d2out_y, d2out_f, d2out_i))

    def test_distance2(self):
        self._d2("0", "0", "0", "0")
        self._d2("1", "0", "0", "1")
        self._d2("12", "0", "1", "0")
        self._d2("13", "0", "1", "1")
        self._d2("36", "1", "0", "0")
        self._d2("37", "1", "0", "1")
        self._d2("48", "1", "1", "0")
        self._d2("49", "1", "1", "1")
        self._d2("137", "3", "2", "5")

    ##

    def _c1(self, c1in_d, c1in_c, c1in_f, c1out):
        self.assertEqual(input_output_test("currency1.py", "{}\n{}\n{}\n".format(c1in_d, c1in_c, c1in_f))[1], "Please enter number of US dollars: 1 USD = ? foreign: Fee for buying currency (in USD): You have {} full unit(s) of foreign currency\n".format(c1out))

    def test_currency1(self):
        self._c1("8", "0.2", "3", "1")
        self._c1("13", "0.2", "3", "2")
        self._c1("14", "0.2", "3", "2")
        self._c1("10", "6", "3", "42")

    ##

    def _c2(self, c2in, c2out_s, c2out_e):
        self.assertEqual(input_output_test("currency2.py", "{}\n".format(c2in))[1], "Enter desired currency: Found in database (size={}): {}\n".format(c2out_s, c2out_e))

    def test_currency2(self):
        self._c2("dollar", "4", "False")
        self._c2("USD", "4", "True")
        self._c2("usd", "4", "False")
        self._c2("EUR", "4", "True")

    ##

    def _nb(self, nbin, nbout):
        self.assertEqual(input_output_test("namebadges.py", "{}\n".format(nbin))[1], "Enter common name: {}\n".format(nbout))

    def test_namebadges(self):
        self._nb("a", "['Hello my name is a']")
        self._nb("Bb", "['Hello my name is Bb', 'Hello my name is Bb']")
        self._nb("Cat", "['Hello my name is Cat', 'Hello my name is Cat', 'Hello my name is Cat']")
        self._nb("Dave", "['Hello my name is Dave', 'Hello my name is Dave', 'Hello my name is Dave', 'Hello my name is Dave']")
        self._nb("Wendy", "['Hello my name is Wendy', 'Hello my name is Wendy', 'Hello my name is Wendy', 'Hello my name is Wendy', 'Hello my name is Wendy']")

if __name__ == '__main__':
    unittest.main(verbosity=2)

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

    def _mc(self, mcin_phrase, mcin_query, mcout):
        self.assertEqual(input_output_test("matchcount.py", "{}\n{}\n".format(mcin_phrase, mcin_query))[1], "Enter phrase: Enter query letters: {}\n".format(mcout))

    def test_matchcount(self):
        self._mc("abcd", "xyz", "Phrase has 0 letters in the query")
        self._mc("the quick brown fox jumps over the lazy dog", "xyz", "Phrase has 3 letters in the query")
        self._mc("the quick brown fox jumps over the lazy dog", "aeiouy", "Phrase has 12 letters in the query")
        self._mc("abcd", "a", "Phrase has 1 letter in the query")
        self._mc("dcba", "a", "Phrase has 1 letter in the query")
        self._mc("phrase", "xaez", "Phrase has 2 letters in the query")
        self._mc("abcabc", "a", "Phrase has 2 letters in the query")
        self._mc("abc", "aa", "Phrase has 1 letter in the query")

    ##

    def _cg(self, cgin_weights, cgin_grades, cgout_prompts, cgout_grade):
        self.assertEqual(input_output_test("coursegrade.py", "{}\n{}\n".format(cgin_weights, "\n".join(cgin_grades)))[1], "Enter grade weights: {}Course grade: {}\n".format("".join(cgout_prompts), cgout_grade))

    def test_coursegrade(self):
        self._cg("100", ["80"], ["Enter grades (100%): "], "80")
        self._cg("100", ["80.4"], ["Enter grades (100%): "], "80")
        self._cg("100", ["80.6"], ["Enter grades (100%): "], "81")
        self._cg("100", ["90 91.1"], ["Enter grades (100%): "], "91")
        self._cg("50 50", ["60", "70 73"], ["Enter grades (50%): ", "Enter grades (50%): "], "66")
        self._cg("10 90", ["60", "70 73"], ["Enter grades (10%): ", "Enter grades (90%): "], "70")
        self._cg("90 10", ["60", "70 73"], ["Enter grades (90%): ", "Enter grades (10%): "], "61")
        self._cg("30 20 25 25", ["100 90 80 70 60 60 70 80 90 100", "90 80 100 70 60", "100 100 100 50 0 100 100 100 100 100", "90.8"], ["Enter grades (30%): ", "Enter grades (20%): ", "Enter grades (25%): ", "Enter grades (25%): "], "84")

    ##

    def _t(self, tin_income, tin_status, tout):
        self.assertEqual(input_output_test("taxes.py", "{}\n{}\n".format(tin_income, tin_status))[1], "Enter income: Enter filing status: {}\n".format(tout))

    def test_taxes(self):
        self._t("5000", "single", "You do not owe any taxes!")
        self._t("5000", "married", "You do not owe any taxes!")

        self._t("10000", "single", "You do not owe any taxes!")
        self._t("10000", "married", "You do not owe any taxes!")

        self._t("20000", "single", "You are in the 10% bracket; you owe $800 in taxes for an effective rate of 4%.")
        self._t("20000", "married", "You do not owe any taxes!")

        self._t("30000", "single", "You are in the 12% bracket; you owe $1970 in taxes for an effective rate of 7%.")
        self._t("30000", "married", "You are in the 10% bracket; you owe $600 in taxes for an effective rate of 2%.")

        self._t("50000", "single", "You are in the 12% bracket; you owe $4370 in taxes for an effective rate of 9%.")
        self._t("50000", "married", "You are in the 12% bracket; you owe $2739 in taxes for an effective rate of 5%.")

        self._t("100000", "single", "You are in the 24% bracket; you owe $15410 in taxes for an effective rate of 15%.")
        self._t("100000", "married", "You are in the 12% bracket; you owe $8739 in taxes for an effective rate of 9%.")

        self._t("250000", "single", "You are in the 35% bracket; you owe $58990 in taxes for an effective rate of 24%.")
        self._t("250000", "married", "You are in the 24% bracket; you owe $42819 in taxes for an effective rate of 17%.")

        self._t("550000", "single", "You are in the 37% bracket; you owe $164750 in taxes for an effective rate of 30%.")
        self._t("550000", "married", "You are in the 35% bracket; you owe $135479 in taxes for an effective rate of 25%.")

        self._t("1000000", "single", "You are in the 37% bracket; you owe $331250 in taxes for an effective rate of 33%.")
        self._t("1000000", "married", "You are in the 37% bracket; you owe $300499 in taxes for an effective rate of 30%.")

if __name__ == '__main__':
    unittest.main(verbosity=2)

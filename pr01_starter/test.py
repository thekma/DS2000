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

    def test_hello(self):
        self.assertEqual(input_output_test("hello.py", "")[1], "Hello, World!\n")

if __name__ == '__main__':
    unittest.main(verbosity=2)

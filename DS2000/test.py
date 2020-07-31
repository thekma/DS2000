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

    def test_num_distinct_letters(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.num_distinct_letters(''), 0)

        self.assertEqual(code.num_distinct_letters('a'), 1)
        self.assertEqual(code.num_distinct_letters('A'), 1)
        self.assertEqual(code.num_distinct_letters('b'), 1)
        self.assertEqual(code.num_distinct_letters('B'), 1)
        self.assertEqual(code.num_distinct_letters('z'), 1)
        self.assertEqual(code.num_distinct_letters('Z'), 1)

        self.assertEqual(code.num_distinct_letters('aa'), 1)
        self.assertEqual(code.num_distinct_letters('AA'), 1)
        self.assertEqual(code.num_distinct_letters('cc'), 1)
        self.assertEqual(code.num_distinct_letters('CC'), 1)
        self.assertEqual(code.num_distinct_letters('ff'), 1)
        self.assertEqual(code.num_distinct_letters('FF'), 1)
        self.assertEqual(code.num_distinct_letters('yy'), 1)
        self.assertEqual(code.num_distinct_letters('YY'), 1)

        self.assertEqual(code.num_distinct_letters('aA'), 1)
        self.assertEqual(code.num_distinct_letters('Aa'), 1)
        self.assertEqual(code.num_distinct_letters('dD'), 1)
        self.assertEqual(code.num_distinct_letters('Gg'), 1)
        self.assertEqual(code.num_distinct_letters('nN'), 1)
        self.assertEqual(code.num_distinct_letters('Qq'), 1)

        self.assertEqual(code.num_distinct_letters('aB'), 2)
        self.assertEqual(code.num_distinct_letters('Za'), 2)

        self.assertEqual(code.num_distinct_letters('cat'), 3)
        self.assertEqual(code.num_distinct_letters('bat'), 3)
        self.assertEqual(code.num_distinct_letters('matt'), 3)
        self.assertEqual(code.num_distinct_letters('ftntt'), 3)

        self.assertEqual(code.num_distinct_letters('Starts'), 4)
        self.assertEqual(code.num_distinct_letters('word'), 4)

        self.assertEqual(code.num_distinct_letters('words'), 5)

        self.assertEqual(code.num_distinct_letters('Python'), 6)

        self.assertEqual(code.num_distinct_letters('Scrabble'), 7)

        self.assertEqual(code.num_distinct_letters('inconceivable'), 9)

        self.assertEqual(code.num_distinct_letters('supercalifragilisticexpialidocious'), 15)

    def test_q_not_qu(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.q_not_qu('a'), 0)
        self.assertEqual(code.q_not_qu('A'), 0)
        self.assertEqual(code.q_not_qu('b'), 0)
        self.assertEqual(code.q_not_qu('B'), 0)
        self.assertEqual(code.q_not_qu('q'), 1)
        self.assertEqual(code.q_not_qu('Q'), 1)
        self.assertEqual(code.q_not_qu('y'), 0)
        self.assertEqual(code.q_not_qu('Y'), 0)

        self.assertEqual(code.q_not_qu('aa'), 0)
        self.assertEqual(code.q_not_qu('AA'), 0)
        self.assertEqual(code.q_not_qu('cc'), 0)
        self.assertEqual(code.q_not_qu('CC'), 0)
        self.assertEqual(code.q_not_qu('ff'), 0)
        self.assertEqual(code.q_not_qu('FF'), 0)
        self.assertEqual(code.q_not_qu('yy'), 0)
        self.assertEqual(code.q_not_qu('YY'), 0)

        self.assertEqual(code.q_not_qu('qa'), 1)
        self.assertEqual(code.q_not_qu('qA'), 1)
        self.assertEqual(code.q_not_qu('Qa'), 1)
        self.assertEqual(code.q_not_qu('QA'), 1)
        self.assertEqual(code.q_not_qu('qb'), 1)
        self.assertEqual(code.q_not_qu('qB'), 1)
        self.assertEqual(code.q_not_qu('Qb'), 1)
        self.assertEqual(code.q_not_qu('QB'), 1)
        self.assertEqual(code.q_not_qu('qq'), 1)
        self.assertEqual(code.q_not_qu('qQ'), 1)
        self.assertEqual(code.q_not_qu('Qq'), 1)
        self.assertEqual(code.q_not_qu('QQ'), 1)
        self.assertEqual(code.q_not_qu('uq'), 1)
        self.assertEqual(code.q_not_qu('Uq'), 1)
        self.assertEqual(code.q_not_qu('uQ'), 1)
        self.assertEqual(code.q_not_qu('UQ'), 1)

        self.assertEqual(code.q_not_qu('qu'), 0)
        self.assertEqual(code.q_not_qu('qU'), 0)
        self.assertEqual(code.q_not_qu('Qu'), 0)
        self.assertEqual(code.q_not_qu('QU'), 0)
        self.assertEqual(code.q_not_qu('uqu'), 0)
        self.assertEqual(code.q_not_qu('uqU'), 0)
        self.assertEqual(code.q_not_qu('uQu'), 0)
        self.assertEqual(code.q_not_qu('uQU'), 0)
        self.assertEqual(code.q_not_qu('aqu'), 0)
        self.assertEqual(code.q_not_qu('AqU'), 0)
        self.assertEqual(code.q_not_qu('aQu'), 0)
        self.assertEqual(code.q_not_qu('AQU'), 0)
        self.assertEqual(code.q_not_qu('qua'), 0)
        self.assertEqual(code.q_not_qu('qUA'), 0)
        self.assertEqual(code.q_not_qu('Qua'), 0)
        self.assertEqual(code.q_not_qu('QUA'), 0)

        self.assertEqual(code.q_not_qu('ablaqueate'), 0)
        self.assertEqual(code.q_not_qu('aceanthrenequinone'), 0)
        self.assertEqual(code.q_not_qu('aeq'), 1)
        self.assertEqual(code.q_not_qu('hindquarters'), 0)
        self.assertEqual(code.q_not_qu('soliloquy'), 0)
        self.assertEqual(code.q_not_qu('qintar'), 1)
        self.assertEqual(code.q_not_qu('qiviuts'), 1)
        self.assertEqual(code.q_not_qu('qoheleth'), 1)
        self.assertEqual(code.q_not_qu('QI'), 1)
        self.assertEqual(code.q_not_qu('SUQ'), 1)
        self.assertEqual(code.q_not_qu('QAID'), 1)


    def test_letter_score(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.letter_score('a', (), 1), 1)
        self.assertEqual(code.letter_score('A', (), 1), 1)
        self.assertEqual(code.letter_score('a', (), 2), 2)
        self.assertEqual(code.letter_score('A', (), 2), 2)

        self.assertEqual(code.letter_score('q', (), 1), 1)
        self.assertEqual(code.letter_score('Q', (), 1), 1)
        self.assertEqual(code.letter_score('q', (), 2), 2)
        self.assertEqual(code.letter_score('Q', (), 2), 2)

        self.assertEqual(code.letter_score('a', (('a', 10),), 1), 10)
        self.assertEqual(code.letter_score('A', (('a', 10),), 1), 10)
        self.assertEqual(code.letter_score('a', (('a', 10),), 12), 10)
        self.assertEqual(code.letter_score('A', (('a', 10),), 12), 10)

        self.assertEqual(code.letter_score('c', (('a', 10),), 1), 1)
        self.assertEqual(code.letter_score('C', (('a', 10),), 1), 1)
        self.assertEqual(code.letter_score('c', (('a', 10),), 12), 12)
        self.assertEqual(code.letter_score('C', (('a', 10),), 12), 12)

        SCRABBLE = (
            ('D', 2), ('G', 2),
            ('B', 3), ('C', 3), ('M', 3), ('P', 3),
            ('F', 4), ('H', 4), ('V', 4), ('W', 4), ('Y', 4),
            ('K', 5),
            ('J', 8), ('X', 8),
            ('Q', 10), ('Z', 10)
        )

        SCRABBLE_DEFAULT = 1

        self.assertEqual(code.letter_score('a', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('b', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.letter_score('c', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.letter_score('d', SCRABBLE, SCRABBLE_DEFAULT), 2)
        self.assertEqual(code.letter_score('e', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('f', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('g', SCRABBLE, SCRABBLE_DEFAULT), 2)
        self.assertEqual(code.letter_score('h', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('i', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('j', SCRABBLE, SCRABBLE_DEFAULT), 8)
        self.assertEqual(code.letter_score('k', SCRABBLE, SCRABBLE_DEFAULT), 5)
        self.assertEqual(code.letter_score('l', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('m', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.letter_score('n', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('o', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('p', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.letter_score('q', SCRABBLE, SCRABBLE_DEFAULT), 10)
        self.assertEqual(code.letter_score('r', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('s', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('t', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('u', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('v', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('w', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('x', SCRABBLE, SCRABBLE_DEFAULT), 8)
        self.assertEqual(code.letter_score('y', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('z', SCRABBLE, SCRABBLE_DEFAULT), 10)

        self.assertEqual(code.letter_score('A', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('B', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.letter_score('C', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.letter_score('D', SCRABBLE, SCRABBLE_DEFAULT), 2)
        self.assertEqual(code.letter_score('E', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('F', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('G', SCRABBLE, SCRABBLE_DEFAULT), 2)
        self.assertEqual(code.letter_score('H', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('I', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('J', SCRABBLE, SCRABBLE_DEFAULT), 8)
        self.assertEqual(code.letter_score('K', SCRABBLE, SCRABBLE_DEFAULT), 5)
        self.assertEqual(code.letter_score('L', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('M', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.letter_score('N', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('O', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('P', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.letter_score('Q', SCRABBLE, SCRABBLE_DEFAULT), 10)
        self.assertEqual(code.letter_score('R', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('S', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('T', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('U', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.letter_score('V', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('W', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('X', SCRABBLE, SCRABBLE_DEFAULT), 8)
        self.assertEqual(code.letter_score('Y', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.letter_score('Z', SCRABBLE, SCRABBLE_DEFAULT), 10)

    def test_word_score(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.word_score('', (), 1), 0)
        self.assertEqual(code.word_score('', (), 10), 0)
        self.assertEqual(code.word_score('', (('a', 10),), 1), 0)

        self.assertEqual(code.word_score('a', (), 1), 1)
        self.assertEqual(code.word_score('A', (), 1), 1)
        self.assertEqual(code.word_score('a', (), 2), 2)
        self.assertEqual(code.word_score('A', (), 2), 2)

        self.assertEqual(code.word_score('q', (), 1), 1)
        self.assertEqual(code.word_score('Q', (), 1), 1)
        self.assertEqual(code.word_score('q', (), 2), 2)
        self.assertEqual(code.word_score('Q', (), 2), 2)

        self.assertEqual(code.word_score('a', (('a', 10),), 1), 10)
        self.assertEqual(code.word_score('A', (('a', 10),), 1), 10)
        self.assertEqual(code.word_score('a', (('a', 10),), 12), 10)
        self.assertEqual(code.word_score('A', (('a', 10),), 12), 10)

        self.assertEqual(code.word_score('c', (('a', 10),), 1), 1)
        self.assertEqual(code.word_score('C', (('a', 10),), 1), 1)
        self.assertEqual(code.word_score('c', (('a', 10),), 12), 12)
        self.assertEqual(code.word_score('C', (('a', 10),), 12), 12)

        SCRABBLE = (
            ('D', 2), ('G', 2),
            ('B', 3), ('C', 3), ('M', 3), ('P', 3),
            ('F', 4), ('H', 4), ('V', 4), ('W', 4), ('Y', 4),
            ('K', 5),
            ('J', 8), ('X', 8),
            ('Q', 10), ('Z', 10)
        )

        SCRABBLE_DEFAULT = 1

        self.assertEqual(code.word_score('a', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('b', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.word_score('c', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.word_score('d', SCRABBLE, SCRABBLE_DEFAULT), 2)
        self.assertEqual(code.word_score('e', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('f', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('g', SCRABBLE, SCRABBLE_DEFAULT), 2)
        self.assertEqual(code.word_score('h', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('i', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('j', SCRABBLE, SCRABBLE_DEFAULT), 8)
        self.assertEqual(code.word_score('k', SCRABBLE, SCRABBLE_DEFAULT), 5)
        self.assertEqual(code.word_score('l', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('m', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.word_score('n', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('o', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('p', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.word_score('q', SCRABBLE, SCRABBLE_DEFAULT), 10)
        self.assertEqual(code.word_score('r', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('s', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('t', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('u', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('v', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('w', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('x', SCRABBLE, SCRABBLE_DEFAULT), 8)
        self.assertEqual(code.word_score('y', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('z', SCRABBLE, SCRABBLE_DEFAULT), 10)

        self.assertEqual(code.word_score('A', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('B', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.word_score('C', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.word_score('D', SCRABBLE, SCRABBLE_DEFAULT), 2)
        self.assertEqual(code.word_score('E', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('F', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('G', SCRABBLE, SCRABBLE_DEFAULT), 2)
        self.assertEqual(code.word_score('H', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('I', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('J', SCRABBLE, SCRABBLE_DEFAULT), 8)
        self.assertEqual(code.word_score('K', SCRABBLE, SCRABBLE_DEFAULT), 5)
        self.assertEqual(code.word_score('L', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('M', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.word_score('N', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('O', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('P', SCRABBLE, SCRABBLE_DEFAULT), 3)
        self.assertEqual(code.word_score('Q', SCRABBLE, SCRABBLE_DEFAULT), 10)
        self.assertEqual(code.word_score('R', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('S', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('T', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('U', SCRABBLE, SCRABBLE_DEFAULT), SCRABBLE_DEFAULT)
        self.assertEqual(code.word_score('V', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('W', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('X', SCRABBLE, SCRABBLE_DEFAULT), 8)
        self.assertEqual(code.word_score('Y', SCRABBLE, SCRABBLE_DEFAULT), 4)
        self.assertEqual(code.word_score('Z', SCRABBLE, SCRABBLE_DEFAULT), 10)

        self.assertEqual(code.word_score('Hello', SCRABBLE, SCRABBLE_DEFAULT), 8)
        self.assertEqual(code.word_score('Weird', SCRABBLE, SCRABBLE_DEFAULT), 9)
        self.assertEqual(code.word_score('magical', SCRABBLE, SCRABBLE_DEFAULT), 12)
        self.assertEqual(code.word_score('SABADILLA', SCRABBLE, SCRABBLE_DEFAULT), 12)
        self.assertEqual(code.word_score('pythons', SCRABBLE, SCRABBLE_DEFAULT), 15)
        self.assertEqual(code.word_score('Zebra', SCRABBLE, SCRABBLE_DEFAULT), 16)
        self.assertEqual(code.word_score('ZABAGLIONE', SCRABBLE, SCRABBLE_DEFAULT), 22)
        self.assertEqual(code.word_score('XYLOPHONE', SCRABBLE, SCRABBLE_DEFAULT), 24)

    def test_most_words(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.most_words('sentence.txt', code.length_score), (11, ['interesting']))
        self.assertEqual(code.most_words('sentence.txt', code.q_not_qu), (1, ['sheqels']))
        self.assertEqual(code.most_words('sentence.txt', code.num_distinct_letters), (8, ['question']))
        self.assertEqual(code.most_words('sentence.txt', code.scrabble_score), (19, ['sheqels']))

        #

        self.assertEqual(code.most_words('one.txt', code.length_score), (12, ['xalostockite']))
        self.assertEqual(code.most_words('one.txt', code.q_not_qu), (1, ['qabbala']))
        self.assertEqual(code.most_words('one.txt', code.num_distinct_letters), (10, ['xalostockite']))
        self.assertEqual(code.most_words('one.txt', code.scrabble_score), (25, ['xalostockite']))

        #

        self.assertEqual(code.most_words('three.txt', code.length_score), (13, ['paaraphimosis']))
        self.assertEqual(code.most_words('three.txt', code.q_not_qu), (1, ['qabbala', 'qabbalah', 'qadarite']))
        self.assertEqual(code.most_words('three.txt', code.num_distinct_letters), (10, ['xalostockite']))
        self.assertEqual(code.most_words('three.txt', code.scrabble_score), (25, ['xalostockite']))

        #

        score, words = code.most_words('scrabble.txt', code.length_score)
        self.assertEqual(score, 15)
        self.assertEqual(len(words), 3157)

        score, words = code.most_words('scrabble.txt', code.q_not_qu)
        self.assertEqual(score, 1)
        self.assertEqual(len(words), 42)

        self.assertEqual(code.most_words('scrabble.txt', code.num_distinct_letters), (15, ['DERMATOGLYPHICS', 'UNCOPYRIGHTABLE']))
        self.assertEqual(code.most_words('scrabble.txt', code.scrabble_score), (51, ['RAZZAMATAZZES']))

        #

        self.assertEqual(code.most_words('words_alpha.txt', code.length_score), (31, ['dichlorodiphenyltrichloroethane']))

        score, words = code.most_words('words_alpha.txt', code.q_not_qu)
        self.assertEqual(score, 1)
        self.assertEqual(len(words), 115)

        self.assertEqual(code.most_words('words_alpha.txt', code.num_distinct_letters), (16, ['blepharoconjunctivitis','formaldehydesulphoxylic','pneumoventriculography','pseudolamellibranchiata','pseudolamellibranchiate','superacknowledgment']))
        self.assertEqual(code.most_words('words_alpha.txt', code.scrabble_score), (66, ['hexahydroxycyclohexane']))


    def test_read_data(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        header, data = code.read_data('littledata.txt')
        self.assertEqual(header, ['ID', 'ColA', 'ColB'])
        self.assertEqual(data, [['0', 'Foo', 'alpha'], ['1', 'Bar', 'BETA'], ['2', 'Baz', 'Gamma'], ['3', 'Qux', 'delta']])

        header, data = code.read_data('qbdata.txt')
        self.assertEqual(header, ['First', 'Last', 'Position', 'Team', 'Completions', 'Attempts', 'Yards', 'TDs', 'Ints', 'Comp%', 'Rating'])
        self.assertEqual(len(data), 34)
        self.assertEqual(data[0], ['Colt', 'McCoy', 'QB', 'CLE', '135', '222', '1576', '6', '9', '60.8%', '74.5'])
        self.assertEqual(data[11], ['Drew', 'Brees', 'QB', 'NO', '448', '658', '4620', '33', '22', '68.1%', '90.9'])
        self.assertEqual(data[33], ['Shaun', 'Hill', 'QB', 'DET', '257', '416', '2686', '16', '12', '61.8%', '81.3'])


    def test_get_column(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.get_column('a', ['a', 'b', 'c'], []), [])
        self.assertEqual(code.get_column('b', ['a', 'b', 'c'], []), [])
        self.assertEqual(code.get_column('c', ['a', 'b', 'c'], []), [])

        self.assertEqual(code.get_column('a', ['a', 'b', 'c'], [[1, 2, 3],]), [1,])
        self.assertEqual(code.get_column('b', ['a', 'b', 'c'], [[1, 2, 3],]), [2,])
        self.assertEqual(code.get_column('c', ['a', 'b', 'c'], [[1, 2, 3],]), [3,])

        self.assertEqual(code.get_column('a', ['a', 'b', 'c'], [[1, 2, 3],[10, 9, 8]]), [1, 10])
        self.assertEqual(code.get_column('b', ['a', 'b', 'c'], [[1, 2, 3],[10, 9, 8]]), [2, 9])
        self.assertEqual(code.get_column('c', ['a', 'b', 'c'], [[1, 2, 3],[10, 9, 8]]), [3, 8])

        little_header = ['ID', 'ColA', 'ColB']
        little_data = [['0', 'Foo', 'alpha'], ['1', 'Bar', 'BETA'], ['2', 'Baz', 'Gamma'], ['3', 'Qux', 'delta']]

        self.assertEqual(code.get_column('ID', little_header, little_data), ['0', '1', '2', '3'])
        self.assertEqual(code.get_column('ColA', little_header, little_data), ['Foo', 'Bar', 'Baz', 'Qux'])
        self.assertEqual(code.get_column('ColB', little_header, little_data), ['alpha', 'BETA', 'Gamma', 'delta'])


    def test_convert_to_nums(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.convert_to_nums([], 0), [])
        self.assertEqual(code.convert_to_nums([], 1), [])
        self.assertEqual(code.convert_to_nums([], 2), [])
        self.assertEqual(code.convert_to_nums([], 10), [])

        self.assertEqual(code.convert_to_nums(['1', '2.22', '4.4444', '6.666', '8.8', '10.01'], 0), [1., 2., 4., 7., 9., 10.])

        result = code.convert_to_nums(['1', '2.22', '4.4444', '6.666', '8.8', '10.01'], 1)
        self.assertEqual(len(result), 6)
        self.assertAlmostEqual(result[0], 1., delta=0.01)
        self.assertAlmostEqual(result[1], 2.2, delta=0.01)
        self.assertAlmostEqual(result[2], 4.4, delta=0.01)
        self.assertAlmostEqual(result[3], 6.7, delta=0.01)
        self.assertAlmostEqual(result[4], 8.8, delta=0.01)
        self.assertAlmostEqual(result[5], 10.0, delta=0.01)

        result = code.convert_to_nums(['1', '2.22', '4.4444', '6.666', '8.8', '10.01'], 2)
        self.assertEqual(len(result), 6)
        self.assertAlmostEqual(result[0], 1., delta=0.001)
        self.assertAlmostEqual(result[1], 2.22, delta=0.001)
        self.assertAlmostEqual(result[2], 4.44, delta=0.001)
        self.assertAlmostEqual(result[3], 6.67, delta=0.001)
        self.assertAlmostEqual(result[4], 8.8, delta=0.001)
        self.assertAlmostEqual(result[5], 10.01, delta=0.001)

        result = code.convert_to_nums(['1', '2.22', '4.4444', '6.666', '8.8', '10.01'], 10)
        self.assertEqual(len(result), 6)
        self.assertAlmostEqual(result[0], 1., delta=1e-10)
        self.assertAlmostEqual(result[1], 2.22, delta=1e-10)
        self.assertAlmostEqual(result[2], 4.4444, delta=1e-10)
        self.assertAlmostEqual(result[3], 6.666, delta=1e-10)
        self.assertAlmostEqual(result[4], 8.8, delta=1e-10)
        self.assertAlmostEqual(result[5], 10.01, delta=1e-10)


    def test_player_with_highest_rating(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.player_with_highest_rating('qbdata.txt'), ['Tom', 'Brady', 'QB', 'NE', '324', '492', '3900', '36', '4', '65.9%', '111.0'])


    def test_convert_to_props(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.convert_to_props([], 0), [])
        self.assertEqual(code.convert_to_props([], 1), [])
        self.assertEqual(code.convert_to_props([], 2), [])
        self.assertEqual(code.convert_to_props([], 10), [])

        self.assertEqual(code.convert_to_props(
            ['1%', '2.22%', '4.4444%', '6.666%', '8.8%', '10.01%', '37.63%', '71.77%', '93.4%'], 0),
            [0., 0., 0., 0., 0., 0., 0., 1., 1.])

        result = code.convert_to_props(['1%', '2.22%', '4.4444%', '6.666%', '8.8%', '10.01%', '37.63%', '71.77%', '93.4%'], 1)
        self.assertEqual(len(result), 9)
        self.assertAlmostEqual(result[0], 0., delta=0.1)
        self.assertAlmostEqual(result[1], 0., delta=0.1)
        self.assertAlmostEqual(result[2], 0., delta=0.1)
        self.assertAlmostEqual(result[3], 0.1, delta=0.1)
        self.assertAlmostEqual(result[4], 0.1, delta=0.1)
        self.assertAlmostEqual(result[5], 0.1, delta=0.1)
        self.assertAlmostEqual(result[6], 0.4, delta=0.1)
        self.assertAlmostEqual(result[7], 0.7, delta=0.1)
        self.assertAlmostEqual(result[8], 0.9, delta=0.1)

        result = code.convert_to_props(['1%', '2.22%', '4.4444%', '6.666%', '8.8%', '10.01%', '37.63%', '71.77%', '93.4%'], 2)
        self.assertEqual(len(result), 9)
        self.assertAlmostEqual(result[0], 0.01, delta=0.01)
        self.assertAlmostEqual(result[1], 0.02, delta=0.01)
        self.assertAlmostEqual(result[2], 0.04, delta=0.01)
        self.assertAlmostEqual(result[3], 0.07, delta=0.01)
        self.assertAlmostEqual(result[4], 0.09, delta=0.01)
        self.assertAlmostEqual(result[5], 0.1, delta=0.01)
        self.assertAlmostEqual(result[6], 0.38, delta=0.01)
        self.assertAlmostEqual(result[7], 0.72, delta=0.01)
        self.assertAlmostEqual(result[8], 0.93, delta=0.01)

        result = code.convert_to_props(['1%', '2.22%', '4.4444%', '6.666%', '8.8%', '10.01%', '37.63%', '71.77%', '93.4%'], 10)
        self.assertEqual(len(result), 9)
        self.assertAlmostEqual(result[0], 0.01, delta=1e-10)
        self.assertAlmostEqual(result[1], 0.0222, delta=1e-10)
        self.assertAlmostEqual(result[2], 0.044444, delta=1e-10)
        self.assertAlmostEqual(result[3], 0.06666, delta=1e-10)
        self.assertAlmostEqual(result[4], 0.088, delta=1e-10)
        self.assertAlmostEqual(result[5], 0.1001, delta=1e-10)
        self.assertAlmostEqual(result[6], 0.3763, delta=1e-10)
        self.assertAlmostEqual(result[7], 0.7177, delta=1e-10)
        self.assertAlmostEqual(result[8], 0.934, delta=1e-10)

    def test_player_names_with_bad_completion(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(
            code.player_names_with_bad_completion('qbdata.txt'),
            [['Matt', 'Hasselbeck'], ['Jimmy', 'Clausen'], ['Kyle', 'Orton'],
             ['Jason', 'Campbell'], ['Matt', 'Cassel'], ['Mark', 'Sanchez'],
             ['Alex', 'Smith'], ['Kerry', 'Collins'], ['Derek', 'Anderson'],
             ['Ryan', 'Fitzpatrick'], ['Donovan', 'McNabb']]
        )

    def test_query_field_if(self):
        code,clean = load_module('hw6')
        self.assertIsNotNone(code, 'Cannot find module :(')

        self.assertEqual(code.query_field_if('ID', 'ID', '3', 'littledata.txt'), '3')
        self.assertEqual(code.query_field_if('ColA', 'ID', '3', 'littledata.txt'), 'Qux')
        self.assertEqual(code.query_field_if('ColB', 'ID', '3', 'littledata.txt'), 'delta')

        self.assertEqual(code.query_field_if('ID', 'ColA', 'Foo', 'littledata.txt'), '0')
        self.assertEqual(code.query_field_if('ColA', 'ColA', 'Foo', 'littledata.txt'), 'Foo')
        self.assertEqual(code.query_field_if('ColB', 'ColA', 'Foo', 'littledata.txt'), 'alpha')

        self.assertEqual(code.query_field_if('ID', 'ColB', 'Gamma', 'littledata.txt'), '2')
        self.assertEqual(code.query_field_if('ColA', 'ColB', 'Gamma', 'littledata.txt'), 'Baz')
        self.assertEqual(code.query_field_if('ColB', 'ColB', 'Gamma', 'littledata.txt'), 'Gamma')

        #

        self.assertEqual(code.query_field_if('Team', 'Last', 'Roethlisberger', 'qbdata.txt'), 'PIT')
        self.assertEqual(code.query_field_if('Rating', 'First', 'Peyton', 'qbdata.txt'), '91.9')
        self.assertEqual(code.query_field_if('Last', 'Team', 'BUF', 'qbdata.txt'), 'Fitzpatrick')
        self.assertEqual(code.query_field_if('First', 'Yards', '4002', 'qbdata.txt'), 'Eli')


if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest
import sys
import subprocess
import os

from remove_duplicates import process_string, remove_duplicates


class UnitTestRemoveDuplicates(unittest.TestCase):
    def test_process_string(self):
        self.assertEqual(process_string('a,b,c\n'), ['a', 'b', 'c'])
        self.assertEqual(process_string('  a ,b ,c\n'), ['  a ', 'b ', 'c'])

class FuncTestRemoveDuplicates(unittest.TestCase):
    
    def template(self, input, output, column):
        result = subprocess.run(
            ['python', 'remove_duplicates.py', input, 'tests/test_output_check.csv', column],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        # print(result.stdout, result.stderr)
        with open('tests/test_output_check.csv', 'r') as actual, open(output, 'r') as expected:
            expected_text = expected.readlines()
            actual_text = actual.readlines()
        self.assertEqual(expected_text, actual_text)
        os.remove('tests/test_output_check.csv')

    def test_functional_test1(self):
        self.template('tests/test1_input.csv', 'tests/test1_output.csv', 'id')
    def test_functional_test2(self):
        self.template('tests/test2_input.csv', 'tests/test2_output.csv', 'one')


if __name__ == '__main__':
    unittest.main()

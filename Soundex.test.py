# soundex.test.py

import unittest
from Soundex import generate_soundex, get_soundex_code

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")
        self.assertEqual(generate_soundex("Z"), "Z000")

    def test_simple_names(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Rubin"), "R150")

    def test_names_with_vowels(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Tymczak"), "T522")

    def test_edge_cases(self):
        self.assertEqual(generate_soundex("Pfister"), "P236")
        self.assertEqual(generate_soundex("Honeyman"), "H555")

    def test_get_soundex_code(self):
        self.assertEqual(get_soundex_code('A'), '0')
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('C'), '2')
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('L'), '4')
        self.assertEqual(get_soundex_code('M'), '5')
        self.assertEqual(get_soundex_code('R'), '6')
        self.assertEqual(get_soundex_code('1'), '0')  # Test non-letter character

if __name__ == '__main__':
    unittest.main()

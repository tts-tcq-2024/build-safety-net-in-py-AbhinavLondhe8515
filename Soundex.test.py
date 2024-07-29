import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):
    #empty string
    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    #single character
    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")

    #vowel start
    def test_vowel_start(self):
        self.assertEqual(generate_soundex("example"), "E251")
        self.assertEqual(generate_soundex("E"), "E000")

    #consonant start
    def test_consonant_start(self):
        self.assertEqual(generate_soundex("sound"), "S530")
        self.assertEqual(generate_soundex("Smith"), "S530")

    #repeated consonants
    def test_repeated_consonants(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")
        self.assertEqual(generate_soundex("Pfister"), "P236")

    #mixed case
    def test_mixed_case(self):
        self.assertEqual(generate_soundex("Example"), "E251")
        self.assertEqual(generate_soundex("SOUND"), "S530")
    
    #alphanumaric
    def test_non_alpha_characters(self):
        self.assertEqual(generate_soundex("S!ound"), "S530")
        self.assertEqual(generate_soundex("1234"), "1000")

    #long string
    def test_long_name(self):
        self.assertEqual(generate_soundex("Washington"), "W252")

if __name__ == '__main__':
    unittest.main()

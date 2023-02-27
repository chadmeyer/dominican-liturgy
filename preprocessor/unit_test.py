from process import *
import unittest

class TestFlex(unittest.TestCase) :

    def test_multisyllable_final_word(self):
        str_in = "He has ^sent de|^li|ver|ance to his ^peo|ple +"
        str_out = "He has sent deliverance to his \\flexfinalaccent{peo}\\flexpostaccent{ple} \\flexsymbol"
        self.assertEqual(process_flex(str_in.split()),str_out)

    def test_final_syllable_accent(self):
        str_in = "Through his ^ho|ly ^pro|phets he ^pro|mised of ^old +"
        str_out = "Through his holy prophets he promised \\flexvirtualfinalaccent{of} \\flexfinalsyllableaccent{old} \\flexsymbol"
        self.assertEqual(process_flex(str_in.split()),str_out)

    def test_multisyllable_penultimate_word_first(self):
        str_in = "When he ^calls on ^me, I will ^an|swer him; +"
        str_out = "When he calls on me, I will \\flexfinalaccent{an}\\flexpostaccent{swer} \\flexpostaccent{him;} \\flexsymbol"
        self.assertEqual(process_flex(str_in.split()),str_out)

    def test_multisyllable_penultimate_word_second(self):
        # Note this is made up; the accents are not real, but the in/out should be
        str_in = "When he ^calls on ^me, I will an|^swer him; +"
        str_out = "When he calls on me, I will an\\flexfinalaccent{swer} \\flexpostaccent{him;} \\flexsymbol"
        self.assertEqual(process_flex(str_in.split()),str_out)

if __name__ == '__main__':
    unittest.main()
import unittest

from libs.tabu_bigrams import parse_raw

class TestA2Q3StrParser(unittest.TestCase):
    def test_single_str(self):
        self.assertRaises(ValueError, parse_raw, "word")

    def test_single_int(self):
        self.assertRaises(ValueError, parse_raw, "6")

    def test_m_too_small(self):
        self.assertRaises(ValueError, parse_raw, "0 1 2 3")

    def test_m_too_big(self):
        self.assertRaises(ValueError, parse_raw, "37 1 2 3")

    def test_n_too_small(self):
        self.assertRaises(ValueError, parse_raw, "8 0 2 3")

    def test_n_too_big(self):
        self.assertRaises(ValueError, parse_raw, "8 101 2 3")

    def test_parsable_1(self):
        parsed = parse_raw("4 1 11 12 23")

        self.assertEqual(parsed.m, 4)
        self.assertEqual(parsed.n, 1)
        self.assertListEqual(parsed.bigrams, ["11", "12", "23"])

    def test_parsable_2(self):
        parsed = parse_raw("10 10 00 11 22 33 44 55")

        self.assertEqual(parsed.m, 10)
        self.assertEqual(parsed.n, 10)
        self.assertListEqual(parsed.bigrams, ["00", "11", "22", "33", "44", "55"])

if __name__ == "__main__":
    unittest.main()

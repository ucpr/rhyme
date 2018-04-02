import unittest
import rhyme


class Rhyme_test(unittest.TestCase):
    def test_conv2roman(self):
        self.assertEqual("okinawa", rhyme._converting_to_roman("沖縄"))
        self.assertEqual("okinawa", rhyme._converting_to_roman("オキナワ"))
        self.assertEqual("okinawa", rhyme._converting_to_roman("おきなわ"))

        self.assertEqual("toukyou", rhyme._converting_to_roman("東京"))
        self.assertEqual("bi-mu", rhyme._converting_to_roman("ビーム"))
        self.assertEqual("hokkaidou", rhyme._converting_to_roman("北海道"))
        self.assertEqual("kappura-men", rhyme._converting_to_roman("カップらーめん"))

    def test_fetch_vowel(self):
        self.assertEqual("oiaa", rhyme._fetch_vowel("okinawa"))
        self.assertEqual("ouou", rhyme._fetch_vowel("toukyou"))
        self.assertEqual("iu", rhyme._fetch_vowel("bi-mu"))
        self.assertEqual("oaiou", rhyme._fetch_vowel("hokkaidou"))
        self.assertEqual("auae", rhyme._fetch_vowel("kappura-men"))

    def test_find_rhyme_words(self):
        self.assertIn("ヨッピ川", rhyme._find_rhyme_words("oiaa"))
        self.assertIn("独特", rhyme._find_rhyme_words("ouou"))
        self.assertIn("マツタケ", rhyme._find_rhyme_words("auae"))
        self.assertIn("お買い得", rhyme._find_rhyme_words("oaiou"))


if __name__ == "__main__":
    unittest.main()

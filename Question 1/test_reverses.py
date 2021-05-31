import unittest
import reverses


class testReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverses.reverse(""), "")
    
    def test_single(self):
        self.assertEqual(reverses.reverse("abc"), "abc")

    def test_two_words(self):
        self.assertEqual(reverses.reverse("Hello World"), "World Hello")

    def test_sentence(self):
        self.assertEqual(reverses.reverse("My name is V Tadimeti"), "Tadimeti V is name My")


if __name__ == "__main__":
    unittest.main()

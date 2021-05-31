import unittest
import reverses


class testReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverses.reverse(""), "")
    
    def test_single(self):
        self.assertEqual(reverses.reverse("abc"), "abc")

    def test_two_words(self):
        self.assertEqual(reverses.reverse("Hello World"), "World Hello")


if __name__ == "__main__":
    unittest.main()

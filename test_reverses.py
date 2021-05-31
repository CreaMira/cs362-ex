import unittest
import reverses


class testReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverses.reverse(""), "")
    
    def test_single(self):
        self.assertEqual(reverses.reverse("abc"), "abc")


if __name__ == "__main__":
    unittest.main()

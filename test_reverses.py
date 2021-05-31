import unittest
import reverses


class testReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverses.reverse(""), "")


if __name__ == "__main__":
    unittest.main()

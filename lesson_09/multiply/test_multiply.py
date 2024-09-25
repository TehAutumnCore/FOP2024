import unittest
from multiply import multiply_3_numbers

class TestListMax(unittest.TestCase):

    def test_multiply_integers(self):
        result = multiply_3_numbers(2,3,4)
        self.assertEqual(result,24)

    def test_multiply_floats(self):
        result = multiply_3_numbers(2.5,1.5,2.0)
        self.assertEqual(result,7.5)

    # def test_3(self):
    #     print("test 3")

    # def test_4(self):
    #     print("test 4")

    # def test_5(self):
    #     print("test 5")



if __name__ == "__main__":
    unittest.main()
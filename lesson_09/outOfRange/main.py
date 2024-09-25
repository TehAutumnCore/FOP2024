# import unittest
# from functions import list_max

# class TestListMax(unittest.TestCase):
    
#     def test_1(self):
#         """Test a list of all positive values"""
#         a_list = [6,43,18,100,9,85]
#         result = list_max(a_list)
#         self.assertEqual(result,100)

#     def test_2(self):
#         """Test a list of all negative values"""
#         a_list = [-7,-1,-38,-2,-99]
#         result = list_max(a_list)
#         self.assertEqual(result,-1)

# if __name__ == "__main__":
#     unittest.main()

import unittest 
from functions import Dog

class TestListMax(unittest.TestCase):

    def test_1(self):
        """Instantiated a Dog object"""
        dog_1 = Dog("Fido", "Pitbull",2)
        self.assertIsInstance(dog_1, Dog, "Object is not an instance of Dog Class")
        self.assertEqual(dog_1._name, "Fido", "The name attribute is not a string")
        self.assertEqual(dog_1._age, 2, "The age attribute is not set correctly")


if __name__ == "__main__":
     unittest.main()
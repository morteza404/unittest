import sys

path = "/home/shahbazi/Desktop/project"

if path not in sys.path:
    sys.path.insert(0, path)


import unittest

from apps import pass_01

class NameTest(unittest.TestCase):  

    def test_check_pass(self):
        result = pass_01.check_pass("admin")
        self.assertEqual(result, True)

    def test_not_check_pass(self):        
        result = pass_01.check_pass("root") 
        self.assertEqual(result, False)

# if __name__ == "__main__":
#     unittest.main() 
          
!/vipul2097/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation

class Testsum(unittest.TestCase) :
  def test_list_int(self):
    #Test case to add two numbers
    data = [23, 32]
    result = summation (data)
    self.assertEqual (result, 55)

if _name_ == '_main_':
  unittest.main()

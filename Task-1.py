import unittest

def addition(a, b):
  return a + b

def subtraction(a, b):
  return a - b

def multiplication(a, b):
  if type(a) == int:
    if type(b) == int:
      return a * b

def division(a, b):
  if type(a) == int:
    if type(b) == int:
      return a / b


class CustomTests(unittest.TestCase): 
  def test_add_1(self):
    print(addition(4, 6))
  def test_add_2(self):
    print(addition(4))
  def test_add_3(self):
    print(addition("4", 6))

  def test_mul_1(self):
    print(multiplication(5, 6))
  def test_mul_2(self):
    print(multiplication(5))
  def test_mul_3(self):
    print(multiplication("sd", 6))
  
  def test_sub_1(self):
    print(subtraction(6, 2))
  def test_sub_2(self):
    print(subtraction(6))
  def test_sub_3(self):
    print(subtraction(6, "2"))

  def test_div_1(self):
    print(subtraction(8, 2))
  def test_div_2(self):
    print(subtraction(8))
  def test_div_3(self):
    print(subtraction(8, "2"))

if __name__ == '__main__':  
    unittest.main(verbosity = 2)
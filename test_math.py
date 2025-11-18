import unittest
from my_math import fibonacci, mean

class TestMyMath(unittest.TestCase):
    # ----- fibonacci-----
    # test if the fabonacci() returns expected values
    # i.e. fibonacci(0) = 0, fibonacci(1)= 1, ..., fibonacci(6)= 8
    def test_fibonacci_basic(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(6), 8)

    # test if an invalid value passed in will raise either an error  
    def test_fibonacci_bad_inputs(self):
        #test if error will raise when a negative number (-1) is passed in
        with self.assertRaises((TypeError, ValueError)):
            fibonacci(-1)

     	#test if error will raise when a float number (3.5) is passed in
        with self.assertRaises((TypeError, ValueError)):
            fibonacci(3.5)        

        #test if error will raise when an invalid type (string "7") is passed in
        with self.assertRaises((TypeError, ValueError)):
            fibonacci("7")        

    # ----- mean -----
    # test if the mean of a group of numbers passed in will return an expected result
    # use assertAlmostEqual() when comparing float numbers.
    def test_mean_basic(self):
        #the mean of numbers 1,2,3 is 2.0
        self.assertAlmostEqual(mean([1, 2, 3]), 2.0)

	#the mean of two numbers 1.5 and 2.5 is 2.0
        self.assertAlmostEqual(mean([1.5, 2.5]), 2.0)

        #the mean of four 0's is 0
        self.assertAlmostEqual(mean([0, 0, 0, 0]), 0.0)

    #test special cases
    def test_mean_singleton_and_mixed(self):
        #the mean of one number passed should be itself
        self.assertAlmostEqual(mean([42]), 42.0)
        #the mean of integer and float numbers mixed, i.e. 1, 2.0 and 3, should be 2.0.
        self.assertAlmostEqual(mean([1, 2.0, 3]), 2.0)

    #test error handles
    def test_mean_errors(self):
        #test if error will raise if no number is passed in.
        with self.assertRaises((ValueError, ZeroDivisionError)):
            mean([])
        #test if error will raise if an invalid data type (string "two") is passed in.
        with self.assertRaises((TypeError, ValueError)):
            mean([1, "two", 3])  

if __name__ == "__main__":
    unittest.main(verbosity=2)

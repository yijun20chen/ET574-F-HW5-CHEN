# Yi Jun Chen 24696599
import unittest
from my_math import fibonacci, mean, comb, stdev, binomial_cdf

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

    # ----- comb -----
    # test if the comb() returns expected values
    # i.e. comb(5, 2) = 10, comb(0, 0)= 1, ..., comb(6, 3)= 20
    def test_generic_comb(self):
        self.assertEqual(comb(5, 2), 10)
        self.assertEqual(comb(0, 0), 1)
        self.assertEqual(comb(6, 3), 20)
        self.assertEqual(comb(4, 4), 1)
        self.assertEqual(comb(7, 0), 1)
    
    # test if 0 is returned when k > n
    def test_comb_k_greater_than_n(self):
        self.assertEqual(comb(3, 5), 0)
        self.assertEqual(comb(0, 1), 0)

    # ----- stdev -----
    # test if the stdev() returns expected values
    def test_stdev_population_and_sample(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        # population standard deviation (ddof=0) is 2.0
        self.assertAlmostEqual(stdev(data, ddof=0), 2.0)
        # sample standard deviation (ddof=1) ~ 2.138089935
        self.assertAlmostEqual(stdev(data, ddof=1), 2.138089935299395)
    
    def test_stdev_empty_and_singleton(self):
        # test if error will raise when an empty list is passed in
        with self.assertRaises((ValueError, ZeroDivisionError)):
            stdev([], ddof=0)
        # test if error will raise when a singleton list is passed in with ddof=1
        with self.assertRaises((ValueError, ZeroDivisionError)):
            stdev([42], ddof=1)

    # ----- binomial_cdf -----
    def test_binomial_cdf_basic(self):
        # For n=2, p=0.5, P(X <= 1) = P(0) + P(1) = 0.25 + 0.5 = 0.75
        self.assertAlmostEqual(binomial_cdf(1, 2, 0.5), 0.75)

        # p = 0 -> X is always 0
        self.assertEqual(binomial_cdf(0, 5, 0.0), 1.0)
        # p = 1 -> X is always n
        self.assertEqual(binomial_cdf(4, 5, 1.0), 0.0)
        self.assertEqual(binomial_cdf(5, 5, 1.0), 1.0)
    
    def test_binomial_cdf_invalid_inputs(self):
        # test if error will raise when n is negative
        with self.assertRaises((TypeError, ValueError)):
            binomial_cdf(2, -5, 0.5)
        # test if error will raise when k is negative
        with self.assertRaises((TypeError, ValueError)):
            binomial_cdf(-1, 5, 0.5)
        # test if error will raise when p is out of range (>1)
        with self.assertRaises((TypeError, ValueError)):
            binomial_cdf(2, 5, 1.5)
        # test if error will raise when p is out of range (<0)
        with self.assertRaises((TypeError, ValueError)):
            binomial_cdf(2, 5, -0.2)

if __name__ == "__main__":
    unittest.main(verbosity=2)

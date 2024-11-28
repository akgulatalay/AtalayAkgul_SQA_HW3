import unittest
import src.primeNeighbor as pn

class PrimeNeighborTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    
    def test_with_valid_prime_input(self):
        actualResult = pn.primeNeighbor(upperBound=29)
        expectedResult = 29
        self.assertEqual(expectedResult, actualResult)

    def test_with_upper_bound_prime(self):
        actualResult = pn.primeNeighbor(upperBound=1000)
        expectedResult = 997
        self.assertEqual(expectedResult, actualResult)

    def test_with_non_prime_input(self):
        actualResult = pn.primeNeighbor(upperBound=30)
        expectedResult = 29
        self.assertEqual(expectedResult, actualResult)

    def test_with_invalid_string_input(self):
        actualResult = pn.primeNeighbor(upperBound="hello")
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)

    def test_with_input_below_2(self):
        actualResult = pn.primeNeighbor(upperBound=1)
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)

    def test_with_input_above_1000(self):
        actualResult = pn.primeNeighbor(upperBound=1001)
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)

    def test_with_negative_input(self):
        actualResult = pn.primeNeighbor(upperBound=-10)
        expectedResult = 0  
        self.assertEqual(expectedResult, actualResult)

    def test_with_float_input(self):
        actualResult = pn.primeNeighbor(upperBound=25.5)
        expectedResult = 0  
        self.assertEqual(expectedResult, actualResult)

    def test_with_large_string_input(self):
        actualResult = pn.primeNeighbor(upperBound="longtext")
        expectedResult = 0  
        self.assertEqual(expectedResult, actualResult)

    def test_with_special_character_input(self):
        actualResult = pn.primeNeighbor(upperBound="#$%")
        expectedResult = 0  
        self.assertEqual(expectedResult, actualResult)

    def test_with_list_input(self):
        with self.assertRaises(TypeError):
            pn.primeNeighbor(upperBound=[10, 20])  

    def test_with_dictionary_input(self):
        with self.assertRaises(TypeError):
            pn.primeNeighbor(upperBound={"num": 10})  

    def test_with_prime_upper_bound(self):
        actualResult = pn.primeNeighbor(upperBound=13)
        expectedResult = 13
        self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
    unittest.main()

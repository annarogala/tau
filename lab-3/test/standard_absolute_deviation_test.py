import unittest
from src.standard_absolute_deviation import StandardAbsoluteDeviationCalculator

class TestStandardAbsoluteDeviationCalculator(unittest.TestCase):

    def test_correct_output(self):
        numbers = [1, 2, 3, 4, 5]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertEqual(result, 1.2)

    def test_output_is_not_negative(self):
        numbers = [1, 2, 3, 4, 5]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertGreaterEqual(result, 0)

    def test_result_is_float(self):
        numbers = [1, 2, 3, 4, 5]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertIsInstance(result, float)

    def test_result_is_not_integer(self):
        numbers = [1, 2, 3, 4]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertIsNot(result, int)

    def test_empty_input_list(self):
        with self.assertRaises(ValueError, msg="The input needs to be a list"):
            numbers = "not_a list"
            calculator = StandardAbsoluteDeviationCalculator(numbers)
            calculator.calculate()

    def test_empty_input_list(self):
        with self.assertRaises(ValueError, msg="Input list cannot be empty"):
            calculator = StandardAbsoluteDeviationCalculator([])
            calculator.calculate()

    def test_valid_inputs(self):
        with self.assertRaises(ValueError, msg="Input list must contain only integers and floats"):
            numbers = [1, 2, 3, "4", 5]
            calculator = StandardAbsoluteDeviationCalculator(numbers)
            calculator.calculate()

    def test_correct_output_with_only_negative_integers(self):
        numbers = [-1, -2, -3, -4, -5]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertAlmostEqual(result, 1.2)

    def test_correct_output_with_mixed_positive_and_negative_integers(self):
        numbers = [-1, 2, -3, 4, -5]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertAlmostEqual(result, 2.88)

    def test_single_integer_input(self):
        numbers = [7]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertAlmostEqual(result, 0.0)

    def test_zeros_input(self):
        numbers = [0, 0, 0, 0, 0]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertAlmostEqual(result, 0.0)

    def test_single_large_integer_input(self):
        numbers = [10**9]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertAlmostEqual(result, 0.0)

    def test_large_positive_integers(self):
        numbers = list(range(1, 10001))
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertAlmostEqual(result, 2500.0, delta=2.9e-03)

    def test_large_negative_integers(self):
        numbers = list(range(-10000, 0))
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertAlmostEqual(result, 2500.0, delta=2.9e-03)

    def test_large_mixed_positive_and_negative_integers(self):
        numbers = list(range(-5000, 5001))
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        result = calculator.calculate()
        self.assertAlmostEqual(result, 2500.25, delta=2.0e-03)

if __name__ == "__main__":
    unittest.main()

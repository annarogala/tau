import pytest
from src.standard_absolute_deviation import StandardAbsoluteDeviationCalculator


def test_correct_output():
    numbers = [1, 2, 3, 4, 5]
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == 1.2

def test_empty_input_list():
    with pytest.raises(ValueError, match="The input needs to be a list"):
        numbers = "not_a list"
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        calculator.calculate()

def test_empty_input_list():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        calculator = StandardAbsoluteDeviationCalculator([])
        calculator.calculate()

def test_valid_inputs():
    with pytest.raises(ValueError, match="Input list must contain only integers"):
        numbers = [1, 2, 3, "4", 5]
        calculator = StandardAbsoluteDeviationCalculator(numbers)
        calculator.calculate()

def test_correct_output_with_only_negative_integers():
    numbers = [-1, -2, -3, -4, -5]
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == 1.2

def test_correct_output_with_mixed_positive_and_negative_integers():
    numbers = [-1, 2, -3, 4, -5]
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == 2.88

def test_single_integer_input():
    numbers = [7]
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == 0.0

def test_zeros_input():
    numbers = [0, 0, 0, 0, 0]
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == 0.0

def test_single_large_integer_input():
    numbers = [10**9]
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == 0.0

def test_large_positive_integers():
    numbers = list(range(1, 10001))
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == pytest.approx(2500.0, abs=2.9e-03)

def test_large_negative_integers():
    numbers = list(range(-10000, 0))
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == pytest.approx(2500.0, abs=2.9e-03)

def test_large_mixed_positive_and_negative_integers():
    numbers = list(range(-5000, 5001))
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == pytest.approx(2500.25, abs=2.0e-03)

if __name__ == "__main__":
    pytest.main()

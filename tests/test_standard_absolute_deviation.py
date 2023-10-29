import pytest
from app.standard_absolute_deviation import StandardAbsoluteDeviationCalculator


def test_valid_input_and_output():
    numbers = [1, 2, 3, 4, 5]
    calculator = StandardAbsoluteDeviationCalculator(numbers)
    result = calculator.calculate()
    assert result == 1.2

if __name__ == "__main__":
    pytest.main()

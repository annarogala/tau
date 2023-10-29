class StandardAbsoluteDeviationCalculator:
    def __init__(self, numbers):
        if not isinstance(numbers, list):
            raise ValueError("The input needs to be a list")
        if len(numbers) == 0:
            raise ValueError("Input list cannot be empty")
        if not all(isinstance(x, int) for x in numbers):
            raise ValueError("Input list must contain only integers")

        self.numbers = numbers

    def calculate(self):
        mean = sum(self.numbers) / len(self.numbers)
        sum_of_absolute_differences = sum(abs(x - mean) for x in self.numbers)
        standard_absolute_deviation = sum_of_absolute_differences / len(self.numbers)
        return standard_absolute_deviation

my_numbers = [1, 2, 3, 4, 5]
calculator = StandardAbsoluteDeviationCalculator(my_numbers)
result = calculator.calculate()
print(result)
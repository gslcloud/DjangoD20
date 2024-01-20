class Example1:
    """A class representing an example implementation."""

    def method1(self, num: int) -> int:
        """A method that returns the square of the input number.

        Args:
            num (int): The input number.

        Returns:
            int: The square of the input number.
        """
        return num ** 2

    def method2(self, value: float) -> float:
        """A method that returns the square root of the input value.

        Args:
            value (float): The input value.

        Returns:
            float: The square root of the input value.
        """
        return value ** 0.5

    def execute(self):
        """Executes the example code.

        Add here the necessary logic for executing the example code.
        """
        # Add your implementation here

# Add unit tests
import unittest


class Example1Test(unittest.TestCase):
    def test_method1_with_valid_input(self):
        instance = Example1()
        result = instance.method1(3)
        self.assertEqual(result, 9)

    def test_method1_with_zero_input(self):
        instance = Example1()
        result = instance.method1(0)
        self.assertEqual(result, 0)

    def test_method2_with_valid_input(self):
        instance = Example1()
        result = instance.method2(25.0)
        self.assertEqual(result, 5.0)

    def test_method2_with_negative_input(self):
        instance = Example1()
        result = instance.method2(-9.0)
        self.assertEqual(result, ValueError)

    def test_method2_with_zero_input(self):
        instance = Example1()
        result = instance.method2(0.0)
        self.assertEqual(result, 0.0)

# Run the unit tests if this script is executed directly
if __name__ == "__main__":
    unittest.main()
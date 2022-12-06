import unittest
from model.calculator import Calculator


class TestCalculator(unittest.TestCase):


    def init(self, a, b):
        self.calc = Calculator(a, b)

    def destroy(self):
        del self.calc
    # AAA
    def test_sum(self):
        # arrange
        a = 10
        b = 20
        self.init(a, b)
        expected = 30

        # action
        actual = self.calc.sum()

        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

        self.destroy()

    def test_sub(self):
        # arrange
        a = 10
        b = 7
        self.init(a, b)
        expected = 3

        # action
        actual = self.calc.sub()


        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

        self.destroy()

    def test_mul(self):
        # arrange
        a = 8
        b = 7
        self.init(a, b)
        expected = 56

        # action
        actual = self.calc.mul()

        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

        self.destroy()

    def test_div(self):
        # arrange
        a = 18
        b = 7
        self.init(a, b)
        expected = 2


        # action
        actual = self.calc.div()

        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

        self.destroy()


if __name__ == "__main__":
    unittest.main()
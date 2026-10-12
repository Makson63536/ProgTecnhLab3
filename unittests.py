import unittest

from counter import Counter
from static_method import MetresToMillimetres
from strategy import (
    Discount10,
    Discount20,
    Discount50,
    PriceCalculator,
    RegularPrice,
)
from student import Student


class TestMetresToMillimetres(unittest.TestCase):
    def test_convert(self):
        result = MetresToMillimetres.convert(100)
        self.assertEqual(result, 100000)


class TestCounter(unittest.TestCase):
    def test_initial_value(self):
        counter = Counter()
        self.assertEqual(counter.get_value(), 0)

    def test_increase(self):
        counter = Counter()
        counter.increase()
        self.assertEqual(counter.get_value(), 1)

    def test_decrease(self):
        counter = Counter()
        counter.decrease()
        self.assertEqual(counter.get_value(), -1)

    def test_custom_initial_value(self):
        counter = Counter(10)
        self.assertEqual(counter.get_value(), 10)


class TestStudent(unittest.TestCase):
    def test_student_attributes(self):
        student = Student("Иван Иванов", "222000", 4.7)

        self.assertEqual(student.name, "Иван Иванов")
        self.assertEqual(student.group, "222000")
        self.assertEqual(student.average_grade, 4.7)


class TestPriceCalculator(unittest.TestCase):
    def test_regular_price(self):
        calculator = PriceCalculator(RegularPrice())
        self.assertEqual(calculator.calculate(1000), 1000)

    def test_discount_10(self):
        calculator = PriceCalculator(Discount10())
        self.assertEqual(calculator.calculate(1000), 900)

    def test_discount_20(self):
        calculator = PriceCalculator(Discount20())
        self.assertEqual(calculator.calculate(1000), 800)

    def test_discount_50(self):
        calculator = PriceCalculator(Discount50())
        self.assertEqual(calculator.calculate(1000), 500)

    def test_negative_price(self):
        calculator = PriceCalculator(RegularPrice())

        with self.assertRaises(ValueError):
            calculator.calculate(-100)


if __name__ == "__main__":
    unittest.main()

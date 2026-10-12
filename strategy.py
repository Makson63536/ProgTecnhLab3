class RegularPrice:
    def calculate(self, price):
        return price


class Discount10:
    def calculate(self, price):
        return price * 0.9


class Discount20:
    def calculate(self, price):
        return price * 0.8


class Discount50:
    def calculate(self, price):
        return price * 0.5


class PriceCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, price):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")

        return self.strategy.calculate(price)


def main():
    price = 1000

    strategies = [
        ("Без скидки", RegularPrice()),
        ("Скидка 10%", Discount10()),
        ("Скидка 20%", Discount20()),
        ("Скидка 50%", Discount50()),
    ]

    for name, strategy in strategies:
        calculator = PriceCalculator(strategy)
        result = calculator.calculate(price)
        print(f"{name}: {result:.2f} руб.")


if __name__ == "__main__":
    main()

class Counter:
    def __init__(self, start_value=0):
        self.value = start_value

    def increase(self):
        self.value += 1

    def decrease(self):
        self.value -= 1

    def get_value(self):
        return self.value


def main():
    counter = Counter()

    print(f"Начальное значение: {counter.get_value()}")

    counter.increase()
    counter.increase()
    print(f"После двойного увеличения: {counter.get_value()}")

    counter.decrease()
    print(f"После уменьшения: {counter.get_value()}")


if __name__ == "__main__":
    main()

"""Переконвертирует метры в миллиметры."""


class MetresToMillimetres:
    """Переконвертирует метры в миллиметры."""

    @staticmethod
    def convert(metres):
        """Метр = 1000 миллиметров."""
        return metres * 1000


def main():
    """Перевод 75 метров 75000 миллиметра."""
    length = 75
    result = MetresToMillimetres.convert(length)

    print(f"Метры: {length}")
    print(f"Миллиметры: {result}")


if __name__ == "__main__":
    main()

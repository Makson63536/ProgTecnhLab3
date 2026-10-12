class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Группа: {self.group}")
        print(f"Средний балл: {self.average_grade}")


def main():
    student = Student("Сиренко Максим", "220042-11", 4.8)
    student.display_info()


if __name__ == "__main__":
    main()

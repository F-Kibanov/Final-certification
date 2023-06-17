
class Counter:
    """Класс счетчик"""

    def __init__(self, count):
        self.__count = count

    def get_count(self):
        return self.__count

    def add(self):
        self.__count += 1

    def print_count(self):
        print(f'The total number of animals: {self.__count}')

# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.

class Counter:  # создаем класс
    def __init__(self, score):
        self.score = score  # атрибут текущего значения счетчика

    def increment(self, addition_score):  # метод увеличения значения счетчика
        self.score += addition_score

    def deincrement(self, subtraction_score):  # метод уменьшения значения счетчика
        self.score -= subtraction_score


counter = Counter(500)  # создание экземпляра
print(counter.__dict__)  # вывод значений этого экземпляра
counter.increment(500)  # вызов метода класса
print(counter.__dict__)  # вывод значений этого экземпляра
counter.deincrement(300)  # вызов метода класса
print(counter.__dict__)  # вывод значений этого экземпляра

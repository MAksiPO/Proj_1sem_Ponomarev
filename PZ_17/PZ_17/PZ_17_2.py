# Создание базового класса "Работник" и его наследование для создания классов
# "Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
# "работать" и "получать зарплату", а классы-наследники будут иметь свои
# уникальные методы и свойства, такие как "управлять командой" и "проектировать
# системы".

class Worker:  # создание класса работник
    def __init__(self, name):
        self.name = name

    def work(self):
        print('Работать')

    def get_paid(self):
        print("Получил зарплату")


class Manager(Worker):  # создание класса менеджер с наследованием класса Работник
    def __init__(self, people_in_teem, name):
        self.people_in_teem = people_in_teem
        super().__init__(name)

    def teem_manage(self):
        print("Управлять командой")


class Engineer(Worker):  # создание класса инженер с наследованием класса Работник

    def system_design(self):
        print("Проектировать системы")


worker = Worker("Рабочий")  # создание экземпляра класса рабочий
manager = Manager(5, "Глеб")  # создание экземпляра класса менеджер
engineer = Engineer("Валерий")  # создание экземпляра класса инженер

print(worker.__dict__)  # проверяем свойства класса
worker.work()  # вызов метода класса
worker.get_paid()  # вызов метода класса

print(manager.__dict__)  # проверяем свойства класса
manager.work()  # вызов наследуемого метода класса
manager.get_paid()  # вызов наследуемого метода класса
manager.teem_manage()  # вызов метода класса

print(engineer.__dict__)  # проверяем свойства класса
engineer.work()  # вызов наследуемого метода класса
engineer.get_paid()  # вызов наследуемого метода класса
engineer.system_design()  # вызов метода класса

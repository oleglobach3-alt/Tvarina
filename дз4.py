
class Tvarina:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print("Тварина видає звук")

    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age} років")


class Sobaka(Tvarina):
    def sound(self):
        print("Гав-гав!")

    def guard(self):
        print(f"{self.name} охороняє дім.")


class Kit(Tvarina):
    def sound(self):
        print("Мяу!")

    def climb(self):
        print(f"{self.name} лізе на дерево.")


sobaka = Sobaka("Бім", 3)
kit = Kit("Мурчик", 2)

sobaka.info()
sobaka.sound()
sobaka.guard()

kit.info()
kit.sound()
kit.climb()

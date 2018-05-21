class PasExeption(Exception):
    def __init__(self):
        self._mas = "Некорерктно введен возраст"
    def __str__(self):
        return self._mas


class Pasanger:
    def __init__(self, name, age):
        if not(type(age) is int):
            raise PasExeption
        self._name = name
        self._age = age
    @property
    def Name(self):
        return self._name
    @Name.setter
    def Name(self, value):
        self._name = value
    @property
    def Age(self):
        return self._age
    @Age.setter
    def Age(self, value):
        if not(type(value) is int):
            raise PasExeption
        self._age = value



if __name__=='__main__':
    pas1 = Pasanger('Рома', 20)
    pas2 = Pasanger('Данил', 'Двадцать')
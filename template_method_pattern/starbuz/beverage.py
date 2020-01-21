from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print('물 끓이는 중')

    def pour_in_cup(self):
        print('컵에 따르는 중')


class Tea(CaffeineBeverage):

    def brew(self):
        print('차를 우리는 중')

    def add_condiments(self):
        print('레몬을 추가하는 중')


class Coffee(CaffeineBeverage):

    def brew(self):
        print('필터로 커피를 우리는 중')

    def add_condiments(self):
        print('설탕과 커피를 추가하는 중')

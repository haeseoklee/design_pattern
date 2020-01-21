from abc import ABCMeta, abstractmethod


class CaffeineBeverageWithHook(metaclass=ABCMeta):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customers_wants_condiments():
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

    def customers_wants_condiments(self):
        return True


class TeaWithHook(CaffeineBeverageWithHook):

    def brew(self):
        print('차를 우리는 중')

    def add_condiments(self):
        print('레몬을 추가하는 중')

    def customers_wants_condiments(self):
        answer = input('차에 레몬을 넣어드릴까요? ').lower()
        return True if 'y' in answer else False


class CoffeeWithHook(CaffeineBeverageWithHook):

    def brew(self):
        print('필터로 커피를 우리는 중')

    def add_condiments(self):
        print('설탕과 커피를 추가하는 중')

    def customers_wants_condiments(self):
        answer = input('커피에 우유와 설탕을 넣어드릴까요?').lower()
        return True if 'y' in answer else False

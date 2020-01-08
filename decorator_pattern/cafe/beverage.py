from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):

    def __init__(self):
        self.description = '제목없음'

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


class Espresso(Beverage):

    def __init__(self):
        self.description = '에스프레소'

    def cost(self):
        return 1.99

class HouseBlend(Beverage):

    def __init__(self):
        self.description = '하우스 블랜드 커피'

    def cost(self):
        return 0.89
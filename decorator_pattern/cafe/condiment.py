from abc import ABCMeta, abstractmethod
from .beverage import Beverage

class CondimentDecorator(Beverage, metaclass=ABCMeta):

    @abstractmethod
    def get_description(self):
        pass


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', 모카'

    def cost(self):
        return self.beverage.cost() + 0.20

class Whip(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', 휘핑크림'

    def cost(self):
        return self.beverage.cost() + 0.3
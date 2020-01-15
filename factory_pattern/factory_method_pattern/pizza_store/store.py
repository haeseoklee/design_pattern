from abc import ABCMeta, abstractmethod
from .pizza import (
    Pizza, 
    NYStyleCheesePizza, 
    ChicagoStyleCheesePizza
)

class PizzaStore(metaclass=ABCMeta):

    def order_pizza(self, type):
        # pizza 에는 Pizza 객체가 담긴다
        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, type):
        pass

class NYPizzaStore(PizzaStore):

    def create_pizza(self, item):
        if item == 'cheese':
            return NYStyleCheesePizza()
        elif item == 'veggie':
            pass
            # return NYStyleVeggiePizza()
        elif item == 'clam':
            pass
            # return NYStyleClamPizza()
        elif item == 'pepperoni':
            pass
            # return NYStylePepperoniPizza()
        else:
            return None


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, item):
        if item == 'cheese':
            return ChicagoStyleCheesePizza()
        elif item == 'veggie':
            pass
            # return ChicagoStyleVeggiePizza()
        elif item == 'clam':
            pass
            # return ChicagoStyleClamPizza()
        elif item == 'pepperoni':
            pass
            # return ChicagoStylePepperoniPizza()
        else:
            return None

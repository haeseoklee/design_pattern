from abc import ABCMeta, abstractmethod
from .pizza import (
    Pizza, 
    CheesePizza,
    ClamPizza
)
from pizza_ingredient.ingredient_factory import(
    NYPizzaIngredientFactory,
    ChicagoPizzaIngredientFactory
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
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if item == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('New York Style Cheese Pizza')
        elif item == 'veggie':
            pass
            # pizza = VeggiePizza(ingredient_factory)
            # pizza.set_name('New York Style Veggie Pizza')
        elif item == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('New York Style Clam Pizza')
        elif item == 'pepperoni':
            pass
            # pizza = PepperoniPizza(ingredient_factory)
            # pizza.set_name('New York Style Pepperoni Pizza')
        else:
            pizza = None
        return pizza


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, item):
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if item == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('Chicago Style Cheese Pizza')
        elif item == 'veggie':
            pass
            # pizza = VeggiePizza(ingredient_factory)
            # pizza.set_name('Chicago Style Cheese Pizza')
        elif item == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('Chicago Style Clam Pizza')
        elif item == 'pepperoni':
            pass
            # pizza = PepperoniPizza(ingredient_factory)
            # pizza.set_name('Chicago Style Pepperoni Pizza')
        else:
            pizza = None
        return pizza
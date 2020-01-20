from abc import ABCMeta, abstractmethod

class Pizza(metaclass=ABCMeta):

    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print('Preparing {}'.format(self.name))
        print('Tossoing dough...')
        print('Adding sauce...')
        print('Adding toppings: ')
        print(' '.join(self.toppings))

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self.name


class NYStyleCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append('Grated Reggiano Cheese')

class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')

    def cut(self):
        print('Cutting the pizza into square slices')



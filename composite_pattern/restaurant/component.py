from abc import ABCMeta, abstractmethod
from .iterator import CompositeIterator, NullIterator


class MenuComponent(metaclass=ABCMeta):

    def add(self, menu_component):
        raise Exception

    def remove(self, menu_component):
        raise Exception

    def get_child(self, index):
        raise Exception

    def get_name(self):
        raise Exception

    def get_description(self):
        raise Exception

    def get_price(self):
        raise Exception

    def is_vegetarian(self):
        raise Exception

    def print_menu(self):
        raise Exception

    @abstractmethod
    def create_iterator(self):
        raise Exception


class MenuItem(MenuComponent):

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.vegetarian = kwargs['vegetarian']
        self.price = kwargs['price']

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def print_menu(self):
        print(
            '{} {}, {}  -- {}'.format(
                self.get_name(),
                '(v)' if self.is_vegetarian() else '',
                self.get_price(),
                self.get_description()))

    def create_iterator(self):
        return NullIterator()


class Menu(MenuComponent):

    def __init__(self, **kwargs):
        self.menu_components = []
        self.name = kwargs['name']
        self.description = kwargs['description']

    def add(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def get_child(self, index):
        return self.menu_components[index]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def print_menu(self):
        print('{} ,{} \n{}'.format(self.get_name(), self.get_description(), '-'*30))

    def create_iterator(self):
        return CompositeIterator(*[iter.create_iterator() for iter in self.menu_components])

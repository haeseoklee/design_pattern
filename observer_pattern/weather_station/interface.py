from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    
    @abstractmethod
    def register_observer(self, obj):
        pass
    
    @abstractmethod
    def remove_observer(self, obj):
        pass

    @abstractmethod
    def notify_observer(self):
        pass


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

class DisplayElement(metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass
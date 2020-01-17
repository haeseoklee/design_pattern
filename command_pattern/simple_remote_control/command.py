from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light


    def execute(self):
        self.light.on()

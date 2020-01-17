from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class MecroCommand(Command):

    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()



class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class FanOnCommand(Command):

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.on()

    def undo(self):
        self.fan.off()


class FanOffCommand(Command):

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.off()

    def undo(self):
        self.fan.on()


class DoorUpCommand(Command):

    def __init__(self, door):
        self.door = door

    def execute(self):
        self.door.up()

    def undo(self):
        self.door.down()

class DoorDownCommand(Command):

    def __init__(self, door):
        self.door = door

    def execute(self):
        self.door.down()

    def undo(self):
        self.door.up()


class StereoOnWithCDCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()

    def undo(self):
        self.stereo.off()


class StereoOffCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
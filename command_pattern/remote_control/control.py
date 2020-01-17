from abc import ABCMeta, abstractmethod
from .receiver import (
    Light,
    Fan,
    Stereo
)

class RemoteController:

    def __init__(self):
        self.on_commands = [None for _ in range(5)]
        self.off_commands = [None for _ in range(5)]
        self.undo_command = None

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pressed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pressed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pressed(self):
        if self.undo_command is not None:
            self.undo_command.undo() 

    def __str__(self):
        return '\n'.join([
            '[slot {}]: {}, {}'.format(i, on, off) for i, (on, off) in enumerate(zip(self.on_commands, self.off_commands))
        ]) + '\n' + '[undo]: {}'.format(self.undo_command)


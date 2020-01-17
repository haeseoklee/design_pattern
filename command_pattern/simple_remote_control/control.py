from .command import LightOnCommand


class SimpleRemoteControl:

    def set_command(self, command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()
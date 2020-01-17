from simple_remote_control.control import SimpleRemoteControl
from simple_remote_control.command import LightOnCommand as LightOnCommand2
from simple_remote_control.receiver import Light as Light2

from remote_control.control import RemoteController 
from remote_control.command import *
from remote_control.receiver import *


def simple_controller_example():
    light = Light2()
    light_on_command = LightOnCommand2(light)
    simple_remote_control = SimpleRemoteControl()
    simple_remote_control.set_command(light_on_command)

    simple_remote_control.button_was_pressed()
    simple_remote_control.button_was_pressed()
    simple_remote_control.button_was_pressed()


def remote_controller_example():
    living_room_light = Light('거실')
    kitchen_light = Light('부엌')
    ceiling_fan = Fan('거실')
    garage_door = Door('차고')
    stereo = Stereo('거실')

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)
    ceiling_fan_on = FanOnCommand(ceiling_fan)
    ceiling_fan_off = FanOffCommand(ceiling_fan)
    garage_door_up = DoorUpCommand(garage_door)
    garage_door_down = DoorDownCommand(garage_door)
    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    remote_controller = RemoteController()
    remote_controller.set_command(0, living_room_light_on, living_room_light_off)
    remote_controller.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_controller.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_controller.set_command(3, stereo_on_with_cd, stereo_off)

    print(remote_controller)
    remote_controller.on_button_was_pressed(0)
    remote_controller.off_button_was_pressed(0)
    remote_controller.on_button_was_pressed(1)
    remote_controller.off_button_was_pressed(1)
    remote_controller.on_button_was_pressed(2)
    remote_controller.off_button_was_pressed(2)
    remote_controller.on_button_was_pressed(3)
    remote_controller.off_button_was_pressed(3)
    print(remote_controller)
    remote_controller.undo_button_was_pressed()


    print('{}{}{}'.format('-'*20, ' 매크로 모드 ', '-'*20))
    party_on = [living_room_light_on, stereo_on_with_cd]
    party_off = [living_room_light_off, stereo_off]
    party_on_mecro = MecroCommand(party_on)
    party_off_mecro = MecroCommand(party_off)
    remote_controller.set_command(4, party_on_mecro, party_off_mecro)
    remote_controller.on_button_was_pressed(4)
    remote_controller.on_button_was_pressed(4)
    remote_controller.on_button_was_pressed(4)
    remote_controller.undo_button_was_pressed()



def main():
    remote_controller_example()
    


if __name__ == '__main__':
    main()
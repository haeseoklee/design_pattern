from gumble_machine.machine import GumbleMachine


def main():
    gumble_machine = GumbleMachine(10)

    gumble_machine.insert_quarter()
    print(gumble_machine.state)
    gumble_machine.turn_crank()
    print(gumble_machine.state)

    gumble_machine.insert_quarter()
    gumble_machine.turn_crank()
    print(gumble_machine.state)

    gumble_machine.insert_quarter()
    gumble_machine.turn_crank()
    print(gumble_machine.state)

    gumble_machine.insert_quarter()
    gumble_machine.turn_crank()
    print(gumble_machine.state)

    gumble_machine.insert_quarter()
    gumble_machine.turn_crank()
    print(gumble_machine.state)


if __name__ == '__main__':
    main()

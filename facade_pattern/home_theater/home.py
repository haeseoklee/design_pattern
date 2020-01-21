class Amplifier:

    def on(self):
        print('엠프를 켭니다')

    def off(self):
        print('엠프를 끕니다')

    def set_dvd(self):
        print('dvd를 세팅합니다')

    def set_surround_sound(self):
        print('서라운드 음향으로 세팅합니다')

    def set_volume(self, volume):
        print('음향을 {}로 설정합니다'.format(volume))


class Tuner:
    pass


class CdPlayer:
    pass


class DvdPlayer:

    def on(self):
        print('dvd를 켭니다')

    def off(self):
        print('dvd를 끕니다')

    def play(self, movie):
        print('dvd에서 {}를 재생시킵니다'.format(movie))

    def stop(self):
        print('dvd를 정지합니다')

    def eject(self):
        print('dvd에서 cd를 빼냅니다')


class Projector:

    def on(self):
        print('프로젝터를 켭니다')

    def off(self):
        print('프로젝터를 끕니다')

    def wide_screen_mode(self):
        print('프로젝터를 넓은 화면 모드로 전환합니다')


class TheaterLights:

    def on(self):
        print('조명을 켭니다')

    def dim(self, light):
        print('조명 밝기를 {}로 설정합니다'.format(light))


class Screen:

    def up(self):
        print('스크린을 올립니다')

    def down(self):
        print('스크린을 내립니다')


class PopcornPopper:

    def on(self):
        print('팝콘 기계를 켭니다')

    def off(self):
        print('팝콘 기계를 끕니다')

    def pop(self):
        print('팝콘을 튀깁니다')

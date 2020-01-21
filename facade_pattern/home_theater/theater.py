from .home import *


class HomeTheaterFacade:

    def __init__(self, **kwargs):
        self.amp = kwargs['amp']
        self.tuner = kwargs['tuner']
        self.dvd = kwargs['dvd']
        self.cd = kwargs['cd']
        self.projector = kwargs['projector']
        self.screen = kwargs['screen']
        self.lights = kwargs['lights']
        self.popper = kwargs['popper']

    def watch_movie(self, movie):
        print('영화를 볼 준비가 되었습니다')
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_dvd()
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print('영화관 모드를 종료합니다')
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

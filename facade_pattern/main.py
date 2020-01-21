from home_theater.home import *
from home_theater.theater import HomeTheaterFacade


def main():
    home_theater_facade = HomeTheaterFacade(
            amp=Amplifier(),
            tuner=Tuner(),
            dvd=DvdPlayer(),
            cd=CdPlayer(),
            projector=Projector(),
            screen=Screen(),
            lights=TheaterLights(),
            popper=PopcornPopper()
        )
    home_theater_facade.watch_movie('어벤저스')
    print('-'*30)
    home_theater_facade.end_movie()


if __name__ == '__main__':
    main()

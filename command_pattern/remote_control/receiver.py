class Light:

    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name + ' 불이 켜집니다')

    def off(self):
        print(self.name + ' 불이 꺼집니다')

    def __str__(self):
        return self.name


class Fan:

    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name + ' 팬이 돌아갑니다')

    def off(self):
        print(self.name + ' 팬이 꺼집니다')

    def __str__(self):
        return self.name


class Door:

    def __init__(self, name):
        self.name = name

    def up(self):
        print(self.name + ' 문이 열립니다')

    def down(self):
        print(self.name + ' 문이 닫힙니다')

    def __str__(self):
        return self.name


class Stereo:

    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name + ' 오디오가 켜집니다')
        print(self.name + ' 오디오에 CD입력이 준비되었습니다')
        print(self.name + ' 오디오의 볼륨이 11로 조정되었습니다')


    def off(self):
        print(self.name + ' 오디오가 꺼집니다')

    def __str__(self):
        return self.name
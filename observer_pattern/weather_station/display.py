from .interface import Observer, DisplayElement


class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, subject):
        self.weather_data = subject
        self.weather_data.register_observer(self)
        self.temperature = 0.
        self.humidity = 0.
        self.pressure = 0.

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: {} F degrees and {}% humidity".format(
            self.temperature, self.humidity))


class StaticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data # weather_data 는 Subject 객체 
        self.weather_data.register_observer(self)

        self.maxTemp = 0.
        self.minTemp = 200
        self.tempSum = 0.
        self.num_readings = 0

    def update(self, temperature, humidity, pressure):
        self.tempSum += temperature
        self.num_readings += 1

        self.maxTemp = max(self.maxTemp, temperature)
        self.minTemp = min(self.minTemp, temperature)

        self.display()

    def display(self):
        print("Avg/Max/Min temperature = {}/{}/{}".format(
            self.tempSum/self.num_readings, self.maxTemp, self.minTemp))
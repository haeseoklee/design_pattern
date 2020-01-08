from .interface import Subject


class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0.
        self.humidity = 0.
        self.pressure = 0.

    def register_observer(self, obj):
        self.observers.append(obj)

    def remove_observer(self, obj):
        if obj in self.observers:
            self.observers.remove(obj)

    def notify_observer(self):
        for obj in self.observers:
            obj.update(self.temperature, self.humidity, self.pressure)
    
    def measurements_changed(self):
        self.notify_observer()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
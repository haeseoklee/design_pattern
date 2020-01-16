from weather_station.weather_data import WeatherData
from weather_station.display import (
    CurrentConditionDisplay,
    StaticsDisplay
)


def main():
    # push 방식의 observer 패턴, pull 방식의 observer 패턴은 따로 구현하지 않음
    weather_data = WeatherData()
    current_display = CurrentConditionDisplay(weather_data)
    statics_display = StaticsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)

    print(weather_data.observers)
    weather_data.remove_observer(current_display)
    weather_data.register_observer(current_display)
    print(weather_data.observers)

    weather_data.set_measurements(90, 70, 29.2)

if __name__ == '__main__':
    main()
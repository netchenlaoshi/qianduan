from chapter3.city_weather import HeFeng
from chapter3.city_weather_db import HefengDb


def save_all_weather():
    hefeng = HeFeng()
    weathers = hefeng.get_all_weather(50)
    hefengDb = HefengDb()
    hefengDb.save_all(weathers)
    hefengDb.show_all()


if __name__ == '__main__':
    # save_all_weather()
    hefengDb=HefengDb()
    for each in hefengDb.find({'HeWeather6.basic.city':'北京'}):
        print(each)
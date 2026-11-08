import csv
from datetime import datetime
from sqlalchemy.orm import Session
from app.db import engine
from app.models import WeatherRecord, WeatherWind, WindDirection
from app.application.go_outside import is_go_outside


def parse_datetime(value):
    return datetime.strptime(value, "%Y-%m-%d %H:%M")


def parse_time(value):
    return datetime.strptime(value, "%I:%M %p").time()


def row_to_weather_record(row):
    record = WeatherRecord(
        country=row["country"],
        last_updated=parse_datetime(row["last_updated"]),
        sunrise=parse_time(row["sunrise"]),
    )
    record.wind = WeatherWind(
        wind_kph=float(row["wind_kph"]),
        wind_degree=int(row["wind_degree"]),
        wind_direction=WindDirection[row["wind_direction"]],
        go_outside=is_go_outside(float(row["wind_kph"]))
    )
    return record



def import_weather_data():
    with Session(engine) as session:
        with open("data/GlobalWeatherRepository-selected-columns.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                record = row_to_weather_record(row)
                session.add(record)
        session.commit()


if __name__ == "__main__":
    import_weather_data()
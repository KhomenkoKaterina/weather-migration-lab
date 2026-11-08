from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.db import engine
from app.models import WeatherRecord


def search(country: str, date: datetime):
    start = datetime(date.year, date.month, date.day)
    end = start + timedelta(days=1)

    with Session(engine) as session:
        records = (
            session.query(WeatherRecord)
            .filter(WeatherRecord.country == country)
            .filter(WeatherRecord.last_updated >= start)
            .filter(WeatherRecord.last_updated < end)
            .all()
        )

        result = []
        for record in records:
            wind = record.wind
            result.append({
                "country": record.country,
                "last_updated": record.last_updated,
                "sunrise": record.sunrise,
                "wind_kph": wind.wind_kph,
                "wind_degree": wind.wind_degree,
                "wind_direction": wind.wind_direction.value,
                "go_outside": wind.go_outside,
            })
        return result
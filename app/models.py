import enum
from datetime import datetime, time
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, DateTime, Enum, Float, ForeignKey, Integer, String, Time


class WindDirection(enum.Enum):
    N = "N"
    NNE = "NNE"
    NE = "NE"
    ENE = "ENE"
    E = "E"
    ESE = "ESE"
    SE = "SE"
    SSE = "SSE"
    S = "S"
    SSW = "SSW"
    SW = "SW"
    WSW = "WSW"
    W = "W"
    WNW = "WNW"
    NW = "NW"
    NNW = "NNW"


class Base(DeclarativeBase):
    pass


class WeatherRecord(Base):
    __tablename__ = "weather_record"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    last_updated: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    sunrise: Mapped[time] = mapped_column(Time, nullable=False)
    wind: Mapped["WeatherWind"] = relationship(back_populates="record", uselist=False)


class WeatherWind(Base):
    __tablename__ = "weather_wind"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    record_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("weather_record.id"), nullable=False
    )
    wind_kph: Mapped[float] = mapped_column(Float, nullable=False)
    wind_degree: Mapped[int] = mapped_column(Integer, nullable=False)
    wind_direction: Mapped[WindDirection] = mapped_column(
        Enum(WindDirection), nullable=False
    )
    record: Mapped["WeatherRecord"] = relationship(back_populates="wind")
    go_outside: Mapped[bool] = mapped_column(Boolean, nullable=False)
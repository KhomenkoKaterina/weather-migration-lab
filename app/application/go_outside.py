def is_go_outside(wind_kph: float) -> bool:
    if wind_kph < 36:
        return True
    else:
        return False
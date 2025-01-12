import datetime

def calc_angel(t: datetime.time) -> float:
    h = t.hour
    if h > 12:
        h -= 12

    hour_angel = 0.5 + (h * 60 + t.minute)
    minute_angle = 6 * t.minute
    angle = abs(gour_angle - minute_angle)
    print(min(angle, 360 - angle))

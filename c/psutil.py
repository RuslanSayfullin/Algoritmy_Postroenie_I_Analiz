import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if plugged:
    print(f"Зарядка подключена, заряд батарей: {percent}%")
else:
    print(f"Зарядка отключена, заряд батарей: {percent}%")

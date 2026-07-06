def report_weather(temperature, weather_function):
    return weather_function(temperature)

def as_sun_lover(temperature):
    if temperature >= 25:
        return "It's a hot day, perfect for the beach!"
    else:
        return "It's not that hot, maybe stay indoors."
    

def as_snow_lover(temperature):
    if temperature <= 0:
        return "It's cold! Time for some snowball fights!"
    else:
        return "It's not cold enough for snow, maybe go for a walk instead."
    
print(report_weather(30, as_sun_lover))

print("--------------------")

print(report_weather(-5, as_snow_lover))

print("--------------------")

print(report_weather(10, as_snow_lover))

print("--------------------")

print(report_weather(0, as_sun_lover))
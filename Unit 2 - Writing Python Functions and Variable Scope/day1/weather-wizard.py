# Prints the app title
# Parameters: none
# Returns: nothing
def show_app_title():
    print("🌦️ Weather Wizard – Your Forecast Friend")

# Converts Celsius to Fahrenheit
# Parameters: temp_c (float)
# Returns: Fahrenheit temperature (float)
def to_fahrenheit(temp_c):
    return temp_c * 9 / 5 + 32

# Calculates wind chill based on temp (°C) and wind speed (km/h)
# Parameters: temp (float), wind_speed (float)
# Returns: wind chill value (float)
def wind_chill(temp, wind_speed):
    return 13.12 + 0.6215 * temp - 11.37 * wind_speed**0.16 + 0.3965 * temp * wind_speed**0.16

# Prints weather summary
# Parameters: city (string), temp (float)
# Returns: nothing
def report(city, temp):
    print("The temperature in " + city + " is " + str(temp) + "°C.")

show_app_title()
city = "Toronto"
temp_c = -5
report(city, temp_c)
to_fahrenheit(temp_c)
wind_speed = 30
ac_wind_chill = wind_chill(temp_c, wind_speed)
print(f"The calculated wind chill is equal to {ac_wind_chill:.2f}")
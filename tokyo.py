import pyowm

apikey= '2ae22c89a8efadd10ee57af8795ac9ab'
owm = pyowm.OWM(apikey)
observation = owm.weather_at_place('Tokyo,Japan')
w = observation.get_weather()
 

w.get_temperature(unit='celsius')         
w.get_temperature('fahrenheit') 

print(w.get_temperature() )
print(w.get_temperature('fahrenheit'))


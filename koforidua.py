import pyowm

apikey= '2ae22c89a8efadd10ee57af8795ac9ab'
owm = pyowm.OWM(apikey)
observation = owm.weather_at_place('KOforidua,Ghana')
w = observation.get_weather()
 
w.get_wind()

print("The wind speed in koforidua is: ", w.get_wind())


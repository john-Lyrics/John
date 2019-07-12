import pyowm

apikey= '2ae22c89a8efadd10ee57af8795ac9ab'
owm = pyowm.OWM(apikey)
observation = owm.weather_at_place('La Rinconada,Peru')
w = observation.get_weather()
 
w.get_pressure()

print("The highest city is La Rinconada, in Peru'")
print("The pressure is: ",w.get_pressure())


import pyowm

apikey= '2ae22c89a8efadd10ee57af8795ac9ab'
owm = pyowm.OWM(apikey)
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
 
w.get_wind()
w.get_humidity()

print("The win is: ", w.get_wind())
print("The humidity is: ", w.get_humidity())
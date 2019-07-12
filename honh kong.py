import pyowm

apikey= '2ae22c89a8efadd10ee57af8795ac9ab'
owm = pyowm.OWM(apikey)
observation = owm.weather_at_place('Hong Kong,China')
w = observation.get_weather()
 
w.get_wind()
w.get_humidity()


print("The humidity  for Hong Kong is: ", w.get_humidity())

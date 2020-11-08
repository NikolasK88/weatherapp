from pyowm import OWM

owm = OWM('96bb4457c2cc3a88d6ca4744ea89936f')
mgr = owm.weather_manager()

city = input('Please choose the city: ')

observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']

print('In ' + city + ' now ' + w.detailed_status)
print('The temperature is ' + str(temperature))

if temperature < 10:
    print('It\'s very cold!')
elif temperature < 20:
    print('Pretty nice temperature for a walk!')
else:
    print('You can wear shorts and swim in the sea!')
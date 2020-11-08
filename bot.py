import telebot
from pyowm import OWM

bot = telebot.TeleBot("1319861508:AAEwLunFQMAQNkqpCor95RUfVkt3ZHObbIs")
owm = OWM('96bb4457c2cc3a88d6ca4744ea89936f')

#city = input('Please choose the city: ')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to our weather app. Please choose your city/country: ")

@bot.message_handler(content_types=['text'])
def weather_bot(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']

    answer = 'In ' + message.text + ' now ' + w.detailed_status + '\n'
    answer += 'The temperature is ' + str(temperature) + '\n\n'

    if temperature < 10:
        answer += 'It\'s very cold!'
    elif temperature < 20:
        answer += 'Pretty nice temperature for a walk!'
    else:
        answer += 'You can wear shorts and swim in the sea!'

    bot.send_message(message.chat.id, answer)

bot.polling()
import telebot
import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = 'ru')
bot = telebot.TeleBot("986734620:AAGo1xhJ2OKjs-xYTqSGkfiR_fsMMx9k8aY")

@bot.message_handler(content_types=['text'])
def send_weather(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()

	temp = w.get_temperature('celsius')['temp']

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"

	answer += 'Температура примерно равна ' + str(temp) + '\n\n'

	if temp < 10:
		answer += 'Советую одеться потеплее'
	elif temp < 20:
		answer += 'Без куртки лучше не выходить'
	else:
		answer += 'Довольно тепло'

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )

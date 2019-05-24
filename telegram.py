import pyowm
import telebot
owm = pyowm.OWM('d467dd260e03062fe98c0c6bb3bbd719', language = "ru")  

bot = telebot.TeleBot("855284934:AAEqhKzaheCyRNwLqurMre3ihkZCHVjTs6c")
@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius') ["temp"] # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
	answer = "в городе  " + message.text +  " сейчас " + w.get_detailed_status() + "\n"                  
	answer += "Temperature in" + str(temp) + "\n\n"

	if temp < 10:
		answer += "put on a warm jacket"
	elif temp > 10:
		answer += "put off anything"
	else:
 		answer += "be careful the weather can be changed"

	#bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)


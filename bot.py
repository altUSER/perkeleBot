# coding: utf-8

appid = "6b6350c1609ca490fc62ec4afa6d30a1"

import os
import time
import requests
import vk_api

vk = vk_api.VkApi(login = '89091126446', password = 'pm24ek75')
vk.auth()

values = {'out': 0,'count': 10,'time_offset': 20}

def write_chat(chat_id, s):
    vk.method('messages.send', {'chat_id':chat_id,'message':s})

outp = ''
sended = 0

while True:
	times = str(time.ctime())[11:16]
	if times == '12:00' or times == '10:56' or sended == 0:
		outp = '[Perkele Bot]\nПогода:\n'
		city_id = 511196
		sended = 1
		try:
			res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
			data = res.json()
			outp = outp + 'Температура: ' + str(data['main']['temp']) + '\nВлажность: ' + str(data['main']['humidity']) + '\nОблачность: ' + str(data['clouds']['all']) + '%'
			write_chat(9, outp)
			print 'Write weather'
		except Exception as e:
			print("Exception (weather):", e)
			pass
	os.system('clear')
	else:
		sended = 1
	time.sleep(5)
	print times
        print outp


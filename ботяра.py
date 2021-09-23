import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

vk = vk_api.VkApi(token='f65b32c72f341489497ee92acdf34452a1076e58d483ef05ac877eb2ec52df9d09c4cfc05e1c5aec9f03b')
longpoll = VkBotLongPoll(vk, '205339952')
vk = vk.get_api()

while True:
    for event in longpoll.listen():

        if event.object.message['text'] == 'привет' or event.object.message['text'] == 'привет ':
            vk.messages.send(peer_id=event.object.message['peer_id'], random_id=0,
                             message='Здарова, я бот!')

            print('Для меня от: ', end='')

            print(event.message.from_id)

            print('Текст:', event.message.text)


        elif event.object.message['text'] == 'Егор' or event.object.message['text'] == 'егор':
            vk.messages.send(peer_id=event.object.message['peer_id'], random_id=0,
                             message='@egsimonov, приди')

            print('Для меня от: ', end='')

            print(event.message.from_id)

            print('Текст:', event.message.text)


        elif event.object.message['text'] == 'р' or event.object.message['text'] == 'Р' or event.object.message[
            'text'] == 'маш' or event.object.message['text'] == 'Маш':
            vk.messages.send(peer_id=event.object.message['peer_id'], random_id=0,
                             message='@rachyak,')
            print('Для меня от: ', end='')
            print(event.message.from_id)
            print('Текст:', event.message.text)
        #  elif event.object.message['text'] == 'ударить':
        #  vk.messages.send(peer_id = event.object.message['peer_id'], random_id = 0, message = 'наа!!, но лучше давайте без драк тут')

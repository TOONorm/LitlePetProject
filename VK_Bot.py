"""""""""""""""
код бота из вк
"""""""""""""""
from IDkeyCOINbruh import ID_coin as ID
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import Parser_base as PrB
from random import randint as rndInt
from wiki import get_wiki_article

token = ID.token_vk()

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

longpool = VkLongPoll(vk_session)

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        msg_id = rndInt(1, 10 ** 8)
        if msg.startswith('-в'):
            res = get_wiki_article(msg[2:])
            vk_session.method("messages.send", {'user_id': user_id,
                                                'message': res,
                                                'random_id': msg_id})
        if 'диаметр планеты' in msg:
            vk_session.method("messages.send", {'user_id': user_id,
                                            'message': PrB.get_info_json('https://swapi.dev/'
                                                                         'api/planets/',
                                                                         "diameter") ,
                                            'random_id': msg_id})
        if 'скорость кораблей' in msg:
            vk_session.method("messages.send", {'user_id': user_id,
                                            'message': PrB.get_info_json('https://swapi.dev/'
                                                                         'api/starships/',
                                                                         "max_atmosphering_speed"),
                                            'random_id': msg_id})
        else:
            vk_session.method("messages.send", {'user_id': user_id,
                                            'message': "Иди нахуй!" ,
                                            'random_id': msg_id})

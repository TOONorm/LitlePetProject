import time
from mail_sendler import main

#функции я хз, но надеюсь так делать правильнее
def end():
    global fact
    print('хорошего дня')
    input()
    fact = False
def start():
    for e in range(3):
        print("...")
        time.sleep(0.5)
    print("*запуск системы*")
    time.sleep(0.5)
    for e in range(3):
        print(".....")
        time.sleep(0.5)
    print("*запуск программы*")
    time.sleep(0.5)
    for e in range(3):
        print(".......")
        time.sleep(0.5)
    print("*запуск скрипта*")
    time.sleep(0.5)
    for e in range(3):
        print(".....")
        time.sleep(0.5)
    print("*настройка и включение интелекта*")
    time.sleep(0.5)
    for e in range(3):
        print("...")
        time.sleep(0.5)
def script():
    global fact, otv, count, end, start, a, i, rep, enter, pupa_zalupa
    start()
    enter = print(rep[0])
    f'\n\n{pupa_zalupa.append(rep[0])}'
    enter = print (rep[1])
    f'\n\n{pupa_zalupa.append(rep[1])}'
    #print(pupa_zalupa)
    while fact == True:
        a = input(rep[2])
        f'\n\n{pupa_zalupa.append(rep[2])}'
        f'\n\n{pupa_zalupa.append(a)}'
        if a in good_emotion:
            enter = print(rep[3])
            f'\n\n{pupa_zalupa.append(rep[3])}'
            otv = input(rep[4])
            f'\n\n{pupa_zalupa.append(rep[4])}'
            f'\n\n{pupa_zalupa.append(otv)}'
            time.sleep(0.3)
            end()
            #print(pupa_zalupa)
        elif a in bad_emotion:
            enter = print(rep[5])
            otv = input(rep[6])
            f'\n\n{pupa_zalupa.append(rep[5])}'
            f'\n\n{pupa_zalupa.append(rep[6])}'
            f'\n\n{pupa_zalupa.append(otv)}'
            time.sleep(4)
            enter = print(rep[7])
            f'\n\n{pupa_zalupa.append(rep[7])}'
            time.sleep(0.5)
            enter = print(rep[8])
            f'\n\n{pupa_zalupa.append(rep[8])}'
            end()
            #print(pupa_zalupa)
        elif a == 'плохо':
            enter = print(rep[5])
            otv = input(rep[6])
            f'\n\n{pupa_zalupa.append(rep[5])}'
            f'\n\n{pupa_zalupa.append(rep[6])}'
            f'\n\n{pupa_zalupa.append(otv)}'
            time.sleep(4)
            enter = print(rep[7])
            f'\n\n{pupa_zalupa.append(rep[7])}'
            time.sleep(0.5)
            enter = print(rep[8])
            f'\n\n{pupa_zalupa.append(rep[8])}'
            end()
            #print(pupa_zalupa)
        elif a in norm_emotion:
            enter = print(rep[9])
            pupa_zalupa.append(rep[9])
            time.sleep(0.3)
            end()
            #print(pupa_zalupa)
        elif a == "нормально":
            enter = print(rep[9]+rep[3])
            f'\n\n{pupa_zalupa.append(rep[3])}'
            time.sleep(0.3)
            end()
            #print(pupa_zalupa)
        elif a == "отлично":
            enter = print(rep[10])
            otv = input(rep[4])
            f'\n\n{pupa_zalupa.append(rep[10])}'
            f'\n\n{pupa_zalupa.append(rep[4])}'
            f'\n\n{pupa_zalupa.append(otv)}'
            time.sleep(4)
            enter = print(rep[11])
            f'\n\n{pupa_zalupa.append(rep[11])}'
            end()
            #print(pupa_zalupa)
        else:
            if count <= 1:
                enter = print(rep[12])
                f'\n\n{pupa_zalupa.append(rep[12])}'
                count += 1
            elif count == 2:
                enter = print(rep[13])
                f'\n\n{pupa_zalupa.append(rep[13])}'
                count += 1
            elif count < 5:
                enter = print(rep[14])
                f'\n\n{pupa_zalupa.append(rep[14])}'
                count += 0.5
            elif count >= 5:
                for i in range(3):
                    enter = print(rep[15])
                    f'\n\n{pupa_zalupa.append(rep[15])}'
                    time.sleep(1)
                fact = False
            #print(pupa_zalupa)

file = open('NoBody.txt', 'a+') #создали файл для истории сообщений

#переменные, списки и прочее
fact = True
count = 0
rep = ["Zuma на связи ;)","Z:Приииииивеееет))))!","Z:как настроение?: ",
               'Z:рад за вас)','Z:А от чего так? ','Z:Обидно(',"Z:А почему?",'Z:Понятно...',
               "Z:Надеюсь ты справишься!)","Z:хорошо","Z:Отлично!","Z:Вот как! Ну ладно.",
               'Z:Не могу разобрать вашу человеческую эмоцию *бип-буп*',
               "Z:Повторите пожалуйста, я вас не понимаю",
               'Z:просто назовите ваше настроение! хорошо/плохо/нормально.',"Z:..."]
pupa_zalupa = []
good_emotion = ['хорошо',"отлично","замечательно","ахуенно","заебись","клёво","кайфово"]
norm_emotion = ["нормально", "норм","нормуль", "всё ок", "ничего нового", "как обычно"]
bad_emotion = ["хуёво", "плохо","так себе", "пиздец", "да пиздец", "лучше и не спрашивай"]
coconut = 0

#сам скрипт
#print(pupa_zalupa)
script()

'''
Планы:
отправка листа на почту + создать таблицу со степенью эмоциональности и хорошего плохого настроения, что бы программа 
решала как правильно ответить, хорошая эмоция или плохая, если плохая/хорошая, то насколько.
получить ехе-шник и выпустить программу в интернет как вирус
'''

#запись истории
for i in range(len(pupa_zalupa)):
    if coconut == 0:
        teetime = time.strftime(f"%d:%m:%Y\n%H:%M")
        file.write(f"\n\n{teetime}\n{pupa_zalupa[coconut]}")
    else:
        file.write(f"\n{pupa_zalupa[coconut]}")
    coconut += 1
file.close()
main('NoBody.txt') #отправка сообщения мне на почту

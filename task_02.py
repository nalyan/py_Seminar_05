# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

q = 121
lim = 28
while True:
    ger_inp = input('Орёл(o) или решка(r): ')
    if ger_inp == 'o' or ger_inp == 'r': break

# *** человек с человеком

'''ger = random.randrange(2)
if ger == 0: print('Выпал орёл!')
else: print('выпала решка!')

print(f'{q} конфет, Ваш ход!')
count = 0
while q!=0:
    if count%2==0: player=1
    else: player=2
    while True:
        if q>=28:
            player_inp = int(input(f'возьмите конфеты, {player} игрок (1-lim): '))
        else:
            player_inp = int(input(f'возьмите конфеты, {player} игрок (1-{q}): '))
        if player_inp > 0 and player_inp <= lim and player_inp <= q: break
    q-=player_inp
    print(f'осталось {q} конфет')
    if q==0: print(f'Победил {player} игрок!')
    count+=1'''

# *** человек с ботом
var = ['r', 'o']
ger = random.choice(var)
if ger == 'o': print('Выпал орёл!')
else: print('выпала решка!')

if ger_inp == ger:
    print(f'* {q} конфет, Ваш ход!')
    count = 0
else:
    print(f'* {q} конфет, начинает бот!')
    count = 1

while q != 0:
    if count % 2 == 0:
        player = 'игрок'
        while True:
            if q >= lim:
                motion = int(input(f'возьмите конфеты, {player} (1-28): '))
            else:
                motion = int(input(f'возьмите конфеты, {player} (1-{q}): '))
            if motion > 0 and motion <= lim and motion <= q: break
    else:
        player = 'бот'

        if q > lim:
            # *** простой бот
            '''motion = random.randint(1, lim)
            print(f'бот взял {motion}')'''

            # *** умный бот
            if q % (lim+1) !=0: motion = q % (lim+1)
            else: motion = random.randint(1, lim)
            print(f'бот взял {motion}')

        else:
            motion = q
            print(f'бот взял {motion}')

    q -= motion
    print(f'* осталось {q} конфет')
    if q == 0: print(f'Победил {player}!')
    count += 1

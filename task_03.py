#Создайте программу для игры в ""Крестики-нолики"".
list = [['   1', ' 2', ' 3'], ['a ', '|', ' ', '|', ' ', '|', ' ', '|'], ['b ', '|', ' ', '|', ' ', '|', ' ', '|'], ['c ', '|', ' ', '|', ' ', '|', ' ', '|']]
list_motion = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
log_motion = []
def print_list():
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end='')
        print()
def write(list, input, elem):
    if input=='a1': list[1][2] = elem
    elif input == 'a2': list[1][4] = elem
    elif input == 'a3': list[1][6] = elem
    elif input == 'b1': list[2][2] = elem
    elif input == 'b2': list[2][4] = elem
    elif input == 'b3': list[2][6] = elem
    elif input == 'c1': list[3][2] = elem
    elif input == 'c2': list[3][4] = elem
    elif input == 'c3': list[3][6] = elem
def check(elem):
    if (list[1][2]==list[1][4]==list[1][6]==elem) or (list[2][2]==list[2][4]==list[2][6]==elem) or (list[3][2]==list[3][4]==list[3][6]==elem) or (list[1][2]==list[2][4]==list[3][6]==elem) or (list[1][6]==list[2][4]==list[3][2]==elem)   : return True

print_list()
print('Вводите заполняемые поле в формате a1')
count=0
for i in range(9):
    if count%2==0:
        elem = 'X'
        player = 'игрок 1'
    else:
        elem = '0'
        player = 'игрок 2'
    while True:
        mot_input = input(f'{player}: ')
        if any(x==mot_input for x in list_motion) and not any(x==mot_input for x in log_motion): break
    log_motion.append(mot_input)
    write(list, mot_input, elem)
    if check(elem)==True:
        print(f'** Победил {player}! **')
        break
    count+=1
    print_list()


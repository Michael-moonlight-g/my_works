import random

def which_type():
    flag = False
    while not flag:
        try:
            b = float(input())
        except ValueError:
            print("Не тот тип файлов")
        else: 
            flag = True
    return b

a = random.randint(0, 100)
print(a) # для отладки
print("Угадай число от 1 до 100")
b = which_type()
while b != a:
    if b < a:
        print("Твое число меньше")
    else:
        print("Твое число больше")
    b = which_type()
print(f"Молодец ты угдал, это число {a}")


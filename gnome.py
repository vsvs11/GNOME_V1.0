import random
import time
password_pool = "987654321"
login_pool = "user_1"
wost_pool = "(забыл пароль)"
loop = False
calc = [1,2,3,4,5,6,7,8,9,0]
pool = random.choice(calc)
pool_1 = random.choice(calc)
pool_2 = random.choice(calc)
pool_3 = random.choice(calc)
pool_all = (str(pool + pool_1 * pool_2 * pool_3))
while True:

    login = input(str("Введите ваш логин для входа в программу:\n "))
    if login == login_pool:
        print("Введите пароль задонного пользователем " , login , ":" )
        password = input(str())
        if password == password_pool:
            print("Welcome to desktop Gnome!")
            loop = True
            break
        else:
            wost = input(str("Если не знаете пароль можете написать (забыл пароль)"))
            if wost == wost_pool:
                print(pool_all)
                pooi = input("ВВЕДИТЕ НАБОР СИМВОЛОВ ДЛЯ ВОСТАННОВЛЕНИЯ")
                if pooi == pool_all:
                    print("Welcome to desktop Gnome!")
                    loop = True
                    break
                else:
                    print("error simvol...")
            else:
                print("error password...")
    else:
        print("error name...")



if loop == True:
    print("Выполняется вход в рабочее окружение Gnome...")
    time.sleep(5)
    while True:
        print("_____________GNOME___V1.0______________")
        print("|      __     __    __      __       |")
        print("|     | 1|   | 2|  | 3|    | 4|      |")
        print("|                                    | ")
        print("|    1- калькулятор; 2- календарь;   | ")
        print("|    3- часы;    4- справка          |") 
        print("_______________________________________")
        print("Выберете приложение(1,2,3,4)")
        soon = input(str("$~/ "))
        if soon == "1":
            print("запуск приложения 'калькулятор'...")
            time.sleep(2)
            print("calculator GNOME V1.0")
            while True:

                print("введите первое число для вычисления или {exit} для выхода ->")
                null_1  = (input())
                if null_1 == "exit":
                    print("выход...")
                    time.sleep(2)
                    break
                else:
                    null_1 = int(null_1)
                    print("введите знак вычисления ->")
                    vcnull = input(str(""))
                    print("введите второе число для вычисления ->")
                    null_2 = int(input())
                    if vcnull == "+":
                        otv = null_1 + null_2
                        print("Ответ:" , otv)
                    elif vcnull == "-":
                        otv = null_1 - null_2
                        print("Ответ:" , otv)
                    elif vcnull == "*":
                        otv = null_1 * null_2
                        print("Ответ:" , otv)
                    elif vcnull == "/":
                        otv = null_1 / null_2
                        print("Ответ:" , otv)
                    elif vcnull == "//":
                        otv = null_1 // null_2
                        print("Ответ:" , otv)
                    elif vcnull == "**":
                        otv = null_1 ** null_2
                        print("Ответ:" , otv)
                    else:
                        print("Неверный ввод...")



        elif soon == "2":
            print("запуск приложения 'календарь'...")
            time.sleep(2)
            print("calendar GNOME V1.0")
            seconds_since_epoch = time.time()
            time_struct = time.localtime(seconds_since_epoch)
            date_string = time.strftime("%Y-%m-%d", time_struct)
            print(date_string)
            time.sleep(2)
                
            
        elif soon == "3":
            print("запуск приложения 'часы'...")
            time.sleep(2)
            scht = 0
            print("watch GNOME V1.0")
            while True:
                timep = time.time()
                formatted_time = time.strftime("%H:%M:%S")
                print(formatted_time)
                scht = scht + 1
                time.sleep(1)
                if scht == 5:
                    break
        elif soon == "4":
            print("запуск приложения 'справка'...")
            time.sleep(2)
            print("reference GNOME V1.0")
            print("GNOME - приложение на питон,которое позволяет")
            print("пользоваться сервисами времени,календаря и часов.")
            print("в данной версии V1.0 представленны 4 программы но")
            print("в новых версиях будут добавленны новые сервисы и ")
            print("приложения для большей ориентации в стороне этой ")
            print("программы. программа может распростронятся,изменятся")
            print("и размещатся повторно по лицензии GPL.")
            time.sleep(2)
        elif soon == "exit":
            print("Завершение работы...")
            time.sleep(2)
            break
        elif soon == "setup":
            print("функции настроек и обновлений будут добавлены в версии GNOME V1.2")   
            time.sleep(2)
        else:
            print("Новые функции и приложения будут добавлены в версии GNOME V1.2")
            time.sleep(2)

       





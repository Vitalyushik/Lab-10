import random
import logging

# конфигурация логгирования
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def game():
    # ввод чисел N и k с проверкой на правильность ввода
    while True:
        try:
            N = int(input("Введите число N (не меньше 1): "))
            logging.info(f"Введено максимальное число N: {N}")
            if N < 1:
                raise ValueError
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")
    
    while True:
        try:
            k = int(input("Введите число попыток k: "))
            logging.info(f"Введено количество попыток k: {k}")
            if k <= 0:
                raise ValueError
                logging.info(f"Введено количество попыток k: {k}")
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")
            logging.info("Некорректный ввод")
    
    # генерация случайного числа
    random_num = random.randint(1, N)
    
    logging.info(f"Случайное число: {random_num}")
    
    # цикл угадывания числа
    for i in range(k):
        # ввод числа для поытки угадать с проверкой на правильность ввода
        while True:
            try:
                try_num = int(input("Введите число от 1 до N: "))
                if try_num < 1 or try_num > N:
                    raise ValueError
                break
            except ValueError:
                print("Некорректный ввод. Попробуйте еще раз.")
                logging.info("Некорректный ввод")
        
        # проверка угаданного числа
        if try_num == random_num:
            print("Вы угадали!")
            logging.info(f"Введено число: {try_num}, число угадано")
            return
        elif try_num < random_num:
            print("Загаданное число больше.")
            logging.info(f"Введено число: {try_num}, загаданное число больше.")
        else:
            print("Загаданное число меньше.")
            logging.info(f"Введено число: {try_num}, 5агаданное число меньше.")
    
    print("Попытки закончились.")
    logging.info("Попытки закончились.")

game()
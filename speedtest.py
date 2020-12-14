import time
class Timer():
    """Выполняет замер среднего времени работы функции по средствам контекстного менеджера. num_runs=0(Число запусков для замера среднего времени), func=None(функция над которой производится замер времени).)"""
    def __init__(self, num_runs=0, func=None):
        # Количество запусков функции для замера
        self.num_runs = num_runs
        # Функция время которой нам необходимо измерить
        self.func = func
        # Переменная для записи времени работы функции и последующего выведения среднего времени работы
        self.sum_time = 0

    def __enter__(self):
        return self

    def __exit__(self, *args):
        # Выполняем функцию столько раз сколько указали в num_runs
        for i in range(self.num_runs):
            print(f"---|{i + 1}|--- запуск функции")
            # Отметка начала выполнения
            start = time.time()
            # Сама функция
            self.func()
            # Итоговое время выполнения
            finish_time = time.time() - start
            # Запись в sum_time
            self.sum_time += finish_time
        # Окончив выполнять функцию num_runs раз считаем среднее время выполнения функции
        self.sum_time /= self.num_runs
        return print(f"Среднее время работы функции {round(self.sum_time, 4)} секунд.")

# Функция Фибоначчи для проверки рабоыт таймера
def fibo():
    "fibo func"
    a, b = 1, 2
    stop = 40000000
    sum_number = 0
    while b < int(stop):
        if b % 2 ==0:
            sum_number += b
        oldb = b
        b += a
        a = oldb
        if b < int(stop):
            print(b)
    print(f"Finish! Sum of even numbers is {sum_number}")

if __name__ == "__main__":
    # Вывод декоратора в качестве контекстного менеджера
    with Timer(num_runs = 10, func=fibo) as timer:
        print(f"Начало замера функции {timer.func.__name__}. Количество запусков {timer.num_runs}.")
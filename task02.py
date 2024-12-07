import threading
import multiprocessing
import time
import math


# запускать с n = 699993
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    #print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    #print(f'trapezoidal_rule = {integral * h}')


def sequence():
    start_time = time.time()
    fibonacci(699993)
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)
    end_time = time.time()
    print(f'sequence time: {end_time - start_time:0.2f} seconds\n')


def threads():
    start_time = time.time()
    threads_list = []

    thread1 = threading.Thread(target=fibonacci, args=(699993,))
    thread2 = threading.Thread(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))

    threads_list.append(thread1)
    threads_list.append(thread2)

    thread1.start()
    thread2.start()

    for thread in threads_list:
        thread.join()

    end_time = time.time()
    print(f'threads time: {end_time - start_time:0.2f} seconds\n')


def processes():
    start_time = time.time()
    processes_list = []

    process1 = multiprocessing.Process(target=fibonacci, args=(699993,))
    process2 = multiprocessing.Process(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))

    processes_list.append(process1)
    processes_list.append(process2)

    process1.start()
    process2.start()

    for process in processes_list:
        process.join()

    end_time = time.time()
    print(f'processes time: {end_time - start_time:0.2f} seconds\n')


if __name__ == '__main__':
    print("Running sequence:")
    sequence()
    print("Running threads:")
    threads()
    print("Running processes:")
    processes()

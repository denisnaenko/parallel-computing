import asyncio
from concurrent.futures import ThreadPoolExecutor
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


async def run_in_executor(executor, func, *args):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, func, *args)


async def asyncio_method():
    start_time = time.time()

    # Используем ThreadPoolExecutor для выполнения задач
    with ThreadPoolExecutor() as executor:
        await asyncio.gather(
            run_in_executor(executor, fibonacci, 699993),
            run_in_executor(executor, trapezoidal_rule, math.sin, 0, math.pi, 20000000)
        )

    end_time = time.time()
    print(f'asyncio time: {end_time - start_time:0.2f} seconds\n')


if __name__ == '__main__':
    print("Running with asyncio:")
    asyncio.run(asyncio_method())

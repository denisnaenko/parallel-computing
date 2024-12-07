import threading
import time
import multiprocessing
import requests

# список url
urls = ['https://www.example.com'] * 10


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    start_time = time.time()
    for url in urls:
        fetch_url(url)
    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} seconds\n')


def threads():
    start_time = time.time()
    threads_list = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()
    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} seconds\n')


def processes():
    start_time = time.time()
    processes_list = []
    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes_list.append(process)
        process.start()

    for process in processes_list:
        process.join()
    end_time = time.time()
    print(f'processes time: {end_time - start_time: 0.2f} seconds\n')


if __name__ == '__main__':
    print("Running with sequence:")
    sequence()
    print("Running with threads:")
    threads()
    print("Running with processes:")
    processes()

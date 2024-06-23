import threading
import logging
from typing import List
import time
import concurrent.futures

def thread_function(value: str):
    logging.info(f'Starting thread #{value}')
    time.sleep(2)
    logging.info(f'Ending thread #{value}')

def test_thread():
    threads: List[threading.Thread] = []
    for i in range(4):
        t = threading.Thread(target=thread_function, args=[str(i)])
        threads.append(t)
        t.start()

    for i, t in enumerate(threads):
        logging.info(f'before joing thread {i}')
        t.join()
        logging.info(f'after joing thread {i}')

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

def test_thread_pool():

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        pool.map(thread_function, range(3))

test_thread_pool()
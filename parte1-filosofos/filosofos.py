# codigo documentacao

import threading
import time

filosofos = 5

def crawl(id_filosofo, delay=3):
    print(f"Filósofo {id_filosofo} começou a pensar/comer.")
    time.sleep(delay)
    print(f"Filósofo {id_filosofo} terminou.")

threads = [
    threading.Thread(target=crawl, args=(i,), kwargs={"delay": 2})
    for i in range(filosofos)
]

# Start each thread
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
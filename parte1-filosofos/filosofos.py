# codigo documentacao

import threading
import time

n = 5
garfos = [threading.Lock() for _ in range(n)]

def crawl(id_filosofo, delay=3):
    idx_garfo_1 = (id_filosofo - 1) % n
    idx_garfo_2 = id_filosofo

    garfo_1 = garfos[idx_garfo_1]
    garfo_2 = garfos[idx_garfo_2]
    print(f"Filósofo {id_filosofo} está tentando pegar os garfos {idx_garfo_1} e {idx_garfo_2}.")
    print(f"Filósofo {id_filosofo} começou a pensar/comer.")
    time.sleep(delay)
    print(f"Filósofo {id_filosofo} terminou.")

threads = [
    threading.Thread(target=crawl, args=(i, ), kwargs={"delay": 2})
    for i in range(n)
]

# Start each thread
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Fim do jantar
print("\nJantar concluído com sucesso!")
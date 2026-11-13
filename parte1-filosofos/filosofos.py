# codigo documentacao

import threading
import time

n = 5
garfos = [threading.Lock() for _ in range(n)]
estados = {1: "PENSANDO", 2: "FAMINTO", 3: "COMENDO"}
filosofos = [
    {"posicao": i, "estado": 1, "tempoNoEstado": 0}
    for i in range(n)
]

def garfo(p):
    numero_garfo_1 = (p - 1) % n
    numero_garfo_2 = p
    
    garfo_1 = garfos[numero_garfo_1]
    garfo_2 = garfos[numero_garfo_2]
    return numero_garfo_1, numero_garfo_2,  garfo_1, garfo_2

def crawl(p, delay=3):
    f = filosofos[p]
    garfo_esquerdo, garfo_direito= garfo(p)
    if f["tempoNoEstado"] > 0:
        f["estado"] = (f["estado"] + 1) % 3
    f["tempoNoEstado"] += 1

    print(f"Filósofo {filosofos[p]['posicao']} está tentando pegar os garfos {garfo_esquerdo} e {garfo_direito}.")
    print(f"Filósofo {filosofos[p]['posicao']} começou a {filosofos[p]['estado']}.")
    time.sleep(delay)
    print(f"Filósofo {filosofos[p]['posicao']} terminou.")

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
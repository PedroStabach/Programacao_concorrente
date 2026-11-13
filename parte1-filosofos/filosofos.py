import random
import threading
import time

n = 5

garfos = [threading.Lock() for _ in range(n)]

estados = {1: "PENSANDO", 2: "FAMINTO", 3: "COMENDO"}

filosofos = [
    {"posicao": i, "estado": "PENSANDO"}
    for i in range(n)
]

print_lock = threading.Lock()

def mudar_estado(p, novo_estado):
    with print_lock:
        filosofos[p]["estado"] = novo_estado
        print(f"Filósofo {p} agora está: {novo_estado}")

def crawl(p, ciclos=2):

    for _ in range(ciclos):
        # PENSANDO
        mudar_estado(p, "PENSANDO")
        tempo_pensar = random.uniform(1, 2)
        time.sleep(tempo_pensar)
        
        # FAMINTO
        mudar_estado(p, "FAMINTO")
        
        # Garfos
        garfo_esquerdo = p
        garfo_direito = (p + 1) % n
        
        # Prevenção de Deadlock: 
        # O último filósofo pega os garfos na ordem inversa (direito, depois esquerdo)
        if p == n - 1:
            primeiro_garfo = garfo_direito
            segundo_garfo = garfo_esquerdo
        else:
            primeiro_garfo = garfo_esquerdo
            segundo_garfo = garfo_direito
            
        with garfos[primeiro_garfo]:
            with garfos[segundo_garfo]:
                # COMENDO
                mudar_estado(p, "COMENDO")
                time.sleep(random.uniform(1, 2))

threads = [
    threading.Thread(target=crawl, args=(i, 2))
    for i in range(n)
]


# Fim do jantar
def main():
    print("--- Início do Jantar dos Filósofos ---")
    
    # Criação das threads para cada filósofo, codigo documentacao
    threads = [
        threading.Thread(target=crawl, args=(i, 2))
        for i in range(n)
    ]

    # Start each thread
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()


    print("\n--- Jantar concluído com sucesso! ---")

if __name__ == "__main__":
    main()
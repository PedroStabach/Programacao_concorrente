# Sem Sincronização
import threading
import time 
# PARAMETROS
n = 8
Incrementos = 200000
valorInicial = 0
ResultadoEsperado = n * Incrementos

def crawl(ciclos=Incrementos):
    global valorInicial
    for _ in range(ciclos):
        # Incrementa o valorInicial
        valorInicial += 1  

def main():
    print("--- Início threads e Semáforos ---")
    inicio = time.perf_counter()
    # Criação das threads
    threads = [
        threading.Thread(target=crawl, args=(Incrementos,))
        for _ in range(n)
    ]

    # Start each thread
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    fim = time.perf_counter()
    tempo_decorrido = fim - inicio
    print(f"\n--- threads e Semáforos concluídos com sucesso! ---")
    print(f"Valor inicial: {valorInicial}")
    print(f"Resultado esperado: {ResultadoEsperado}")
    print(f"Tempo percorrido: {tempo_decorrido} ")

if __name__ == "__main__":
    main()
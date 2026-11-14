import threading
import time

n = 2
a = threading.Lock()
b = threading.Lock()

def crawl(i):
    print(f"Thread  {i} iniciada.")
    if i == 0:
        print(f"Thread {i} tentando adquirir lock A.")
        with a:
            print(f"Thread {i} adquiriu lock A.")
            time.sleep(0.05)
            print(f"Thread {i} tentando adquirir lock B.")
            with b:
                print(f"Thread {i} adquiriu lock B.")
                print(f"Thread {i} liberando lock B.")
            print(f"Thread {i} liberando lock A.")
    else:
        print(f"Thread {i} tentando adquirir lock B.")
        with b:
                print(f"Thread {i} adquiriu lock B.")
                time.sleep(0.05)
                print(f"Thread {i} tentando adquirir lock A.")
                with a:
                    print(f"Thread {i} adquiriu lock A.")
                    print(f"Thread {i} liberando lock A.")
                print(f"Thread {i} liberando lock B.")

def main():
    print("--- Início do deadLock ---")
    
    # Criação das threads 
    threads = [
        threading.Thread(target=crawl, args=(i,))
        for i in range(n)
    ]

    # Start each thread
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()


    print("\n--- deadLock concluído com sucesso! ---")

if __name__ == "__main__":
    main()
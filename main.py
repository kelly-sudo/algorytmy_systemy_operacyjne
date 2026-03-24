import os
from generator import DataGenerator
from cpu_scheduling import Process, FCFS, RoundRobin
from memory_replacement import FIFO, LRU

def load_cpu_data(filename):
    processes = []
    if not os.path.exists(filename):
        print(f"Plik {filename} nie istnieje!")
        return []
    
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(';')
            if len(parts) == 3:
                pid = int(parts[0])
                arrival = int(parts[1])
                burst = int(parts[2])
                processes.append(Process(pid, arrival, burst))
    return processes

def load_memory_data(filename):
    if not os.path.exists(filename):
        print(f"Plik {filename} nie istnieje!")
        return []
    
    with open(filename, 'r') as f:
        content = f.read().strip()
        #Format oddzielony spacjami
        pages = [int(p) for p in content.split()]
    return pages

def print_cpu_results(result):
    print(f"\nWyniki dla algorytmu: {result['name']}")
    print("-" * 65)
    print(f"{'PID':<5} | {'Arrival':<8} | {'Burst':<6} | {'Waiting':<8} | {'Turnaround':<10}")
    print("-" * 65)
    
    for p in result['processes']:
        print(f"{p.pid:<5} | {p.arrival_time:<8} | {p.burst_time:<6} | {p.waiting_time:<8} | {p.turnaround_time:<10}")
    
    print("-" * 65)
    print(f"Średni czas oczekiwania: {result['avg_waiting_time']:.2f}")
    print(f"Średni czas cyklu:       {result['avg_turnaround_time']:.2f}")

def main():
    print("=== Symulator Algorytmów Systemów Operacyjnych ===")
    
    cpu_file = "procesy.txt"
    mem_file = "pamiec.txt"
    
    choice = input("Czy wygenerować nowe dane? (t/n): ").strip().lower()
    if choice == 't':
        try:
            n_proc = int(input("Podaj liczbę procesów do wygenerowania: "))
            DataGenerator.generate_cpu_data(n_proc, cpu_file)
            
            n_pages = int(input("Podaj liczbę odwołań do stron: "))
            max_page = int(input("Podaj maksymalny numer strony (zakres stron): "))
            DataGenerator.generate_memory_data(n_pages, max_page, mem_file)
        except ValueError:
            print(" Podano nieprawidłową liczbę. Używam istniejących plików (jeśli są).")

    #2.Symulacja CPU
    print("\n>>> Symulacja Planowania CPU <<<")
    processes = load_cpu_data(cpu_file)
    
    if processes:
        #FCFS
        fcfs = FCFS()
        fcfs_result = fcfs.run(processes) #przekazujemy listę obiektów Process
        print_cpu_results(fcfs_result)
        
        #Round Robin
        try:
            quantum = int(input("\nPodaj kwant czasu dla Round Robin: "))
        except ValueError:
            quantum = 2
            print(f"Nieprawidłowa wartość, przyjęto domyślny kwant = {quantum}")
            
        rr = RoundRobin()
        rr_result = rr.run(processes, quantum)
        print_cpu_results(rr_result)
    else:
        print("Brak danych procesów do symulacji.")

    #3.Symulacja Pamięci
    print("\n>>> Symulacja Zastępowania Stron (Page Replacement) <<<")
    pages = load_memory_data(mem_file)
    
    if pages:
        try:
            frames = int(input("Podaj liczbę ramek pamięci: "))
        except ValueError:
            frames = 3
            print(f"Nieprawidłowa wartość, przyjęto domyślnie {frames} ramek.")
        
        #FIFO
        fifo = FIFO()
        fifo_faults = fifo.run(pages, frames)
        
        #LRU
        lru = LRU()
        lru_faults = lru.run(pages, frames)
        
        print("\nWyniki symulacji pamięci:")
        print("-" * 30)
        print(f"Algorytm | Liczba błędów strony")
        print("-" * 30)
        print(f"{'FIFO':<8} | {fifo_faults}")
        print(f"{'LRU':<8} | {lru_faults}")
        print("-" * 30)
    else:
        print("Brak danych pamięci do symulacji.")

if __name__ == "__main__":
    main()
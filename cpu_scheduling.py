from collections import deque

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid                  #ID procesu
        self.arrival_time = arrival_time #Czas nadejścia
        self.burst_time = burst_time     #Całkowity czas wykonywania 
        self.remaining_time = burst_time #Pozostały czas do wykonania 
        
        self.start_time = -1       #Czas pierwszego uruchomienia
        self.completion_time = 0   #Czas zakończenia
        self.waiting_time = 0      #Czas oczekiwania
        self.turnaround_time = 0   #Czas cyklu przetworzenia 

class FCFS:
    def run(self, processes):
        #Sortujemy wg czasu nadejścia
        sim_processes = sorted(processes, key=lambda p: p.arrival_time)
        
        current_time = 0
        total_waiting_time = 0
        total_turnaround_time = 0
        
        print("\n--- Rozpoczęcie symulacji FCFS ---")
        
        for p in sim_processes:
            #przesuwamy czas do czasu nadejścia
            if current_time < p.arrival_time:
                current_time = p.arrival_time
            
            p.start_time = current_time
            current_time += p.burst_time
            p.completion_time = current_time
            
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            
            total_waiting_time += p.waiting_time
            total_turnaround_time += p.turnaround_time
            
            #Resetujemy remaining_time 
            p.remaining_time = 0

        avg_waiting = total_waiting_time / len(processes)
        avg_turnaround = total_turnaround_time / len(processes)
        
        return {
            "name": "FCFS",
            "processes": sim_processes,
            "avg_waiting_time": avg_waiting,
            "avg_turnaround_time": avg_turnaround
        }

class RoundRobin:
    def run(self, processes, quantum):
        #Kopiujemy obiekty procesów, aby nie modyfikować z FCFS
        sim_processes = [Process(p.pid, p.arrival_time, p.burst_time) for p in processes]
        
        #Sortujemy wg czasu nadejścia
        processes_by_arrival = sorted(sim_processes, key=lambda p: p.arrival_time)
        
        queue = deque()
        current_time = 0
        completed_processes = []
        process_idx = 0
        n = len(sim_processes)
        
        total_waiting_time = 0
        total_turnaround_time = 0
        
        #Dodajemy pierwszy proces
        if n > 0 and processes_by_arrival[0].arrival_time > 0:
             current_time = processes_by_arrival[0].arrival_time

        #Pętla działa dopóki wszystkie procesy nie zostaną zakończone
        while len(completed_processes) < n:
            #Dodaj nowe procesy, które nadeszły do current_time
            while process_idx < n and processes_by_arrival[process_idx].arrival_time <= current_time:
                queue.append(processes_by_arrival[process_idx])
                process_idx += 1
            
            if not queue:
                # eśli kolejka pusta ale są jeszcze procesy które nadejdą później
                if process_idx < n:
                    current_time = processes_by_arrival[process_idx].arrival_time
                    queue.append(processes_by_arrival[process_idx])
                    process_idx += 1
                else:
                    break
            
            #Pobieramy proces z początku kolejki
            current_process = queue.popleft()
            
            #Jeśli to pierwsze uruchomienie procesu
            if current_process.start_time == -1:
                current_process.start_time = current_time
            
            #Wykonanie procesu
            if current_process.remaining_time > quantum:
                #Proces nie zdąży się wykonać w jednym kwancie
                current_time += quantum
                current_process.remaining_time -= quantum

                while process_idx < n and processes_by_arrival[process_idx].arrival_time <= current_time:
                    queue.append(processes_by_arrival[process_idx])
                    process_idx += 1
                
                queue.append(current_process)
            else:
                #Proces zakończy się w tym cyklu
                current_time += current_process.remaining_time
                current_process.remaining_time = 0
                current_process.completion_time = current_time
                
                #Obliczamy statystyki
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                
                total_waiting_time += current_process.waiting_time
                total_turnaround_time += current_process.turnaround_time
                
                completed_processes.append(current_process)
                
                while process_idx < n and processes_by_arrival[process_idx].arrival_time <= current_time:
                    queue.append(processes_by_arrival[process_idx])
                    process_idx += 1

        avg_waiting = total_waiting_time / n
        avg_turnaround = total_turnaround_time / n
        
        #Sortowanie wedlug ID
        completed_processes.sort(key=lambda p: p.pid)

        return {
            "name": f"Round Robin (Q={quantum})",
            "processes": completed_processes,
            "avg_waiting_time": avg_waiting,
            "avg_turnaround_time": avg_turnaround
        }



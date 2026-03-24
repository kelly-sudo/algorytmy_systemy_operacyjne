from collections import deque

class FIFO:
    #Symulacja algorytmu zastępowania stron FIFO (First In First Out)
    def run(self, pages, num_frames):
        frames = []
        page_faults = 0
        
        #Kolejka 
        queue = deque()
        
        for page in pages:
            if page not in frames:
                page_faults += 1
                if len(frames) < num_frames:
                    #Mamy wolne ramki
                    frames.append(page)
                    queue.append(page)
                else:
                    #Brak miejsca, usuwamy najstarszą stronę (z początku kolejki)
                    victim = queue.popleft()
                    frames.remove(victim)
                    
                    frames.append(page)
                    queue.append(page)
            #Jesli strona juz jest nic nie robimy
            
        return page_faults

class LRU:
    #Symulacja algorytmu zastępowania stron LRU (Least Recently Used)
    def run(self, pages, num_frames):
        frames = []
        page_faults = 0
        
        for page in pages:
            if page not in frames:
                page_faults += 1
                if len(frames) < num_frames:
                    frames.append(page)
                else:
                    #Usuwamy stronę, która była używana najdawniej
                    #Na liście 'frames', element na początku (indeks 0) będzie tym LRU,
                    #ponieważ przy każdym użyciu przesuwamy stronę na koniec listy
                    frames.pop(0)
                    frames.append(page)
            else:
                #Strona jest już w ramkach. Aktualizujemy jej pozycję jako "ostatnio używana"
                #Usuwamy ją z obecnej pozycji i dodajemy na koniec
                frames.remove(page)
                frames.append(page)
                
        return page_faults

        

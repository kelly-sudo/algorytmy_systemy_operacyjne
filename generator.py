import random

class DataGenerator:

    @staticmethod
    def generate_cpu_data(n, filename):   
        #Parametry
        #n (int): Liczba procesów do wygenerowania.
        #filename (str): Nazwa pliku do zapisu danych.

        try:
            with open(filename, 'w') as f:
                for i in range(n):
                    process_id = i + 1
                    arrival_time = random.randint(0, 50)
                    burst_time = random.randint(1, 20)
                    
                    # Zapis w formacie: ID;Arrival_Time;Burst_Time
                    f.write(f"{process_id};{arrival_time};{burst_time}\n")
            print(f"Wygenerowano {n} procesów i zapisano do pliku '{filename}'.")
        except IOError as e:
            print(f"Nie udało się zapisać danych do pliku: {e}")

    @staticmethod
    def generate_memory_data(n, max_page_id, filename):
        #Parametry
        #n (int): Długość ciągu odwołań (liczba zapytań).
        #max_page_id (int): Maksymalny numer strony (zakres 0 do max_page_id).
        #filename (str): Nazwa pliku do zapisu danych.
        try:
            with open(filename, 'w') as f:
                pages = []
                for _ in range(n):
                    page = random.randint(0, max_page_id)
                    pages.append(str(page))
                
                #Zapisujemy ciąg odwołań w jednej linii oddzielony spacjami
                f.write(" ".join(pages))
            print(f"Wygenerowano {n} odwołań do stron i zapisano do pliku '{filename}'.")
        except IOError as e:
            print(f"Nie udało się zapisać danych pamięci do pliku: {e}")




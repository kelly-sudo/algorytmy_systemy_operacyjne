Wstęp 
Celem projektu było stworzenie i zaimplementowanie wybranych algorytmów zarządzania 
zasobami w systemie operacyjnym. Kod został napisany w języku Python w sposób modułowy.  
Opis wybranych algorytmów 
Planowanie czasu procesora 
• FCFS (First Come First Serve): Jest to algorytm bez wywłaszczenia. Proces, który 
nadejdzie najszybciej jest obsługiwany jako pierwszy w całości.  
• Round Robin (RR): Jest to algorytm z wywłaszczeniem. Wykorzystuje się w nim kwant 
czasu.  Każdy proces otrzymuje dostęp do procesora na określony odcinek czasu, czyli 
kwant. Jeżeli nie zdąży się wykonać, trafia na koniec kolejki a jego miejscu zajmuje 
kolejny proces, który czeka.  
Zastępowania stron 
• FIFO (First In First Out): Najprostszy algorytm. Działa on na zasadzie usuwania strony, 
która została załadowana najwcześniej.  
• LRU (Least Recently Used): Wykorzystuje on historie użycia stron. W przypadku wolnej 
ramki, usuwa stronę, która była używana najrzadziej.  

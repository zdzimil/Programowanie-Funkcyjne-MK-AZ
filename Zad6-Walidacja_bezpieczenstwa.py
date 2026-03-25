# Słownik: "id": (rozmiar_naglowka, rozmiar_danych, port, flaga_aktywna)
pakiety_raw = {
    101: (20, 1480, 80, True),
    102: (40, 60, 443, True),
    103: (20, 1000, 22, False),
    104: (20, 0, 80, True),     # Pakiet pusty (podejrzany)
    105: (60, 1500, 443, True),
    106: (20, 500, 23, True),   # Port Telnet (niebezpieczny)
}

# 1. Walidacja Bezpieczeństwa (Czysta Funkcja)
# Napisz funkcję czy_bezpieczny(dane_pakietu). Pakiet jest niebezpieczny, jeśli:
# •	Jest kierowany na port 23 (Telnet) lub 22 (SSH).
# •	Jego rozmiar danych wynosi 0 przy aktywnej fladze. Użyj tej funkcji wraz z filter(), aby odsiać niebezpieczne pakiety ze słownika.
# Podpowiedź:
# pakiety_raw.items() zwraca listę krotek (id_pakietu, (rozmiar_naglowka, rozmiar_danych, port, flaga_aktywna)).
# Funkcja czy_bezpieczny powinna przyjmować taką krotkę i zwracać True, jeśli pakiet jest bezpieczny, lub False, jeśli jest niebezpieczny.
# header, data, port, active = item[1] pozwala na rozpakowanie wartości z krotki dla łatwiejszego dostępu.


# 2. Obliczanie Narzutu 
# Zdefiniuj wzór na narzut protokołu (overhead) jako stosunek nagłówka do całkowitego rozmiaru pakietu:
# Overhead = rozmiar_naglowka/(rozmiar_naglowka + rozmiar_danych)
# Użyj map() i lambdy, aby stworzyć nową listę krotek zawierających (id_pakietu, obliczony_overhead).
# Podpowiedź:
# jeśli bezpieczne to lista krotek (id_pakietu, (rozmiar_naglowka, rozmiar_danych, port, flaga_aktywna)) to,
# x[0] to ID pakietu, x[1][0] to rozmiar nagłówka, x[1][1] to rozmiar danych.


# 3. Kategoryzacja
# Napisz funkcję kategoryzuj(threshold), która zwraca funkcję (slajd 12).
# •	Funkcja wewnętrzna powinna sprawdzać, czy overhead pakietu przekracza podany próg .
# •	Wykorzystaj tę funkcję, aby przefiltrować listę z Kroku 2, zostawiając tylko pakiety o wysokim narzucie (np. powyżej 10%).

# 4. Statystyka Zbiorcza (Reduce)
# Zaimportuj reduce z functools. Oblicz łączną sumę wszystkich danych (rozmiar danych) tylko dla pakietów, które przeszły pomyślnie wszystkie poprzednie testy

# 5. Prezentacja Wyników
# Stwórz czytelny raport w konsoli, który wyświetli:
# • Pakiety z wysokim narzutem (ID i wartość overhead).
# • Końcową, zsumowaną wielkość przefiltrowanych danych z kroku 4.

# Poprawne wyniki:
# Pakiety z wysokim narzutem: [(102, 0.4)]
# Łączny rozmiar danych: 60

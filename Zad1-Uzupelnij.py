"""1.Uzupełnij by poprawnie powiększyć dwukrotnie tane liczby"""
liczby = [1, 2, 3, 4, 5]
powiekszone_liczby = list(map(lambda x: ___, liczby))

print(powiekszone_liczby)
# Oczekiwany wynik to [2, 4, 6, 8, 10]

"""2.Uzupełnij wyrażenie lambda oraz brakujący argument funkcji reduce, 
aby obliczyć iloczyn (wynik mnożenia) wszystkich liczb w liście."""
from functools import reduce

liczby = [1, 2, 3, 4, 5]
iloczyn = reduce(lambda x, y: ___, ___)

print(iloczyn)
# Oczekiwany wynik: 120

"""3.Uzupełnij wywołanie funkcji sorted, przekazując odpowiednią listę oraz tworząc wyrażenie lambda,
 które posortuje słowa według ich długości"""

slowa = ["Kapusta", "Kawa", "Fajerwerki", "Rurka"]

slowa_posortowane = sorted(___, key=___)

print(slowa_posortowane)
#Oczekiwany wynik to ['Kawa', 'Rurka', 'Kapusta', 'Fajerwerki']

"""Napisz funkcję, która rekurencyjnie oblicza sumę
 liczb od podanego n w dół do 0 (np. dla n=3 będzie to 3+2+1). """
def suma_rekurencyjna(n):
    if ___:
        return 0

    return n + ___

print(suma_rekurencyjna(5))
# Oczekiwany wynik: 15 (bo 5 + 4 + 3 + 2 + 1 + 0)

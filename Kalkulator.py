"""
Na slajdzie 11 pokazano kalkulator. Twoim zadaniem jest jego rozbudowa.
Stwórz cztery czyste funkcje: dla dodawania, odejmowania, mnożenia, dzielenia i potęgowania.
Zbuduj słownik, który jako klucze przyjmie znaki "+", "-", "*", "/", "^", a jako wartości przypisze odpowiednie funkcje.
"""

def dodaj(a,b): return a+b
def odejmij(a,b): return a-b
def pomnoz(a,b): return a*b
def podziel(a,b): return a/b
def podeguj(a,b): return a**b

kalkulator = {
    "+": dodaj,
    "-": odejmij,
    "*": pomnoz,
    "/": podziel,
    "^": podeguj
}

print(kalkulator["*"](2,3))
print(kalkulator["/"](6,2))
print(kalkulator["^"](2,3))

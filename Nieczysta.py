

Taski = ["Iść na siłkę", "Zrobić obiad"]
licznik_operacji = 2

def dodaj_taska(lista, nowe_zadanie):
    global licznik_operacji
    licznik_operacji += 1
    lista.append(nowe_zadanie)
    print(f"Dodano: {nowe_zadanie}. To już {licznik_operacji} task.")
    return lista

nowe_Taski = dodaj_taska(Taski, "Poczytaj książkę")


"""moje rozwiązanie

Taski = ["Iść na siłkę", "Zrobić obiad"]
licznik_operacji = 2

def dodaj_taska(lista, nowe_zadanie,obecny_licznik):
    nowy_licznik = obecny_licznik + 1
    nowa_lista = lista + [nowe_zadanie]
    return nowa_lista,nowy_licznik

nowe_taski, nowy_licznik = dodaj_taska(Taski,"Przeczytaj książkę",licznik_operacji)

print(nowe_taski, nowy_licznik) """
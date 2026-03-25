"""Twoim zadaniem jest przekształcenie tego kodu w poprawną czystą funkcje."""

Taski = ["Iść na siłkę", "Zrobić obiad"]
licznik_operacji = 2

def dodaj_taska(lista, nowe_zadanie):
    global licznik_operacji
    licznik_operacji += 1
    lista.append(nowe_zadanie)
    print(f"Dodano: {nowe_zadanie}. To już {licznik_operacji} task.")
    return lista

nowe_Taski = dodaj_taska(Taski, "Poczytaj książkę")



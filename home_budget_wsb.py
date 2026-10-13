import random


def pokaz_menu() -> None:
    print("\n=== MENEDŻER BUDŻETU ===")
    print("1. Dodaj przychód")
    print("2. Dodaj wydatek")
    print("3. Pokaż wszystkie transakcje")
    print("4. Pokaż saldo")
    print("5. Wydatki według kategorii")
    print("6. Usuń transakcję")
    print("0. Wyjście")

def wczytaj_kwote(komunikat: str) -> float:
    """Wczytuje dodatnią kwotę; powtarza pytanie przy błędnych danych."""
    # TODO: pętla while, sprawdzenie czy napis jest liczbą i czy > 0
    return float(input(komunikat))

def dodaj_transakcje(transakcje: list, typ: str) -> None:
    # TODO: wczytaj kategorię, kwotę, opis i dodaj słownik do listy
    kategoria = input("Podaj kategorię: ").strip()
    kwota = wczytaj_kwote('podaj kwotę, która stanowi ' + typ + ':')
    opis = input("Podaj opis: ").strip()
    transakcja = {'typ':typ, "kategoria": kategoria, "kwota": kwota, "opis": opis}
    transakcje.append(transakcja)

    # {"typ": "wydatek", "kategoria": "jedzenie", "kwota": 45.50, "opis": "zakupy"}

def pokaz_transakcje(transakcje: list) -> None:
    # TODO: tabela z numerami (enumerate) i f-stringami
    for n, transakcja in enumerate(transakcje):
        print(f'{n + 1:4} {transakcja['typ']:10} {transakcja['kategoria']:10} {transakcja['kwota']:10} {transakcja['opis']:10}')

def oblicz_saldo(transakcje: list) -> float:
    # TODO
    pass

def wydatki_wg_kategorii(transakcje: list) -> dict:
    # TODO
    pass

def usun_transakcje(transakcje: list) -> None:
    # TODO
    pass

def generuj(transakcje: list, trans_count) -> None:
    for _ in range(trans_count):
        typy = ['wydatek', 'przychód']
        typ = random.choice(typy)
        kategorie = ['jedzenie', 'picie', 'paliwo', 'telefon', 'wegiel']
        kategoria = random.choice(kategorie)
        kwota = round(random.random() * 100, 2)
        opis = 'losowanie'
        transakcja = {'typ': typ, "kategoria": kategoria, "kwota": kwota, "opis": opis}
        transakcje.append(transakcja)

def main() -> None:
    transakcje = []
    generuj(transakcje, 10)
    pokaz_transakcje(transakcje)

    while True:
        pokaz_menu()
        wybor = input("Wybierz opcję: ").strip()
        # TODO: obsługa opcji (if/elif lub match)
        match wybor:
            case "0":
                print("Do zobaczenia!")
                break
            case "1":
                dodaj_transakcje(transakcje, 'przychód')
                continue
            case "2":
                dodaj_transakcje(transakcje, 'wydatek')
                continue
            case "3":
                pokaz_transakcje(transakcje)
                continue
            case "4":
                oblicz_saldo(transakcje)
                continue
            case "5":
                wydatki_wg_kategorii(transakcje)
                continue
            case "6":
                usun_transakcje(transakcje)
                continue
            case _:
                print('Błędna komenda!\n')





if __name__ == "__main__":
    main()

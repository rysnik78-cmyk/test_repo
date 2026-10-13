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
    while True:
        try:
            kwota = float(input(komunikat))
        except ValueError:
            print("podaj poprawną liczbę")
            continue
        if kwota <= 0:
            print("podaj dodatnią liczbę")
            continue
        return kwota

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
    print('Transakcje w bazie:')
    print('-' * 60)
    nazwy_kolumn = ['l.p.', 'typ', 'kategoria', 'kwota', 'opis']
    print(f'| {nazwy_kolumn[0] :4} | {nazwy_kolumn[1]:10} | {nazwy_kolumn[2]:10} | {nazwy_kolumn[3]:10} | {nazwy_kolumn[4]:10} |')
    print('-' * 60)
    for n, transakcja in enumerate(transakcje):
        print(f'| {n+1 :4} | {transakcja['typ']:10} | {transakcja['kategoria']:10} | {transakcja['kwota']:10} | {transakcja['opis']:10} |')
    print('-' * 60)

def oblicz_saldo(transakcje: list) -> float:
    saldo = 0
    for transakcja in transakcje:
        if transakcja['typ'] == 'przychód':
            saldo += transakcja['kwota']
        else:
            saldo -= transakcja['kwota']
    return saldo

def wydatki_wg_kategorii(transakcje: list) -> dict:
    # TODO
    wydatki_kat_salda_dict = {}
    for transakcja in transakcje:
        if transakcja['kategoria'] not in wydatki_kat_salda_dict.keys():
            wydatki_kat_salda_dict[transakcja['kategoria']] = 0
        wydatki_kat_salda_dict[transakcja['kategoria']] += transakcja['kwota']

    return wydatki_kat_salda_dict

def usun_transakcje(transakcje: list, numer_transakcji) -> None:
    # TODO
    transakcje.pop(numer_transakcji - 1)

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
                print('Transakcja dodana do bazy')
                continue
            case "2":
                dodaj_transakcje(transakcje, 'wydatek')
                print('Transakcja dodana do bazy')
                continue
            case "3":
                pokaz_transakcje(transakcje)
                continue
            case "4":
                print(f'Saldo transakcji:{str(round(oblicz_saldo(transakcje), 2)):10}')
                continue
            case "5":
                print('\nSalda w obrębie kategorii:\n')

                for n, saldo in enumerate(wydatki_wg_kategorii(transakcje).items()):
                    print(f'{n+1:3} | {saldo[0]:20} | {round(saldo[1],2):7}')
                continue
            case "6":
                pokaz_transakcje(transakcje)
                no_trans_do_usun = int(input("Podaj numer transakcji do usunięcia: "))
                usun_transakcje(transakcje, no_trans_do_usun)
                print('Transakcje została usunięta z bazy')
                continue
            case "7":
                generuj(transakcje, 10)
                pokaz_transakcje(transakcje)
            case _:
                print('Błędna komenda!\n')





if __name__ == "__main__":
    main()

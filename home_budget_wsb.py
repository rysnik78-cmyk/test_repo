import os
import random
from datetime import date, datetime
import json

def pokaz_menu() -> None:
    print("\n=== MENEDŻER BUDŻETU ===")
    print("1. Dodaj przychód")
    print("2. Dodaj wydatek")
    print("3. Pokaż wszystkie transakcje")
    print("4. Pokaż saldo")
    print("5. Wydatki według kategorii")
    print("6. Usuń transakcję")
    print("7. *** Dodaj losowe transakcje ***")
    print("8. Największy wydatek")
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
    data_transakcji = str(date.today())
    transakcja = {'typ':typ, "kategoria": kategoria, "kwota": kwota, "opis": opis, "data": data_transakcji}
    transakcje.append(transakcja)
    print('Transakcja dodana do bazy')
    saldo = oblicz_saldo(transakcje)
    if saldo < 0:
        print('Uwaga!!! Saldo jest ujemne i wynosi', round(saldo, 2))
    # {"typ": "wydatek", "kategoria": "jedzenie", "kwota": 45.50, "opis": "zakupy"}

def pokaz_transakcje(transakcje: list, kat='all') -> None:
    # TODO: tabela z numerami (enumerate) i f-stringami
    print('Transakcje w bazie:')
    print('-' * 83)
    nazwy_kolumn = ['l.p.', 'typ', 'kategoria', 'kwota', 'opis', 'Data transakcji']
    print(f'| {nazwy_kolumn[0] :4} | {nazwy_kolumn[1]:10} | {nazwy_kolumn[2]:10} | {nazwy_kolumn[3]:10} | {nazwy_kolumn[4]:10} | {nazwy_kolumn[5]:20} |')
    print('-' * 83)
    znaleziono = 0
    for n, transakcja in enumerate(transakcje):
        # print(transakcja)
        if kat == 'all' or kat == transakcja['kategoria']:
            znaleziono += 1
            print(f'| {n+1 :4} | {transakcja['typ']:10} | {transakcja['kategoria']:10} | {transakcja['kwota']:10} | {transakcja['opis']:10} | {str(transakcja['data']):20} |')
    print('-' * 83)
    print(f'Znaleziono {znaleziono} transakcji.')

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
        data = str(datetime(random.randint(1900,2026), random.randint(1,12),random.randint(1,28)).date())
        transakcja = {'typ': typ, "kategoria": kategoria, "kwota": kwota, "opis": opis, "data": data}
        transakcje.append(transakcja)

def najwiekszy_wydatek(transakcje: list) -> None:
    max_wydatek = None
    for transakcja in transakcje:
        if transakcja['typ'] == 'przychód':
            continue
        if max_wydatek is None:
            max_wydatek = transakcja
            continue
        if transakcja['kwota'] > max_wydatek['kwota']:
            max_wydatek = transakcja
    return max_wydatek

def load_transactions():
    # TODO: obsługa ładowania z pliku
    if os.path.isfile("save_file.json"):
        save_file = open('save_file.json', 'r')
        transactions = json.load(save_file)
        save_file.close()
        return transactions
    else:
        return []

def save_transactions(transactions: list) -> None:
    # TODO: obsługa zapisu do pliku
        save_file = open('save_file.json', 'w')
        json.dump(transactions, save_file)
        save_file.close()

def main() -> None:
    transakcje = load_transactions()
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
                save_transactions(transakcje)
            case "2":
                dodaj_transakcje(transakcje, 'wydatek')
                save_transactions(transakcje)
            case "3":
                print('Podaj kategorię transakcji, które pokazać')
                print('Jeśli chcesz zobaczyć transakcje w zakresie wszystkich kategorii wpisz "ALL"')
                input_kategoria = input().strip().lower()
                pokaz_transakcje(transakcje, input_kategoria)
            case "4":
                print(f'Saldo transakcji:{str(round(oblicz_saldo(transakcje), 2)):10}')
            case "5":
                print('\nSalda w obrębie kategorii:\n')
                for n, saldo in enumerate(wydatki_wg_kategorii(transakcje).items()):
                    print(f'{n+1:3} | {saldo[0]:20} | {round(saldo[1],2):7}')
            case "6":
                pokaz_transakcje(transakcje)
                no_trans_do_usun = int(input("Podaj numer transakcji do usunięcia: "))
                usun_transakcje(transakcje, no_trans_do_usun)
                print('Transakcje została usunięta z bazy')
            case "7":
                generuj(transakcje, 10)
                # print(transakcje)
                pokaz_transakcje(transakcje)
                save_transactions(transakcje)
            case "8":
                max_wyd = najwiekszy_wydatek(transakcje)
                print('Największy wydatek to: ')
                print(f'| {max_wyd['typ']:10} | {max_wyd['kategoria']:10} | {max_wyd['kwota']:10} | {max_wyd['opis']:10} |')
            case _:
                print('Błędna komenda!\n')

if __name__ == "__main__":
    main()

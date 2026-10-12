## Godzina 8 – Projekt podsumowujący: Menedżer budżetu domowego

### Cel
Połączyć wszystkie poznane elementy w jedną aplikację konsolową, zbudowaną **proceduralnie** – z wielu małych funkcji.

### 8.1. Wymagania

Aplikacja przechowuje listę transakcji. Każda transakcja to słownik:
```python
{"typ": "wydatek", "kategoria": "jedzenie", "kwota": 45.50, "opis": "zakupy"}
```

Menu:
```
=== MENEDŻER BUDŻETU ===
1. Dodaj przychód
2. Dodaj wydatek
3. Pokaż wszystkie transakcje
4. Pokaż saldo
5. Wydatki według kategorii
6. Usuń transakcję
0. Wyjście
```

### 8.2. Projekt struktury (przed pisaniem kodu!)

Najpierw zaplanuj funkcje – każda robi **jedną rzecz**:

| Funkcja | Zadanie |
|---|---|
| `pokaz_menu()` | wypisuje menu |
| `wczytaj_kwote(komunikat)` | pobiera kwotę > 0 z walidacją |
| `dodaj_transakcje(transakcje, typ)` | pyta o dane i dodaje transakcję |
| `pokaz_transakcje(transakcje)` | wypisuje tabelę transakcji |
| `oblicz_saldo(transakcje)` | zwraca saldo (przychody − wydatki) |
| `wydatki_wg_kategorii(transakcje)` | zwraca słownik kategoria → suma |
| `usun_transakcje(transakcje)` | usuwa transakcję o podanym numerze |
| `main()` | pętla główna programu |

### 8.3. Szkielet do uzupełnienia przez studentów

```python
"""Menedżer budżetu domowego – projekt podsumowujący dzień 2."""


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
    pass


def dodaj_transakcje(transakcje: list, typ: str) -> None:
    # TODO: wczytaj kategorię, kwotę, opis i dodaj słownik do listy
    pass


def pokaz_transakcje(transakcje: list) -> None:
    # TODO: tabela z numerami (enumerate) i f-stringami
    pass


def oblicz_saldo(transakcje: list) -> float:
    # TODO
    pass


def wydatki_wg_kategorii(transakcje: list) -> dict:
    # TODO
    pass


def usun_transakcje(transakcje: list) -> None:
    # TODO
    pass


def main() -> None:
    transakcje = []
    while True:
        pokaz_menu()
        wybor = input("Wybierz opcję: ").strip()
        # TODO: obsługa opcji (if/elif lub match)
        if wybor == "0":
            print("Do zobaczenia!")
            break


if __name__ == "__main__":
    main()
```

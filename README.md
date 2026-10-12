# test_repo
testing git

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
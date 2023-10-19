# Cel: Stworzenie aplikacji ułatwiającej odczytywanie danych administracyjnych
## Opis:  
Stworzony przez nas system przedstawiający podział administracyjny Rzeczypospolitej Polskiej będzie się składał z aplikacji dostępowej oraz bazy danych.

Baza danych będzie się składać z trzech encji odpowiadającym stopniom jednostek administracyjnych w Polsce- województwa (1 stopień), powiatu (2stopień) oraz gmin (3 stopień).
### Encja województw będzie przechowywać dane dot. odpowiednich województw takich jak: 
- nazwa
- niepowtarzalny numer id
- powierzchnia
- ludność
- miasto wojewódzkie
- inne dane
### Encja powiatów będzie przechowywać dane dot. odpowiednich powiatów takich jak: 
- nazwa
- niepowtarzalny numer id
- powierzchnia
- ludność
- typ powiatu- miasto na prawie powiatu etc.
- województwo w którym się znajduje
- inne dane 
### Encja gmin będzie przechowywać dane dot. odpowiednich gmin takich jak: 
- nazwa
- niepowtarzalny numer id
- powierzchnia
- ludność
- typ gminy- miejska/wiejska/wiejsko-miejska
- powiat, w którym się znajduje
- inne dane
## Z systemu będą korzystać: odbiorcy danych (pracownicy urzędów), administratorzy danych oraz administratorzy IT.
### Odbiorca danych będzie mógł:
- wyświetlanie odpowiednich danych
- wnioskowanie o edycje danych
### Administrator danych:  
- edycja danych
- zapisywanie danych
### Administrator IT:  
- Robienie kopii zapasowej

Cechy funkcjonalne:
- System będzie pozwalał na wyszukiwanie elementów bazy danych za pomocą aplikacji dostępowej
- W bazie danych będzie istniała możliwość dodawania, edycji i usuwania danych
- System będzie automatycznie tworzył kopię danych poddawanych edycji czy usunięciu (kopia zapasowa starych danych)
- System będzie pozwalał na złożenie wniosku o edycję danych


Cechy niefunkcjonalne:
- Wyszukiwanie danych będzie mogło być ograniczone według dostępnych narzędzi filtrowania np.: wyświetlenie gmin w województwie, czy wyświetlenie zadanych powiatów zaczynających się na jakąś literę
- Dodawanie, edycja i usuwanie danych będzie możliwe tylko z poziomu administratora danych
- Wnioski o edycję dane składane będą przez użytkowników (odbiorców danych) i będą mogły być zaakceptowane lub odrzucone przez administratorów bazy danych
- Administrator IT będzie miał kontrolę nad tworzoną kopią zapasową


*~~Dostęp do bazy danych będzie możliwy poprzez aplikację dostępową, za pomocą której użytkownik będzie miał dostęp do przechowywanych danych oraz możliwość manipulacji nimi, czyli operacje ich dodawania, usuwania i edytowania. Użytkownik będzie miał możliwość wyświetlania zawartości bazy danych według podanych przez niego kryteriów np.: wyświetlanie wszystkich gmin w województwie, których nazwa zaczyna się na literę „A”, czy wyświetlenie wszystkich nazw gmin wiejskich w danym powiecie.~~*

# Aplikacja Administracji Polski
#### Przedmiot: Bazy Danych 2 <br> Prowadzący: dr inż. Roman Ptak
<pre>

</pre>
| Nr grupy     |        1        |
|--------------|:---------------:|
| Skład grupy  | Jan Zieniewicz,   Adrian Kotula,   Jędrzej Koba|
| Termin       | Pt 11:15  rok akademicki 2023/34      |
| Temat projektu| „Podział administracyjny Polski”|
<pre>

</pre>
# Aplikacja "Podział administracyjny RP"
## Cel: Stworzenie aplikacji ułatwiającej odczytywanie danych administracyjnych
## Opis:  
Stworzony przez nas system przedstawiający podział administracyjny Rzeczypospolitej Polskiej składa się z aplikacji dostępowej oraz bazy danych.

Baza danych składa się z trzech encji odpowiadającym stopniom jednostek administracyjnych w Polsce- województwa (1 stopień), powiatu (2stopień) oraz gmin (3 stopień).
### Encja województw przechowuje dane dot. odpowiednich województw takich jak: 
- nazwa
- niepowtarzalny numer id- teryt
- powierzchnia
- ludność
- miasto wojewódzkie
- współrzędne miasta wojewódzkiego
- inne dane
### Encja powiatów przechowuje dane dot. odpowiednich powiatów takich jak: 
- nazwa
- niepowtarzalny numer idv
- powierzchnia
- ludność
- typ powiatu- miasto na prawie powiatu etc.
- stolica powiatu
- współrzędne stolicy powiatu
- województwo w którym się znajduje
- inne dane 
### Encja gmin przechowuje dane dot. odpowiednich gmin takich jak: 
- nazwa
- niepowtarzalny numer id- teryt
- powierzchnia
- ludność
- typ gminy- miejska/wiejska/wiejsko-miejska
- stolica gminy
- współrzędne stolicy gminy
- powiat, w którym się znajduje
- inne dane
## Z systemu będą korzystać: odbiorcy danych (pracownicy urzędów), administratorzy danych oraz administratorzy IT.
### Odbiorca danych:
- wyświetlanie danych o województwach
- wyświetlanie danych o powiatach/ gminach na podstawie danych dotyczących województw
- wyświetlanie danych o powiatach
- wyświetlanie danych o województwach/ gminach na podstawie danych dot. powiatów
- wyświetlanie danych o gminach
- wyświetlanie danych o województwach/ powiatach na podstawie danych dot. gmin
- wyświetlanie danych spełniających warunki zadane przez użytkownika
- składanie wniosku o edycję istniejących danych lub dodanie nowych
### Administrator danych: 
- administrator danych posiada dostęp do takich samych funkcjonalności co odbiorca danych
- dodawanie nowych województw
- usuwanie województw
- modyfikowanie danych podstawowych województwa
- modyfikowanie danych statystycznych województwa
- modyfikowanie danych administracyjnych województwa
- modyfikowanie danych geolokalizacyjnych województwa
- wyszukiwanie województw
- dodawanie nowych powiatów
- usuwanie powiatu
- modyfikowanie danych podstawowych powiatu
- modyfikowanie danych statystycznych powiatu
- modyfikowanie danych administracyjnych powiatu
- modyfikowanie danych geolokalizacyjnych powiatu
- wyszukiwanie powiatów
- dodawanie nowych gmin
- usuwanie gmin
- modyfikowanie danych podstawowych gminy
- modyfikowanie danych statystycznych gminy
- modyfikowanie danych administracyjnych gminy
- modyfikowanie danych geolokalizacyjnych gminy
- wyszukiwanie gmin
- zapisywanie danych
- rozpatrywanie wniosków o dodanie/zmianę/usunięcie danych złożonych przez użytkownika
### Administrator IT:  
- administrator IT ma dostęp do takich samych funkcjonalności co administrator danych oraz odbiorca danych
- konfiguracja zasad tworzenia automatycnzej kopii zapasowej
- tworzenie kont dla nowych użytkownikow
- zarządzanie bazą danych


### Cechy niefunkcjonalne:
- Aplikacja dostępowa do bazy danych będzie w formie aplikacji webowej.
- Aplikacja dostępowa będzie napisana w Python3 z wykorzystaniem framework`u Django.
- Aplikacja będzie posiadać intuicyjny interfejs uzytkownika.
- Aplikacja będzie działać na przęglądarkach dostępnych na systemach: Windows, Linux, macOS.
- Baza danych będzie wykorzystywać technologię MySQL.
- Stabilność zapewniają testy manualne dla aplikacji django.
- System gwarantuje integralność danych, poprzez weryfikację użytkowników.
- System obsługuje 300 zapytań na sekundę 
- System jest ciągle dostępny z wyjątkiem czasu, w którym prowadzone są prace konserwacyjne. 
- Prace konserwacyjne odbywają się w środy w godzinach 11-16.
- Zapewniamy całodobowe wsparcie techniczne.
- Monitorujemy użycie zasobów.
- największa encja (gmin) ma około 2500 rekordów.





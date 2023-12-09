## Indeksy jednokolumnowe:
### według nazw: województw, powiatów i gmin
---
### Indeksy złożone:
- Indeks łączący id, nazwę i stolicę (województwa, powiatu, gminy)
- Indeks łączący id, nazwę i powierzchnię (województwa, powiatu, gminy)
- Indeks łączący id, nazwę i ludność (województwa, powiatu, gminy)
- Indeks łączący id, nazwę i typ gminy lub powiatu (w zależności czy to powiat czy gmina)
- Indeks łączący id, nazwę i inne dane (województwa, powiatu, gminy)
- Indeks łączący id, nazwę i województwo w którym znajduje się powiat/ powiat w którym znajduje się gmina
- Indeks łączący id, nazwę, stolicę, współrzędne stolicy i powierzchnię (województwa, powiatu, gminy)
- Indeks łączący id, nazwę, stolicę, współrzędne stolicy (województwa, powiatu, gminy)
- Indeks łączący id, nazwę, stolicę i typ gminy lub powiatu (w zależności czy to powiat czy gmina)

### Widoki:
- Widok pokazujący nazwę, stolicę, współrzędne stolicy (lub stolic) i  powierzchnię  (województwa, powiatu, gminy)
- Widok pokazujący nazwę,  stolicę i typ gminy, to w jakim powiecie się znajduje i w jakim województwie się znajduje
- Widok pokazujący nazwę, stolicę i typ powiatu, to w jakim województwie się znajduje i jakie gminy się w nim znajdują
- Widok pokazujący nazwę i stolicę (lub stolice) województwa, to jakie są w nim powiaty i jakie są w nim gminy
- Widok pokazujący nazwę, stolicę, powierzchnię, ludność i inne dane (województwo, powiat, gmina)

### Poziomy uprawnień:
- Użytkownik podstawowy, będzie mógł tylko odczytywać dane z bazy (dostęp do tablicy województw, powiatów i gmin typu read only)
- Administrator danych, będzie mógł edytować informacje, które zawiera baza danych (dostęp do całej bazy, edycja danych, dodawanie rekordów, usuwanie ich)
- Administrator aplikacji, będzie mógł zarządzać bazą danych jak i tworzyć wymagane konta użytkowników, i wykonywać kopie zapasowe bazy danych

### Procedury składowane:
- Procedura realizująca dodawanie nowych województw, powiatów czy gmin do bazy danych
- Procedura pozwalająca na edycję i aktualizację danych województw, powiatów czy gmin
- Procedury pozwalające na wyszukiwanie danych województw, powiatów czy gmin według określonych kryteriów


### Triggery:
Before delete (województwo, powiat) sprawdzający przed usunięciem czy nie ma powiązanych rekordów z tym rekordem
Trigger sprawdzający poprawność wprowadzanych danych np.: czy liczba ludności nie jest liczbą ujemną

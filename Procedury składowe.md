## Procedury składowe:
### Województwa:
#### DodajWojewództwo:
```
SQL
CREATE PROCEDURE DodajWojewodstwo 
( 
    IN p_Nazwa varchar(255), 
    IN p_MiastoWojewodzkie varchar(255), 
    IN p_WspolrzedneMiastaWojewodzkiego varchar(255), 
    IN p_DrugieMiastoWojewodzkie varchar(255), 
    IN p_WspolrzedneDrugiegoMiastaWojewodzkiego varchar(255),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    INSERT INTO Wojewodstwa (Nazwa, Miasto_wojewodzkie, Współrzędne_miasta_wojewódzkiego, Drugie_miasto_wojewódzkie, Współrzędne_drugiego_miasta_wojewódzkiego, dodatkowe_informacje)
    VALUES (p_Nazwa, p_MiastoWojewodzkie, p_WspolrzedneMiastaWojewodzkiego, p_DrugieMiastoWojewodzkie, p_WspolrzedneDrugiegoMiastaWojewodzkiego, p_DodatkoweInformacje);
END;
```
#### EdytujDaneWojewództwa
```
SQL
CREATE PROCEDURE EdytujDaneWojewodztwa
(
    IN p_IdTerytowe integer,
    IN p_Nazwa varchar(255),
    IN p_MiastoWojewodzkie varchar(255),
    IN p_WspolrzedneMiastaWojewodzkiego varchar(255),
    IN p_DrugieMiastoWojewodzkie varchar(255),
    IN p_WspolrzedneDrugiegoMiastaWojewodzkiego varchar(255),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    UPDATE Województwa
    SET 
        Nazwa = p_Nazwa,
        Miasto_wojewodzkie = p_MiastoWojewodzkie,
        Współrzędne_miasta_wojewódzkiego = p_WspolrzedneMiastaWojewodzkiego,
        Drugie_miasto_wojewódzkie = p_DrugieMiastoWojewodzkie,
        Współrzędne_drugiego_miasta_wojewódzkiego = p_WspolrzedneDrugiegoMiastaWojewodzkiego,
        dodatkowe_informacje = p_DodatkoweInformacje
    WHERE Id_terytowe = p_IdTerytowe;
END;
```
#### WyszukajWojewództwo
```
SQL
CREATE PROCEDURE WyszukajWojewodztwo
(
    IN p_Kryterium varchar(255)
)
BEGIN
    SELECT *
    FROM JednostkiTerytorialne
    WHERE Nazwa LIKE CONCAT('%', p_Kryterium, '%')
       OR Miasto_wojewodzkie LIKE CONCAT('%', p_Kryterium, '%')
       OR dodatkowe_informacje LIKE CONCAT('%', p_Kryterium, '%')
       OR Drugie_miasto_wojewódzkie LIKE CONCAT('%', p_Kryterium, '%');
END;
```
### Powiaty:
#### DodajPowiat:
```
SQL
CREATE PROCEDURE DodajPowiat
(
    IN p_Nazwa varchar(255),
    IN p_StolicaPowiatu varchar(255),
    IN p_WspolrzedneStolicyPowiatu varchar(255),
    IN p_TypPowiatu integer(10),
    IN p_Wojewodztwo integer(10),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    INSERT INTO JednostkiAdministracyjne (Nazwa, Stolica_powiatu, Współrzędne_stolicy_powiatu, Typ_powiatu, Województwo_w_którym_się_znajduje, dodatkowe_informacje)
    VALUES (p_Nazwa, p_StolicaPowiatu, p_WspolrzedneStolicyPowiatu, p_TypPowiatu, p_Wojewodztwo, p_DodatkoweInformacje);
END;
```
#### EdytujDanePowiatu
```
SQL
CREATE PROCEDURE EdytujDanePowiatu
(
    IN p_IdTerytowe integer(10),
    IN p_Nazwa varchar(255),
    IN p_StolicaPowiatu varchar(255),
    IN p_WspolrzedneStolicyPowiatu varchar(255),
    IN p_TypPowiatu integer(10),
    IN p_Wojewodztwo integer(10),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    UPDATE Powiaty
    SET 
        Nazwa = p_Nazwa,
        Stolica_powiatu = p_StolicaPowiatu,
        Współrzędne_stolicy_powiatu = p_WspolrzedneStolicyPowiatu,
        Typ_powiatu = p_TypPowiatu,
        Województwo_w_którym_się_znajduje = p_Wojewodztwo,
        dodatkowe_informacje = p_DodatkoweInformacje
    WHERE Id_terytowe = p_IdTerytowe;
END;
```
#### WyszukajPowiat
```
SQL
CREATE PROCEDURE WyszukajPowiat
(
    IN p_Kryterium varchar(255)
)
BEGIN
    SELECT *
    FROM JednostkiAdministracyjne
    WHERE Nazwa LIKE CONCAT('%', p_Kryterium, '%')
       OR Stolica_powiatu LIKE CONCAT('%', p_Kryterium, '%')
       OR dodatkowe_informacje LIKE CONCAT('%', p_Kryterium, '%');
END;
```
### Gminy:
#### DodajGminę:
```
SQL
CREATE PROCEDURE DodajGmine
(
    IN p_Nazwa varchar(255),
    IN p_StolicaGminy varchar(255),
    IN p_WspolrzedneStolicyGminy varchar(255),
    IN p_TypGminy integer(10),
    IN p_Powierzchnia float(10),
    IN p_Ludnosc integer(10),
    IN p_Powiat integer(10),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    INSERT INTO JednostkiAdministracyjne (Nazwa, Stolica_gminy, Współrzędne_stolicy_gminy, Typ_gminy, Powierzchnia, Ludnosc, Powiat_w_którym_się_znajduje, dodatkowe_informacje)
    VALUES (p_Nazwa, p_StolicaGminy, p_WspolrzedneStolicyGminy, p_TypGminy, p_Powierzchnia, p_Ludnosc, p_Powiat, p_DodatkoweInformacje);
END;
```
#### EdytujDaneGminy
```
SQL
CREATE PROCEDURE EdytujDaneGminy
(
    IN p_IdTerytowe integer(10),
    IN p_Nazwa varchar(255),
    IN p_StolicaGminy varchar(255),
    IN p_WspolrzedneStolicyGminy varchar(255),
    IN p_TypGminy integer(10),
    IN p_Powierzchnia float(10),
    IN p_Ludnosc integer(10),
    IN p_Powiat integer(10),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    UPDATE Gminy
    SET 
        Nazwa = p_Nazwa,
        Stolica_gminy = p_StolicaGminy,
        Współrzędne_stolicy_gminy = p_WspolrzedneStolicyGminy,
        Typ_gminy = p_TypGminy,
        Powierzchnia = p_Powierzchnia,
        Ludnosc = p_Ludnosc,
        Powiat_w_którym_się_znajduje = p_Powiat,
        dodatkowe_informacje = p_DodatkoweInformacje
    WHERE Id_terytowe = p_IdTerytowe;
END;
```
#### WyszukajGminę
```
SQL
CREATE PROCEDURE WyszukajGmine
(
    IN p_Kryterium varchar(255)
)
BEGIN
    SELECT *
    FROM JednostkiAdministracyjne
    WHERE Nazwa LIKE CONCAT('%', p_Kryterium, '%')
       OR Stolica_gminy LIKE CONCAT('%', p_Kryterium, '%')
       OR dodatkowe_informacje LIKE CONCAT('%', p_Kryterium, '%');
END;
```


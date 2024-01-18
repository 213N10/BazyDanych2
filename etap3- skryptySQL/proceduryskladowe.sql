CREATE PROCEDURE DodajWojewodstwo
(
    IN p_Nazwa varchar(255),
    IN p_MiastoWojewodzkie varchar(255),
    IN p_WspolrzedneMiastaWojewodzkiegoX varchar(255),
    IN p_WspolrzedneMiastaWojewodzkiegoY varchar(255),
    IN p_DrugieMiastoWojewodzkie varchar(255),
    IN p_WspolrzedneDrugiegoMiastaWojewodzkiegoX varchar(255),
    IN p_WspolrzedneDrugiegoMiastaWojewodzkiegoY varchar(255),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    INSERT INTO administracjaRP.Wojewodztwa (Nazwa, Miasto_wojewodzkie, Wspolrzedne_miasta_wojewodzkiego_x,Wspolrzedne_miasta_wojewodzkiego_y, Drugie_miasto_wojewodzkie, Wspolrzedne_drugiego_miasta_wojewodzkiego_x,Wspolrzedne_drugiego_miasta_wojewodzkiego_y, inne_dane)
    VALUES (p_Nazwa, p_MiastoWojewodzkie, p_WspolrzedneMiastaWojewodzkiegoX,p_WspolrzedneMiastaWojewodzkiegoY, p_DrugieMiastoWojewodzkie, p_WspolrzedneDrugiegoMiastaWojewodzkiegoX,p_WspolrzedneDrugiegoMiastaWojewodzkiegoY, p_DodatkoweInformacje);
END;


CREATE PROCEDURE EdytujDaneWojewodztwa
(
    IN p_IdTerytowe integer,
    IN p_Nazwa varchar(255),
    IN p_MiastoWojewodzkie varchar(255),
    IN p_WspolrzedneMiastaWojewodzkiegoX varchar(255),
    IN p_WspolrzedneMiastaWojewodzkiegoY varchar(255),
    IN p_DrugieMiastoWojewodzkie varchar(255),
    IN p_WspolrzedneDrugiegoMiastaWojewodzkiegoX varchar(255),
    IN p_WspolrzedneDrugiegoMiastaWojewodzkiegoY varchar(255),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    UPDATE administracjaRP.Wojewodztwa
    SET
        Nazwa = p_Nazwa,
        Miasto_wojewodzkie = p_MiastoWojewodzkie,
        Wspolrzedne_miasta_wojewodzkiego_x = p_WspolrzedneMiastaWojewodzkiegoX,
        Wspolrzedne_miasta_wojewodzkiego_y = p_WspolrzedneMiastaWojewodzkiegoY,
        Drugie_miasto_wojewodzkie = p_DrugieMiastoWojewodzkie,
        Wspolrzedne_drugiego_miasta_wojewodzkiego_x = p_WspolrzedneDrugiegoMiastaWojewodzkiegoX,
        Wspolrzedne_drugiego_miasta_wojewodzkiego_y = p_WspolrzedneDrugiegoMiastaWojewodzkiegoY,
        inne_dane = p_DodatkoweInformacje
    WHERE Id_terytowe = p_IdTerytowe;
END;


CREATE PROCEDURE WyszukajWojewodztwo
(
    IN p_Kryterium varchar(255)
)
BEGIN
    SELECT *
    FROM administracjaRP.Wojewodztwa
    WHERE Nazwa LIKE CONCAT('%', p_Kryterium, '%')
       OR Miasto_wojewodzkie LIKE CONCAT('%', p_Kryterium, '%')
       OR inne_dane LIKE CONCAT('%', p_Kryterium, '%')
       OR Drugie_miasto_wojewodzkie LIKE CONCAT('%', p_Kryterium, '%');
END;




CREATE PROCEDURE DodajPowiat
(
    IN p_Nazwa varchar(255),
    IN p_StolicaPowiatu varchar(255),
    IN p_WspolrzedneStolicyPowiatuX varchar(255),
    IN p_WspolrzedneStolicyPowiatuY varchar(255),
    IN p_TypPowiatu integer(10),
    IN p_Wojewodztwo integer(10),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    INSERT INTO administracjaRP.Powiaty (Nazwa, Stolica_powiatu, Wspolrzedne_stolicy_x, Wspolrzedne_stolicy_y, Typ_powiatu, Wojewodztwo_w_ktorym_sie_znajduje, inne_dane)
    VALUES (p_Nazwa, p_StolicaPowiatu, p_WspolrzedneStolicyPowiatuX,p_WspolrzedneStolicyPowiatuY, p_TypPowiatu, p_Wojewodztwo, p_DodatkoweInformacje);
END;



CREATE PROCEDURE EdytujDanePowiatu
(
    IN p_IdTerytowe integer(10),
    IN p_Nazwa varchar(255),
    IN p_StolicaPowiatu varchar(255),
    IN p_WspolrzedneStolicyPowiatuX varchar(255),
    IN p_WspolrzedneStolicyPowiatuY varchar(255),
    IN p_TypPowiatu integer(10),
    IN p_Wojewodztwo integer(10),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    UPDATE administracjaRP.Powiaty
    SET
        Nazwa = p_Nazwa,
        Stolica_powiatu = p_StolicaPowiatu,
        Wspolrzedne_stolicy_x = p_WspolrzedneStolicyPowiatuX,
        Wspolrzedne_stolicy_y = p_WspolrzedneStolicyPowiatuY,
        Typ_powiatu = p_TypPowiatu,
        Wojewodztwo_w_ktorym_sie_znajduje = p_Wojewodztwo,
        inne_dane = p_DodatkoweInformacje
    WHERE Id_terytowe = p_IdTerytowe;
END;



CREATE PROCEDURE WyszukajPowiat
(
    IN p_Kryterium varchar(255)
)
BEGIN
    SELECT *
    FROM administracjaRP.Powiaty
    WHERE Nazwa LIKE CONCAT('%', p_Kryterium, '%')
       OR Stolica_powiatu LIKE CONCAT('%', p_Kryterium, '%')
       OR inne_dane LIKE CONCAT('%', p_Kryterium, '%');
END;


CREATE PROCEDURE DodajGmine
(
    IN p_Nazwa varchar(255),
    IN p_StolicaGminy varchar(255),
    IN p_WspolrzedneStolicyGminyX varchar(255),
    IN p_WspolrzedneStolicyGminyY varchar(255),
    IN p_TypGminy integer(10),
    IN p_Powierzchnia float(10),
    IN p_Ludnosc integer(10),
    IN p_Powiat integer(10),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    INSERT INTO administracjaRP.Gminy (Nazwa, Stolica_gminy, Wspolrzedne_stolicy_x,Wspolrzedne_stolicy_y, Typ_gminy, Powierzchnia, Ludnosc, Powiat_w_ktorym_sie_znajduje, inne_dane)
    VALUES (p_Nazwa, p_StolicaGminy, p_WspolrzedneStolicyGminyX,p_WspolrzedneStolicyGminyY, p_TypGminy, p_Powierzchnia, p_Ludnosc, p_Powiat, p_DodatkoweInformacje);
END;




CREATE PROCEDURE EdytujDaneGminy
(
    IN p_IdTerytowe integer(10),
    IN p_Nazwa varchar(255),
    IN p_StolicaGminy varchar(255),
    IN p_WspolrzedneStolicyGminyX varchar(255),
    IN p_WspolrzedneStolicyGminyY varchar(255),
    IN p_TypGminy integer(10),
    IN p_Powierzchnia float(10),
    IN p_Ludnosc integer(10),
    IN p_Powiat integer(10),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    UPDATE administracjaRP.Gminy
    SET
        Nazwa = p_Nazwa,
        Stolica_gminy = p_StolicaGminy,
        Wspolrzedne_stolicy_x = p_WspolrzedneStolicyGminyX,
        Wspolrzedne_stolicy_y = p_WspolrzedneStolicyGminyY,
        Typ_gminy = p_TypGminy,
        Powierzchnia = p_Powierzchnia,
        Ludnosc = p_Ludnosc,
        Powiat_w_ktorym_sie_znajduje = p_Powiat,
        inne_dane = p_DodatkoweInformacje
    WHERE Id_terytowe = p_IdTerytowe;
END;


CREATE PROCEDURE WyszukajGmine
(
    IN p_Kryterium varchar(255)
)
BEGIN
    SELECT *
    FROM administracjaRP.Gminy
    WHERE Nazwa LIKE CONCAT('%', p_Kryterium, '%')
       OR Stolica_gminy LIKE CONCAT('%', p_Kryterium, '%')
       OR inne_dane LIKE CONCAT('%', p_Kryterium, '%');
END;





-- Widok pokazujący nazwę województwa, stolicę województwa, współrzędne stolicy
-- województwa, możliwej drugiej stolicy województwa i powierzchnię województwa
CREATE VIEW WidokWojewodztw AS
SELECT
    Nazwa,
    Miasto_wojewodzkie,
    Wspolrzedne_miasta_wojewodzkiego_x,
    Wspolrzedne_miasta_wojewodzkiego_y,
    Drugie_miasto_wojewódzkie,
    Wspolrzedne_drugiego_miasta_wojewodzkiego_x,
    Wspolrzedne_drugiego_miasta_wojewodzkiego_y,
    Powierzchnia
FROM
    administracjaRP.Wojewodztwa;


-- Widok pokazujący nazwę powiatu, stolicę powiatu, współrzędne stolicy powiatu i  powierzchnię powiatu
CREATE VIEW WidokPowiatow AS
SELECT
    Nazwa,
    Stolica_powiatu,
    Wspolrzedne_stolicy_x,
    Wspolrzedne_stolicy_y,
    Powierzchnia
FROM
    administracjaRP.Powiaty;


-- Widok pokazujący nazwę gminy, stolicę gminy, współrzędne stolicy gminy i  powierzchnię gminy

CREATE VIEW WidokGmin AS
SELECT
    Nazwa,
    Stolica_gminy,
    Wspolrzedne_stolicy_x,
    Wspolrzedne_stolicy_y,
    Powierzchnia
FROM
    administracjaRP.Gminy;








-- Widok pokazujący nazwę gminy, stolicę gminy, typ gminy, to w jakim powiecie gmina się znajduje (nazwa powiatu) i w jakim województwie gmina się znajduje (nazwa województwa)

CREATE VIEW WidokInformacjiGminNazwaPowiatuWojewodztwa AS
SELECT
    administracjaRP.Gminy.Nazwa AS GminaNazwa,
    administracjaRP.Gminy.Stolica_gminy,
    administracjaRP.Typ_gminy.Typ,
    administracjaRP.Powiaty.Nazwa AS PowiatNazwa,
    administracjaRP.Wojewodztwa.Nazwa AS WojewodztwoNazwa
FROM
    administracjaRP.Gminy
JOIN
    administracjaRP.Powiaty ON Gminy.Powiat_w_ktorym_sie_znajduje = Powiaty.Id_terytowe
JOIN
    administracjaRP.Wojewodztwa ON Powiaty.Wojewodztwo_w_ktorym_sie_znajduje = Wojewodztwa.Id_terytowe
JOIN
    administracjaRP.Typ_gminy ON Gminy.Id_terytowe = Typ_gminy.Id;



-- Widok pokazujący nazwę powiatu, stolicę powiatu, typ powiatu, to w jakim województwie (nazwa województwa) powiat się znajduje i jakie gminy (nazwy gmin) znajdują się w tym powiecie

CREATE VIEW WidokInformacjiPowiatowNazwyWojewodztGmin AS
SELECT
    P.Nazwa AS PowiatNazwa,
    P.Stolica_powiatu,
    P.Wspolrzedne_stolicy_x,
    P.Wspolrzedne_stolicy_y,
    P.Powierzchnia AS PowiatPowierzchnia,
    P.Ludnosc AS PowiatLudnosc,
    P.Inne_dane AS PowiatInneDane,
    W.Nazwa AS WojewodztwoNazwa,
    G.Nazwa AS GminaNazwa,
    TP.Typ AS TypPowiatu
FROM
    administracjaRP.Powiaty P
JOIN
    administracjaRP.Wojewodztwa W ON P.Wojewodztwo_w_ktorym_sie_znajduje = W.Id_terytowe
LEFT JOIN
    administracjaRP.Gminy G ON P.Id_terytowe = G.Powiat_w_ktorym_sie_znajduje
JOIN
    administracjaRP.Typy_powiatow TP ON P.Typ_powiatu = TP.Id;



-- Widok pokazujący nazwę województwa, stolicę województwa i możliwą drugą stolicę województwa, to jakie powiaty są w tym województwie (nazwy powiatów) i jakie gminy są w tym województwie (nazwy gmin)

CREATE VIEW WidokInformacjiWojewodztwNazwyPowiatowGmin AS
SELECT
    W.Nazwa AS WojewodztwoNazwa,
    W.Miasto_wojewodzkie AS MiastoWojewodzkie,
    W.Drugie_miasto_wojewódzkie AS DrugieMiastoWojewodzkie,
    P.Nazwa AS PowiatNazwa,
    G.Nazwa AS GminaNazwa
FROM
    administracjaRP.Wojewodztwa W
LEFT JOIN
    administracjaRP.Powiaty P ON W.Id_terytowe = P.Wojewodztwo_w_ktorym_sie_znajduje
LEFT JOIN
    administracjaRP.Gminy G ON P.Id_terytowe = G.Powiat_w_ktorym_sie_znajduje;


-- Widok pokazujący nazwę województwa, stolicę województwa, powierzchnię województwa, ludność województwa i inne dane województwa

CREATE VIEW WidokInformacjiWojewodztwInne AS
SELECT
    Nazwa,
    Miasto_wojewodzkie,
    Powierzchnia,
    Ludnosc,
    Inne_dane
FROM
    administracjaRP.Wojewodztwa;

-- Widok pokazujący nazwę powiatu, stolicę powiatu, powierzchnię powiatu, ludność powiatu i inne dane powiatu

CREATE VIEW WidokInformacjiPowiatowInne AS
SELECT
    Nazwa,
    Stolica_powiatu,
    Powierzchnia,
    Ludnosc,
    Inne_dane
FROM
    administracjaRP.Powiaty;

-- Widok pokazujący nazwę gminy, stolicę gminy, powierzchnię gminy, ludność gminy i inne dane gminy

CREATE VIEW WidokInformacjiGminInne AS
SELECT
    Nazwa,
    Stolica_gminy,
    Powierzchnia,
    Ludnosc,
    Inne_dane
FROM
    administracjaRP.Gminy;


-- Widok pokazujący nazwę województwa, stolicę województwa, powiaty jakie się w nim znajdują (nazwa powiatu, typ powiatu) i gminy jakie znajdują się w tym województwie (nazwa gminy, typ gminy)

CREATE VIEW WidokWojewodztwaWszystkieTypy AS
SELECT
    W.Nazwa AS WojewodztwoNazwa,
    W.Miasto_wojewodzkie AS MiastoWojewodzkie,
    TP.Typ AS TypPowiatu,
    TG.Typ AS TypGminy,
    P.Nazwa AS PowiatNazwa,
    G.Nazwa AS GminaNazwa
FROM
    administracjaRP.Wojewodztwa W
JOIN
    administracjaRP.Powiaty P ON W.Id_terytowe = P.Wojewodztwo_w_ktorym_sie_znajduje
JOIN
    administracjaRP.Gminy G ON P.Id_terytowe = G.Powiat_w_ktorym_sie_znajduje
JOIN
    administracjaRP.Typy_powiatow TP ON P.Typ_powiatu = TP.Id
JOIN
    administracjaRP.Typ_gminy TG ON G.Typ_gminy = TG.Id;



CREATE PROCEDURE DodajWojewodztwo(
    IN Id_terytowe_param INT,
    IN Nazwa_param VARCHAR(100),
    IN Miasto_wojewodzkie_param VARCHAR(100),
    IN Wspolrzedne_miasta_wojewodzkiego_x_param FLOAT,
    IN Wspolrzedne_miasta_wojewodzkiego_y_param FLOAT,
    IN Drugie_miasto_wojewodzkie_param VARCHAR(100),
    IN Wspolrzedne_drugiego_miasta_wojewodzkiego_x_param FLOAT,
    IN Wspolrzedne_drugiego_miasta_wojewodzkiego_y_param FLOAT,
    IN Powierzchnia_param FLOAT,
    IN Ludnosc_param INT,
    IN Inne_dane_param VARCHAR(255)
)
BEGIN
    INSERT INTO administracjaRP.Wojewodztwa (Id_terytowe, Nazwa, Miasto_wojewodzkie, Wspolrzedne_miasta_wojewodzkiego_x, Wspolrzedne_miasta_wojewodzkiego_y, Drugie_miasto_wojewódzkie, Wspolrzedne_drugiego_miasta_wojewodzkiego_x, Wspolrzedne_drugiego_miasta_wojewodzkiego_y, Powierzchnia, Ludnosc, Inne_dane)
    VALUES (
        Id_terytowe_param,
        Nazwa_param,
        Miasto_wojewodzkie_param,
        Wspolrzedne_miasta_wojewodzkiego_x_param,
        Wspolrzedne_miasta_wojewodzkiego_y_param,
        Drugie_miasto_wojewodzkie_param,
        Wspolrzedne_drugiego_miasta_wojewodzkiego_x_param,
        Wspolrzedne_drugiego_miasta_wojewodzkiego_y_param,
        Powierzchnia_param,
        Ludnosc_param,
        Inne_dane_param
    );
END;

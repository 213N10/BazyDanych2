
CREATE PROCEDURE DodajNowaJednostke
(
    IN p_Nazwa varchar(255),
    IN p_MiastoWojewodzkie varchar(255),
    IN p_WspolrzedneMiastaWojewodzkiego varchar(255),
    IN p_DrugieMiastoWojewodzkie varchar(255),
    IN p_WspolrzedneDrugiegoMiastaWojewodzkiego varchar(255),
    IN p_DodatkoweInformacje varchar(255)
)
BEGIN
    INSERT INTO JednostkiTerytorialne (Nazwa, Miasto_wojewodzkie, Współrzędne_miasta_wojewódzkiego, Drugie_miasto_wojewódzkie, Współrzędne_drugiego_miasta_wojewódzkiego, dodatkowe_informacje)
    VALUES (p_Nazwa, p_MiastoWojewodzkie, p_WspolrzedneMiastaWojewodzkiego, p_DrugieMiastoWojewodzkie, p_WspolrzedneDrugiegoMiastaWojewodzkiego, p_DodatkoweInformacje);
END;
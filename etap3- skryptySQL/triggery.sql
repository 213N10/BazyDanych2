
CREATE TRIGGER after_insert_powiat_population
AFTER INSERT ON administracjaRP.Powiaty
FOR EACH ROW
BEGIN
    UPDATE administracjaRP.Wojewodztwa W
    SET W.Ludnosc = (SELECT SUM(P.Ludnosc) FROM administracjaRP.Powiaty P WHERE P.Wojewodztwo_w_ktorym_sie_znajduje = W.Id_terytowe)
    WHERE W.Id_terytowe = NEW.Wojewodztwo_w_ktorym_sie_znajduje;
END;


CREATE TRIGGER after_update_powiat_population
AFTER UPDATE ON administracjaRP.Powiaty
FOR EACH ROW
BEGIN
    UPDATE administracjaRP.Wojewodztwa W
    SET W.Ludnosc = (SELECT SUM(P.Ludnosc) FROM administracjaRP.Powiaty P WHERE P.Wojewodztwo_w_ktorym_sie_znajduje = W.Id_terytowe)
    WHERE W.Id_terytowe = NEW.Wojewodztwo_w_ktorym_sie_znajduje;
END;


CREATE TRIGGER after_delete_powiat_population
AFTER DELETE ON administracjaRP.Powiaty
FOR EACH ROW
BEGIN
    UPDATE administracjaRP.Wojewodztwa W
    SET W.Ludnosc = (SELECT SUM(P.Ludnosc) FROM administracjaRP.Powiaty P WHERE P.Wojewodztwo_w_ktorym_sie_znajduje = W.Id_terytowe)
    WHERE W.Id_terytowe = OLD.Wojewodztwo_w_ktorym_sie_znajduje;
END;


CREATE TRIGGER after_delete_powiat
AFTER DELETE ON administracjaRP.Powiaty
FOR EACH ROW
BEGIN
    UPDATE administracjaRP.Wojewodztwa W
    SET W.Powierzchnia = (SELECT SUM(P.Powierzchnia) FROM administracjaRP.Powiaty P WHERE P.Wojewodztwo_w_ktorym_sie_znajduje = W.Id_terytowe)
    WHERE W.Id_terytowe = OLD.Wojewodztwo_w_ktorym_sie_znajduje;
END;






CREATE TRIGGER after_insert_powiat
AFTER INSERT ON administracjaRP.Powiaty
FOR EACH ROW
BEGIN
    UPDATE administracjaRP.Wojewodztwa W
    SET W.Powierzchnia = (SELECT SUM(P.Powierzchnia) FROM administracjaRP.Powiaty P WHERE P.Wojewodztwo_w_ktorym_sie_znajduje = W.Id_terytowe)
    WHERE W.Id_terytowe = NEW.Wojewodztwo_w_ktorym_sie_znajduje;
END;

CREATE TRIGGER after_insert_gmina
AFTER INSERT ON administracjaRP.Gminy
FOR EACH ROW
BEGIN
    UPDATE administracjaRP.Powiaty P
    SET P.Powierzchnia = (SELECT SUM(G.Powierzchnia) FROM administracjaRP.Gminy G WHERE G.Powiat_w_ktorym_sie_znajduje = P.Id_terytowe)
    WHERE P.Id_terytowe = NEW.Powiat_w_ktorym_sie_znajduje;
END;


CREATE TRIGGER after_update_powiat
AFTER UPDATE ON administracjaRP.Powiaty
FOR EACH ROW
BEGIN
    UPDATE administracjaRP.Wojewodztwa W
    SET W.Powierzchnia = (SELECT SUM(P.Powierzchnia) FROM administracjaRP.Powiaty P WHERE P.Wojewodztwo_w_ktorym_sie_znajduje = W.Id_terytowe)
    WHERE W.Id_terytowe = NEW.Wojewodztwo_w_ktorym_sie_znajduje;
END;


CREATE TRIGGER after_update_gmina
AFTER UPDATE ON administracjaRP.Gminy
FOR EACH ROW
BEGIN
    UPDATE administracjaRP.Powiaty P
    SET P.Powierzchnia = (SELECT SUM(G.Powierzchnia) FROM administracjaRP.Gminy G WHERE G.Powiat_w_ktorym_sie_znajduje = P.Id_terytowe)
    WHERE P.Id_terytowe = NEW.Powiat_w_ktorym_sie_znajduje;
END;


CREATE TRIGGER after_delete_gmina
AFTER DELETE ON administracjaRP.Gminy
FOR EACH ROW
BEGIN
    UPDATE administracjaRP.Powiaty P
    SET P.Powierzchnia = (SELECT SUM(G.Powierzchnia) FROM administracjaRP.Gminy G WHERE G.Powiat_w_ktorym_sie_znajduje = P.Id_terytowe)
    WHERE P.Id_terytowe = OLD.Powiat_w_ktorym_sie_znajduje;
END;

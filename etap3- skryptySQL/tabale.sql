drop database if exists administracjaRP;
create database administracjaRP;
use administracjaRP;
CREATE TABLE Gminy (Id_terytowe int(10) NOT NULL AUTO_INCREMENT,
                    Nazwa varchar(50) NOT NULL,
                    Stolica_gminy varchar(50) NOT NULL,
                    Wspolrzedne_stolicy_x float NOT NULL,
                    Wspolrzedne_stolicy_y float NOT NULL,
                    Powierzchnia float,
                    Ludnosc int(10),
                    Inne_dane varchar(10000),
                    Powiat_w_ktorym_sie_znajduje int(10) NOT NULL,
                    Typ_gminy int(10) NOT NULL, PRIMARY KEY (Id_terytowe),
                    INDEX (Nazwa), INDEX (Stolica_gminy),
                    INDEX (Powierzchnia),
                    INDEX (Ludnosc), INDEX (Powiat_w_ktorym_sie_znajduje),
                    INDEX (Typ_gminy),
                    CHECK (ludnosc >= 0 AND powierzchnia > 0));

CREATE TABLE Typ_gminy (Id int(10) NOT NULL AUTO_INCREMENT, Typ varchar(50) NOT NULL UNIQUE, PRIMARY KEY (Id));

CREATE TABLE Powiaty (Id_terytowe int(10) NOT NULL AUTO_INCREMENT,
                      Nazwa varchar(50) NOT NULL,
                      Stolica_powiatu varchar(50) NOT NULL,
                      Wspolrzedne_stolicy_x float NOT NULL,
                      Wspolrzedne_stolicy_y float NOT NULL,
                      Powierzchnia float, Ludnosc int(10),
                      Inne_dane varchar(10000),
                      Wojewodztwo_w_ktorym_sie_znajduje int(10) NOT NULL,
                      Typ_powiatu int(10) NOT NULL, PRIMARY KEY (Id_terytowe),
                      INDEX (Nazwa),
                      INDEX (Stolica_powiatu),
                      INDEX (Powierzchnia),
                      INDEX (Ludnosc),
                      INDEX (Wojewodztwo_w_ktorym_sie_znajduje),
                      INDEX (Typ_powiatu));

CREATE TABLE Typy_powiatow (Id int(10) NOT NULL AUTO_INCREMENT, Typ varchar(50) NOT NULL UNIQUE, PRIMARY KEY (Id));

CREATE TABLE Wojewodztwa (Id_terytowe int(10) NOT NULL AUTO_INCREMENT,
                          Nazwa varchar(50) NOT NULL,
                          Miasto_wojewodzkie varchar(50) NOT NULL,
                          Wspolrzedne_miasta_wojewodzkiego_x float NOT NULL,
                          Wspolrzedne_miasta_wojewodzkiego_y float NOT NULL,
                          Drugie_miasto_wojewódzkie varchar(50),
                          Wspolrzedne_drugiego_miasta_wojewodzkiego_x float,
                          Wspolrzedne_drugiego_miasta_wojewodzkiego_y float,
                          Powierzchnia float, Ludnosc int(10),
                          Inne_dane varchar(10000),
                          PRIMARY KEY (Id_terytowe),
                          INDEX (Nazwa),
                          INDEX (Miasto_wojewodzkie),
                          INDEX (Drugie_miasto_wojewodzkie),
                          INDEX (Powierzchnia),
                          INDEX (Ludnosc));
ALTER TABLE Gminy ADD CONSTRAINT FKGminy238740 FOREIGN KEY (Powiat_w_ktorym_sie_znajduje) REFERENCES Powiaty (Id_terytowe);
ALTER TABLE Gminy ADD CONSTRAINT FKGminy440456 FOREIGN KEY (Typ_gminy) REFERENCES Typ_gminy (Id);
ALTER TABLE Powiaty ADD CONSTRAINT FKPowiaty461300 FOREIGN KEY (Wojewodztwo_w_ktorym_sie_znajduje) REFERENCES Wojewodztwa (Id_terytowe);
ALTER TABLE Powiaty ADD CONSTRAINT FKPowiaty612684 FOREIGN KEY (Typ_powiatu) REFERENCES Typy_powiatow (Id);




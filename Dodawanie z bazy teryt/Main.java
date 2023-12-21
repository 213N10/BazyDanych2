import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int currentCityNumber = 0;
        int currentWojewodztwoId = 0;
        int currentPowiatId = 0;
        int lines = 0;
        int lastIdGminy = 0;


        String url = "jdbc:mysql://localhost:3306/administracjaRP";
        String username = ""; //username
        String password = ""; //password
        try(Connection connection = DriverManager.getConnection(url,username,password)){

        try(BufferedReader buffer = new BufferedReader(new FileReader("TERC_Urzedowy_2023-12-21.csv"))) {
            String line;
            Random random = new Random();
            while((line = buffer.readLine()) != null){
                if(lines == 0){
                    lines++;
                    continue;
                }
                String miasto = "miasto" + currentCityNumber;
                currentCityNumber++;
                String[] values = line.split(";");
                float randomPowierzchnia = random.nextFloat() * 20;
                int randomPopulacja = random.nextInt(10000) + 100;
                int randomint = random.nextInt(6);
                float randomX = random.nextFloat() + 49 + randomint;
                float randomintY = random.nextInt(9);
                float randomY = random.nextFloat() + randomintY ;
                int randomStringLength = random.nextInt(1001);
                //wojewodztwo
                if(values[1] == ""){
                    currentWojewodztwoId = Integer.parseInt(values[0]);
                    String insertWoj = "INSERT INTO Wojewodztwa (Id_terytowe,Nazwa, Miasto_wojewodzkie, Wspolrzedne_miasta_wojewodzkiego_x, Wspolrzedne_miasta_wojewodzkiego_y, " +
                            " Inne_dane) VALUES (?, ?, ?, ?, ?, ?)";
                    PreparedStatement preparewWoj = connection.prepareStatement(insertWoj);
                    String randomString = generateRandomString(randomStringLength);
                    preparewWoj.setString(1, values[0]);
                    preparewWoj.setString(2, values[4]);
                    preparewWoj.setString(3, miasto);
                    preparewWoj.setString(4, Float.toString(randomX));
                    preparewWoj.setString(5, Float.toString(randomY));
                    preparewWoj.setString(6, randomString);

                    preparewWoj.addBatch();
                    preparewWoj.executeBatch();
                } else if (values[2] == "") {

                    String insertPowiat = "INSERT INTO Powiaty (Id_terytowe,Nazwa, Stolica_powiatu, Wspolrzedne_stolicy_x, Wspolrzedne_stolicy_y, " +
                            " Inne_dane, Wojewodztwo_w_ktorym_sie_znajduje, Typ_powiatu) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
                    PreparedStatement preparePowiat = connection.prepareStatement(insertPowiat);
                    String randomString = generateRandomString(randomStringLength);
                    String idPowiatu = values[0] + values[1];
                    currentPowiatId = Integer.parseInt(idPowiatu);
                            String typ_powiatu;
                    if(values[5].equals("powiat")) {
                        typ_powiatu = "1";
                    } else {
                        typ_powiatu = "2";
                    }
                    preparePowiat.setString(1, idPowiatu);
                    preparePowiat.setString(2, values[4]);
                    preparePowiat.setString(3, miasto);
                    preparePowiat.setString(4, Float.toString(randomX));
                    preparePowiat.setString(5, Float.toString(randomY));
                    preparePowiat.setString(6, randomString);
                    preparePowiat.setString(7, Integer.toString(currentWojewodztwoId));
                    preparePowiat.setString(8, typ_powiatu);
                    preparePowiat.addBatch();
                    preparePowiat.executeBatch();
                } else{
                    System.out.println("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
                    String insertGmina = "INSERT INTO Gminy (Id_terytowe,Nazwa, Stolica_gminy, Wspolrzedne_stolicy_x, Wspolrzedne_stolicy_y, " +
                            "Powierzchnia, Ludnosc, Inne_dane, Powiat_w_ktorym_sie_znajduje, Typ_gminy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
                    PreparedStatement prepareGmina = connection.prepareStatement(insertGmina);
                    String randomString = generateRandomString(randomStringLength);
                    int typ_gminy = Integer.parseInt(values[3]);
                    if(typ_gminy > 5){
                        typ_gminy = typ_gminy - 2;
                    }

                    String idGminy = values[0] + values[1] + values[2];

                    if(lastIdGminy == Integer.parseInt(idGminy)){
                        continue;
                    }
                    lastIdGminy = Integer.parseInt(idGminy);
                    prepareGmina.setString(1, idGminy);
                    prepareGmina.setString(2, values[4]);
                    prepareGmina.setString(3, miasto);
                    prepareGmina.setString(4, Float.toString(randomX));
                    prepareGmina.setString(5, Float.toString(randomY));
                    prepareGmina.setString(6, Float.toString(randomPowierzchnia));
                    prepareGmina.setString(7, Integer.toString(randomPopulacja));
                    prepareGmina.setString(8, randomString);
                    prepareGmina.setString(9, Integer.toString(currentPowiatId));
                    prepareGmina.setString(10, Integer.toString(typ_gminy));

                    prepareGmina.addBatch();
                    prepareGmina.executeBatch();
                }
            }

        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } ;
    } catch (SQLException e) {
            throw new RuntimeException(e);
       }
    }

    public static String generateRandomString(int length) {
        int leftLimit = 97; // 'a'
        int rightLimit = 122; // 'z'
        Random random = new Random();

        String generatedString = random.ints(leftLimit, rightLimit + 1)
                .limit(length)
                .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                .toString();

        return generatedString;
    }
}

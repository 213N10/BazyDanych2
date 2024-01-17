from django.db import models

# Create your models here.






class Gminy(models.Model):
    id_terytowe = models.AutoField(db_column='Id_terytowe', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=50)  # Field name made lowercase.
    stolica_gminy = models.CharField(db_column='Stolica_gminy', max_length=50)  # Field name made lowercase.
    wspolrzedne_stolicy_x = models.FloatField(db_column='Wspolrzedne_stolicy_x')  # Field name made lowercase.
    wspolrzedne_stolicy_y = models.FloatField(db_column='Wspolrzedne_stolicy_y')  # Field name made lowercase.
    powierzchnia = models.FloatField(db_column='Powierzchnia', blank=True, null=True)  # Field name made lowercase.
    ludnosc = models.IntegerField(db_column='Ludnosc', blank=True, null=True)  # Field name made lowercase.
    inne_dane = models.CharField(db_column='Inne_dane', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    powiat_w_ktorym_sie_znajduje = models.ForeignKey('Powiaty', db_column='Powiat_w_ktorym_sie_znajduje', on_delete=models.CASCADE)  # Field name made lowercase.
    typ_gminy = models.ForeignKey('TypGminy', db_column='Typ_gminy',on_delete=models.CASCADE)  # Field name made lowercase.

    def __str__(self):
        return self.nazwa

    class Meta:
        
        db_table = 'gminy'


class Powiaty(models.Model):
    id_terytowe = models.AutoField(db_column='Id_terytowe', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=50)  # Field name made lowercase.
    stolica_powiatu = models.CharField(db_column='Stolica_powiatu', max_length=50)  # Field name made lowercase.
    wspolrzedne_stolicy_x = models.FloatField(db_column='Wspolrzedne_stolicy_x')  # Field name made lowercase.
    wspolrzedne_stolicy_y = models.FloatField(db_column='Wspolrzedne_stolicy_y')  # Field name made lowercase.
    powierzchnia = models.FloatField(db_column='Powierzchnia', blank=True, null=True)  # Field name made lowercase.
    ludnosc = models.IntegerField(db_column='Ludnosc', blank=True, null=True)  # Field name made lowercase.
    inne_dane = models.CharField(db_column='Inne_dane', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    wojewodztwo_w_ktorym_sie_znajduje = models.ForeignKey('Wojewodztwa', db_column='Wojewodztwo_w_ktorym_sie_znajduje', on_delete=models.CASCADE)  # Field name made lowercase.
    typ_powiatu = models.ForeignKey('TypyPowiatow', db_column='Typ_powiatu',on_delete=models.CASCADE)  # Field name made lowercase.

    def __str__(self):
        return self.nazwa

    class Meta:
        
        db_table = 'powiaty'


class TypGminy(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    typ = models.CharField(db_column='Typ', unique=True, max_length=50)  # Field name made lowercase.

    def __str__(self):
        return self.typ

    class Meta:
        
        db_table = 'typ_gminy'


class TypyPowiatow(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    typ = models.CharField(db_column='Typ', unique=True, max_length=50)  # Field name made lowercase.

    def __str__(self):
        return self.typ

    class Meta:
        
        db_table = 'typy_powiatow'


class Wojewodztwa(models.Model):
    id_terytowe = models.AutoField(db_column='Id_terytowe', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=50)  # Field name made lowercase.
    miasto_wojewodzkie = models.CharField(db_column='Miasto_wojewodzkie', max_length=50)  # Field name made lowercase.
    wspolrzedne_miasta_wojewodzkiego_x = models.FloatField(db_column='Wspolrzedne_miasta_wojewodzkiego_x')  # Field name made lowercase.
    wspolrzedne_miasta_wojewodzkiego_y = models.FloatField(db_column='Wspolrzedne_miasta_wojewodzkiego_y')  # Field name made lowercase.
    drugie_miasto_wojewodzkie = models.CharField(db_column='Drugie_miasto_wojewodzkie', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wspolrzedne_drugiego_miasta_wojewodzkiego_x = models.FloatField(db_column='Wspolrzedne_drugiego_miasta_wojewodzkiego_x', blank=True, null=True)  # Field name made lowercase.
    wspolrzedne_drugiego_miasta_wojewodzkiego_y = models.FloatField(db_column='Wspolrzedne_drugiego_miasta_wojewodzkiego_y', blank=True, null=True)  # Field name made lowercase.
    powierzchnia = models.FloatField(db_column='Powierzchnia', blank=True, null=True)  # Field name made lowercase.
    ludnosc = models.IntegerField(db_column='Ludnosc', blank=True, null=True)  # Field name made lowercase.
    inne_dane = models.CharField(db_column='Inne_dane', max_length=10000, blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return self.nazwa

    class Meta:
        
        db_table = 'wojewodztwa'

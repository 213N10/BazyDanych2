from django.db import models

# Create your models here.



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gminy(models.Model):
    id_terytowe = models.AutoField(db_column='Id_terytowe', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=50)  # Field name made lowercase.
    stolica_gminy = models.CharField(db_column='Stolica_gminy', max_length=50)  # Field name made lowercase.
    wspolrzedne_stolicy_x = models.FloatField(db_column='Wspolrzedne_stolicy_x')  # Field name made lowercase.
    wspolrzedne_stolicy_y = models.FloatField(db_column='Wspolrzedne_stolicy_y')  # Field name made lowercase.
    powierzchnia = models.FloatField(db_column='Powierzchnia', blank=True, null=True)  # Field name made lowercase.
    ludnosc = models.IntegerField(db_column='Ludnosc', blank=True, null=True)  # Field name made lowercase.
    inne_dane = models.CharField(db_column='Inne_dane', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    powiat_w_ktorym_sie_znajduje = models.ForeignKey('Powiaty', models.DO_NOTHING, db_column='Powiat_w_ktorym_sie_znajduje')  # Field name made lowercase.
    typ_gminy = models.ForeignKey('TypGminy', models.DO_NOTHING, db_column='Typ_gminy')  # Field name made lowercase.

    class Meta:
        managed = False
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
    wojewodztwo_w_ktorym_sie_znajduje = models.ForeignKey('Wojewodztwa', models.DO_NOTHING, db_column='Wojewodztwo_w_ktorym_sie_znajduje')  # Field name made lowercase.
    typ_powiatu = models.ForeignKey('TypyPowiatow', models.DO_NOTHING, db_column='Typ_powiatu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'powiaty'


class TypGminy(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    typ = models.CharField(db_column='Typ', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typ_gminy'


class TypyPowiatow(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    typ = models.CharField(db_column='Typ', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typy_powiatow'


class Wojewodztwa(models.Model):
    id_terytowe = models.AutoField(db_column='Id_terytowe', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=50)  # Field name made lowercase.
    miasto_wojewodzkie = models.CharField(db_column='Miasto_wojewodzkie', max_length=50)  # Field name made lowercase.
    wspolrzedne_miasta_wojewodzkiego_x = models.FloatField(db_column='Wspolrzedne_miasta_wojewodzkiego_x')  # Field name made lowercase.
    wspolrzedne_miasta_wojewodzkiego_y = models.FloatField(db_column='Wspolrzedne_miasta_wojewodzkiego_y')  # Field name made lowercase.
    drugie_miasto_wojewˇdzkie = models.CharField(db_column='Drugie_miasto_wojewˇdzkie', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wspolrzedne_drugiego_miasta_wojewodzkiego_x = models.FloatField(db_column='Wspolrzedne_drugiego_miasta_wojewodzkiego_x', blank=True, null=True)  # Field name made lowercase.
    wspolrzedne_drugiego_miasta_wojewodzkiego_y = models.FloatField(db_column='Wspolrzedne_drugiego_miasta_wojewodzkiego_y', blank=True, null=True)  # Field name made lowercase.
    powierzchnia = models.FloatField(db_column='Powierzchnia', blank=True, null=True)  # Field name made lowercase.
    ludnosc = models.IntegerField(db_column='Ludnosc', blank=True, null=True)  # Field name made lowercase.
    inne_dane = models.CharField(db_column='Inne_dane', max_length=10000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wojewodztwa'

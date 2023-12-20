create user 'adminDanych'@'localhost' identified by '0000';
grant create, alter, drop, insert, update, delete, select, references on administracjaRP.* to 'adminDanych'@'localhost' WITH GRANT OPTION;
create user 'gosc'@'localhost';
grant select on administracjaRP.* to 'gosc'@'localhost' with grant option;
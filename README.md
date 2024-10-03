/EN<br /> Since this is a highly specific hacked together program for college, to launch it you'll need to:<br /> a) Tweak it to use an SQL engine of your liking (SQLite for example), then create a user with specific credential setup mentioned in code, and then create the database and users using .sql query files in /mysql <br />
OR<br />
b) Launch a MySQL/MariaDB server and create a user with specific credential setup mentioned in code, and then create the database and users using query files in /mysql Only then the DB part of the program will be functional
<br />
/RU<br /> Так как это очень специфическое и сделанное на скорую руку для техникума приложение, то для его запуска понадобится: а) Изменение кода для использования СУБД вашего предпочтения (напр. SQLite), и после этого создание пользователей с входными данными, указанными в коде, а далее создание базы данных с использованием .sql файлов в /mysql <br />
ИЛИ<br />
b) Запуск сервера MySQL/MariaDB, и после этого создание пользователей с входными данными, указанными в коде, а далее создание базы данных с использованием .sql файлов в /mysql
Только после этого часть программы с обращениями к БД будет работать

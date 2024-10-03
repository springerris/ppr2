""" 
Название: модуль соединения с базой данных MySQL
Разработал: Асанишвили Лука Гелович ТИП-63
Дата: 09.05.2025

Основные классы:
▪ Dbcon() - Является классом для соединения с СУБД MySQL. Содержит курсор, соединение и метод создания курсора.
"""


import mysql.connector
from mysql.connector import errorcode

class Dbcon():
    def __init__(self):
        self.role = ""
        self.user_login = ""
        self.user_password = ""
        self.cnx = mysql.connector.connect(user='registrator', password='', database='computer_db')
        self.cur = self.cnx.cursor(buffered=True)
    
    def setupcur(self):
        self.cur = self.cnx.cursor(buffered=True)
     

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
     

"""
Производственная практика ПП02 по модулю ПМ02. ПМ.02 Осуществление интеграции
программных модулей
Название: приложение для выполнения инвентаризации помещений проведения киберспортивных соревнований.
Разработал: Асанишвили Лука Гелович ТИП-63
Дата: 10.05.2025
Язык: Python
Краткое описание:
Данное программное обеспечение предназначено для выполнения инвентаризации 
помещений проведения киберспортивных соревнований.
Задание:
Разработать ПО, которое должно обеспечивать:
▪ Ффункции просмотра списка компьютеров в каждом отделении, их характеристик, стоимости и состояния. 
  Данные выводятся в виде таблицы и списка. 
▪ Также ПО должно выводить список ФИО и должностей сотрудников в виде таблицы.
▪ Функционал перемещения компьютеров на склад
▪ Функционал перемещения компьютеров со склада в отделения.
▪ Входные данные поступают в виде информации, заполняемой пользователем на форме.
▪ Выходные данные показываются в списках, таблицах и всплывающих окнах.

Формы, используемые в программе:
▪ Приветствия
▪ Авторизации
▪ Регистрации
▪ Главного меню
▪ Просмотра сотрудников
▪ Просмотра компьютеров
▪ Редактирования списка компьютеров + просмотра склада

Основные классы:
▪ Program() - Является главным классом. Управляет ходом программы
▪ Welcome_window(QWidget) - Реализация окна приветствия. Даёт возможность выбрать регистрацию или авторизацию как способ входа.
▪ Main_menu(QWidget) - Реализация главного меню. Содержит меторы quit, goto_editpcs(переход в редактирование списка компьютеров), 
goto_viewpcs(переход в просмотр компьютеров), goto_viewemp(переход в просмотр сотрудников)
▪ Registration_window(QWidget) - Реализует окно регистрации. Имеет методы проверки пароля на правильность и метод проверки занятости логина.
▪ Authorization_window(QWidget) - Реализация окна авторизации. Имеет методы проверки существования аккаунта с таким логином и паролем.
▪ View_pcs(QWidget) - Реализация окна просмотра списка компьютеров. Имеет метод просмотра характеристик компьютера, выбора помещения из списка, заполнения таблицы данными.
▪ View_employees(QWidget) - Реализация окна просмотра сотрудников. Имеет методы сортировки по ФИО и по должности.
▪ Edit_pcs(QWidget) - Реализация окна редактирования списка компьютеров. Имеет методы как у View_pcs и также: перемещения компьютеров на склад, со склада, списывания со склада.
"""




import sys
import mysql.connector
from mysql.connector import errorcode
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QLineEdit
from PyQt6.QtCore import QDate, Qt
from PyQt6 import uic
from string import ascii_uppercase
from charshift import shift_chars
from dbconnector import Dbcon




class Program():                            # Класс главной программы
    def __init__(self):
        self.main_menu = self.Main_menu()
        self.dbcon = Dbcon()
        self.welcome_window = self.Welcome_window()
        self.dlg = QtWidgets.QDialog()
        uic.loadUi("warning_dialog.ui",self.dlg)
      

    class Main_menu(QWidget):               # Класс главного окна

        class Edit_pcs(QWidget):            # Класс окна редактирования компьютеров
            def __init__(self):
                super().__init__()
                uic.loadUi("edit_pcs.ui",self)
                self.goback_button.clicked.connect(self.goback)
                self.exit_button.clicked.connect(self.quit)
                self.adres_box.currentTextChanged.connect(self.query_pcs)
                self.adres_box_2.currentTextChanged.connect(self.query_pcs_2)
                self.pc_table.itemClicked.connect(self.listfill_1)
                self.delete_pc_button.clicked.connect(self.delete_pc)
                self.send_pc_button.clicked.connect(self.move_pc)
                self.send_pc_button_2.clicked.connect(self.move_pc_2)
                self.pc_table.setColumnWidth(0,180)
                self.pc_table.setColumnWidth(1,180)
                self.pc_table.setColumnWidth(2,240)
                self.pc_table.setColumnWidth(3,240)
                self.pc_table.setColumnWidth(4,260)
                self.pc_table.setColumnWidth(5,260)
                self.pc_table.setColumnWidth(6,180)
                self.pc_table.setColumnWidth(7,180)
                self.pc_table.setColumnWidth(8,180)
                self.pc_table.setColumnWidth(9,160)
                self.pc_table.setColumnWidth(10,160)
                self.pc_table.setColumnWidth(11,170)
                self.pc_table_2.setColumnWidth(0,180)
                self.pc_table_2.setColumnWidth(1,180)
                self.pc_table_2.setColumnWidth(2,240)
                self.pc_table_2.setColumnWidth(3,240)
                self.pc_table_2.setColumnWidth(4,260)
                self.pc_table_2.setColumnWidth(5,260)
                self.pc_table_2.setColumnWidth(6,180)
                self.pc_table_2.setColumnWidth(7,180)
                self.pc_table_2.setColumnWidth(8,180)
                self.pc_table_2.setColumnWidth(9,160)
                self.pc_table_2.setColumnWidth(10,160)
                self.pc_table_2.setColumnWidth(11,170)
                self.data1 = []
                self.data2 = []
                program.dbcon.cur.execute("SELECT adres FROM room")
                addresses = program.dbcon.cur.fetchall()
                for adr in addresses:
                    self.adres_box.addItem(adr[0])
                    self.adres_box_2.addItem(adr[0])
                self.show()
                self.query_pcs()
                self.fill_table()

                

            def quit(self):
                self.close()

            def goback(self):
                self.hide()
                program.main_menu.show()

            def delete_pc(self):
                y = self.pc_table.currentRow()
                if y == -1:
                    program.dlg.label.setText("Ошибка: не выбран компьютер для удаления")
                    program.dlg.exec()
                else:
                    id_pc = self.data[y][11]
                    program.dbcon.cur.execute(f"DELETE from computer WHERE id_pc = {id_pc}")
                program.dbcon.cnx.commit()
                self.query_pcs()
                self.fill_table()
            
            def move_pc(self):
                y = self.pc_table.currentRow()
                if y == -1:
                    program.dlg.label.setText("Ошибка: не выбран компьютер для отправления")
                    program.dlg.exec()
                else:
                    id_pc = self.data[y][11]
                    adr = self.adres_box.currentText()
                    program.dbcon.cur.execute(f"SELECT id_room FROM room WHERE adres = \'{adr}\'")
                    id_r = program.dbcon.cur.fetchone()[0]
                    # print(id_r)

                    program.dbcon.cur.execute(f"UPDATE computer SET room_id = {id_r} WHERE id_pc = {id_pc}")
                program.dbcon.cnx.commit()
                self.query_pcs()
                self.query_pcs_2()
                self.fill_table()
                self.fill_table_2()
            
        
            def move_pc_2(self):
                y = self.pc_table_2.currentRow()
                if y == -1:
                    program.dlg.label.setText("Ошибка: не выбран компьютер для отправления")
                    program.dlg.exec()
                else:
                    id_pc = self.data2[y][11]

                    program.dbcon.cur.execute(f"UPDATE computer SET room_id = NULL  WHERE id_pc = {id_pc}")
                program.dbcon.cnx.commit()
                self.query_pcs()
                self.query_pcs_2()
                self.fill_table()
                self.fill_table_2()

            def check_quality(self):
                for i in range(len(self.data)):
                    if self.pc_table.item(i,11).text() == "Удовлетворительное":
                        for j in range(12):
                            self.pc_table.item(i,j).setBackground(QtGui.QColor(235, 195, 77))
                    elif self.pc_table.item(i,11).text() == "Критическое":
                        for j in range(12):
                            self.pc_table.item(i,j).setBackground(QtGui.QColor(161, 56, 56))

            def check_quality_2(self):
                for i in range(len(self.data2)):
                    if self.pc_table_2.item(i,11).text() == "Удовлетворительное":
                        for j in range(12):
                            self.pc_table_2.item(i,j).setBackground(QtGui.QColor(235, 195, 77))
                    elif self.pc_table_2.item(i,11).text() == "Критическое":
                        for j in range(12):
                            self.pc_table_2.item(i,j).setBackground(QtGui.QColor(161, 56, 56))


            def fill_table(self):
                self.pc_table.setRowCount(len(self.data))
                for i in range(len(self.data)):
                    self.pc_table.setItem(i,0,QTableWidgetItem(self.data[i][0]))
                    self.pc_table.setItem(i,1,QTableWidgetItem(self.data[i][1]))
                    self.pc_table.setItem(i,2,QTableWidgetItem(self.data[i][3]))
                    self.pc_table.setItem(i,4,QTableWidgetItem(self.data[i][2]))
                    self.pc_table.setItem(i,6,QTableWidgetItem(self.data[i][4]))
                    self.pc_table.setItem(i,7,QTableWidgetItem(self.data[i][5]))
                    self.pc_table.setItem(i,8,QTableWidgetItem(self.data[i][6]))
                    self.pc_table.setItem(i,9,QTableWidgetItem(str(self.data[i][7])))
                    self.pc_table.setItem(i,10,QTableWidgetItem(str(self.data[i][8])))
                    self.pc_table.setItem(i,11,QTableWidgetItem(str(self.data[i][12])))

                    if self.data[i][10] is None:
                        self.pc_table.setItem(i,3,QTableWidgetItem("Пусто"))
                    else: self.pc_table.setItem(i,3,QTableWidgetItem(self.data[i][10]))

                    if self.data[i][9] is None:
                        self.pc_table.setItem(i,5,QTableWidgetItem("Пусто"))
                    else: self.pc_table.setItem(i,5,QTableWidgetItem(self.data[i][9]))
                self.label_2.setText(str(len(self.data)))
                self.check_quality()

            def query_pcs(self):
                self.listclear_1()
                self.data = []
                adr = self.adres_box.currentText()
                program.dbcon.cur.execute(f"SELECT id_room FROM room WHERE adres = \'{adr}\'")
                id_r = program.dbcon.cur.fetchone()[0]
                # print(id_r)

                query_storage1 = """SELECT pccpu.model, g.model, d.model, r.model, k.model, m.model, mon.model,assign_date,move_date FROM computer
                    INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
                    INNER JOIN gpu g  ON g.id_g = computer.gpu_id
                    INNER JOIN ram r  ON r.id_r  = computer.ram1_id
                    INNER JOIN drive d ON d.id_dr = computer.dr_id1
                    INNER JOIN keyboard k ON k.id_k = computer.kb_id 
                    INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
                    INNER JOIN mouse m ON m.id_m = computer.m_id
                    WHERE room_id IS NULL
                    """

                query_storage2 = """SELECT d.model, r.model, computer.id_pc, state FROM computer
                            LEFT JOIN ram r  ON r.id_r  = computer.ram2_id
                            LEFT JOIN drive d ON d.id_dr = computer.dr_id2 
                            WHERE room_id IS NULL""" 



                program.dbcon.cur.execute(query_storage1)
                data1 = list(program.dbcon.cur.fetchall())
                program.dbcon.cur.execute(query_storage2)
                data2 = list(program.dbcon.cur.fetchall())
                """program.dbcon.cur.execute(costquery)
                cost = 0
                costup = (list(program.dbcon.cur.fetchall()))
                for n in costup:
                    for i in range(7):
                        if not (n[i] is None): cost = cost + n[i]

                program.dbcon.cur.execute(costquery2)

                costup = (list(program.dbcon.cur.fetchall()))
                for n in costup:
                    for i in range(2):
                        if not (n[i] is None): cost = cost + n[i]

                
                print(cost)
                self.label_2.setText(str(cost))
                """
                for i in range(len(data1)):
                    l1 = list(data1[i])
                    l2 = list(data2[i])
                    l1.extend(l2)  
                    self.data.append(l1)
                
                # print(self.data)

                self.fill_table_2()

            def listclear_1(self):
                self.pc_list.clear()
                self.pc_list.addItem(QListWidgetItem("Кол-во ядер: "))
                self.pc_list.addItem(QListWidgetItem("Частота проц. (в мГц): "))
                self.pc_list.addItem(QListWidgetItem("Кол-во видеопамяти (в ГБ): "))
                self.pc_list.addItem(QListWidgetItem("Кол-во ОЗУ (в ГБ): "))
                self.pc_list.addItem(QListWidgetItem("Размер накопителей (в ГБ): "))
                self.pc_list.addItem(QListWidgetItem("Разрешение экрана: "))
                self.pc_list.addItem(QListWidgetItem("Частота монитора: "))
                self.pc_list.addItem(QListWidgetItem("Цена компонентов (в руб.): "))

            def listfill_1(self):
                y = self.pc_table.currentRow()
                cpumodel = self.pc_table.item(y,0).text()
                gpumodel = self.pc_table.item(y,1).text()
                rmodel = self.pc_table.item(y,2).text()
                drmodel = self.pc_table.item(y,4).text()
                kbmodel = self.pc_table.item(y,6).text()
                mmodel = self.pc_table.item(y,7).text()
                monmodel = self.pc_table.item(y,8).text()
                # print(cpumodel,gpumodel,rmodel,drmodel,kbmodel,mmodel,monmodel)
                
                query1 = f"""SELECT DISTINCT cores, pccpu.freq, vram, r.capacity, d.capacity, mon.height,mon.width, mon.freq,
                                pccpu.cost,g.cost,r.cost,d.cost,k.cost,mon.cost,m.cost
                                FROM computer 
                                INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
                                INNER JOIN gpu g  ON g.id_g = computer.gpu_id
                                INNER JOIN ram r  ON r.id_r  = computer.ram1_id
                                INNER JOIN drive d ON d.id_dr = computer.dr_id1
                                INNER JOIN keyboard k ON k.id_k = computer.kb_id 
                                INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
                                INNER JOIN mouse m ON m.id_m = computer.m_id
                                WHERE m.model = \'{mmodel}\' AND mon.model = \'{monmodel}\'
                                AND d.model = \'{drmodel}\' AND g.model = \'{gpumodel}\'
                                AND r.model = \'{rmodel}\' AND k.model = \'{kbmodel}\' 
                                AND pccpu.model = \'{cpumodel}\'                           
                                """

                program.dbcon.cur.execute(query1)
                results = program.dbcon.cur.fetchall()
                #print(results)
                cores = results[0][0]
                cpufreq = results[0][1]
                vram = results[0][2]
                rams = results[0][3]
                drs = results[0][4]
                he = results[0][6]
                wi = results[0][5]
                freq = results[0][7]
                costsum = 0

                if self.pc_table.item(y,3).text() != "Пусто":
                    r2model = self.pc_table.item(y,3).text()
                    program.dbcon.cur.execute(f"SELECT DISTINCT capacity,cost FROM ram WHERE model = \'{r2model}\'")
                    res = program.dbcon.cur.fetchall()
                    rams = str(rams) + '+' + str(res[0][0])
                    costsum = costsum + res[0][1]
                if self.pc_table.item(y,5).text() != "Пусто":
                    dr2model = self.pc_table.item(y,5).text()
                    program.dbcon.cur.execute(f"SELECT DISTINCT capacity,cost FROM drive WHERE model = \'{dr2model}\'")
                    res = program.dbcon.cur.fetchall()
                    drs = drs + res[0][0]
                    costsum = costsum + res[0][1]

                
                costsum = results[0][8] +results[0][9] +results[0][10] +results[0][11] +results[0][12] +results[0][13] +results[0][14]

                self.pc_list.clear()
                self.pc_list.addItem(QListWidgetItem(f"Кол-во ядер: {cores}"))
                self.pc_list.addItem(QListWidgetItem(f"Частота проц. (в мГц): {cpufreq}"))
                self.pc_list.addItem(QListWidgetItem(f"Кол-во видеопамяти (в ГБ): {vram}"))
                self.pc_list.addItem(QListWidgetItem(f"Кол-во ОЗУ (в ГБ): {rams}"))
                self.pc_list.addItem(QListWidgetItem(f"Размер накопителей (в ГБ): {drs}"))
                self.pc_list.addItem(QListWidgetItem(f"Разрешение экрана: {he}x{wi}"))
                self.pc_list.addItem(QListWidgetItem(f"Частота монитора: {freq}"))
                self.pc_list.addItem(QListWidgetItem(f"Цена компонентов (в руб.): {costsum}"))

            def query_pcs_2(self):
                self.listclear_2()
                self.data2 = []
                adr = self.adres_box_2.currentText()
                program.dbcon.cur.execute(f"SELECT id_room FROM room WHERE adres = \'{adr}\'")
                id_r = program.dbcon.cur.fetchone()[0]
               # print(id_r)

                query1 = """SELECT pccpu.model, g.model, d.model, r.model, k.model, m.model, mon.model,assign_date,move_date FROM computer
                    INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
                    INNER JOIN gpu g  ON g.id_g = computer.gpu_id
                    INNER JOIN ram r  ON r.id_r  = computer.ram1_id
                    INNER JOIN drive d ON d.id_dr = computer.dr_id1
                    INNER JOIN keyboard k ON k.id_k = computer.kb_id 
                    INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
                    INNER JOIN mouse m ON m.id_m = computer.m_id
                    WHERE room_id =
                    """

                query2 = """SELECT d.model, r.model, computer.id_pc, state FROM computer
                            LEFT JOIN ram r  ON r.id_r  = computer.ram2_id
                            LEFT JOIN drive d ON d.id_dr = computer.dr_id2 
                            WHERE room_id =""" 
                costquery = """
                SELECT sum(pccpu.cost),sum(g.cost),sum(r.cost),sum(d.cost),sum(k.cost),sum(mon.cost),sum(m.cost)
                FROM computer
                INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
                INNER JOIN gpu g  ON g.id_g = computer.gpu_id
                INNER JOIN ram r  ON r.id_r  = computer.ram1_id
                INNER JOIN drive d ON d.id_dr = computer.dr_id1
                INNER JOIN keyboard k ON k.id_k = computer.kb_id 
                INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
                INNER JOIN mouse m ON m.id_m = computer.m_id
                WHERE room_id =
                """

                costquery2 = """SELECT sum(d.cost), sum(r.cost) FROM computer
                            LEFT JOIN ram r  ON r.id_r  = computer.ram2_id
                            LEFT JOIN drive d ON d.id_dr = computer.dr_id2 
                            WHERE room_id ="""

                query1 = query1 + str(id_r) + " ORDER BY id_pc"
                query2 = query2 + str(id_r) + " ORDER BY id_pc"
                costquery = costquery + str(id_r)
                costquery2 = costquery2 + str(id_r)
                program.dbcon.cur.execute(query1)
                data21 = list(program.dbcon.cur.fetchall())
                program.dbcon.cur.execute(query2)
                data22 = list(program.dbcon.cur.fetchall())
                program.dbcon.cur.execute(costquery)
                cost = 0
                costup = (list(program.dbcon.cur.fetchall()))
                for n in costup:
                    for i in range(7):
                        if not (n[i] is None): cost = cost + n[i]

                program.dbcon.cur.execute(costquery2)

                costup = (list(program.dbcon.cur.fetchall()))
                for n in costup:
                    for i in range(2):
                        if not (n[i] is None): cost = cost + n[i]

                
                # print(cost)
                self.label_2.setText(str(cost))

                for i in range(len(data21)):
                    l1 = list(data21[i])
                    l2 = list(data22[i])
                    l1.extend(l2)  
                    self.data2.append(l1)
                
                #print(self.data2)

                self.fill_table_2()
                
            def fill_table_2(self):
                self.pc_table_2.setRowCount(len(self.data2))
                for i in range(len(self.data2)):
                    self.pc_table_2.setItem(i,0,QTableWidgetItem(self.data2[i][0]))
                    self.pc_table_2.setItem(i,1,QTableWidgetItem(self.data2[i][1]))
                    self.pc_table_2.setItem(i,2,QTableWidgetItem(self.data2[i][3]))
                    self.pc_table_2.setItem(i,4,QTableWidgetItem(self.data2[i][2]))
                    self.pc_table_2.setItem(i,6,QTableWidgetItem(self.data2[i][4]))
                    self.pc_table_2.setItem(i,7,QTableWidgetItem(self.data2[i][5]))
                    self.pc_table_2.setItem(i,8,QTableWidgetItem(self.data2[i][6]))
                    self.pc_table_2.setItem(i,9,QTableWidgetItem(str(self.data2[i][7])))
                    self.pc_table_2.setItem(i,10,QTableWidgetItem(str(self.data2[i][8])))
                    self.pc_table_2.setItem(i,11,QTableWidgetItem(str(self.data2[i][12])))
                    

                    if self.data2[i][10] is None:
                        self.pc_table_2.setItem(i,3,QTableWidgetItem("Пусто"))
                    else: self.pc_table_2.setItem(i,3,QTableWidgetItem(self.data2[i][10]))

                    if self.data2[i][9] is None:
                        self.pc_table_2.setItem(i,5,QTableWidgetItem("Пусто"))
                    else: self.pc_table_2.setItem(i,5,QTableWidgetItem(self.data2[i][9]))
                self.check_quality_2()



            def listclear_2(self):
                self.pc_list_2.clear()
                self.pc_list_2.addItem(QListWidgetItem("Кол-во ядер: "))
                self.pc_list_2.addItem(QListWidgetItem("Частота проц. (в мГц): "))
                self.pc_list_2.addItem(QListWidgetItem("Кол-во видеопамяти (в ГБ): "))
                self.pc_list_2.addItem(QListWidgetItem("Кол-во ОЗУ (в ГБ): "))
                self.pc_list_2.addItem(QListWidgetItem("Размер накопителей (в ГБ): "))
                self.pc_list_2.addItem(QListWidgetItem("Разрешение экрана: "))
                self.pc_list_2.addItem(QListWidgetItem("Частота монитора: "))
                self.pc_list_2.addItem(QListWidgetItem("Цена компонентов (в руб.): "))

            def listfill_2(self):
                y = self.pc_table_2.currentRow()
                cpumodel = self.pc_table_2.item(y,0).text()
                gpumodel = self.pc_table_2.item(y,1).text()
                rmodel = self.pc_table_2.item(y,2).text()
                drmodel = self.pc_table_2.item(y,4).text()
                kbmodel = self.pc_table_2.item(y,6).text()
                mmodel = self.pc_table_2.item(y,7).text()
                monmodel = self.pc_table_2.item(y,8).text()
                # print(cpumodel,gpumodel,rmodel,drmodel,kbmodel,mmodel,monmodel)
                
                query1 = f"""SELECT DISTINCT cores, pccpu.freq, vram, r.capacity, d.capacity, mon.height,mon.width, mon.freq,
                                pccpu.cost,g.cost,r.cost,d.cost,k.cost,mon.cost,m.cost
                                FROM computer 
                                INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
                                INNER JOIN gpu g  ON g.id_g = computer.gpu_id
                                INNER JOIN ram r  ON r.id_r  = computer.ram1_id
                                INNER JOIN drive d ON d.id_dr = computer.dr_id1
                                INNER JOIN keyboard k ON k.id_k = computer.kb_id 
                                INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
                                INNER JOIN mouse m ON m.id_m = computer.m_id
                                WHERE m.model = \'{mmodel}\' AND mon.model = \'{monmodel}\'
                                AND d.model = \'{drmodel}\' AND g.model = \'{gpumodel}\'
                                AND r.model = \'{rmodel}\' AND k.model = \'{kbmodel}\' 
                                AND pccpu.model = \'{cpumodel}\'                           
                                """

                program.dbcon.cur.execute(query1)
                results = program.dbcon.cur.fetchall()
                #print(results)
                cores = results[0][0]
                cpufreq = results[0][1]
                vram = results[0][2]
                rams = results[0][3]
                drs = results[0][4]
                he = results[0][6]
                wi = results[0][5]
                freq = results[0][7]
                costsum = 0

                if self.pc_table_2.item(y,3).text() != "Пусто":
                    r2model = self.pc_table_2.item(y,3).text()
                    program.dbcon.cur.execute(f"SELECT DISTINCT capacity,cost FROM ram WHERE model = \'{r2model}\'")
                    res = program.dbcon.cur.fetchall()
                    rams = str(rams) + '+' + str(res[0][0])
                    costsum = costsum + res[0][1]
                if self.pc_table_2.item(y,5).text() != "Пусто":
                    dr2model = self.pc_table_2.item(y,5).text()
                    program.dbcon.cur.execute(f"SELECT DISTINCT capacity,cost FROM drive WHERE model = \'{dr2model}\'")
                    res = program.dbcon.cur.fetchall()
                    drs = drs + res[0][0]
                    costsum = costsum + res[0][1]

                
                costsum = results[0][8] +results[0][9] +results[0][10] +results[0][11] +results[0][12] +results[0][13] +results[0][14]


                self.pc_list_2.clear()
                self.pc_list_2.addItem(QListWidgetItem(f"Кол-во ядер: {cores}"))
                self.pc_list_2.addItem(QListWidgetItem(f"Частота проц. (в мГц): {cpufreq}"))
                self.pc_list_2.addItem(QListWidgetItem(f"Кол-во видеопамяти (в ГБ): {vram}"))
                self.pc_list_2.addItem(QListWidgetItem(f"Кол-во ОЗУ (в ГБ): {rams}"))
                self.pc_list_2.addItem(QListWidgetItem(f"Размер накопителей (в ГБ): {drs}"))
                self.pc_list_2.addItem(QListWidgetItem(f"Разрешение экрана: {he}x{wi}"))
                self.pc_list_2.addItem(QListWidgetItem(f"Частота монитора: {freq}"))
                self.pc_list_2.addItem(QListWidgetItem(f"Цена компонентов (в руб.): {costsum}"))                

        class View_employees(QWidget):      # Класс окна просмотра сотрудников

            def __init__(self):
                super().__init__()
                uic.loadUi("view_employees.ui",self)
                self.goback_button.clicked.connect(self.goback)
                self.exit_button.clicked.connect(self.quit)
                self.sort_dol_button.clicked.connect(self.sort_by_dol)
                self.sort_fio_button.clicked.connect(self.sort_by_fio)
                self.employee_table.setColumnWidth(0,155)
                self.employee_table.setColumnWidth(1,150)
                self.adres_box.currentTextChanged.connect(self.query_emps)
                self.show()
                self.data = []

                program.dbcon.cur.execute("SELECT adres FROM room")
                addresses = program.dbcon.cur.fetchall()
                for adr in addresses:
                    self.adres_box.addItem(adr[0])


            def quit(self):
                self.close()

            def goback(self):
                self.hide()
                program.main_menu.show()
            
            def sort_by_fio(self):
                self.data.sort(key=lambda x: x[0])
                self.fill_emp()

            def sort_by_dol(self):
                self.data.sort(key=lambda x: x[1])
                self.fill_emp()

            def query_emps(self):
                self.data = []
                adr = self.adres_box.currentText()
                program.dbcon.cur.execute(f"SELECT id_room FROM room WHERE adres = \'{adr}\'")
                id_r = program.dbcon.cur.fetchone()[0]
                # print(id_r)
                query = f"""SELECT fio,naz FROM employee e 
                        INNER JOIN assign a ON a.em_id = e.id_em 
                        INNER JOIN room r ON r.id_room = a.room_id 
                        INNER JOIN dolzhnost d ON d.id_dol = e.dolzh_id 
                        WHERE room_id = {id_r}"""
                program.dbcon.cur.execute(query)
                data = program.dbcon.cur.fetchall()
                for dt in data:
                    self.data.append(list(dt))
                self.fill_emp()
            
            def fill_emp(self):
                self.employee_table.setRowCount(len(self.data))
                for i in range(len(self.data)):
                    self.employee_table.setItem(i,0,QTableWidgetItem(self.data[i][0]))
                    self.employee_table.setItem(i,1,QTableWidgetItem(self.data[i][1]))



        class View_pcs(QWidget):            # Класс окна просмотра компьютеров
            def __init__(self):
                super().__init__()
                uic.loadUi("view_pcs.ui",self)
                self.goback_button.clicked.connect(self.goback)
                self.exit_button.clicked.connect(self.quit)
                self.adres_box.currentTextChanged.connect(self.query_pcs)
                self.pc_table.itemClicked.connect(self.listfill)

                self.pc_table.setColumnWidth(0,180)
                self.pc_table.setColumnWidth(1,180)
                self.pc_table.setColumnWidth(2,240)
                self.pc_table.setColumnWidth(3,240)
                self.pc_table.setColumnWidth(4,260)
                self.pc_table.setColumnWidth(5,260)
                self.pc_table.setColumnWidth(6,180)
                self.pc_table.setColumnWidth(7,180)
                self.pc_table.setColumnWidth(8,180)
                self.pc_table.setColumnWidth(9,160)
                self.pc_table.setColumnWidth(10,160)
                self.pc_table.setColumnWidth(11,170)
                self.data = []              # Содержит данные, полученные из БД


                program.dbcon.cur.execute("SELECT adres FROM room")
                addresses = program.dbcon.cur.fetchall()
                for adr in addresses:
                    self.adres_box.addItem(adr[0])


                self.show()

            def check_quality(self):        # Метод проверки состояния компьютеров
                for i in range(len(self.data)):
                    if self.pc_table.item(i,11).text() == "Удовлетворительное":
                        for j in range(12):
                            self.pc_table.item(i,j).setBackground(QtGui.QColor(235, 195, 77))
                    elif self.pc_table.item(i,11).text() == "Критическое":
                        for j in range(12):
                            self.pc_table.item(i,j).setBackground(QtGui.QColor(161, 56, 56))     

            def query_pcs(self):            # Метод запроса компьютеров из БД
                self.listclear()
                self.data = []
                adr = self.adres_box.currentText()
                program.dbcon.cur.execute(f"SELECT id_room FROM room WHERE adres = \'{adr}\'")
                id_r = program.dbcon.cur.fetchone()[0]
                # print(id_r)

                query1 = """SELECT pccpu.model, g.model, d.model, r.model, k.model, m.model, mon.model,assign_date,move_date FROM computer
                    INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
                    INNER JOIN gpu g  ON g.id_g = computer.gpu_id
                    INNER JOIN ram r  ON r.id_r  = computer.ram1_id
                    INNER JOIN drive d ON d.id_dr = computer.dr_id1
                    INNER JOIN keyboard k ON k.id_k = computer.kb_id 
                    INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
                    INNER JOIN mouse m ON m.id_m = computer.m_id
                    WHERE room_id =
                    """

                query2 = """SELECT d.model, r.model, state FROM computer
                            LEFT JOIN ram r  ON r.id_r  = computer.ram2_id
                            LEFT JOIN drive d ON d.id_dr = computer.dr_id2 
                            WHERE room_id =""" 
                costquery = """
                SELECT sum(pccpu.cost),sum(g.cost),sum(r.cost),sum(d.cost),sum(k.cost),sum(mon.cost),sum(m.cost)
                FROM computer
                INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
                INNER JOIN gpu g  ON g.id_g = computer.gpu_id
                INNER JOIN ram r  ON r.id_r  = computer.ram1_id
                INNER JOIN drive d ON d.id_dr = computer.dr_id1
                INNER JOIN keyboard k ON k.id_k = computer.kb_id 
                INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
                INNER JOIN mouse m ON m.id_m = computer.m_id
                WHERE room_id =
                """

                costquery2 = """SELECT sum(d.cost), sum(r.cost) FROM computer
                            LEFT JOIN ram r  ON r.id_r  = computer.ram2_id
                            LEFT JOIN drive d ON d.id_dr = computer.dr_id2 
                            WHERE room_id ="""

                query1 = query1 + str(id_r) + " ORDER BY id_pc"
                query2 = query2 + str(id_r) + " ORDER BY id_pc"
                costquery = costquery + str(id_r)
                costquery2 = costquery2 + str(id_r)
                program.dbcon.cur.execute(query1)
                data1 = list(program.dbcon.cur.fetchall())
                program.dbcon.cur.execute(query2)
                data2 = list(program.dbcon.cur.fetchall())
                program.dbcon.cur.execute(costquery)
                cost = 0
                costup = (list(program.dbcon.cur.fetchall()))
                for n in costup:
                    for i in range(7):
                        if not (n[i] is None): cost = cost + n[i]

                program.dbcon.cur.execute(costquery2)

                costup = (list(program.dbcon.cur.fetchall()))
                for n in costup:
                    for i in range(2):
                        if not (n[i] is None): cost = cost + n[i]

                
                # print(cost)
                self.label_2.setText(str(cost))

                for i in range(len(data1)):
                    l1 = list(data1[i])
                    l2 = list(data2[i])
                    l1.extend(l2)  
                    self.data.append(l1)
                
                #print(self.data)

                self.fill_table()
                
            def fill_table(self):       # Метод распределения полученных данных по таблице
                self.pc_table.setRowCount(len(self.data))
                for i in range(len(self.data)):
                    self.pc_table.setItem(i,0,QTableWidgetItem(self.data[i][0]))
                    self.pc_table.setItem(i,1,QTableWidgetItem(self.data[i][1]))
                    self.pc_table.setItem(i,2,QTableWidgetItem(self.data[i][3]))
                    self.pc_table.setItem(i,4,QTableWidgetItem(self.data[i][2]))
                    self.pc_table.setItem(i,6,QTableWidgetItem(self.data[i][4]))
                    self.pc_table.setItem(i,7,QTableWidgetItem(self.data[i][5]))
                    self.pc_table.setItem(i,8,QTableWidgetItem(self.data[i][6]))
                    self.pc_table.setItem(i,9,QTableWidgetItem(str(self.data[i][7])))
                    self.pc_table.setItem(i,10,QTableWidgetItem(str(self.data[i][8])))
                    self.pc_table.setItem(i,11,QTableWidgetItem(str(self.data[i][11])))

                    if self.data[i][10] is None:
                        self.pc_table.setItem(i,3,QTableWidgetItem("Пусто"))
                    else: self.pc_table.setItem(i,3,QTableWidgetItem(self.data[i][10]))

                    if self.data[i][9] is None:
                        self.pc_table.setItem(i,5,QTableWidgetItem("Пусто"))
                    else: self.pc_table.setItem(i,5,QTableWidgetItem(self.data[i][9]))
                self.check_quality()



            def listclear(self):
                self.pc_list.clear()
                self.pc_list.addItem(QListWidgetItem("Кол-во ядер: "))
                self.pc_list.addItem(QListWidgetItem("Частота проц. (в мГц): "))
                self.pc_list.addItem(QListWidgetItem("Кол-во видеопамяти (в ГБ): "))
                self.pc_list.addItem(QListWidgetItem("Кол-во ОЗУ (в ГБ): "))
                self.pc_list.addItem(QListWidgetItem("Размер накопителей (в ГБ): "))
                self.pc_list.addItem(QListWidgetItem("Разрешение экрана: "))
                self.pc_list.addItem(QListWidgetItem("Частота монитора: "))
                self.pc_list.addItem(QListWidgetItem("Цена компонентов (в руб.): "))

            def listfill(self):
                y = self.pc_table.currentRow()
                cpumodel = self.pc_table.item(y,0).text()
                gpumodel = self.pc_table.item(y,1).text()
                rmodel = self.pc_table.item(y,2).text()
                drmodel = self.pc_table.item(y,4).text()
                kbmodel = self.pc_table.item(y,6).text()
                mmodel = self.pc_table.item(y,7).text()
                monmodel = self.pc_table.item(y,8).text()
                # print(cpumodel,gpumodel,rmodel,drmodel,kbmodel,mmodel,monmodel)
                
                query1 = f"""SELECT DISTINCT cores, pccpu.freq, vram, r.capacity, d.capacity, mon.height,mon.width, mon.freq,
                                pccpu.cost,g.cost,r.cost,d.cost,k.cost,mon.cost,m.cost
                                FROM computer 
                                INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
                                INNER JOIN gpu g  ON g.id_g = computer.gpu_id
                                INNER JOIN ram r  ON r.id_r  = computer.ram1_id
                                INNER JOIN drive d ON d.id_dr = computer.dr_id1
                                INNER JOIN keyboard k ON k.id_k = computer.kb_id 
                                INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
                                INNER JOIN mouse m ON m.id_m = computer.m_id
                                WHERE m.model = \'{mmodel}\' AND mon.model = \'{monmodel}\'
                                AND d.model = \'{drmodel}\' AND g.model = \'{gpumodel}\'
                                AND r.model = \'{rmodel}\' AND k.model = \'{kbmodel}\' 
                                AND pccpu.model = \'{cpumodel}\'                           
                                """

                program.dbcon.cur.execute(query1)
                results = program.dbcon.cur.fetchall()
                #print(results)
                cores = results[0][0]
                cpufreq = results[0][1]
                vram = results[0][2]
                rams = results[0][3]
                drs = results[0][4]
                he = results[0][6]
                wi = results[0][5]
                freq = results[0][7]
                costsum = 0

                if self.pc_table.item(y,3).text() != "Пусто":
                    r2model = self.pc_table.item(y,3).text()
                    program.dbcon.cur.execute(f"SELECT DISTINCT capacity,cost FROM ram WHERE model = \'{r2model}\'")
                    res = program.dbcon.cur.fetchall()
                    rams = str(rams) + '+' + str(res[0][0])
                    costsum = costsum + res[0][1]
                if self.pc_table.item(y,5).text() != "Пусто":
                    dr2model = self.pc_table.item(y,5).text()
                    program.dbcon.cur.execute(f"SELECT DISTINCT capacity,cost FROM drive WHERE model = \'{dr2model}\'")
                    res = program.dbcon.cur.fetchall()
                    drs = drs + res[0][0]
                    costsum = costsum + res[0][1]

                
                costsum = results[0][8] +results[0][9] +results[0][10] +results[0][11] +results[0][12] +results[0][13] +results[0][14]


                self.pc_list.clear()
                self.pc_list.addItem(QListWidgetItem(f"Кол-во ядер: {cores}"))
                self.pc_list.addItem(QListWidgetItem(f"Частота проц. (в мГц): {cpufreq}"))
                self.pc_list.addItem(QListWidgetItem(f"Кол-во видеопамяти (в ГБ): {vram}"))
                self.pc_list.addItem(QListWidgetItem(f"Кол-во ОЗУ (в ГБ): {rams}"))
                self.pc_list.addItem(QListWidgetItem(f"Размер накопителей (в ГБ): {drs}"))
                self.pc_list.addItem(QListWidgetItem(f"Разрешение экрана: {he}x{wi}"))
                self.pc_list.addItem(QListWidgetItem(f"Частота монитора: {freq}"))
                self.pc_list.addItem(QListWidgetItem(f"Цена компонентов (в руб.): {costsum}"))



            def quit(self):
                self.close()

            def goback(self):
                self.hide()
                program.main_menu.show()
                



        def __init__(self):
            super().__init__()
            uic.loadUi("mainmenu.ui",self)
            self.button_pcs.clicked.connect(self.goto_viewpcs)
            self.button_emp.clicked.connect(self.goto_viewemp)
            self.button_edit.clicked.connect(self.goto_editpcs)
            self.exitbutton.clicked.connect(self.quit)
            
            self.adminframe.hide()

        def quit(self):
            self.close()

        def goto_editpcs(self):
            self.hide()
            self.edit_pcs = self.Edit_pcs()

        def goto_viewpcs(self):
            self.hide()
            self.view_pcs = self.View_pcs()
        
        def goto_viewemp(self):
            self.hide()
            self.view_employees = self.View_employees()

    class Welcome_window(QMainWindow):
        def openauth(self):
            self.hide()
            self.authorization = self.Authorization_window()
            
        def openreg(self):
            self.hide()
            self.registration = self.Registration_window()

        def showself(self):
            self.show()
        
        def __init__(self):
            super().__init__()
            
            uic.loadUi('welcomewindow.ui',self)
            self.show()
            self.pushButton.clicked.connect(self.openauth)
            self.pushButton_2.clicked.connect(self.openreg)
        

        class Authorization_window(QWidget):    # Класс окна авторизации
            def __init__(self):
                super().__init__()
                uic.loadUi("authorization.ui",self)
                self.show()
                self.goback_button.clicked.connect(self.goback)
                self.reg_button.clicked.connect(self.start_auth)
                

            

            def goback(self):
                self.hide()
                program.welcome_window.show()

            def start_auth(self):

                pwd = self.password_edit1.text()
                login = self.login_edit.text()
                args = [login,shift_chars(pwd),'USR',0]
                
                results = program.dbcon.cur.callproc("check_user", args)
                # print(results)
                if results[3] == 10:
                    program.dlg.label.setText("Ошибка: неправильный логин или пароль.")
                    program.dlg.exec()
                else:
                    role = results[2]
                    # print(role)
                    match role:
                        case 'USR':
                            program.dbcon.cnx = mysql.connector.connect(user='pc_viewer', password='', database='computer_db')        
                            program.dbcon.setupcur()
                        case 'MNG':
                            program.dbcon.cnx = mysql.connector.connect(user='pc_manager', password='', database='computer_db')
                            program.dbcon.setupcur()
                            program.main_menu.adminframe.show()
                        case 'ADM':
                            program.dbcon.cnx = mysql.connector.connect(user='pc_admin', password='', database='computer_db')
                            program.dbcon.setupcur()
                            program.main_menu.adminframe.show()

                    self.close()
                    program.main_menu.show()                
                


        class Registration_window(QWidget):     # Класс окна регистрации
            
            def __init__(self):
                    super().__init__()
                    
                    
                    uic.loadUi("registration.ui",self)
                    self.show()
                    self.reg_button.clicked.connect(self.start_reg)
                    self.goback_button_2.clicked.connect(self.goback)
                    self.toggle_button.clicked.connect(self.toggle_passwords)

            def goback(self):
                self.hide()
                program.welcome_window.show()

            def toggle_passwords(self):
                if self.toggle_button.isChecked():
                    self.password_edit1.setEchoMode(QLineEdit.EchoMode.Normal)
                    self.password_edit2.setEchoMode(QLineEdit.EchoMode.Normal)
                else:
                    self.password_edit1.setEchoMode(QLineEdit.EchoMode.Password)
                    self.password_edit2.setEchoMode(QLineEdit.EchoMode.Password)


            def check_pwdchars(self) -> int:
                errorcode = 0
                found_cap = False
                found_num = False
                pwd = self.password_edit1.text()
                if len(pwd) < 4: errorcode = 11
                if len(pwd) > 16: errorcode = 12
                forb = ['*','&','}','{','|','+']
                for chr in forb:
                    if chr in pwd: errorcode = 20
                
                for chr in ascii_uppercase:
                    if chr in pwd: found_cap = True
                
                for i in range(0,10):
                    if str(i) in pwd: found_num = True
                
                if found_cap == False: errorcode = 31
                if found_num == False: errorcode = 32

                return errorcode


            def check_passw(self) -> bool:

                success = False

                pwd = self.password_edit1.text()
                if (pwd != self.password_edit2.text()):
                    program.dlg.label.setText("Ошибка: пароль и повтор пароля не совпадают!")
                    program.dlg.exec()

                errorcode = 0
                errorcode = self.check_pwdchars()

                match errorcode:
                    case 11:
                        program.dlg.label.setText("Ошибка: пароль короче 4 символов")
                        program.dlg.exec()
                    case 12:
                        program.dlg.label.setText("Ошибка: пароль длинее 16 символов")
                        program.dlg.exec()
                    case 20:
                        program.dlg.label.setText("Ошибка: в пароле есть спец. символы")
                        program.dlg.exec()
                    case 31:
                        program.dlg.label.setText("Ошибка: в пароле нет заглавных букв")
                        program.dlg.exec()
                    case 32:
                        program.dlg.label.setText("Ошибка: в пароле нет цифр")
                        program.dlg.exec()
                    case 0: success = True

                return success
                
            def start_reg(self):

                success = self.check_passw()
                pwd = self.password_edit1.text()
                login = self.login_edit.text()
                if (success == True):
                    if (len(login) > 50):
                        program.dlg.label.setText("Ошибка: слишком длинный логин")
                        program.dlg.exec()
                    elif (len(login) < 3):
                        program.dlg.label.setText("Ошибка: слишком короткий логин")
                        program.dlg.exec()
                    else:
                        sql_error = 0
                        args = (login,shift_chars(pwd),0)
                        results = program.dbcon.cur.callproc('add_user',args)
                        program.dbcon.cnx.commit()
                        # print(results)
                        sql_error = results[2]
                    
                        if sql_error == 10:
                            program.dlg.label.setText("Ошибка: такой пользователь уже существует.\nИспользуйте другой логин.")
                            program.dlg.exec()  
                        else:
                            self.close()
                            program.dbcon.role = 'USR'
                            program.main_menu.show()
                            
                            program.dbcon.cnx = mysql.connector.connect(user='pc_viewer', password='', database='computer_db')
                            program.dbcon.setupcur()

                                                # Запуск программы
app = QApplication(sys.argv)
program = Program() 
sys.exit(app.exec())




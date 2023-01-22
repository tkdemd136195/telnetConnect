# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
#
# Use PyCharm Community
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import telnetlib
import sqlite3
con = sqlite3.connect('infra.db')
cur = con.cursor()
class Ui_Dialog(object):
    #sql 구문 
    sql_select_id = '''select id from devicetbl'''
    sql_select_all = '''select * from devicetbl'''
    sql_create = '''create table IF NOT EXISTS devicetbl(
            id char(20) primary key,
            model char(20),
            ipaddress char(20),
            userId char(20),
            passwd char(20))'''
    sql_insert = '''insert into devicetbl values(?,?,?,?,?)'''
    sql_delete = '''delete from devicetbl where id = %s'''
    sql_update = '''update devicetbl set model = ?, ipaddress = ?, userId = ?, passwd = ? where id = ?'''
    sql_insert_example = '''insert into devicetbl values('0', 'router', '1.1.1.1', 'example', 'example')'''
    sql_contel = '''select model, ipaddress, userId, passwd from devicetbl where id = ?'''

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(660, 550)
        self.create_table()
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 641, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 617, 270))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 290, 617, 211))
        self.groupBox.setObjectName("groupBox")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(10, 30, 56, 21))
        self.label_28.setObjectName("label_28")
        self.ID_5 = QtWidgets.QLineEdit(self.groupBox)
        self.ID_5.setGeometry(QtCore.QRect(80, 30, 113, 21))
        self.ID_5.setObjectName("ID_5")
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setGeometry(QtCore.QRect(10, 65, 56, 21))
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_31.setObjectName("label_31")
        self.ipAddress_5 = QtWidgets.QLineEdit(self.groupBox)
        self.ipAddress_5.setGeometry(QtCore.QRect(80, 100, 113, 21))
        self.ipAddress_5.setObjectName("ipAddress_5")
        self.label_32 = QtWidgets.QLabel(self.groupBox)
        self.label_32.setGeometry(QtCore.QRect(10, 135, 61, 21))
        self.label_32.setObjectName("label_32")
        self.UserName_5 = QtWidgets.QLineEdit(self.groupBox)
        self.UserName_5.setGeometry(QtCore.QRect(80, 135, 113, 21))
        self.UserName_5.setObjectName("UserName_5")
        self.label_33 = QtWidgets.QLabel(self.groupBox)
        self.label_33.setGeometry(QtCore.QRect(10, 170, 61, 21))
        self.label_33.setObjectName("label_33")
        self.Password_5 = QtWidgets.QLineEdit(self.groupBox)
        self.Password_5.setGeometry(QtCore.QRect(80, 170, 113, 21))
        self.Password_5.setObjectName("Password_5")
        self.delButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.delButton_4.setGeometry(QtCore.QRect(490, 165, 111, 31))
        self.delButton_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.delButton_4.setAutoDefault(False)
        self.delButton_4.setObjectName("delButton_4")
        self.updateButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.updateButton_4.setGeometry(QtCore.QRect(370, 165, 111, 31))
        self.updateButton_4.setAutoDefault(False)
        self.updateButton_4.setObjectName("updateButton_4")
        self.addButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.addButton_4.setGeometry(QtCore.QRect(250, 165, 111, 31))
        self.addButton_4.setAutoDefault(False)
        self.addButton_4.setObjectName("addButton_4")
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(250, 18, 331, 41))
        self.label_34.setObjectName("label_34")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(80, 65, 113, 21))
        self.comboBox.setObjectName("comboBox")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 617, 241))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 270, 391, 221))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(520, 440, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 470, 76, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setGeometry(QtCore.QRect(420, 440, 51, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 270, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.ID_5, self.ipAddress_5)
        Dialog.setTabOrder(self.ipAddress_5, self.UserName_5)
        Dialog.setTabOrder(self.UserName_5, self.Password_5)
        Dialog.setTabOrder(self.Password_5, self.addButton_4)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(1)
        self.comboBox.addItem("router")
        self.comboBox.addItem("switch")
        self.refreshDB()
        self.refreshDB2()
        self.addButton_4.clicked.connect(self.add_data)
        self.updateButton_4.clicked.connect(self.update_data)
        self.delButton_4.clicked.connect(self.delete_data)
        self.pushButton.clicked.connect(self.conTel)
        self.pushButton_2.clicked.connect(self.clearButton)
        self.sqlData()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Data Input"))
        self.label_28.setText(_translate("Dialog", "I          D"))
        self.label_29.setText(_translate("Dialog", "M o d e l"))
        self.label_31.setText(_translate("Dialog", "Ip Address"))
        self.label_32.setText(_translate("Dialog", "UserName"))
        self.label_33.setText(_translate("Dialog", "Password"))
        self.delButton_4.setText(_translate("Dialog", "Delete"))
        self.updateButton_4.setText(_translate("Dialog", "Update"))
        self.addButton_4.setText(_translate("Dialog", "Add"))
        self.label_34.setText(_translate("Dialog", "ID값을 기준으로 모든 기능이 작동합니다"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "DB List"))
        self.pushButton.setText(_translate("Dialog", "Connect"))
        self.label_30.setText(_translate("Dialog", "ID"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Telnet connect"))

    # DB테이블 없을 때 생성
    def create_table(self):
        cur.execute(self.sql_create)
        a = cur.execute(self.sql_select_all).fetchall()
        if len(a) == 0:
            cur.execute(self.sql_insert_example)
        con.commit()

    # 첫번째 페이지 목록 갱신
    def refreshDB(self):
        self.tableWidget.clear()
        cur.execute(self.sql_select_all)
        sqlfetchall = cur.fetchall()
        self.tableWidget.setRowCount(len(sqlfetchall))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(pd.read_sql("select * from devicetbl", con))
        for cnt in range(len(sqlfetchall)):
            for num in range(0, 5, 1):
                self.tableWidget.setItem(cnt, num, QtWidgets.QTableWidgetItem(str(sqlfetchall[cnt][num])))
        self.refreshDB2()

    # 두번째 페이지 목록 갱신
    def refreshDB2(self):
        self.tableWidget_2.clear()
        cur.execute(self.sql_select_all)
        sqlfetchall = cur.fetchall()
        self.tableWidget_2.setRowCount(len(sqlfetchall))
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setHorizontalHeaderLabels(pd.read_sql("select * from devicetbl", con))
        for cnt in range(len(sqlfetchall)):
            for num in range(0, 5, 1):
                self.tableWidget_2.setItem(cnt, num, QtWidgets.QTableWidgetItem(str(sqlfetchall[cnt][num])))
        self.sqlData()

    # 체크박스 값
    def sqlData(self):
        self.comboBox_2.clear()
        listI = cur.execute(self.sql_select_all).fetchall()
        for i in range(len(listI)):
            self.comboBox_2.addItem(str(listI[i][0]))

    # 데이터 추가 
    def add_data(self):
        if self.ID_5.text() == "":
            self.label_34.setText("Id value not entered")
            return 0

        if int(self.ID_5.text()) > 9999 or int(self.ID_5.text()) < 0:
            self.label_34.setText('ID value can only be a number from 0 to 9999')
            return 0
        id_val = list(cur.execute(self.sql_select_id).fetchall())
        for i in range(len(id_val)):
            if id_val[i][0] == self.ID_5.text():
                self.label_34.setText("ID value cannot be duplicate")
                return 0

        val = (self.ID_5.text(), self.comboBox.currentText(), self.ipAddress_5.text(), self.UserName_5.text(), \
               self.Password_5.text())
        cur.execute(self.sql_insert, val)
        con.commit()
        self.refreshDB()
        self.ID_5.clear()
        self.ipAddress_5.clear()
        self.UserName_5.clear()
        self.Password_5.clear()
        self.label_34.setText("Data add Success")

    # 데이터 수정 버튼
    def update_data(self):
        if self.ID_5.text() == "":
            self.label_34.setText("Id value not entered")
            return 0

        if int(self.ID_5.text()) > 9999 or int(self.ID_5.text()) < 0:
            self.label_34.setText('ID value can only be a number from 0 to 9999')
            return 0
        cur.execute(self.sql_select_id)
        id_val = list(cur.fetchall())
        tmp = 0
        for i in range(len(id_val)):
            if id_val[i][0] == self.ID_5.text():
                tmp += 1
        if tmp != 1:
            self.label_34.setText("ID value can't find")
            return 0;

        val = (self.comboBox.currentText(), self.ipAddress_5.text(), self.UserName_5.text(), \
               self.Password_5.text(), self.ID_5.text())
        cur.execute(self.sql_update, val)
        con.commit()
        self.refreshDB()
        self.ID_5.clear()
        self.ipAddress_5.clear()
        self.UserName_5.clear()
        self.Password_5.clear()
        self.label_34.setText("Data update Success")

    # 데이터 삭제 버튼
    def delete_data(self):
        if self.ID_5.text() == "":
            self.label_34.setText("Id value not entered")
            return 0

        cur.execute(self.sql_select_id)
        id_val = list(cur.fetchall())
        tmp = 0
        for i in range(len(id_val)):
            if id_val[i][0] == self.ID_5.text():
                tmp += 1
        if tmp != 1:
            self.label_34.setText("ID value can't find")
            return 0;

        cur.execute(self.sql_delete % self.ID_5.text())
        con.commit()
        self.refreshDB()
        self.ID_5.clear()
        self.ipAddress_5.clear()
        self.UserName_5.clear()
        self.Password_5.clear()
        self.refreshDB()
        self.label_34.setText("Data delete Success")

    # 텔넷 접속
    def conTel(self):
        val = self.comboBox_2.currentText()
        cur.execute(self.sql_contel, val)
        listA = list(cur.fetchall())
        IN_INPtext = self.textEdit.toPlainText()
        w_txt = IN_INPtext.split('\n')
        model = str(listA[0][0])
        host = str(listA[0][1])
        userId = str(listA[0][2])
        userPw = str(listA[0][3])

        tn = telnetlib.Telnet(host)
        tn.read_until(b"Username: ")
        tn.write(userId.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(userPw.encode('ascii') + b"\n")
        tn.write(b"enable\n")
        tn.write(userPw.encode('ascii') + b"\n")
        tn.write(b"conf t\n")
        for data in w_txt:
            tn.write(data.encode('ascii') + b"\n")
        tn.write(b"end\n")
        tn.write(b"exit\n")
        self.textEdit.setText(str(tn.read_all().decode('ascii'))[2:])

    # 결과창 공백으로
    def clearButton(self):
        self.textEdit.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

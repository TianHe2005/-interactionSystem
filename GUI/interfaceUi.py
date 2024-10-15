
import sys
import json
import jsonpickle
import os
import thread1

from PyQt5 import sip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPoint
from PyQt5.QtGui import QPixmap, QIntValidator, QMouseEvent, QDesktopServices
from PyQt5.QtWidgets import QMessageBox

import detect

from utils.myutil import file_is_pic, Globals
from service.ControlVideoPlay import ControlVideoPlay
from service.PlayService import PlayService
from service.PlayShootingGameService import PlayShootingGameService

from entity.action import Action
from entity.angle import Angle
from entity.software import Software
from entity.judge import Judge
from entity.position import Position
from entity.VoiceInteraction import VoiceAction




def action_update_name(input_action, save_action):
    save_action.name = input_action.text()



def action_update_level(input_action, save_action):
    save_action.level = input_action.text()



def action_update_keys(input_action, save_action):
    save_action.keys = input_action.text()






class Ui_MainWindow(object):
    def __init__(self):
        self.software = Software("", "", "", "", [])
        self.VOICE_ACTION = VoiceAction("", "", "", "", "")
        self.m_bPressed = False
        self.m_point = QPoint()
        self.recording = False


    def mousePressEvent(self, event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.m_bPressed = True
                self.m_point = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
            if self.m_bPressed:
                self.move(event.globalPos() - self.m_point)

    def mouseReleaseEvent(self, event: QMouseEvent):
            self.m_bPressed = False





    def action_ui(self, actions, software, index, index_y):
        action_ui = QtWidgets.QWidget(actions)
        action_ui.resize(150, 200)
        action_ui.move((200 * index) + (15 * index), 320 * index_y)
        software_name = QtWidgets.QLabel(action_ui)
        software_name.setText("软件名称：" + software.name)
        object_name = "game" + str(index)
        action_ui.setObjectName(object_name)
        action_ui.setStyleSheet("#" + object_name + "{border:1px solid}")
        software_name.move(10, 20)

        description_label = QtWidgets.QLabel(action_ui)
        description_label.setMaximumSize(150, 170)
        description_label.setText("介绍：\n" + software.description)
        description_label.move(10, 50)
        description_label.setWordWrap(True)

        play_game_button = QtWidgets.QPushButton(action_ui)
        play_game_button.setText("启动互动")
        play_game_button.setMinimumSize(150, 30)
        play_game_button.move(0, 140)
        play_game_button.clicked.connect(lambda: self.play_game_1(software))

        edit_button = QtWidgets.QPushButton(action_ui)
        edit_button.setText("修改动作")
        edit_button.setMinimumSize(150, 30)
        edit_button.move(0, 170)
        edit_button.clicked.connect(lambda: self.edit_game())


    @staticmethod
    def shooting():
        shootingGame = PlayShootingGameService()
        shootingGame.play()
    @staticmethod
    def controlVideo():
        control = ControlVideoPlay()
        control.play()
    @staticmethod
    def edit_game(self):
        self.tabWidget.show()
        self.tabWidget_2.close()
        self.textBrowser.close()
        self.tabWidget_3.close()
        self.stackedWidget.close()


    @staticmethod
    def play_game_1(self, game):
            play = PlayService()
            play.playGame(game)





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 681)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 841, 621))
        self.widget.setStyleSheet("#widget{\n"
"        \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 841, 41))
        self.widget_2.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.widget_15 = QtWidgets.QWidget(self.widget_2)
        self.widget_15.setGeometry(QtCore.QRect(0, 0, 141, 41))
        self.widget_15.setObjectName("widget_15")
        self.pushButton = QtWidgets.QPushButton(self.widget_15)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 131, 41))
        self.pushButton.setStyleSheet("border:none;\n"
"font: 12pt \"方正粗黑宋简体\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/aikj.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.widget_16 = QtWidgets.QWidget(self.widget_2)
        self.widget_16.setGeometry(QtCore.QRect(640, 0, 201, 41))
        self.widget_16.setObjectName("widget_16")
        self.layoutWidget = QtWidgets.QWidget(self.widget_16)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 0, 111, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_logout = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_logout.setStyleSheet("QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_logout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icon_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon1)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout.addWidget(self.pushButton_logout)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icon_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setStyleSheet("\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/icon_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(0, 40, 131, 581))
        self.widget_3.setStyleSheet("#widget_3{\n"
"    background-image: url(:/images/image/beijing1.jpg);\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    color:rgb(255,255,255);\n"
"    \n"
"    font: 12pt \"黑体\";\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(158, 158, 158);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(6, 2, 121, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)


        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)

        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(130, 40, 711, 581))
        self.widget_6.setStyleSheet("#widget_6{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom-right-radius:20px;\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_6)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 711, 581))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")





        self.widget_21 = QtWidgets.QWidget(self.tab)
        self.widget_21.setGeometry(QtCore.QRect(0, 0, 701, 541))
        self.widget_21.setObjectName("widget_21")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_21)
        self.tableWidget.setGeometry(QtCore.QRect(155, 0, 551, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_21)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(
            lambda: self.set_software_name(self.software, self.lineEdit)
        )
        self.textEdit_5 = QtWidgets.QTextEdit(self.widget_21)
        self.textEdit_5.setGeometry(QtCore.QRect(30, 100, 111, 71))
        self.textEdit_5.setDocumentTitle("")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.textChanged.connect(
            lambda: self.set_software_description(self.software, self.textEdit_5)
        )
        self.tableWidget.setHorizontalHeaderLabels(["动作名称", "动作类型", "动作优先级", "判断条件", "输出按键"])
        for i in range(len(self.software.actions)):
            self.show_actions(self.tableWidget, self.software.actions[i])
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_21)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 500, 75, 23))
        self.pushButton_9.setObjectName("pushButton")
        self.pushButton_9.clicked.connect(lambda: self.add_action(self.tableWidget))
        self.pushButton_15 = QtWidgets.QPushButton(self.tab)
        self.pushButton_15.setGeometry(QtCore.QRect(40, 500, 191, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.save_software)





        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")


        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                "")
        self.tab_11.setObjectName("tab_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_12.setGeometry(QtCore.QRect(260, 470, 111, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda: self.add_action_1(self.tableWidget_2))
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_13.setGeometry(QtCore.QRect(30, 520, 75, 24))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.save_software_1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_11)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 701, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setHorizontalHeaderLabels(["动作名称", "指令类型", "指令优先级", "判断条件", "输出指令"])
        for i in range(len(self.software.actions)):
            self.show_actions(self.tableWidget, self.software.actions[i])
        self.tabWidget.addTab(self.tab_11, "")



        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget_6)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 711, 581))
        self.tabWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_11 = QtWidgets.QWidget(self.tab_3)
        self.widget_11.setGeometry(QtCore.QRect(-1, -1, 711, 501))
        self.widget_11.setObjectName("widget_11")
        self.layoutWidget3 = QtWidgets.QWidget(self.widget_11)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 721, 501))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.widget_12 = QtWidgets.QWidget(self.tab_3)
        self.widget_12.setGeometry(QtCore.QRect(10, 500, 701, 51))
        self.widget_12.setObjectName("widget_12")
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget_12)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 10, 631, 26))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_4.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_4.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_4.addWidget(self.pushButton_18)

        self.pushButton_30 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_4.addWidget(self.pushButton_30)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget_13 = QtWidgets.QWidget(self.tab_4)
        self.widget_13.setGeometry(QtCore.QRect(0, 0, 721, 501))
        self.widget_13.setObjectName("widget_13")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget_13)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 0, 657, 554))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_19.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_6.addWidget(self.label_19)
        self.widget_14 = QtWidgets.QWidget(self.tab_4)
        self.widget_14.setGeometry(QtCore.QRect(20, 500, 681, 51))
        self.widget_14.setObjectName("widget_14")
        self.layoutWidget_4 = QtWidgets.QWidget(self.widget_14)
        self.layoutWidget_4.setGeometry(QtCore.QRect(20, 20, 651, 26))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_7.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_7.addWidget(self.pushButton_21)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.widget_6)
        self.tabWidget_3.setGeometry(QtCore.QRect(-4, -1, 711, 571))
        self.tabWidget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(0, 30, 701, 521))
        self.label_16.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")


        self.widget_5 = QtWidgets.QWidget(self.tab_5)
        self.widget_5.setGeometry(QtCore.QRect(-1, 0, 711, 631))
        self.widget_5.setObjectName("widget_5")
        self.pushButton_22 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_22.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.pushButton_22.setObjectName("pushButton_22")




        actions = QtWidgets.QWidget(self.widget_5)
        actions.setMinimumSize(700, 700)
        actions.move(0, 20)
        actions.setObjectName("game_actions")
        actions.setStyleSheet("#game_actions{border:1px solid}")

        scroll_area = QtWidgets.QScrollArea(self.widget_5)
        scroll_area.setWidget(actions)
        scroll_area.move(0, 20)
        scroll_area.setMinimumSize(600, 700)
        prefix_url = "./data1/"
        files = os.listdir(prefix_url)
        index = 0
        index_y = -1
        for game_str in files:
            if index % 6 == 0:
                index_y += 1
                index = 0
            with open(prefix_url + game_str, encoding="utf-8") as game_file:
                # dict_game =
                s = game_file.read()
                software = jsonpickle.decode(s)
                self.action_ui(actions, software, index, index_y)
                index += 1






        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.widget_17 = QtWidgets.QWidget(self.tab_6)
        self.widget_17.setGeometry(QtCore.QRect(0, 0, 711, 31))
        self.widget_17.setObjectName("widget_17")
        self.pushButton_23 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_23.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_17 = QtWidgets.QLabel(self.tab_6)
        self.label_17.setGeometry(QtCore.QRect(1, 30, 701, 531))
        self.label_17.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.widget_18 = QtWidgets.QWidget(self.tab_7)
        self.widget_18.setGeometry(QtCore.QRect(0, 0, 711, 31))
        self.widget_18.setObjectName("widget_18")
        self.pushButton_24 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_24.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_20 = QtWidgets.QLabel(self.tab_7)
        self.label_20.setGeometry(QtCore.QRect(1, 30, 701, 521))
        self.label_20.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.tabWidget_3.addTab(self.tab_7, "")





        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.widget_19 = QtWidgets.QWidget(self.tab_8)
        self.widget_19.setGeometry(QtCore.QRect(0, 490, 701, 51))
        self.widget_19.setObjectName("widget_19")
        self.textEdit = QtWidgets.QTextEdit(self.widget_19)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 711, 61))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 4, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")


        self.widget_20 = QtWidgets.QWidget(self.tab_8)
        self.widget_20.setGeometry(QtCore.QRect(-1, -1, 711, 491))
        self.widget_20.setObjectName("widget_20")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_20)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 711, 491))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.widget_20)
        self.label.setGeometry(QtCore.QRect(3, 1, 701, 481))
        self.label.setText("")
        self.label.setObjectName("label")

        self.tabWidget_3.addTab(self.tab_8, "")







        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_6)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 711, 581))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 711, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 290, 391, 291))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.widget1 = QtWidgets.QWidget(self.page)
        self.widget1.setGeometry(QtCore.QRect(390, 290, 321, 121))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_2.setText('<a href="https://www.kaggle.com/">点击访问https://www.kaggle.com</a>')
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction)
        self.label_2.linkActivated.connect(self.link_clicked)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_3.setText('<a href="https://www.aigc.cn/">点击访问https://www.aigc.cn</a>')
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction)
        self.label_3.linkActivated.connect(self.link_clicked)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_4.setText('<a href="https://www.csdn.net/">点击访问https://www.csdn.net</a>')
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction)
        self.label_4.linkActivated.connect(self.link_clicked)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_5.setText('<a href="https://docs.ultralytics.com/">点击访问https://docs.ultralytics.com</a>')
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction)
        self.label_5.linkActivated.connect(self.link_clicked)
        self.label_21 = QtWidgets.QLabel(self.widget1)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.label_21.setText('<a href="https://roboflow.com/">点击访问https://roboflow.com</a>')
        self.label_21.setOpenExternalLinks(True)
        self.label_21.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction)
        self.label_21.linkActivated.connect(self.link_clicked)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)




        self.tabWidget_3.raise_()
        self.tabWidget.raise_()
        self.tabWidget_2.raise_()
        self.textBrowser.raise_()
        self.stackedWidget.raise_()
        self.pushButton_3.clicked.connect(self.change_widget1)
        self.pushButton_5.clicked.connect(self.change_widget2)
        self.pushButton_6.clicked.connect(self.change_widget3)
        self.pushButton_7.clicked.connect(self.change_widget4)
        self.pushButton_8.clicked.connect(self.yuying)
        self.pushButton_16.clicked.connect(self.load_source)
        self.pushButton_18.clicked.connect(self.select_model)
        self.pushButton_17.clicked.connect(self.target_detect)
        self.pushButton_30.clicked.connect(self.show_dir)
        self.pushButton_20.clicked.connect(self.camera_detect)
        self.pushButton_21.clicked.connect(self.select_videomodel)
        self.pushButton_23.clicked.connect(self.shooting)
        self.pushButton_24.clicked.connect(self.controlVideo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_4.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton_2.clicked.connect(MainWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "人机互动系统"))
        self.pushButton_3.setText(_translate("MainWindow", "首页"))
        self.pushButton_5.setText(_translate("MainWindow", "动作编辑"))
        self.pushButton_6.setText(_translate("MainWindow", "目标识别"))
        self.pushButton_7.setText(_translate("MainWindow", "人机互动"))
        self.pushButton_8.setText(_translate("MainWindow", "开始识别"))
        self.pushButton_9.setText(_translate("MainWindow", "添加动作"))
        self.pushButton_15.setText(_translate("MainWindow", "保存"))
        self.pushButton_12.setText(_translate("MainWindow", "添加指令"))
        self.pushButton_13.setText(_translate("MainWindow", "保存"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "组别名称"))
        self.textEdit_5.setPlaceholderText(_translate("MainWindow", "介绍"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "人体姿态交互设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "手势交互设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "人脸交互设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "语音交互设置"))
        self.label_14.setText(_translate("MainWindow", "原图"))
        self.label_15.setText(_translate("MainWindow", "识别结果"))
        self.pushButton_16.setText(_translate("MainWindow", "选择图片/视频"))
        self.pushButton_17.setText(_translate("MainWindow", "开始识别"))
        self.pushButton_18.setText(_translate("MainWindow", "选择模型"))
        self.pushButton_30.setText(_translate("MainWindow", "保存资源"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "图片/视频识别"))
        self.pushButton_20.setText(_translate("MainWindow", "开始识别"))
        self.pushButton_21.setText(_translate("MainWindow", "选择模型"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "实时识别检测"))
        self.pushButton_22.setText(_translate("MainWindow", "启动动交互"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "人体姿态交互"))
        self.pushButton_23.setText(_translate("MainWindow", "启动动交互"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "手势交互"))
        self.pushButton_24.setText(_translate("MainWindow", "启动动交互"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("MainWindow", "人脸交互"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "语音交互"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600; color:#aaaaff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600; color:#aaaaff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#aaaaff;\">本系统可进行目标检测识别，人体姿态估计，手势识别，人脸识别可通过人体姿态估计，手势识别，人脸识别进行人机交互可自定义设置关键点坐标夹角达到检测关键动作从而进行交互，可自定义绑定任何信号，如键盘消息信号，鼠标，或者嵌入式系统中的其他信号</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600; color:#aaaaff;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600; color:#aaaaff;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#aaaaff;\">以下是一些数据集模型素材网站</span></p></body></html>"))




    def link_clicked(url):
        print("Link clicked:", url.toString())
        # 打开网页
        QDesktopServices.openUrl(url)




    def change_widget3(self):
        self.tabWidget_2.show()
        self.tabWidget_3.close()
        self.textBrowser.close()
        self.stackedWidget.close()
        self.tabWidget.close()


    def change_widget2(self):
                self.tabWidget.show()
                self.tabWidget_2.close()
                self.tabWidget_3.close()
                self.textBrowser.close()
                self.stackedWidget.close()
    def change_widget1(self):
                self.textBrowser.show()
                self.tabWidget.close()
                self.tabWidget_2.close()
                self.tabWidget_3.close()
                self.stackedWidget.show()
    def change_widget4(self):
                self.textBrowser.close()
                self.tabWidget.close()
                self.tabWidget_2.close()
                self.tabWidget_3.show()
                self.label_16.close()
                self.stackedWidget.close()


    def init_file(self):
        if not os.path.exists(self.result_path):
            os.mkdir(self.result_path)





    def load_source(self):
            self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "加载数据", "data", "All Files(*)")
            self.suffix = self.file_path.split(".")[-1]  # 读取后缀
            pixmap = QPixmap(self.file_path)
            pixmap = pixmap.scaled(self.label_14.size(), Qt.IgnoreAspectRatio)
            self.label_14.setPixmap(pixmap)
            if self.file_path != "":
                    self.pushButton_16.setText(self.file_path.split('/')[-1])
            # 清空result文件夹内容
            for i in os.listdir(self.result_path):
                    file_data = self.result_path + "/" + i
                    os.remove(file_data)

            # 选择模型


    def select_model(self):
            model_path = QtWidgets.QFileDialog.getOpenFileName(self, "选择模型", "weights", "Model files(*.pt)")
            self.model_path = model_path
            if model_path[0] != "":
                    self.pushButton_18.setText(self.model_path[0].split('/')[-1])
    def select_videomodel(self):
            model_path = QtWidgets.QFileDialog.getOpenFileName(self, "选择模型", "weights", "Model files(*.pt)")
            self.model_path = model_path
            if model_path[0] != "":
                    self.pushButton_21.setText(self.model_path[0].split('/')[-1])
    def target_detect(self):
        if self.check_file():
            # 点击之后防止误触，禁用按钮
            self.pushButton_16.setEnabled(False)
            self.pushButton_18.setEnabled(False)
            self.pushButton_17.setEnabled(False)
            self.thread = DetectionThread(self.file_path, self.model_path, self.label_15)
            self.thread.start()
            # 子线程运行结束之后signal_done，主线程执行UI更新操作
            self.thread.signal_done.connect(self.flash_target)

    def check_file(self):
        if self.file_path is None or self.file_path == "":
            QMessageBox.information(self, '提示', '请先导入数据')
            return False
        if self.model_path is None or self.model_path[0] == "":
            QMessageBox.information(self, '提示', '请先选择模型')
            return False
        return True

    def flash_target(self):
        if file_is_pic(self.suffix):
            img_path = os.getcwd() + '/result/' + [f for f in os.listdir('../result')][0]
            pixmap = QPixmap(img_path)
            pixmap = pixmap.scaled(self.label_15.size(), Qt.IgnoreAspectRatio)
            self.label_15.setPixmap(pixmap)
        # 刷新完之后恢复按钮状态
        self.pushButton_16.setEnabled(True)
        self.pushButton_18.setEnabled(True)
        self.pushButton_17.setEnabled(True)


    def check_model(self):
        if self.model_path is None or self.model_path[0] == "":
            QMessageBox.information(self, '提示', '请先选择模型')
            return False
        return True
    def show_dir(self):
        path = os.path.join(os.getcwd(), 'result')
        os.system(f"start explorer {path}")

    # 摄像头检测
    def camera_detect(self):
        if Globals.camera_running:
            Globals.camera_running = False
            self.pushButton_20.setText("摄像头检测")
            self.pushButton_16.setEnabled(True)
            self.pushButton_18.setEnabled(True)
            self.pushButton_17.setEnabled(True)
            self.label_19.clear()
        else:
            if self.check_model():
                Globals.camera_running = True
                self.pushButton_16.setEnabled(False)
                self.pushButton_18.setEnabled(False)
                self.pushButton_17.setEnabled(False)
                self.pushButton_20.setText("关闭摄像头")
                self.camera_thread = CameraDetectionThread(self.model_path, self.label_19)
                self.camera_thread.start()

    def yuying(self):

            self.recognition_thread = RecognitionThread(self.label)
            self.recognition_thread.start()



    def save_software(self):
        with open(
            "./data1/" + self.software.name + ".json", "w", encoding="utf-8"
        ) as out_file:
            s = json.dumps(
                json.loads(jsonpickle.encode(self.software)), indent=4, ensure_ascii=False
            )
            out_file.write(s)
            # json.dump(self.software, out_file, default=lambda o: o.__dict__, ensure_ascii=False)
            # print(type(my_software))
            # d = json.loads(my_software)
            # new_software1 = DefaultMunch.fromDict(d)


    # 添加动作判定
    def append_angle(self, action, lay):
        self.delete_all_children(lay)
        angle = Angle("", "", "", "", "", "", "")
        action.judge.angles.append(angle)
        self.show_judge(action, lay)

    # 添加位置判断
    def append_position(self, action, lay):
        self.delete_all_children(lay)
        position = Position("", "", "", "")
        action.judge.positions.append(position)
        self.show_judge(action, lay)

    def show_judge(self, action, lay):
        angle_index = 0
        for position in action.judge.positions:
            self.position_widget(position, lay, angle_index, action)
            angle_index += 1
        for angle in action.judge.angles:
            self.angle_widget(angle, lay, angle_index, action)
            angle_index += 1

    # 删除角度判定
    def delete_judge_angle(self, angle, action):
        action.judge.angles.remove(angle)
        self.edit_judge(action)

    # 删除位置判定
    def delete_judge_position(self, position, action):
        action.judge.positions.remove(position)
        self.edit_judge(action)



    def delete_all_children(self, lay):
        for i in lay.children():
            if not i.objectName() == "box_layout":
                i.deleteLater()
                sip.delete(i)


    def angle_widget(self, angle, lay, index, action):
        action_angle = QtWidgets.QWidget(lay)
        object_name = "position" + str(index)
        action_angle.setObjectName(object_name)
        action_angle.setStyleSheet("#" + object_name + "{border:1px solid}")
        action_angle.setMinimumSize(680, 180)

        action_angle.move(0, 180 * index + 5)
        vector_label_1 = QtWidgets.QLabel(action_angle)
        vector_label_1.setText("向量1 :")
        vector_label_1.move(5, 33)


        vector_point_box_1 = QtWidgets.QLineEdit(action_angle)
        vector_point_box_1.setText(angle.organ1)
        vector_point_box_1.setPlaceholderText("填图片上关节点的数字")
        vector_point_box_1.setMaximumWidth(150)
        vector_point_box_1.textChanged.connect(
            lambda: self.set_organ1_value(angle, vector_point_box_1)
        )
        vector_point_box_1.move(50, 30)

        vector_point_box_2 = QtWidgets.QLineEdit(action_angle)
        vector_point_box_2.setText(angle.organ2)
        vector_point_box_2.setPlaceholderText("填图片上关节点的数字")
        vector_point_box_2.setMaximumWidth(150)
        vector_point_box_2.textChanged.connect(
            lambda: self.set_organ2_value(angle, vector_point_box_2)
        )
        vector_point_box_2.move(200, 30)

        vector_label_2 = QtWidgets.QLabel(action_angle)
        vector_label_2.setText("向量2 :")
        vector_label_2.move(360, 33)

        vector_point_box_3 = QtWidgets.QLineEdit(action_angle)
        vector_point_box_3.setMaximumWidth(150)
        vector_point_box_3.setPlaceholderText("填图片上关节点的数字")
        vector_point_box_3.setText(angle.organ3)
        vector_point_box_3.textChanged.connect(
            lambda: self.set_organ3_value(angle, vector_point_box_3)
        )
        vector_point_box_3.move(395, 30)

        vector_point_box_4 = QtWidgets.QLineEdit(action_angle)
        vector_point_box_4.setText(angle.organ4)
        vector_point_box_4.setPlaceholderText("填图片上关节点的数字")
        vector_point_box_4.setMaximumWidth(150)
        vector_point_box_4.textChanged.connect(
            lambda: self.set_organ4_value(angle, vector_point_box_4)
        )
        vector_point_box_4.move(545, 30)

        angle_label = QtWidgets.QLabel(action_angle)
        angle_label.move(5, 73)
        angle_label.setText("向量组成夹角范围 :")

        min_angle = QtWidgets.QLineEdit(action_angle)
        min_angle.move(120, 70)
        min_angle.setValidator(QIntValidator(0, 150))
        min_angle.setPlaceholderText("例如:10")
        min_angle.setText(angle.angle1)
        min_angle.setMaximumWidth(90)
        min_angle.textChanged.connect(lambda: self.set_angle1_value(angle, min_angle))

        max_angle = QtWidgets.QLineEdit(action_angle)
        max_angle.move(230, 70)
        max_angle.setValidator(QIntValidator(0, 150))
        max_angle.setPlaceholderText("例如:100")
        max_angle.setText(angle.angle2)
        max_angle.setMaximumWidth(90)
        max_angle.textChanged.connect(lambda: self.set_angle2_value(angle, max_angle))
        instructions = QtWidgets.QLabel(action_angle)
        instructions.setText(
            "说明:左边输入框为小的值，右边输入框为大的值."
            + "\n"
            + "如果向量1与向量2组成的夹角的角度在这个范围之内，"
            + "\n"
            + "则判断为成功做出动作"
        )
        instructions.move(390, 70)

        description_label = QtWidgets.QLabel(action_angle)
        description_label.setText("说明 :")
        description_label.move(5, 113)
        description = QtWidgets.QLineEdit(action_angle)
        description.move(50, 110)
        description.setMinimumWidth(300)
        description.setText(angle.description)
        description.textChanged.connect(
            lambda: self.set_description_value(angle, description)
        )

        delete_angle = QtWidgets.QPushButton(action_angle)
        delete_angle.setText("删除")
        delete_angle.move(500, 135)
        delete_angle.clicked.connect(lambda: self.delete_judge_angle(angle, action))

        action_angle.show()

    def position_widget(self, position, lay, index, action):
        action_position = QtWidgets.QWidget(lay)
        object_name = "position" + str(index)
        action_position.setObjectName(object_name)
        action_position.setStyleSheet("#" + object_name + "{border:1px solid}")
        action_position.setMinimumSize(680, 180)

        action_position.move(0, 180 * index + 5)
        judge_point_label = QtWidgets.QLabel(action_position)
        judge_point_label.setText("判断点:")
        judge_point_label.move(10, 30)
        judge_point_input = QtWidgets.QLineEdit(action_position)
        judge_point_input.setText(position.judge_point)
        judge_point_input.setPlaceholderText("填图片上对应的关节点数字")
        judge_point_input.setMinimumWidth(200)
        judge_point_input.textChanged.connect(
            lambda: self.set_judge_point(position, judge_point_input)
        )
        judge_point_input.move(60, 30)

        judge_point_description = QtWidgets.QLabel(action_position)
        judge_point_description.setText("说明:填写关节点的数字，多个使用竖线分隔。\n例如:10|18|19")
        judge_point_description.move(320, 30)

        standard_point_label = QtWidgets.QLabel(action_position)
        standard_point_label.setText("标准点:")
        standard_point_label.move(10, 65)
        standard_point_input = QtWidgets.QLineEdit(action_position)
        standard_point_input.setText(position.standard)
        standard_point_input.setPlaceholderText("只能填写一个关节点数字")
        standard_point_input.setMinimumWidth(200)
        standard_point_input.move(60, 65)
        standard_point_input.textChanged.connect(
            lambda: self.set_standard_point(position, standard_point_input)
        )

        judge_in_standard_label = QtWidgets.QLabel(action_position)
        judge_in_standard_label.setText("判断点位于标准点的:")
        judge_in_standard_label.move(10, 100)
        judge_in_standard_input = QtWidgets.QLineEdit(action_position)
        judge_in_standard_input.setText(position.located)
        judge_in_standard_input.setMaximumWidth(80)
        judge_in_standard_input.move(130, 98)
        judge_in_standard_input.textChanged.connect(
            lambda: self.set_located_point(position, judge_in_standard_input)
        )

        judge_in_standard_description = QtWidgets.QLabel(action_position)
        judge_in_standard_description.move(250, 100)
        judge_in_standard_description.setText(
            "只能填写：上，下，左，右。\n例如：填写上表示判断点位于标准的上边，则判断动作为成功"
        )

        position_description_label = QtWidgets.QLabel(action_position)
        position_description_label.setText("说明:")
        position_description_label.move(10, 135)

        position_description_input = QtWidgets.QLineEdit(action_position)
        position_description_input.setText(position.description)
        position_description_input.setMinimumWidth(300)
        position_description_input.move(60, 135)
        position_description_input.textChanged.connect(
            lambda: self.set_position_description_value(
                position, position_description_input
            )
        )

        delete_position = QtWidgets.QPushButton(action_position)
        delete_position.setText("删除")
        delete_position.move(500, 135)
        delete_position.clicked.connect(
            lambda: self.delete_judge_position(position, action)
        )

        action_position.show()

    def show_window(self):
        self.r_main.hide()

    def edit_judge(self, action):
        if not self.r_main is None:
            self.r_main.close()
            self.r_main.deleteLater()
            sip.delete(self.r_main)


        self.r_main = QtWidgets.QWidget(self.tab)
        self.r_main.setGeometry(QtCore.QRect(0, 0, 701, 551))
        self.r_main.setObjectName("widget_22")



        r_main_action = QtWidgets.QWidget(self.r_main)
        r_main_action.move(0, 0)
        r_main_action.setMinimumSize(701, 1000)
        r_main_action.setMaximumSize(701, 1000)
        r_main_action.setObjectName("r_main_action")
        r_main_action.setStyleSheet("#r_main_action{border:1px solid}")
        lay = QtWidgets.QVBoxLayout()
        lay.setObjectName("box_layout")

        scrollArea = QtWidgets.QScrollArea(self.r_main)
        scrollArea.move(0, 60)
        scrollArea.setMinimumWidth(700)
        scrollArea.setMinimumHeight(190)
        scrollArea.setWidget(r_main_action)
        scrollArea.show()

        judge_label = QtWidgets.QLabel(self.r_main)
        judge_label.setText("判定条件")
        judge_label.setStyleSheet("font:bold 20px")
        judge_label.move(300, 0)

        self.pushButton_10 = QtWidgets.QPushButton(self.r_main)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 30, 91, 16))
        self.pushButton_10.setObjectName("pushButton_3")
        self.pushButton_10.clicked.connect(
            lambda: self.append_position(action, scrollArea.widget())
        )
        self.pushButton_11 = QtWidgets.QPushButton(self.r_main)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 30, 91, 16))
        self.pushButton_11.setObjectName("pushButton_4")
        self.pushButton_11.clicked.connect(
            lambda: self.append_angle(action, scrollArea.widget())
        )
        self.pushButton_19 = QtWidgets.QPushButton(self.r_main)
        self.pushButton_19.setGeometry(QtCore.QRect(620, 0, 75, 23))
        self.pushButton_19.setObjectName("pushButton_8")
        self.pushButton_19.clicked.connect(self.show_window)
        _translate = QtCore.QCoreApplication.translate

        self.pushButton_19.setText(_translate("Form", "返回"))
        self.pushButton_10.setText(_translate("Form", "添加位置判断"))
        self.pushButton_11.setText(_translate("Form", "添加角度判断"))
        self.label_18 = QtWidgets.QLabel(self.r_main)
        self.label_18.setGeometry(QtCore.QRect(0, 290, 700, 270))
        self.label_18.setStyleSheet("image: url(:/images/image/position.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")

        self.show_judge(action, scrollArea.widget())
        self.r_main.show()

    def action_update_name_1(self, line_edit, action):
            # 获取输入框中的文本
            new_name = line_edit.text()

            # 更新`action`对象的名称
            action.name = new_name

    def action_update_keys_1(self, line_edit, action):
            # 获取输入框中的文本
            new_keys = line_edit.text()
            action.keys = new_keys
    def action_update_level_1(self, line_edit, action):
            # 获取输入框中的文本
            new_level = line_edit.text()

            # 更新`action`对象的名称
            action.level = new_level

    def action_update_judge_1(self, line_edit, action):
            # 获取输入框中的文本
            new_judge = line_edit.text()
            action.judge = new_judge


    def add_action_to_voice_action(self, action):
        """向 VOICE_ACTION 添加一个 action"""
        if isinstance(action, VoiceAction):
            self.VOICE_ACTION.add_action(action)
        else:
            raise ValueError("The action must be an instance of VoiceAction.")
    def save_software_1(self):
        with open(
            "./data2/" + self.VOICE_ACTION.name + ".json", "w", encoding="utf-8"
        ) as out_file:
            s = json.dumps(
                json.loads(jsonpickle.encode(self.VOICE_ACTION)), indent=4, ensure_ascii=False
            )
            out_file.write(s)

    def add_action_1(self, table):
        index = table.rowCount()
        table.insertRow(index)
        action = VoiceAction("", "", "", "", "")
        self.add_action_to_voice_action(action)
        action_name = QtWidgets.QLineEdit()
        table.setCellWidget(index, 0, action_name)
        action_name.textChanged.connect(lambda: self.action_update_name_1(action_name, action))

        table.setItem(index, 1, QtWidgets.QTableWidgetItem("自定义类型"))

        action_level = QtWidgets.QLineEdit()
        action_level.setPlaceholderText("数字，越小越先")
        table.setCellWidget(index, 2, action_level)
        action_level.textChanged.connect(
            lambda: self.action_update_level_1(action_level, action)
        )
        rang = QIntValidator()
        rang.setRange(0, 10)
        action_level.setValidator(rang)

        Judge = QtWidgets.QLineEdit()
        Judge.setPlaceholderText("例如：打开百度，鼠标上移")
        table.setCellWidget(index, 3, Judge)
        Judge.textChanged.connect(
                lambda: self.action_update_judge_1(Judge, action)
        )

        action_keys = QtWidgets.QLineEdit()
        table.setCellWidget(index, 4, action_keys)
        action_keys.textChanged.connect(lambda: self.action_update_keys_1(action_keys, action))
        action_keys.setPlaceholderText("例如：网址，按键")
        table.update()

    def add_action(self, table):
        index = table.rowCount()
        table.insertRow(index)
        judge_button = QtWidgets.QPushButton()
        judge_button.setText("编辑")
        judge = Judge()
        action = Action("", "", "", judge, "")
        self.software.actions.append(action)

        action_name = QtWidgets.QLineEdit()
        table.setCellWidget(index, 0, action_name)
        action_name.textChanged.connect(lambda: action_update_name(action_name, action))

        table.setItem(index, 1, QtWidgets.QTableWidgetItem("自定义类型"))

        action_level = QtWidgets.QLineEdit()
        action_level.setPlaceholderText("数字，越小越先")
        table.setCellWidget(index, 2, action_level)
        action_level.textChanged.connect(
            lambda: action_update_level(action_level, action)
        )
        rang = QIntValidator()
        rang.setRange(0, 10)
        action_level.setValidator(rang)

        table.setCellWidget(index, 3, judge_button)
        judge_button.clicked.connect(lambda: self.edit_judge(action))
        action_keys = QtWidgets.QLineEdit()
        table.setCellWidget(index, 4, action_keys)
        action_keys.textChanged.connect(lambda: action_update_keys(action_keys, action))
        action_keys.setPlaceholderText("例如：s+d+j")
        table.update()
    def show_actions(self, table, action):

        index = table.rowCount()
        table.insertRow(index)
        self.judge_button = QtWidgets.QPushButton(self.tableWidget)
        self.judge_button.setText("编辑")
        action_name = QtWidgets.QLineEdit()
        table.setCellWidget(index, 0, action_name)
        action_name.setText(action.name)
        action_name.textChanged.connect(lambda: action_update_name(action_name, action))
        table.setItem(index, 1, QtWidgets.QTableWidgetItem("自定义类型"))

        action_level = QtWidgets.QLineEdit()
        action_level.setPlaceholderText("数字，越小越先")
        action_level.setText(action.level)
        table.setCellWidget(index, 2, action_level)
        action_level.textChanged.connect(
            lambda: action_update_level(action_level, action)
        )
        rang = QtWidgets.QIntValidator()
        rang.setRange(0, 10)
        action_level.setValidator(rang)

        table.setCellWidget(index, 3, self.judge_button)
        self.judge_button.clicked.connect(lambda: self.edit_judge(action))
        action_keys = QtWidgets.QLineEdit()
        table.setCellWidget(index, 4, action_keys)
        action_keys.textChanged.connect(lambda: action_update_keys(action_keys, action))
        action_keys.setPlaceholderText("例如：s+d+j")
        action_keys.setText(action.keys)
        table.update()


    # 角度判定设置向量1
    def set_organ1_value(self, angle, value):
        angle.organ1 = str(value.text())

    def set_organ2_value(self, angle, value):
        angle.organ2 = str(value.text())

    def set_organ3_value(self, angle, value):
        angle.organ3 = str(value.text())

    def set_organ4_value(self, angle, value):
        angle.organ4 = str(value.text())

    def set_angle1_value(self, angle, value):
        angle.angle1 = str(value.text())

    def set_angle2_value(self, angle, value):
        angle.angle2 = str(value.text())

    def set_description_value(self, angle, value):
        angle.description = str(value.text())

    def set_judge_point(self, position, value):
        position.judge_point = str(value.text())

    def set_standard_point(self, position, value):
        position.standard = str(value.text())

    def set_located_point(self, position, value):
        position.located = str(value.text())

    def set_position_description_value(self, angle, value):
        angle.description = str(value.text())

    def set_software_name(self, software, value):
        software.name = str(value.text())

    def set_software_description(self, software, value):
        software.description = value.document().toPlainText()

    def set_software_type(self, software, value):
        software.type = value.currentText()


import res_rc


class DetectionThread(QThread):
    signal_done = pyqtSignal(int)  # 是否结束信号

    def __init__(self, file_path, model_path, label_15):
        super(DetectionThread, self).__init__()
        self.file_path = file_path
        self.model_path = model_path
        self.label_15 = label_15

    def run(self):
        detect.run(source=self.file_path, weights=self.model_path[0], show_label=self.label_15, save_img=True)
        self.signal_done.emit(1)  # 发送结束信号

class CameraDetectionThread(QThread):
    def __init__(self, model_path, label_19):
        super(CameraDetectionThread, self).__init__()
        self.model_path = model_path
        self.label_19 = label_19

    def run(self):
        detect.run(source=0, weights=self.model_path[0], show_label=self.label_19, save_img=False, use_camera=True)


class RecognitionThread(QThread):
    update_text_1 = pyqtSignal(str)

    def __init__(self, label):
        super().__init__()
        self.recording = False
        self.label = label

    def run(self):
        thread1.run(show_label=self.label)








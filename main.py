import sys

import PyQt5.QtCore
import pymysql
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from pymysql.cursors import DictCursor

from GUI.interfaceUi import Ui_MainWindow
from GUI.loginUi import Ui_loginWindow
import hashlib

def getCon():
    # 连接到MySQL数据库
    con = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',  # 数据库用户名
        password='123456',  # 数据库密码
        database='interaction',  # 数据库名称
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return con
def encrypt_password(password):

    # 创建一个md5对象
    md5_obj = hashlib.md5()
    # 更新md5对象以hash密码字符串, 注意这里需要将密码转换为bytes
    md5_obj.update(password.encode('utf-8'))
    # 获取加密后的字符串
    encrypted_password = md5_obj.hexdigest()
    return encrypted_password


class  loginWindow(QMainWindow, Ui_loginWindow):   # 多重继承QMainWindow和Ui_MainWindow

    def __init__(self):
        super(loginWindow, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法
        self.pushButton_login_2.clicked.connect(lambda: self.switch_window())
        self.pushButton_register_5.clicked.connect(lambda: self.save_data())

    def switch_window(self):
        con = None
        try:
            con = getCon()
            username = self.lineEdit_username_1.text()
            password_1 = self.lineEdit_password_2.text()
            password = encrypt_password(password_1)
            if not username or not password:
                QMessageBox.warning(self, "警告", "请输入用户名和密码！")
                return
            with con.cursor() as cursor:
                sql = "SELECT * FROM user WHERE username=%s AND password=%s"
                cursor.execute(sql, (username, password))
                result = cursor.fetchone()

                if result:
                    self.close()
                    b.show()
                else:
                    QMessageBox.warning(self, "警告", "用户名或密码错误！")
        finally:
            # 确保连接关闭
            if con:
                con.close()

    def save_data(self):
        username = self.lineEdit_username_3.text()
        password1 = self.lineEdit_password_4.text()
        password2 = self.lineEdit_password_5.text()
        password = encrypt_password(password1)
        if not username or not password:
            QMessageBox.warning(self, "警告", "请输入用户名和密码！")
            return
        if password2 == password1:
            try:
                self.insert_into_database(username, password)
                QMessageBox.information(self, "注册成功", "数据已保存！")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存数据时发生错误：{str(e)}")
        else:
            QMessageBox.warning(self, "警告", "两次密码输入不一致！")
            return

    def insert_into_database(self, username, password):
        con = None
        try:
            con = getCon()
            with con.cursor() as cursor:
                sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
                cursor.execute(sql, (username, password))
                con.commit()
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存数据时发生错误：{str(e)}")
        finally:
            if con:
                con.close()

class mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.timer_detect = QtCore.QTimer()
        self.file_path = None  # 数据路径
        self.model_path = None  # 模型路径
        self.file_suffix = None  # 文件后缀
        self.result_path = "result"  # 检测图片保存路径
        self.init_file()  # 初始化必要的文件夹
        self.r_main = None





if __name__ == "__main__":
    PyQt5.QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    a = loginWindow()
    b = mainwindow()
    a.show()
    sys.exit(app.exec_())


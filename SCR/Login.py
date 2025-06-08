import json
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget, QLabel,QVBoxLayout,QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("D:/Workspace/Python/PTI06/SPK/UI/login.ui", self)
        self.setWindowTitle("Login")
        self.homeWindow = None
        self.signupWindow = None
        self.accWindow = None
        self.btn_LogIn.clicked.connect(self.xu_ly_dang_nhap)
        self.btn_SignUpnow.clicked.connect(self.vao_trang_dang_ki)


        self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))
        self.password_edit = self.txt_Password
        self.show_password_btn.clicked.connect(self.toggle_password_visibility)

    def xu_ly_dang_nhap(self):
        txtUser = self.txt_Username.text().strip()
        txtPass = self.txt_Password.text().strip()
        
        with open("account.json", "r") as file:
            data = json.load(file)
            
        for item in data["accounts"]:
            if item["username"] == txtUser and item["password"] == txtPass:
                self.toast = SimpleToast("Đăng Nhập Thành Công")
                self.username = item["username"]
                from Home import Home
                if self.homeWindow is None:
                    self.homeWindow = Home(self.username)
                self.homeWindow.show()
                self.hide()
                from ACc import Acc
                self.accWindow = Acc(self.username)
                return

        self.toast = SimpleToast("Sai tên đăng nhập hoặc mật khẩu")

            
    def vao_trang_dang_ki(self):
        from SignUp import SignUp

        if(self.signupWindow) == None:
            self.signupWindow = SignUp()

        self.signupWindow.show()
        self.hide()

    def thongBao(self, TieuDe, NoiDung):
        self.toast = SimpleToast(f"{TieuDe}: {NoiDung}")


    def toggle_password_visibility(self):
        if self.show_password_btn.isChecked():
            self.password_edit.setEchoMode(QLineEdit.Normal)
            self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-open.png"))
        else:
            self.password_edit.setEchoMode(QLineEdit.Password)
            self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))
    

class SimpleToast(QWidget):
    def __init__(self, message, duration=4000):
        super().__init__()
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("""
            QLabel {
                background-color: #333;
                color: white;
                padding: 12px;
                border-radius: 8px;
                font-size: 10pt;
            }
        """)
        label = QLabel(message, self)
        label.adjustSize()
        self.resize(label.width(), label.height())

        screen = QApplication.primaryScreen().availableGeometry()
        x = screen.width() - self.width() - 50
        y = screen.height() - self.height() - 50
        self.move(x, y)
        self.show()
        QTimer.singleShot(duration, self.close)




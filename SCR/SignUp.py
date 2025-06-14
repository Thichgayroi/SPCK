import json
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication, QLabel,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer

class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("D:/Workspace/Python/PTI06/SPK/UI/SignUp.ui", self)
        self.setWindowTitle("SignUp")
        self.loginWindow = None
        self.btn_SignUp.clicked.connect(self.xu_ly_dang_ky)
        self.btn_Loginnow.clicked.connect(self.vao_trang_dang_nhap)

        self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))
        self.show_password_btn2.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))
        self.password_edit1 = self.txtPassword
        self.password_edit2 = self.txtConfirmPassword
        self.show_password_btn.clicked.connect(self.toggle_password_visibility)
        self.show_password_btn2.clicked.connect(self.toggle_password_visibility)


    def xu_ly_dang_ky(self):
        txtUser = self.txtUsername.text().strip()
        txtPass = self.txtPassword.text().strip()
        txtConfirmPass = self.txtConfirmPassword.text().strip()
        
        if txtUser == "" or txtPass == "" or txtConfirmPass == "":
            self.toast = SimpleToast("Vui lòng nhập đầy đủ thông tin")
            return

        if len(txtPass) < 6:
            self.toast = SimpleToast("Mật khẩu phải có ít nhất 6 ký tự")
            return

        with open("account.json", "r") as file:
            data = json.load(file)
        
        for item in data["accounts"]:
            if item["username"] == txtUser:
                self.toast = SimpleToast("Tài khoản đã tồn tại")
                return

        if txtPass != txtConfirmPass:
            self.toast = SimpleToast("Mật khẩu xác nhận không khớp")
            return

        data["accounts"].append(dict(
            username = txtUser,
            password = txtPass,
            darkmode = False,
            notification = True,
            ))
        
        with open("account.json", "w") as file:
            json.dump(data, file, indent=4)
            self.toast = SimpleToast("Đăng ký tài khoản thành công")
            from Login import Login

            if(self.loginWindow) == None:
                self.loginWindow = Login()

            self.loginWindow.show()
            self.hide()
            return

        
    def vao_trang_dang_nhap(self):
        from Login import Login

        if(self.loginWindow) == None:
            self.loginWindow = Login()

        self.loginWindow.show()
        self.hide()

    def thongBao(self, NoiDung):
        self.toast = SimpleToast(f"{NoiDung}")

    def toggle_password_visibility(self):
        if (self.show_password_btn.isChecked()) or (self.show_password_btn2.isChecked()):
            self.password_edit1.setEchoMode(QLineEdit.Normal)
            self.password_edit2.setEchoMode(QLineEdit.Normal)  # Hiện mật khẩu
            self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-open.png"))
            self.show_password_btn2.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-open.png"))
        else:
            self.password_edit1.setEchoMode(QLineEdit.Password)
            self.password_edit2.setEchoMode(QLineEdit.Password)  # Ẩn mật khẩu
            self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))
            self.show_password_btn2.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))

class SimpleToast(QMainWindow):
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
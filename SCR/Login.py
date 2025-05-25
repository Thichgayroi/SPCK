import json
from PyQt5.QtWidgets import QMainWindow, QMessageBox,QVBoxLayout,QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from qtwidgets import AnimatedToggle
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("D:/Workspace/Python/PTI06/SPK/UI/login.ui", self)
        self.setWindowTitle("Login")
        self.homeWindow = None
        self.signupWindow = None
        self.btn_LogIn.clicked.connect(self.xu_ly_dang_nhap)
        self.btn_SignUpnow.clicked.connect(self.vao_trang_dang_ki)

        self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))
        self.password_edit = self.txt_Password
        self.show_password_btn.clicked.connect(self.toggle_password_visibility)

        toggle = AnimatedToggle(checked_color="#536DFE", pulse_checked_color="#C5CAE9")
        toggle.toggled.connect(self.toggle_dark_light_mode)  # Gắn sự kiện
        layout = QVBoxLayout()
        layout.addWidget(toggle)
        self.frame.setLayout(layout)

    def xu_ly_dang_nhap(self):
        txtUser = self.txt_Username.text().strip()
        txtPass = self.txt_Password.text().strip()
        
        with open("account.json", "r") as file:
            data = json.load(file)
            
        for item in data["accounts"]:
            if item["username"] == txtUser and item["password"] == txtPass:
                self.thongBao("Thông báo", "Đăng Nhập Thành công")
                from Home import Home

                if(self.homeWindow) == None:
                    self.homeWindow = Home()

                self.homeWindow.show()
                self.hide()
                return
            
    def vao_trang_dang_ki(self):
        from SignUp import SignUp

        if(self.signupWindow) == None:
            self.signupWindow = SignUp()

        self.signupWindow.show()
        self.hide()

    def thongBao(self,TieuDe,NoiDung):
        message = QMessageBox()
        message.setWindowTitle(TieuDe)
        message.setIcon(QMessageBox.Icon.Information)
        message.setText(NoiDung)
        message.exec()

    def toggle_password_visibility(self):
        if self.show_password_btn.isChecked():
            self.password_edit.setEchoMode(QLineEdit.Normal)
            self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-open.png"))
        else:
            self.password_edit.setEchoMode(QLineEdit.Password)
            self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))
    
    def toggle_dark_light_mode(self, checked):
        if checked:
            # DARK MODE
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #3B3F4E;
                    color: white;
                }
                QPushButton {
                    padding:2px 2px;
                    border: 1px solid #555;
                }
                
                QLabel{
                    color:white;            
                }
            """)

        else:
            # LIGHT MODE
            self.setStyleSheet("""
                QMainWindow {
                    background-color: white;
                    color: black;
                }
                QLineEdit, QPushButton {
                    border: 1px solid #ccc;
                }
            """)



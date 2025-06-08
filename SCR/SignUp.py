import json
from PyQt5.QtWidgets import QMainWindow, QMessageBox,QVBoxLayout,QLineEdit  # Import từ QtWidgets
from PyQt5 import uic #uic để tạo giao diện cửa sổ từ file thiết kế (.ui)
from PyQt5.QtGui import QIcon
from qtwidgets import AnimatedToggle
class SignUp(QMainWindow): #Kế thừa các thuộc tính và phương thức từ QMainWindow
    def __init__(self): #Hàm init tự động chạy khi khởi tạo đối tượng
        super().__init__() #super giúp gọi hàm init của QMainWindow
        uic.loadUi("D:/Workspace/Python/PTI06/SPK/UI/SignUp.ui", self) #Load giao diện từ file
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
        
        if txtUser == "" or txtPass == "":
            self.thongBao("Thông báo", "Vui lòng nhập đầy đủ thông tin")
            return
        
        with open("account.json", "r") as file:
            data = json.load(file)
            
        for item in data["accounts"]:
            if item["username"] == txtUser:
                self.thongBao("Thông báo", "Tài khoản đã tồn tại")
                return
            
        data["accounts"].append(dict(
            username = txtUser,
            password = txtPass,
            darkmode = False,
            notification = True,
            ))
        
        with open("account.json", "w") as file:
            json.dump(data, file, indent=4)
            self.thongBao("Thông báo", "Đăng ký tài khoản thành công")
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

    def thongBao(self,TieuDe,NoiDung):
        message = QMessageBox()
        message.setWindowTitle(TieuDe)
        message.setIcon(QMessageBox.Icon.Information)
        message.setText(NoiDung)
        message.exec()

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
    

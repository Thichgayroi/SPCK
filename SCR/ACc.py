from PyQt5.QtWidgets import QMainWindow, QMessageBox,QLineEdit
from PyQt5 import uic
import json
from PyQt5.QtGui import QIcon
class Acc(QMainWindow): #Kế thừa các thuộc tính và phương thức từ QMainWindow
    def __init__(self,username=None,password=None): #Hàm init tự động chạy khi khởi tạo đối tượng
        super().__init__() #super giúp gọi hàm init của QMainWindow
        uic.loadUi("D:/Workspace/Python/PTI06/SPK/UI/Accounts.ui", self) #Load giao diện từ file
        self.setWindowTitle("Home")
        self.username = username  # Lưu username
        self.password = password  # Lưu password
        if self.username:
            self.cant_change.setText(self.username)  # Gán vào QLineEdit
        if self.password:
            self.cant_change2.setText(self.password)  # Gán vào QLineEdit
        self.btn_ATA.clicked.connect(self.vao_ATA)
        self.btn_LYA.clicked.connect(self.vao_LYA)
        self.btn_settings.clicked.connect(self.vao_SETTING)
        self.btn_logout.clicked.connect(self.dang_xuat)
        self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))
        self.password_edit = self.cant_change2
        self.show_password_btn.clicked.connect(self.toggle_password_visibility)

        self.ataWindow = None
        self.lyaWindow = None
        self.settingWindow = None
        self.loginWindow = None

        self.apply_darkmode()
    def apply_darkmode(self):
        darkmode = False
        if self.username:
            try:
                with open("d:/WorkSpace/Python/PTI06/SPK/account.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                for acc in data["accounts"]:
                    if acc["username"] == self.username:
                        darkmode = acc.get("darkmode", False)
                        break
            except Exception as e:
                print("Lỗi đọc darkmode:", e)


        if darkmode:
            for w in [self.widget_2, self.widget_5, self.widget_6, self.widget_11, self.widget_12,self.widget_8]:
                w.setStyleSheet("")
            for btn in [self.btn_LYA, self.btn_accounts, self.btn_settings, self.btn_ATA,self.lbl_title]:
                btn.setStyleSheet("")
            self.setStyleSheet("")

            self.widget_2.setStyleSheet("""
                background-color: #2b2b2b;
                color: white;
                border-radius: 24px;
                """)
            self.widget_5.setStyleSheet("""
                background-color: #3a3a3a;
                border-radius: 12px;
                """)
            self.widget_12.setStyleSheet("""
                background-color: #3a3a3a;
                border-radius: 12px;
                """)
            self.widget_11.setStyleSheet("""
                background-color: #3a3a3a;
                border-radius: 12px;
                """)
            self.widget_6.setStyleSheet("""
                background-color: #3a3a3a;
                border-radius: 12px;
                """)
            self.widget_8.setStyleSheet("""
                background-color: #2b2b2b;
                border-radius: 12px;
                """)
            self.btn_LYA.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: white;
                    border-radius: 10px;
                    padding: 8px 16px;
                }

                QPushButton:hover {
                    background-color: #505050;
                    border: 1.5px solid #c0c0c0;
                }

                QPushButton:pressed {
                    background-color: #2f2f2f;
                    border: 1.5px solid #a0a0a0;
                }

                """)
            self.btn_accounts.setStyleSheet("""
                QPushButton {
                    background-color: #505050;
                    color: white;
                    border-radius: 10px;
                    padding: 8px 16px;
                }
                """)
            self.btn_settings.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: white;
                    border-radius: 10px;
                    padding: 8px 16px;
                }

                QPushButton:hover {
                    background-color: #505050;
                    border: 1.5px solid #c0c0c0;
                }

                QPushButton:pressed {
                    background-color: #2f2f2f;
                    border: 1.5px solid #a0a0a0;
                }
                """)
            self.btn_ATA.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: white;
                    border-radius: 10px;
                    padding: 8px 16px;
                }

                QPushButton:hover {
                    background-color: #505050;
                    border: 1.5px solid #c0c0c0;
                }

                QPushButton:pressed {
                    background-color: #2f2f2f;
                    border: 1.5px solid #a0a0a0;
                }

                """)
            self.lbl_title.setStyleSheet("""
                    background-color: #2c2c2c;
                    color: white;
                    border-radius: 12px;
            """)
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #1e1e1e;
                    color: #e0e0e0;
                }


                QLabel {
                    color: #cccccc;
                }


                QComboBox {
                    background-color: #2c2c2c;
                    color: #e0e0e0;
                    border: 1px solid #555;
                    padding: 4px;
                }

                QComboBox QAbstractItemView {
                    background-color: #2c2c2c;
                    color: #e0e0e0;
                    selection-background-color: #444;
                }
            """)
        else:
            # StyleSheet lightmode (bạn có thể copy từ Settings)
            self.setStyleSheet("""
                QMainWindow, QWidget {
                    background-color: #f5f5f5;
                    color: #222;
                }
                QLabel {
                    color: #222;
                }
                QPushButton {
                    background-color: #fff;
                    color: #222;
                    border-radius: 10px;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """)

    def vao_ATA(self):
        from ATa import Ata
        if(self.ataWindow) == None:
            self.ataWindow = Ata(self.username,self.password)
        self.ataWindow.show()
        self.hide()

    def vao_LYA(self):
        from LYa import Lya
        if(self.lyaWindow) == None:
            self.lyaWindow = Lya(self.username,self.password)
        self.lyaWindow.show()
        self.hide()

    def vao_SETTING(self):
        from Settings import Setting
        if(self.settingWindow) == None:
            self.settingWindow = Setting(self.username,self.password)
        self.settingWindow.show()
        self.hide()

    def vao_trang_dang_nhap(self):
        from Login import Login

        if(self.loginWindow) == None:
            self.loginWindow = Login()

        self.loginWindow.show()
        self.hide()

    def thongbao(self,TieuDe,NoiDung):
        message = QMessageBox()
        message.setWindowTitle(TieuDe)
        message.setIcon(QMessageBox.Icon.Warning)
        message.setText(NoiDung)
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setDefaultButton(QMessageBox.No)
        
        reply = message.exec()
        if(reply == QMessageBox.Yes):
            self.vao_trang_dang_nhap()

        

    def dang_xuat(self):
        if(self.btn_logout):
            self.thongbao("LogOut","Are you sure?")
            return
    

    def toggle_password_visibility(self):
        if self.show_password_btn.isChecked():
            # Hiện hộp thoại nhập mật khẩu xác thực
            from PyQt5.QtWidgets import QInputDialog
            text, ok = QInputDialog.getText(self, "Xác thực", "Nhập mật khẩu để xem:", QLineEdit.Password)
            if ok and text == self.password:
                self.password_edit.setEchoMode(QLineEdit.Normal)
                self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-open.png"))
            else:
                # Nếu sai mật khẩu hoặc bấm Cancel thì không cho xem, trả lại trạng thái cũ
                self.show_password_btn.setChecked(False)
                self.password_edit.setEchoMode(QLineEdit.Password)
                self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))
        else:
            self.password_edit.setEchoMode(QLineEdit.Password)
            self.show_password_btn.setIcon(QIcon("D:/WorkSpace/Python/PTI06/SPK/IMG/eye-closed.png"))

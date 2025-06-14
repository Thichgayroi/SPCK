import json
from PyQt5.QtWidgets import QMainWindow, QMessageBox,QVBoxLayout,QWidget,QLabel,QApplication
from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from qtwidgets import AnimatedToggle

class Setting(QMainWindow):
    def __init__(self, username=None,password=None):
        super().__init__()
        uic.loadUi("D:/Workspace/Python/PTI06/SPK/UI/Settings.ui", self)
        self.setWindowTitle("Home")
        self.username = username
        self.password = password
        self.btn_ATA.clicked.connect(self.vao_ATA)
        self.btn_LYA.clicked.connect(self.vao_LYA)
        self.btn_accounts.clicked.connect(self.vao_ACC)
        self.btn_apply.clicked.connect(self.save_settings)

        self.ataWindow = None
        self.lyaWindow = None
        self.accWindow = None

        darkmode, notification = self.load_user_settings(self.username)

        self.enable_toast = notification

        self.toggle1 = AnimatedToggle(checked_color="#536DFE", pulse_checked_color="#C5CAE9")
        self.toggle1.setChecked(darkmode)
        self.toggle1.toggled.connect(self.toggle_dark_light_mode)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.toggle1)
        self.frame1.setLayout(layout1)

        self.toggle2 = AnimatedToggle(checked_color="#536DFE", pulse_checked_color="#C5CAE9")
        self.toggle2.setChecked(notification)
        self.toggle2.toggled.connect(self.toggle_notice)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.toggle2)
        self.frame2.setLayout(layout2)

        # Áp dụng darkmode ngay khi vào
        self.toggle_dark_light_mode(darkmode)

    def load_user_settings(self, username):
        with open("d:/WorkSpace/Python/PTI06/SPK/account.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        for acc in data["accounts"]:
            if acc["username"] == username:
                return acc.get("darkmode", False), acc.get("notification", True)
        return False, True  # Mặc định nếu không tìm thấy

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
    
    def vao_ACC(self):
        from ACc import Acc
        if(self.accWindow) == None:
            self.accWindow = Acc(self.username,self.password)
        self.accWindow.show()
        self.hide()

    def toggle_notice(self, checked=False):
        self.enable_toast = checked
        if not checked:
            print("(-)")
        else:
            self.toast = SimpleToast("Notifications: ON", duration=2000)

    def toggle_dark_light_mode(self, checked):
        if self.enable_toast:
            if checked:
                self.toast = SimpleToast("Dark Mode: ON", duration=2000)
            else:
                self.toast = SimpleToast("Dark Mode: OFF", duration=2000)

        if checked:
                # Xóa styleSheet cũ trước khi set mới
            for w in [self.widget_2, self.widget_5, self.widget_6, self.widget_11, self.widget_12,self.widget_8]:
                w.setStyleSheet("")
            for btn in [self.btn_LYA, self.btn_accounts, self.btn_settings, self.btn_ATA,self.lbl_title,self.comboBox]:
                btn.setStyleSheet("")
            self.setStyleSheet("")
            self.widget_2.setStyleSheet("""
                background-color: #2b2b2b;
                color: white;
                border-radius: 24px;
                """)
            self.lbl_title.setStyleSheet("""
                background-color: #2b2b2b;
                color: white;
                border-radius: 12px;
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
            self.btn_settings.setStyleSheet("""
                QPushButton {
                    background-color: #505050;
                    color: white;
                    border-radius: 10px;
                    padding: 8px 16px;
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
            self.comboBox.setStyleSheet("""
                QComboBox {
                    background-color: #2e2e2e;
                    color: #ffffff;
                    border: 1px solid #555555;
                    border-radius: 5px;
                    padding: 5px;
                }

                QComboBox:hover {
                    border: 1px solid #888888;
                }
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
            self.widget_2.setStyleSheet("""
                background-color: #d8e0ea;
                color: black;
                border-radius: 24px;
                """)
            self.lbl_title.setStyleSheet("""
                background-color: #DCEEFF;
                color: black;
                border-radius: 12px;
                """)
            self.widget_5.setStyleSheet("""
                background-color: #EEF3FB;
                border-radius: 18px;
                """)
            self.widget_12.setStyleSheet("""
                background-color: #EEF3FB;
                border-radius: 18px;
                """)
            self.widget_11.setStyleSheet("""
                background-color: #EEF3FB;
                border-radius: 18px;
                """)
            self.widget_6.setStyleSheet("""
                background-color: #EEF3FB;
                border-radius: 18px;
                """)
            self.widget_8.setStyleSheet("""
                background-color: #EDF4FC;
                border-radius: 12px;
                """)
            self.btn_LYA.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #1a1a1a;
                    border-radius: 10px;
                    padding: 8px 16px;
                }

                QPushButton:hover {
                    background-color: #f5f5f5;
                    border: 1.5px solid #c0c0c0;
                }

                QPushButton:pressed {
                    background-color: #e0e0e0;
                    border: 1.5px solid #a0a0a0;
                }
                """)
            self.btn_accounts.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #1a1a1a;
                    border-radius: 10px;
                    padding: 8px 16px;
                }

                QPushButton:hover {
                    background-color: #f5f5f5;
                    border: 1.5px solid #c0c0c0;
                }

                QPushButton:pressed {
                    background-color: #e0e0e0;
                    border: 1.5px solid #a0a0a0;
                }
                """)
            self.btn_settings.setStyleSheet("""
                QPushButton {
                    background-color: #f5f5f5;
                    color: #1a1a1a;
                    border-radius: 10px;
                    padding: 8px 16px;
                    border: 1.5px solid #c0c0c0;
                }


                """)
            self.btn_ATA.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #1a1a1a;
                    border-radius: 10px;
                    padding: 8px 16px;
                }

                QPushButton:hover {
                    background-color: #f5f5f5;
                    border: 1.5px solid #c0c0c0;
                }

                QPushButton:pressed {
                    background-color: #e0e0e0;
                    border: 1.5px solid #a0a0a0;
                }
                """)
            self.comboBox.setStyleSheet("""
                QComboBox {
                    background-color: #ffffff;
                    color: #000000;
                    padding: 5px;
                    border: 1px solid #cccccc;
                    border-radius: 5px;
                }

                QComboBox:hover {
                    border: 1px solid #888888;
                }
                """)
            self.setStyleSheet("""

                QLabel {
                    color: #222222;
                }
            """)


            # Thêm logic để tắt thông báo

    def save_settings(self):
        darkmode = self.toggle1.isChecked()
        notification = self.toggle2.isChecked()
        username = self.username

        if not username:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy tài khoản.")
            return
        with open("d:/WorkSpace/Python/PTI06/SPK/account.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        found = False
        for acc in data["accounts"]:
            if acc["username"] == username:
                acc["darkmode"] = darkmode
                acc["notification"] = notification
                found = True
                break

        if not found:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy tài khoản trong dữ liệu.")
            return
        
        if(self.btn_apply):
            with open("d:/WorkSpace/Python/PTI06/SPK/account.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        QMessageBox.information(self, "Thành công", "Đã lưu cài đặt thành công!")

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



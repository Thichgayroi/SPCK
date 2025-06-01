import json
from PyQt5.QtWidgets import QMainWindow, QMessageBox,QVBoxLayout  # Import từ QtWidgets
from PyQt5 import uic #uic để tạo giao diện cửa sổ từ file thiết kế (.ui)
from qtwidgets import AnimatedToggle
class Setting(QMainWindow): #Kế thừa các thuộc tính và phương thức từ QMainWindow
    def __init__(self): #Hàm init tự động chạy khi khởi tạo đối tượng
        super().__init__() #super giúp gọi hàm init của QMainWindow
        uic.loadUi("D:/Workspace/Python/PTI06/SPK/UI/Settings.ui", self) #Load giao diện từ file
        self.setWindowTitle("Home")
        self.btn_ATA.clicked.connect(self.vao_ATA)
        self.btn_LYA.clicked.connect(self.vao_LYA)
        self.btn_accounts.clicked.connect(self.vao_ACC)

        self.ataWindow = None
        self.lyaWindow = None
        self.accWindow = None

        toggle1 = AnimatedToggle(checked_color="#536DFE", pulse_checked_color="#C5CAE9")
        toggle1.toggled.connect(self.toggle_dark_light_mode)  # Gắn sự kiện
        layout1 = QVBoxLayout()
        layout1.addWidget(toggle1)
        self.frame1.setLayout(layout1)

        toggle2 = AnimatedToggle(checked_color="#536DFE", pulse_checked_color="#C5CAE9")
        toggle2.toggled.connect(self.toggle_dark_light_mode)  # Gắn sự kiện
        layout2 = QVBoxLayout()
        layout2.addWidget(toggle2)
        self.frame2.setLayout(layout2)
    def vao_ATA(self):
        from ATa import Ata
        if(self.ataWindow) == None:
            self.ataWindow = Ata()
        self.ataWindow.show()
        self.hide()

    def vao_LYA(self):
        from LYa import Lya
        if(self.lyaWindow) == None:
            self.lyaWindow = Lya()
        self.lyaWindow.show()
        self.hide()
    
    def vao_ACC(self):
        from ACc import Acc
        if(self.accWindow) == None:
            self.accWindow = Acc()
        self.accWindow.show()
        self.hide()

    def toggle_dark_light_mode(self, checked):
        if checked:
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #3B3F4E;
                    color: white;
                }
                QPushButton {
                    padding: 2px 2px;
                    border: 1px solid #555;
                }
                
                QLabel{
                    color:white;            
                }
            """)

        else:
            self.setStyleSheet("""
                QMainWindow {
                    background-color: white;
                    color: black;
                }
                QLineEdit, QPushButton {
                    border: 1px solid #ccc;
                }
            """)
        # if hasattr(self, "current_user"):  # Đảm bảo có user hiện tại
        #     new_settings = {
        #         "dark_mode": checked,
        #         # Nếu bạn có thêm toggle hoặc combo box thì thêm vào đây
        #         "notifications": True,  # giả sử luôn bật
        #         "region": "VN"  # giả sử mặc định VN
        #     }
        #     self.cap_nhat_settings(self.current_user, new_settings)
    
    # def cap_nhat_settings(self, username, new_settings):
    #     with open("account.json", "r") as file:
    #         data = json.load(file)

    #     for account in data["accounts"]:
    #         if account["username"] == username:
    #             account["settings"] = new_settings
    #             break

    #     with open("account.json", "w") as file:
    #         json.dump(data, file, indent=4)


    # def tai_settings(self, username):
    #     with open("account.json", "r") as file:
    #         data = json.load(file)

    #     for account in data["accounts"]:
    #         if account["username"] == username:
    #             return account.get("settings", {})
    #     return {}
    




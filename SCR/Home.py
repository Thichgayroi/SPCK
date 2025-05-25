from PyQt5.QtWidgets import QMainWindow, QMessageBox,QVBoxLayout  # Import từ QtWidgets
from PyQt5 import uic #uic để tạo giao diện cửa sổ từ file thiết kế (.ui)
class Home(QMainWindow): #Kế thừa các thuộc tính và phương thức từ QMainWindow
    def __init__(self): #Hàm init tự động chạy khi khởi tạo đối tượng
        super().__init__() #super giúp gọi hàm init của QMainWindow
        uic.loadUi("D:/Workspace/Python/PTI06/SPK/UI/Home.ui", self) #Load giao diện từ file
        self.setWindowTitle("Home")
        self.btn_ATA.clicked.connect(self.vao_ATA)
        self.btn_LYA.clicked.connect(self.vao_LYA)
        self.btn_accounts.clicked.connect(self.vao_ACC)
        # self.btn_settings.clicked.connect(self.vao_SETTING)
        self.ataWindow = None
        self.lyaWindow = None
        self.accWindow = None
        # self.settingWindow = None
        
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
    
    # def vao_SETTING(self):
    #     from ATa import Ata
    #     if(self.ataWindow) == None:
    #         self.ataWindow = Ata()
    #     self.ataWindow.show()
    #     self.hide()
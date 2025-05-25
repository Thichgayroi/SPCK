import sys
from PyQt5.QtWidgets import QApplication
from SignUp import SignUp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignUp()
    window.show()
    app.exec()



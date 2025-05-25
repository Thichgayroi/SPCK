import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QPushButton, QListWidget, QFileDialog, QMessageBox, QInputDialog,QListWidgetItem
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic

class AppManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản Lý Ứng Dụng")
        self.setGeometry(300, 300, 400, 400)
        uic.loadUi("D:/Workspace/Python/PTI06/SPK/UI/ListApp.ui",self)

        self.add_button.clicked.connect(self.add_app)

        self.delete_button.clicked.connect(self.delete_app)

        self.open_button.clicked.connect(self.open_app)

        self.group_button.clicked.connect(self.create_group)

        self.list_widget.model().rowsMoved.connect(self.update_indentation)

        self.current_group_index = None

    def add_app(self):
        file_dialog = QFileDialog()
        app_path, _ = file_dialog.getOpenFileName(self, "Chọn Ứng Dụng")
        if app_path:
            selected_row = self.list_widget.currentRow()
            item = QListWidgetItem(f"{app_path}")

            # Nếu đang chọn group thì chèn vào sau group đó
            if selected_row != -1:
                selected_item = self.list_widget.item(selected_row)
                if selected_item.text().startswith("---"):
                    insert_row = selected_row + 1
                    while insert_row < self.list_widget.count():
                        if self.list_widget.item(insert_row).text().startswith("---"):
                            break
                        insert_row += 1
                    item.setText(f"    {app_path}")
                    self.list_widget.insertItem(insert_row, item)
                    return

            # Không có group thì thêm vào cuối
            self.list_widget.addItem(item)


    def delete_app(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "Thông Báo", "Chọn ứng dụng để xóa.")
            return
        for item in selected_items:
            row = self.list_widget.row(item)
            self.list_widget.takeItem(row)
            if row == self.current_group_index:
                self.current_group_index = None

    def open_app(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "Thông Báo", "Chọn ứng dụng để mở.")
            return
        app_path = selected_items[0].text().strip()
        if app_path.startswith("---"):
            QMessageBox.information(self, "Thông Báo", "Không thể mở group.")
            return
        try:
            os.startfile(app_path.strip())
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể mở ứng dụng:\n{e}")

    def create_group(self):
        text, ok = QInputDialog.getText(self, "Tạo Group", "Nhập tên group:")
        if ok and text:
            item_text = f"--- {text.upper()} ---"
            item = QListWidgetItem(item_text)
            item.setFont(QFont("Arial", weight=QFont.Bold))
            item.setBackground(QColor("lightgray"))
            item.setTextAlignment(Qt.AlignCenter)
            self.list_widget.addItem(item)
            self.current_group_index = self.list_widget.count() - 1
            self.list_widget.setCurrentRow(self.current_group_index)

    def update_indentation(self):
        current_group = None
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            text = item.text().strip()
            if text.startswith("---"):
                current_group = item
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("Arial", weight=QFont.Bold))
                item.setBackground(QColor("lightgray"))
            else:
                # Nếu có group phía trên => thụt vào
                if current_group:
                    item.setText(f"    {text.strip()}")
                else:
                    item.setText(text.strip())  # không thụt


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = AppManager()
#     window.show()
#     sys.exit(app.exec_())

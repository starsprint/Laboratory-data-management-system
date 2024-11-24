from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QMessageBox, QWidget, QInputDialog, QSizePolicy
from function.functions import query_readers, query_reader, add_reader, edit_reader, delete_reader
from functools import partial
class ReaderInfoUI(QDialog):
    def __init__(self, user_role):
        super().__init__()
        self.user_role = user_role
        self.setWindowTitle("读者信息")
        self.setGeometry(100, 100, 800, 600)

        # Layout
        main_layout = QVBoxLayout()

        # Top layout for admin buttons
        top_layout = QHBoxLayout()
        
        # Admin buttons
        if user_role == 'admin':
            self.reader_count_label = QLabel("读者数量: ")
            top_layout.addWidget(self.reader_count_label)

            find_reader_btn = QPushButton("查找读者")
            add_reader_btn = QPushButton("添加读者")
            find_reader_btn.clicked.connect(self.find_reader)
            add_reader_btn.clicked.connect(self.add_reader)
            top_layout.addWidget(find_reader_btn)
            top_layout.addWidget(add_reader_btn)

        main_layout.addLayout(top_layout)

        # Table to display reader information
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Columns: Name, Email, Phone, Actions
        self.table.setHorizontalHeaderLabels(["Name", "Email", "Phone", "Actions"])
        main_layout.addWidget(self.table)

        # Load reader data
        self.load_reader_data()

        # Close button
        close_btn = QPushButton("返回")
        close_btn.clicked.connect(self.close)
        main_layout.addWidget(close_btn)

        self.setLayout(main_layout)

    def load_reader_data(self):
        readers = query_readers()  # Fetch reader data
        self.table.setRowCount(len(readers))
        
        if self.user_role == 'admin':
            self.reader_count_label.setText(f"读者数量: {len(readers)}")
        
        for row, reader in enumerate(readers):
            self.table.setItem(row, 0, QTableWidgetItem(reader[0]))  # Name
            self.table.setItem(row, 1, QTableWidgetItem(reader[1]))  # Email
            self.table.setItem(row, 2, QTableWidgetItem(reader[2]))  # Phone

            # Actions based on user role
            if self.user_role == 'admin':
                action_layout = QHBoxLayout()
                edit_btn = QPushButton("编辑")
                delete_btn = QPushButton("删除")
                
                # Set minimum size for buttons
                edit_btn.setMinimumSize(20, 20)
                delete_btn.setMinimumSize(20, 20)
                
                # Set size policy to allow expansion
                edit_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                delete_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                
                # Use partial to bind the row index to the button click handlers
                edit_btn.clicked.connect(partial(self.edit_reader, row))
                delete_btn.clicked.connect(partial(self.delete_reader, row))
                action_layout.addWidget(edit_btn)
                action_layout.addWidget(delete_btn)

                action_widget = QWidget()
                action_widget.setLayout(action_layout)
                self.table.setCellWidget(row, 3, action_widget)

    def find_reader(self):
        name, ok = QInputDialog.getText(self, "查找读者", "输入读者姓名:")
        if ok and name:
            reader = query_reader(name)
            if reader:
                QMessageBox.information(self, "读者信息", f"Name: {reader[0]}\nEmail: {reader[1]}\nPhone: {reader[2]}")
            else:
                QMessageBox.warning(self, "查找失败", "未找到该读者。")

    def add_reader(self):
        # Example logic to add a reader
        name, ok = QInputDialog.getText(self, "添加读者", "输入姓名:")
        if ok and name:
            email, ok = QInputDialog.getText(self, "添加读者", "输入邮箱:")
            if ok and email:
                phone, ok = QInputDialog.getText(self, "添加读者", "输入电话:")
                if ok and phone:
                    add_reader(name, email, phone)
                    self.load_reader_data()  # Refresh the table

    def edit_reader(self, row):
        # Example logic to edit a reader
        name = self.table.item(row, 0).text()
        email, ok = QInputDialog.getText(self, "编辑读者", "输入新邮箱:", text=self.table.item(row, 1).text())
        if ok:
            phone, ok = QInputDialog.getText(self, "编辑读者", "输入新电话:", text=self.table.item(row, 2).text())
            if ok:
                edit_reader(name, email, phone)
                self.load_reader_data()  # Refresh the table

    def delete_reader(self, row):
        name = self.table.item(row, 0).text()
        delete_reader(name)
        self.load_reader_data()  # Refresh the table
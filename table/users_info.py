from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from database.queries import query_users  

class UserInfoUI(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用户信息")
        self.setGeometry(100, 100, 600, 400)

        # Layout
        layout = QVBoxLayout()

        # Table to display user information
        self.table = QTableWidget()
        self.table.setColumnCount(3)  # Assuming 3 columns: ID, Name, Email
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Email"])
        layout.addWidget(self.table)

        # Close button
        close_btn = QPushButton("关闭")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)
        self.load_user_data()

    def load_user_data(self):
        users = query_users()  # Fetch user data
        self.table.setRowCount(len(users))
        for row, user in enumerate(users):
            self.table.setItem(row, 0, QTableWidgetItem(str(user[0])))
            self.table.setItem(row, 1, QTableWidgetItem(user[1]))
            self.table.setItem(row, 2, QTableWidgetItem(user[2]))
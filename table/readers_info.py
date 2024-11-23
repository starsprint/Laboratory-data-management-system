from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from database.queries import query_readers  

class ReaderInfoUI(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("读者信息")
        self.setGeometry(100, 100, 600, 400)

        # Layout
        layout = QVBoxLayout()

        # Table to display reader information
        self.table = QTableWidget()
        self.table.setColumnCount(3)  # Assuming 3 columns: ID, Name, Email
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Email"])
        layout.addWidget(self.table)

        # Close button
        close_btn = QPushButton("关闭")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)
        self.load_reader_data()

    def load_reader_data(self):
        readers = query_readers()  # Fetch reader data
        self.table.setRowCount(len(readers))
        for row, reader in enumerate(readers):
            self.table.setItem(row, 0, QTableWidgetItem(str(reader[0])))
            self.table.setItem(row, 1, QTableWidgetItem(reader[1]))
            self.table.setItem(row, 2, QTableWidgetItem(reader[2]))
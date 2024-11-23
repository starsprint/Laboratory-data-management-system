from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from database.queries import query_theses  

class ThesisInfoUI(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("论文信息")
        self.setGeometry(100, 100, 600, 400)

        # Layout
        layout = QVBoxLayout()

        # Table to display thesis information
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Assuming 4 columns: ID, Title, Author, DOI
        self.table.setHorizontalHeaderLabels(["ID", "Title", "Author", "DOI"])
        layout.addWidget(self.table)

        # Close button
        close_btn = QPushButton("关闭")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)
        self.load_thesis_data()

    def load_thesis_data(self):
        theses = query_theses()  # Fetch thesis data
        self.table.setRowCount(len(theses))
        for row, thesis in enumerate(theses):
            self.table.setItem(row, 0, QTableWidgetItem(str(thesis[0])))
            self.table.setItem(row, 1, QTableWidgetItem(thesis[1]))
            self.table.setItem(row, 2, QTableWidgetItem(thesis[2]))
            self.table.setItem(row, 3, QTableWidgetItem(thesis[3]))
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from database.queries import query_books  

class BookInfoUI(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图书信息")
        self.setGeometry(100, 100, 800, 400)  # Adjusted width for more columns

        # Layout
        layout = QVBoxLayout()

        # Table to display book information
        self.table = QTableWidget()
        self.table.setColumnCount(6)  # Assuming 6 columns: ID, Title, Author, Publisher, Date, Stock
        self.table.setHorizontalHeaderLabels(["ID", "Title", "Author", "Publisher", "Date", "Stock"])
        layout.addWidget(self.table)

        # Close button
        close_btn = QPushButton("关闭")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)
        self.load_book_data()

    def load_book_data(self):
        books = query_books()  # Fetch book data
        self.table.setRowCount(len(books))
        for row, book in enumerate(books):
            self.table.setItem(row, 0, QTableWidgetItem(str(book[0])))
            self.table.setItem(row, 1, QTableWidgetItem(book[1]))
            self.table.setItem(row, 2, QTableWidgetItem(book[2]))
            self.table.setItem(row, 3, QTableWidgetItem(book[3]))
            
            # Convert the date to a string format
            date_str = book[4].strftime('%Y-%m-%d') if book[4] else ''
            self.table.setItem(row, 4, QTableWidgetItem(date_str))
            
            self.table.setItem(row, 5, QTableWidgetItem(str(book[5])))
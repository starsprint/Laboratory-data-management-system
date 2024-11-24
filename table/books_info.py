from datetime import datetime
from functools import partial
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QMessageBox, QWidget, QInputDialog, QSizePolicy
from function.functions import query_books, query_book, add_book, edit_book, delete_book, borrow_book, return_book, get_book_statistics

class BookInfoUI(QDialog):
    def __init__(self, user_role):
        super().__init__()
        self.user_role = user_role
        self.setWindowTitle("图书信息")
        self.setGeometry(100, 100, 1000, 600)

        # Layout
        main_layout = QVBoxLayout()

        # Top layout for buttons
        top_layout = QHBoxLayout()
        
        # Common buttons for reader and admin
        if user_role == 'reader' or user_role == 'admin':
            find_book_btn = QPushButton("查找图书")
            find_book_btn.clicked.connect(self.find_book)
            top_layout.addWidget(find_book_btn)

        # Additional buttons for readers
        if user_role == 'reader':
            borrow_btn = QPushButton("借阅")
            return_btn = QPushButton("归还")
            borrow_btn.clicked.connect(lambda: self.borrow_book(self.table.currentRow()))
            return_btn.clicked.connect(lambda: self.return_book(self.table.currentRow()))
            top_layout.addWidget(borrow_btn)
            top_layout.addWidget(return_btn)

        # Additional buttons for admins
        if user_role == 'admin':
            add_book_btn = QPushButton("添加图书")
            add_book_btn.clicked.connect(self.add_book)
            top_layout.addWidget(add_book_btn)

        main_layout.addLayout(top_layout)

        # Table to display book information
        self.table = QTableWidget()
        self.table.setColumnCount(6)  # Columns: Title, Author, Publisher, Date, Stock, Actions
        self.table.setHorizontalHeaderLabels(["Title", "Author", "Publisher", "Date", "Stock", "Actions"])
        main_layout.addWidget(self.table)

        # Load book data
        self.load_book_data()

        # Close button
        close_btn = QPushButton("返回")
        close_btn.clicked.connect(self.close)
        main_layout.addWidget(close_btn)

        self.setLayout(main_layout)

    def load_book_data(self):
        try:
            books = query_books() or []  # Fetch book data, default to empty list if None
            self.table.setRowCount(len(books))
            
            for row, book in enumerate(books):
                self.table.setItem(row, 0, QTableWidgetItem(book[0]))  # Title
                self.table.setItem(row, 1, QTableWidgetItem(book[1]))  # Author
                self.table.setItem(row, 2, QTableWidgetItem(book[2]))  # Publisher
                
                # Convert the date to a string format
                date_str = book[3].strftime('%Y-%m-%d') if book[3] else ''
                self.table.setItem(row, 3, QTableWidgetItem(date_str))
                
                self.table.setItem(row, 4, QTableWidgetItem(str(book[4])))  # Stock

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
                    edit_btn.clicked.connect(partial(self.edit_book, row))
                    delete_btn.clicked.connect(partial(self.delete_book, row))
                    action_layout.addWidget(edit_btn)
                    action_layout.addWidget(delete_btn)

                    action_widget = QWidget()
                    action_widget.setLayout(action_layout)
                    self.table.setCellWidget(row, 5, action_widget)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"加载图书数据时出错: {e}")

    def find_book(self):
        title, ok = QInputDialog.getText(self, "查找图书", "输入书名:")
        if ok and title:
            book = query_book(title)
            if book:
                QMessageBox.information(self, "图书信息", f"Title: {book[0]}\nAuthor: {book[1]}\nPublisher: {book[2]}\nDate: {book[3]}\nStock: {book[4]}")
            else:
                QMessageBox.warning(self, "查找失败", "未找到该图书。")

    def add_book(self):
        # Example logic to add a book
        title, ok = QInputDialog.getText(self, "添加图书", "输入书名:")
        if ok and title:
            author, ok = QInputDialog.getText(self, "添加图书", "输入作者:")
            if ok and author:
                publisher, ok = QInputDialog.getText(self, "添加图书", "输入出版社:")
                if ok and publisher:
                    publication_date, ok = QInputDialog.getText(self, "添加图书", "输入出版日期 (YYYY-MM-DD):")
                    if ok:
                        try:
                            # Validate and format the date
                            publication_date = datetime.strptime(publication_date, '%Y-%m-%d').date()
                        except ValueError:
                            QMessageBox.warning(self, "日期错误", "请输入有效的日期格式 (YYYY-MM-DD)。")
                            return
                        
                        stock, ok = QInputDialog.getInt(self, "添加图书", "输入库存数量:")
                        if ok:
                            try:
                                add_book(title, author, publisher, publication_date, stock)
                                self.load_book_data()  # Refresh the table
                            except Exception as e:
                                QMessageBox.critical(self, "错误", f"添加图书时出错: {e}")

    def edit_book(self, row):
        # Example logic to edit a book
        title = self.table.item(row, 0).text()
        author, ok = QInputDialog.getText(self, "编辑图书", "输入新作者:", text=self.table.item(row, 1).text())
        if ok:
            publisher, ok = QInputDialog.getText(self, "编辑图书", "输入新出版社:", text=self.table.item(row, 2).text())
            if ok:
                publication_date, ok = QInputDialog.getText(self, "编辑图书", "输入新出版日期 (YYYY-MM-DD):", text=self.table.item(row, 3).text())
                if ok:
                    stock, ok = QInputDialog.getInt(self, "编辑图书", "输入新库存数量:", value=int(self.table.item(row, 4).text()))
                    if ok:
                        edit_book(title, author, publisher, publication_date, stock)
                        self.load_book_data()  # Refresh the table

    def delete_book(self, row):
        title = self.table.item(row, 0).text()
        delete_book(title)
        self.load_book_data()  # Refresh the table

    def borrow_book(self, row):
        try:
            # Check if the row is valid
            if row < 0 or row >= self.table.rowCount():
                QMessageBox.warning(self, "错误", "请选择有效的图书。")
                return

            reader_name, ok = QInputDialog.getText(self, "借阅图书", "输入读者姓名:")
            if ok and reader_name:
                book_title_item = self.table.item(row, 0)
                if book_title_item is None:
                    QMessageBox.critical(self, "错误", "无法获取图书信息。")
                    return

                book_title = book_title_item.text()
                borrow_book(reader_name, book_title)  # Call the function from functions.py
                self.load_book_data()  # Refresh the table
                QMessageBox.information(self, "成功", f"图书 '{book_title}' 已成功借阅。")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"借阅图书时出错: {e}")

    def return_book(self, row):
        try:
            # Check if the row is valid
            if row < 0 or row >= self.table.rowCount():
                QMessageBox.warning(self, "错误", "请选择有效的图书。")
                return

            reader_name, ok = QInputDialog.getText(self, "归还图书", "输入读者姓名:")
            if ok and reader_name:
                book_title_item = self.table.item(row, 0)
                if book_title_item is None:
                    QMessageBox.critical(self, "错误", "无法获取图书信息。")
                    return

                book_title = book_title_item.text()
                return_book(reader_name, book_title)  # Call the function from functions.py
                self.load_book_data()  # Refresh the table
                QMessageBox.information(self, "成功", f"图书 '{book_title}' 已成功归还。")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"归还图书时出错: {e}")
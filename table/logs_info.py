from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QMessageBox, QWidget, QInputDialog
from function.functions import query_logs, query_log, delete_log

class LogInfoUI(QDialog):
    def __init__(self, user_role):
        super().__init__()
        self.user_role = user_role
        self.setWindowTitle("日志管理")
        self.setGeometry(100, 100, 1000, 600)

        # Layout
        main_layout = QVBoxLayout()

        # Top layout for search functionality
        top_layout = QHBoxLayout()
        
        # Search button
        search_btn = QPushButton("查询日志")
        search_btn.clicked.connect(self.search_log)
        top_layout.addWidget(search_btn)

        main_layout.addLayout(top_layout)

        # Table to display log information
        self.table = QTableWidget()
        self.table.setColumnCount(3)  # Columns: Reader Name, Book Title, Time
        self.table.setHorizontalHeaderLabels(["Reader Name", "Book Title", "Time", "Actions"])
        main_layout.addWidget(self.table)

        # Load all logs initially
        self.load_logs()

        # Close button
        close_btn = QPushButton("返回")
        close_btn.clicked.connect(self.close)
        main_layout.addWidget(close_btn)

        self.setLayout(main_layout)

    def load_logs(self):
        """Load all logs into the table."""
        logs = query_logs()
        self.table.setRowCount(len(logs))
        
        for row, log in enumerate(logs):
            self.table.setItem(row, 0, QTableWidgetItem(log[0]))  # Reader Name
            self.table.setItem(row, 1, QTableWidgetItem(log[1]))  # Book Title
            self.table.setItem(row, 2, QTableWidgetItem(log[2].strftime('%Y-%m-%d %H:%M:%S')))  # Time

            # Add delete button for each log
            delete_btn = QPushButton("删除")
            delete_btn.clicked.connect(lambda _, r=row: self.delete_log(r))
            self.table.setCellWidget(row, 3, delete_btn)

    def search_log(self):
        """Search for a specific log based on reader name and book title using a message box."""
        search_text, ok = QInputDialog.getText(self, "查询日志", "输入读者姓名和书名 (格式: 读者姓名, 书名):")
        if ok and search_text:
            try:
                reader_name, book_title = map(str.strip, search_text.split(','))
                log = query_log(reader_name, book_title)
                if log:
                    QMessageBox.information(self, "日志信息", f"Reader Name: {log[0]}\nBook Title: {log[1]}\nTime: {log[2].strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    QMessageBox.warning(self, "查找失败", "未找到该日志。")
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入格式为 '读者姓名, 书名' 的查询条件")

    def delete_log(self, row):
        """Delete a log entry."""
        reader_name = self.table.item(row, 0).text()
        book_title = self.table.item(row, 1).text()
        delete_log(reader_name, book_title)
        self.load_logs()  # Refresh the table

from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from table.books_info import BookInfoUI
from table.theses_info import ThesisInfoUI
from table.readers_info import ReaderInfoUI
from table.logs_info import LogInfoUI

class AdminUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("管理员操作界面")
        self.setGeometry(100, 100, 800, 600)

        # Create buttons
        manage_books_btn = QPushButton("管理图书")
        manage_theses_btn = QPushButton("管理论文")
        manage_readers_btn = QPushButton("管理读者")
        manage_logs_btn = QPushButton("管理日志")
        return_btn = QPushButton("返回")

        # Enlarge buttons
        button_style = """
            QPushButton {
                font-size: 18px;
                padding: 15px;
                margin: 10px;
                border-radius: 8px;
                background-color: #4CAF50;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        manage_books_btn.setStyleSheet(button_style)
        manage_theses_btn.setStyleSheet(button_style)
        manage_readers_btn.setStyleSheet(button_style)
        manage_logs_btn.setStyleSheet(button_style)
        return_btn.setStyleSheet(button_style)

        # Connect buttons to their respective actions
        manage_books_btn.clicked.connect(self.open_books_info)
        manage_theses_btn.clicked.connect(self.open_theses_info)
        manage_readers_btn.clicked.connect(self.open_readers_info)
        manage_logs_btn.clicked.connect(self.open_logs_info)
        return_btn.clicked.connect(self.close)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(manage_books_btn)
        layout.addWidget(manage_theses_btn)
        layout.addWidget(manage_readers_btn)
        layout.addWidget(manage_logs_btn)
        layout.addWidget(return_btn)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_books_info(self):
        """Open the book management interface."""
        book_info_dialog = BookInfoUI(user_role='admin')
        book_info_dialog.exec()

    def open_theses_info(self):
        """Open the thesis management interface."""
        thesis_info_dialog = ThesisInfoUI(user_role='admin')
        thesis_info_dialog.exec()

    def open_readers_info(self):
        """Open the reader management interface."""
        reader_info_dialog = ReaderInfoUI(user_role='admin')
        reader_info_dialog.exec()

    def open_logs_info(self):
        """Open the log management interface."""
        log_info_dialog = LogInfoUI(user_role='admin')
        log_info_dialog.exec()
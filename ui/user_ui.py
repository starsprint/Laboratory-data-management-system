from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from table.books_info import BookInfoUI
from table.theses_info import ThesisInfoUI

class UserUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用户操作界面")
        self.setGeometry(100, 100, 800, 600)

        # Create buttons
        view_books_btn = QPushButton("查看图书")
        view_theses_btn = QPushButton("查看论文")
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
        view_books_btn.setStyleSheet(button_style)
        view_theses_btn.setStyleSheet(button_style)
        return_btn.setStyleSheet(button_style)

        # Connect buttons to their respective actions
        view_books_btn.clicked.connect(self.open_books_info)
        view_theses_btn.clicked.connect(self.open_theses_info)
        return_btn.clicked.connect(self.close)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(view_books_btn)
        layout.addWidget(view_theses_btn)
        layout.addWidget(return_btn)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_books_info(self):
        """Open the book viewing interface for users."""
        book_info_dialog = BookInfoUI(user_role='reader')
        book_info_dialog.exec()

    def open_theses_info(self):
        """Open the thesis viewing interface for users."""
        thesis_info_dialog = ThesisInfoUI(user_role='reader')
        thesis_info_dialog.exec()
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from table.books_info import BookInfoUI
from table.theses_info import ThesisInfoUI

class GuestUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("游客操作界面")
        self.setGeometry(100, 100, 800, 600)

        # Create buttons
        browse_books_btn = QPushButton("浏览公开图书")
        browse_theses_btn = QPushButton("浏览公开论文")
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
        browse_books_btn.setStyleSheet(button_style)
        browse_theses_btn.setStyleSheet(button_style)
        return_btn.setStyleSheet(button_style)

        # Connect buttons to their respective actions
        browse_books_btn.clicked.connect(self.open_books_info)
        browse_theses_btn.clicked.connect(self.open_theses_info)
        return_btn.clicked.connect(self.close)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(browse_books_btn)
        layout.addWidget(browse_theses_btn)
        layout.addWidget(return_btn)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_books_info(self):
        """Open the book browsing interface for guests."""
        book_info_dialog = BookInfoUI(user_role='guest')
        book_info_dialog.exec()

    def open_theses_info(self):
        """Open the thesis browsing interface for guests."""
        thesis_info_dialog = ThesisInfoUI(user_role='guest')
        thesis_info_dialog.exec()

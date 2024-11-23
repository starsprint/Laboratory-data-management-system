from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QLabel, QListWidget, QDialog, QHBoxLayout
from PySide6.QtGui import QFont
from table.books_info import BookInfoUI  
from table.theses_info import ThesisInfoUI  

class GuestUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("游客操作界面")
        self.setGeometry(100, 100, 600, 400)

        # Set font for buttons
        button_font = QFont("Arial", 12)

        # 功能按钮
        browse_books_btn = QPushButton("浏览图书")
        browse_theses_btn = QPushButton("浏览论文")
        back_btn = QPushButton("返回")

        # Apply font to buttons
        for btn in [browse_books_btn, browse_theses_btn, back_btn]:
            btn.setFont(button_font)
            btn.setFixedHeight(40)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(browse_books_btn)
        layout.addWidget(browse_theses_btn)

        # Add return button at the bottom
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(back_btn)
        layout.addLayout(button_layout)

        # 事件绑定
        browse_books_btn.clicked.connect(self.browse_books_action)
        browse_theses_btn.clicked.connect(self.browse_theses_action)
        back_btn.clicked.connect(self.close)

        # 设置主窗口
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def browse_books_action(self):
        # Open the book information dialog
        book_info_dialog = BookInfoUI()
        book_info_dialog.exec()  # Use exec to open the dialog modally

    def browse_theses_action(self):
        # Open the thesis information dialog
        thesis_info_dialog = ThesisInfoUI()
        thesis_info_dialog.exec()  # Use exec to open the dialog modally

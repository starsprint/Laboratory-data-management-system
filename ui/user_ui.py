from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog, QHBoxLayout
from PySide6.QtGui import QFont
from database.queries import upload_thesis, borrow_book, return_book, user_exists
from table.books_info import BookInfoUI  # Import the BookInfoUI class
from table.theses_info import ThesisInfoUI  # Import the ThesisInfoUI class

class UserUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("一般用户操作界面")
        self.setGeometry(100, 100, 600, 400)

        # 设置字体
        font = QFont("Arial", 12)

        # 功能按钮
        upload_thesis_btn = QPushButton("上传论文")
        borrow_book_btn = QPushButton("借阅图书")
        return_book_btn = QPushButton("归还图书")
        query_books_btn = QPushButton("查询图书")
        query_theses_btn = QPushButton("查询论文")
        download_thesis_btn = QPushButton("下载论文")
        back_btn = QPushButton("返回")

        # 设置按钮字体
        for btn in [upload_thesis_btn, borrow_book_btn, return_book_btn, query_books_btn, query_theses_btn, download_thesis_btn, back_btn]:
            btn.setFont(font)
            btn.setFixedHeight(40)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(upload_thesis_btn)
        layout.addWidget(borrow_book_btn)
        layout.addWidget(return_book_btn)
        layout.addWidget(query_books_btn)
        layout.addWidget(query_theses_btn)
        layout.addWidget(download_thesis_btn)

        # 添加返回按钮
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(back_btn)
        layout.addLayout(button_layout)

        # 事件绑定
        upload_thesis_btn.clicked.connect(self.upload_thesis_action)
        borrow_book_btn.clicked.connect(self.borrow_book_action)
        return_book_btn.clicked.connect(self.return_book_action)
        query_books_btn.clicked.connect(self.query_books_action)
        query_theses_btn.clicked.connect(self.query_theses_action)
        download_thesis_btn.clicked.connect(self.download_thesis_action)
        back_btn.clicked.connect(self.close)

        # 设置主窗口
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def upload_thesis_action(self):
        title = self.get_input("请输入论文标题")
        author = self.get_input("请输入作者")
        doi = self.get_input("请输入DOI")
        if title and author and doi:
            upload_thesis(title, author, doi)
            QMessageBox.information(self, "操作完成", "论文上传完成")
        else:
            QMessageBox.warning(self, "输入错误", "请填写所有必填项")

    def borrow_book_action(self):
        user_id = self.get_input("请输入用户ID")
        book_id = self.get_input("请输入图书ID")
        if user_id and book_id:
            if not user_exists(user_id):
                QMessageBox.warning(self, "错误", f"用户ID {user_id} 不存在。")
                return
            borrow_book(user_id, book_id)
            QMessageBox.information(self, "操作完成", "借阅图书完成")
        else:
            QMessageBox.warning(self, "输入错误", "请填写所有必填项")

    def return_book_action(self):
        user_id = self.get_input("请输入用户ID")
        book_id = self.get_input("请输入图书ID")
        if user_id and book_id:
            if not user_exists(user_id):
                QMessageBox.warning(self, "错误", f"用户ID {user_id} 不存在。")
                return
            return_book(user_id, book_id)
            QMessageBox.information(self, "操作完成", "归还图书完成")
        else:
            QMessageBox.warning(self, "输入错误", "请填写所有必填项")

    def query_books_action(self):
        # Open the book information dialog
        book_info_dialog = BookInfoUI()
        book_info_dialog.exec()  # Use exec to open the dialog modally

    def query_theses_action(self):
        # Open the thesis information dialog
        thesis_info_dialog = ThesisInfoUI()
        thesis_info_dialog.exec()  # Use exec to open the dialog modally

    def download_thesis_action(self):
        thesis_id = self.get_input("请输入论文ID")
        if thesis_id:
            # Implement download logic here
            QMessageBox.information(self, "操作完成", "论文下载完成")
        else:
            QMessageBox.warning(self, "输入错误", "请填写所有必填项")

    def get_input(self, prompt):
        text, ok = QInputDialog.getText(self, "输入", prompt)
        if ok and text:
            return text
        return None
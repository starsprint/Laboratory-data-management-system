from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QInputDialog, QMessageBox, QHBoxLayout
from PySide6.QtGui import QFont
from database.queries import (
    add_book, edit_book, delete_book, add_thesis, edit_thesis, delete_thesis,
    add_reader, edit_reader, delete_reader, delete_log, query_logs, get_statistics
)
from table.readers_info import ReaderInfoUI
from table.theses_info import ThesisInfoUI
from table.books_info import BookInfoUI  

class AdminUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("管理员操作界面")
        self.setGeometry(100, 100, 600, 400)

        # Set font for buttons
        button_font = QFont("Arial", 10, QFont.Bold)

        # 功能按钮
        add_book_btn = QPushButton("添加图书")
        edit_book_btn = QPushButton("编辑图书")
        query_book_btn = QPushButton("查询图书")
        delete_book_btn = QPushButton("删除图书")
        add_thesis_btn = QPushButton("添加论文")
        edit_thesis_btn = QPushButton("编辑论文")
        query_thesis_btn = QPushButton("查询论文")
        delete_thesis_btn = QPushButton("删除论文")
        add_reader_btn = QPushButton("添加读者")
        edit_reader_btn = QPushButton("编辑读者")
        query_reader_btn = QPushButton("查询读者")
        delete_reader_btn = QPushButton("删除读者")
        delete_log_btn = QPushButton("删除借阅日志")
        query_log_btn = QPushButton("查询借阅日志")
        statistics_btn = QPushButton("获取统计信息")
        return_btn = QPushButton("返回")  # New return button

        # Apply font to buttons
        for btn in [add_book_btn, edit_book_btn, query_book_btn, delete_book_btn, add_thesis_btn, edit_thesis_btn, 
                    query_thesis_btn, delete_thesis_btn, add_reader_btn, edit_reader_btn, query_reader_btn, 
                    delete_reader_btn, delete_log_btn, query_log_btn, statistics_btn, return_btn]:
            btn.setFont(button_font)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(add_book_btn)
        layout.addWidget(edit_book_btn)
        layout.addWidget(query_book_btn)
        layout.addWidget(delete_book_btn)
        layout.addWidget(add_thesis_btn)
        layout.addWidget(edit_thesis_btn)
        layout.addWidget(query_thesis_btn)
        layout.addWidget(delete_thesis_btn)
        layout.addWidget(add_reader_btn)
        layout.addWidget(edit_reader_btn)
        layout.addWidget(query_reader_btn)
        layout.addWidget(delete_reader_btn)
        layout.addWidget(delete_log_btn)
        layout.addWidget(query_log_btn)
        layout.addWidget(statistics_btn)

        # Add return button at the bottom
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(return_btn)
        layout.addLayout(button_layout)

        # 事件绑定
        add_book_btn.clicked.connect(self.add_book_action)
        edit_book_btn.clicked.connect(self.edit_book_action)
        query_book_btn.clicked.connect(self.query_book_action)
        delete_book_btn.clicked.connect(self.delete_book_action)
        add_thesis_btn.clicked.connect(self.add_thesis_action)
        edit_thesis_btn.clicked.connect(self.edit_thesis_action)
        query_thesis_btn.clicked.connect(self.query_thesis_action)
        delete_thesis_btn.clicked.connect(self.delete_thesis_action)
        add_reader_btn.clicked.connect(self.add_reader_action)
        edit_reader_btn.clicked.connect(self.edit_reader_action)
        query_reader_btn.clicked.connect(self.query_reader_action)
        delete_reader_btn.clicked.connect(self.delete_reader_action)
        delete_log_btn.clicked.connect(self.delete_log_action)
        query_log_btn.clicked.connect(self.query_log_action)
        statistics_btn.clicked.connect(self.get_statistics_action)
        return_btn.clicked.connect(self.close)  # Close the window on return button click

        # 设置主窗口
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_book_action(self):
        title, ok = QInputDialog.getText(self, "添加图书", "输入书名:")
        if not ok: return
        author, ok = QInputDialog.getText(self, "添加图书", "输入作者:")
        if not ok: return
        publisher, ok = QInputDialog.getText(self, "添加图书", "输入出版社:")
        if not ok: return
        publication_date, ok = QInputDialog.getText(self, "添加图书", "输入出版日期 (YYYY-MM-DD):")
        if not ok: return
        stock, ok = QInputDialog.getInt(self, "添加图书", "输入库存数量:")
        if not ok: return
        try:
            add_book(title, author, publisher, publication_date, stock)
            QMessageBox.information(self, "成功", "图书添加完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"添加图书时出错: {e}")

    def edit_book_action(self):
        book_id, ok = QInputDialog.getInt(self, "编辑图书", "输入图书ID:")
        if not ok: return
        title, ok = QInputDialog.getText(self, "编辑图书", "输入新书名 (留空则不修改):")
        if not ok: return
        author, ok = QInputDialog.getText(self, "编辑图书", "输入新作者 (留空则不修改):")
        if not ok: return
        publisher, ok = QInputDialog.getText(self, "编辑图书", "输入新出版社 (留空则不修改):")
        if not ok: return
        publication_date, ok = QInputDialog.getText(self, "编辑图书", "输入新出版日期 (YYYY-MM-DD) (留空则不修改):")
        if not ok: return
        stock, ok = QInputDialog.getInt(self, "编辑图书", "输入新库存数量 (留空则不修改):", value=-1)
        if not ok: return
        try:
            edit_book(book_id, title or None, author or None, publisher or None, publication_date or None, stock if stock != -1 else None)
            QMessageBox.information(self, "成功", "图书编辑完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"编辑图书时出错: {e}")

    def query_book_action(self):
        # Open the book information dialog
        book_info_dialog = BookInfoUI()
        book_info_dialog.exec()  # Use exec to open the dialog modally

    def delete_book_action(self):
        book_id, ok = QInputDialog.getInt(self, "删除图书", "输入图书ID:")
        if not ok: return
        try:
            delete_book(book_id)
            QMessageBox.information(self, "成功", "图书删除完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"删除图书时出错: {e}")

    def add_thesis_action(self):
        title, ok = QInputDialog.getText(self, "添加论文", "输入论文题目:")
        if not ok: return
        author, ok = QInputDialog.getText(self, "添加论文", "输入作者:")
        if not ok: return
        doi, ok = QInputDialog.getText(self, "添加论文", "输入DOI:") 
        if not ok: return
        try:
            add_thesis(title, author, doi)  
            QMessageBox.information(self, "成功", "论文添加完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"添加论文时出错: {e}")

    def edit_thesis_action(self):
        thesis_id, ok = QInputDialog.getInt(self, "编辑论文", "输入论文ID:")
        if not ok: return
        title, ok = QInputDialog.getText(self, "编辑论文", "输入新论文题目 (留空则不修改):")
        if not ok: return
        author, ok = QInputDialog.getText(self, "编辑论文", "输入新作者 (留空则不修改):")
        if not ok: return
        doi, ok = QInputDialog.getText(self, "编辑论文", "输入新DOI (留空则不修改):")  
        if not ok: return
        try:
            edit_thesis(thesis_id, title or None, author or None, doi or None)  
            QMessageBox.information(self, "成功", "论文编辑完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"编辑论文时出错: {e}")

    def query_thesis_action(self):
        thesis_info_dialog = ThesisInfoUI()
        thesis_info_dialog.exec()  

    def delete_thesis_action(self):
        thesis_id, ok = QInputDialog.getInt(self, "删除论文", "输入论文ID:")
        if not ok: return
        try:
            delete_thesis(thesis_id)
            QMessageBox.information(self, "成功", "论文删除完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"删除论文时出错: {e}")

    def add_reader_action(self):
        name, ok = QInputDialog.getText(self, "添加读者", "输入读者名:")
        if not ok: return
        email, ok = QInputDialog.getText(self, "添加读者", "输入邮箱:")
        if not ok: return
        phone, ok = QInputDialog.getText(self, "添加读者", "输入电话:")
        if not ok: return
        try:
            add_reader(name, email, phone)
            QMessageBox.information(self, "成功", "读者添加完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"添加读者时出错: {e}")

    def edit_reader_action(self):
        reader_id, ok = QInputDialog.getInt(self, "编辑读者", "输入读者ID:")
        if not ok: return
        name, ok = QInputDialog.getText(self, "编辑读者", "输入新读者名 (留空则不修改):")
        if not ok: return
        email, ok = QInputDialog.getText(self, "编辑读者", "输入新邮箱 (留空则不修改):")
        if not ok: return
        phone, ok = QInputDialog.getText(self, "编辑读者", "输入新电话 (留空则不修改):")
        if not ok: return
        try:
            edit_reader(reader_id, name or None, email or None, phone or None)
            QMessageBox.information(self, "成功", "读者编辑完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"编辑读者时出错: {e}")


    def query_reader_action(self):
        reader_info_dialog = ReaderInfoUI()
        reader_info_dialog.exec()  

    def delete_reader_action(self):
        reader_id, ok = QInputDialog.getInt(self, "删除读者", "输入读者ID:")
        if not ok: return
        try:
            delete_reader(reader_id)
            QMessageBox.information(self, "成功", "读者删除完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"删除读者时出错: {e}")

    def delete_log_action(self):
        log_id, ok = QInputDialog.getInt(self, "删除借阅日志", "输入日志ID:")
        if not ok: return
        try:
            delete_log(log_id)
            QMessageBox.information(self, "成功", "借阅日志删除完成")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"删除借阅日志时出错: {e}")

    def query_log_action(self):
        logs = query_logs()
        if logs:
            message = "\n".join([f"Log ID: {log[0]}, User ID: {log[1]}, Book ID: {log[2]}" for log in logs])
        else:
            message = "No logs found."
        QMessageBox.information(self, "查询借阅日志", message)

    def get_statistics_action(self):
        try:
            stats = get_statistics()
            message = f"图书总数: {stats[0]}, 论文总数: {stats[1]}, 图书借阅总数: {stats[2]}, 论文下载总数: {stats[3]}"
            QMessageBox.information(self, "统计信息", message)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"获取统计信息时出错: {e}")
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from ui.admin_ui import AdminUI
from ui.user_ui import UserUI
from ui.guest_ui import GuestUI

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("实验室资料管理系统")
        self.setGeometry(100, 100, 600, 400)

        # 设置窗口背景颜色
        self.setStyleSheet("background-color: #f0f0f0;")

        # 创建按钮
        admin_btn = QPushButton("管理员")
        user_btn = QPushButton("一般用户")
        guest_btn = QPushButton("游客")
        exit_btn = QPushButton("退出")

        # 设置按钮样式
        button_style = """
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        """
        admin_btn.setStyleSheet(button_style)
        user_btn.setStyleSheet(button_style)
        guest_btn.setStyleSheet(button_style)
        exit_btn.setStyleSheet(button_style)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(admin_btn)
        layout.addWidget(user_btn)
        layout.addWidget(guest_btn)
        layout.addWidget(exit_btn)

        # 事件绑定
        admin_btn.clicked.connect(self.open_admin_ui)
        user_btn.clicked.connect(self.open_user_ui)
        guest_btn.clicked.connect(self.open_guest_ui)
        exit_btn.clicked.connect(self.close)

        # 设置主窗口中心
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_admin_ui(self):
        self.admin_ui = AdminUI()
        self.admin_ui.show()

    def open_user_ui(self):
        self.user_ui = UserUI()
        self.user_ui.show()

    def open_guest_ui(self):
        self.guest_ui = GuestUI()
        self.guest_ui.show()

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainApp()
    main_window.show()
    app.exec()

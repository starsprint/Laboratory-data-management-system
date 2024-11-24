from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from ui.admin_ui import AdminUI
from ui.user_ui import UserUI
from ui.guest_ui import GuestUI

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("实验室资料管理系统")
        self.setGeometry(100, 100, 800, 600)

        # 设置窗口背景颜色
        self.setStyleSheet("background-color: #f0f0f0;")

        # 创建标签
        title_label = QLabel("实验室资料管理系统")
        title_label.setAlignment(Qt.AlignCenter)
        # 修改字体大小和加粗
        title_label.setStyleSheet("font-size: 50px; font-weight: bold;")

        # 创建按钮
        admin_btn = QPushButton("管理员")
        user_btn = QPushButton("一般用户")
        guest_btn = QPushButton("游客")
        exit_btn = QPushButton("退出")

        # 设置按钮样式
        admin_btn.setStyleSheet("""
            QPushButton {
                background-color: yellow; 
                color: black; 
                border-radius: 1px; 
                padding: 20px;
            }
            QPushButton:hover {
                background-color: lightyellow;
            }
            QPushButton:pressed {
                background-color: darkyellow;
            }
        """)
        user_btn.setStyleSheet("""
            QPushButton {
                background-color: blue; 
                color: white; 
                border-radius: 1px; 
                padding: 20px;
            }
            QPushButton:hover {
                background-color: lightblue;
            }
            QPushButton:pressed {
                background-color: darkblue;
            }
        """)
        guest_btn.setStyleSheet("""
            QPushButton {
                background-color: green; 
                color: white; 
                border-radius: 1px; 
                padding: 20px;
            }
            QPushButton:hover {
                background-color: lightgreen;
            }
            QPushButton:pressed {
                background-color: darkgreen;
            }
        """)
        exit_btn.setStyleSheet("""
            QPushButton {
                background-color: red; 
                color: white; 
                border-radius: 1px; 
                padding: 30px;
            }
            QPushButton:hover {
                background-color: lightcoral;
            }
            QPushButton:pressed {
                background-color: darkred;
            }
        """)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(title_label)

        # 将按钮垂直排列
        layout.addWidget(admin_btn)
        layout.addWidget(user_btn)
        layout.addWidget(guest_btn)
        layout.addWidget(exit_btn)

        # 设置主窗口中心
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 事件绑定
        admin_btn.clicked.connect(self.open_admin_ui)
        user_btn.clicked.connect(self.open_user_ui)
        guest_btn.clicked.connect(self.open_guest_ui)
        exit_btn.clicked.connect(self.close)

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

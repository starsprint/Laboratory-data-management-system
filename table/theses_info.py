from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QMessageBox, QWidget, QInputDialog, QSizePolicy
from function.functions import query_theses, query_thesis, add_thesis, edit_thesis, delete_thesis, download_thesis, get_thesis_statistics, upload_thesis

class ThesisInfoUI(QDialog):
    def __init__(self, user_role):
        super().__init__()
        self.user_role = user_role
        self.setWindowTitle("论文信息")
        self.setGeometry(100, 100, 1000, 600)

        # Layout
        main_layout = QVBoxLayout()

        # Top layout for thesis count and admin buttons
        top_layout = QHBoxLayout()
        
        # Admin buttons
        if user_role == 'admin':
            # Fetch and display thesis statistics
            stats = get_thesis_statistics()
            self.thesis_count_label = QLabel(f"论文数量: {stats[0]}, 总下载量: {stats[1]}")
            top_layout.addWidget(self.thesis_count_label)

            find_thesis_btn = QPushButton("查找论文")
            add_thesis_btn = QPushButton("添加论文")
            find_thesis_btn.clicked.connect(self.find_thesis)
            add_thesis_btn.clicked.connect(self.add_thesis)
            top_layout.addWidget(find_thesis_btn)
            top_layout.addWidget(add_thesis_btn)
        elif user_role == 'reader':
            upload_thesis_btn = QPushButton("上传论文")
            upload_thesis_btn.clicked.connect(self.upload_thesis)
            top_layout.addWidget(upload_thesis_btn)

            find_thesis_btn = QPushButton("查找论文")
            find_thesis_btn.clicked.connect(self.find_thesis)
            top_layout.addWidget(find_thesis_btn)

        main_layout.addLayout(top_layout)

        # Table to display thesis information
        self.table = QTableWidget()
        self.table.setColumnCount(5)  # Columns: Title, Author, DOI, Downloads, Actions
        self.table.setHorizontalHeaderLabels(["Title", "Author", "DOI", "Downloads", "Actions"])
        main_layout.addWidget(self.table)

        # Load thesis data
        self.load_thesis_data()

        # Close button
        close_btn = QPushButton("返回")
        close_btn.clicked.connect(self.close)
        main_layout.addWidget(close_btn)

        self.setLayout(main_layout)

    def load_thesis_data(self):
        theses = query_theses()  # Fetch thesis data
        self.table.setRowCount(len(theses))
        
        for row, thesis in enumerate(theses):
            self.table.setItem(row, 0, QTableWidgetItem(thesis[0]))  # Title
            self.table.setItem(row, 1, QTableWidgetItem(thesis[1]))  # Author
            self.table.setItem(row, 2, QTableWidgetItem(thesis[3]))  # DOI
            self.table.setItem(row, 3, QTableWidgetItem(str(thesis[2])))  # Downloads

            # Actions based on user role
            action_layout = QHBoxLayout()
            if self.user_role == 'admin':
                edit_btn = QPushButton("编辑")
                delete_btn = QPushButton("删除")
                
                # Set minimum size for buttons
                edit_btn.setMinimumSize(20, 20)
                delete_btn.setMinimumSize(20, 20)
                
                # Set size policy to allow expansion
                edit_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                delete_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                
                edit_btn.clicked.connect(lambda _, r=row: self.edit_thesis(r))
                delete_btn.clicked.connect(lambda _, r=row: self.delete_thesis(r))
                action_layout.addWidget(edit_btn)
                action_layout.addWidget(delete_btn)
            elif self.user_role == 'reader':
                download_btn = QPushButton("下载")
                
                # Set minimum size for download button
                download_btn.setMinimumSize(30, 20)
                
                # Set size policy to allow expansion
                download_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                
                download_btn.clicked.connect(lambda _, r=row: self.download_thesis(r))
                action_layout.addWidget(download_btn)

            action_widget = QWidget()
            action_widget.setLayout(action_layout)
            self.table.setCellWidget(row, 4, action_widget)

    def find_thesis(self):
        title, ok = QInputDialog.getText(self, "查找论文", "输入论文标题:")
        if ok and title:
            thesis = query_thesis(title)
            if thesis:
                QMessageBox.information(self, "论文信息", f"Title: {thesis[0]}\nAuthor: {thesis[1]}\nDOI: {thesis[3]}\nDownloads: {thesis[2]}")
            else:
                QMessageBox.warning(self, "查找失败", "未找到该论文。")

    def add_thesis(self):
        # Example logic to add a thesis
        title, ok = QInputDialog.getText(self, "添加论文", "输入论文标题:")
        if ok and title:
            author, ok = QInputDialog.getText(self, "添加论文", "输入作者:")
            if ok and author:
                doi, ok = QInputDialog.getText(self, "添加论文", "输入DOI:")
                if ok and doi:
                    add_thesis(title, author, doi)
                    self.load_thesis_data()  # Refresh the table

    def edit_thesis(self, row):
        # Example logic to edit a thesis
        title = self.table.item(row, 0).text()
        author, ok = QInputDialog.getText(self, "编辑论文", "输入新作者:", text=self.table.item(row, 1).text())
        if ok:
            doi, ok = QInputDialog.getText(self, "编辑论文", "输入新DOI:", text=self.table.item(row, 2).text())
            if ok:
                edit_thesis(title, author, doi)
                self.load_thesis_data()  # Refresh the table

    def delete_thesis(self, row):
        title = self.table.item(row, 0).text()
        delete_thesis(title)
        self.load_thesis_data()  # Refresh the table

    def download_thesis(self, row):
        title = self.table.item(row, 0).text()
        download_thesis(title)
        self.load_thesis_data()  # Refresh the table

    def upload_thesis(self):
        # Example logic to upload a thesis
        title, ok = QInputDialog.getText(self, "上传论文", "输入论文标题:")
        if ok and title:
            author, ok = QInputDialog.getText(self, "上传论文", "输入作者:")
            if ok and author:
                doi, ok = QInputDialog.getText(self, "上传论文", "输入DOI:")
                if ok and doi:
                    upload_thesis(title, author, doi)
                    self.load_thesis_data()  # Refresh the table
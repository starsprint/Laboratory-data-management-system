from PySide6.QtWidgets import QApplication
from ui.main_window import MainApp

def main():
    app = QApplication([])
    main_window = MainApp()
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()
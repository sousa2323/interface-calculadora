import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label = QLabel('O Meu texto')
    label.setStyleSheet('font-size: 50px;')
    window.v_layout.addWidget(label)
    window.adjustFixedSize()

    window.show()
    app.exec()

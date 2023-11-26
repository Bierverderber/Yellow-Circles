import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from ui_file import Ui_Dialog
from random import randint


class Suprematism(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()
        self.flag = True

    def run(self, qp):
        diameter = randint(20, 150)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(randint(50, 800) - diameter // 2, randint(50, 600) - diameter // 2, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
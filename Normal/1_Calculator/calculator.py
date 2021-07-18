from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Ui_calculator as ui

class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # expression_label setTextdisplay text.
        self.text = str()

        self.arithmetic_list = []

        # 0 ~ 9 numeric signal.
        self.zero.clicked.connect(self.zero_clicked)
        self.one.clicked.connect(self.one_clicked)
        self.two.clicked.connect(self.two_clicked)
        self.three.clicked.connect(self.three_clicked)
        self.four.clicked.connect(self.four_clicked)
        self.five.clicked.connect(self.five_clicked)
        self.six.clicked.connect(self.six_clicked)
        self.seven.clicked.connect(self.seven_clicked)
        self.eight.clicked.connect(self.eight_clicked)
        self.nine.clicked.connect(self.nine_clicked)

        # Arithmetic signal.
        self.clear.clicked.connect(self.clear_clicked)
        self.equal.clicked.connect(self.calc_answer)
        self.point.clicked.connect(self.point_clicked)
        self.add.clicked.connect(self.add_clicked)
        self.subtract.clicked.connect(self.subtract_clicked)
        self.multiplication.clicked.connect(self.multiplication_clicked)
        self.division.clicked.connect(self.division_clicked)


    # 0 ~ 9 numeric slot.
    def zero_clicked(self):
        self.text += "0"
        self.expression_label.setText(self.text)

    def one_clicked(self):
        self.text += "1"
        self.expression_label.setText(self.text)
    
    def two_clicked(self):
        self.text += "2"
        self.expression_label.setText(self.text)
    
    def three_clicked(self):
        self.text += "3"
        self.expression_label.setText(self.text)
    
    def four_clicked(self):
        self.text += "4"
        self.expression_label.setText(self.text)
    
    def five_clicked(self):
        self.text += "5"
        self.expression_label.setText(self.text)
    
    def six_clicked(self):
        self.text += "6"
        self.expression_label.setText(self.text)
    
    def seven_clicked(self):
        self.text += "7"
        self.expression_label.setText(self.text)
    
    def eight_clicked(self):
        self.text += "8"
        self.expression_label.setText(self.text)
    
    def nine_clicked(self):
        self.text += "9"
        self.expression_label.setText(self.text)


    # Arithmetic slot.
    def clear_clicked(self):
        self.text = ""
        self.expression_label.setText(self.text)

    def point_clicked(self):
        self.text += "."
        self.expression_label.setText(self.text)
    
    def add_clicked(self):
        self.text += "+"
        self.expression_label.setText(self.text)
    
    def subtract_clicked(self):
        self.text += "-"
        self.expression_label.setText(self.text)
    
    def multiplication_clicked(self):
        self.text += "×"
        self.expression_label.setText(self.text)
    
    def division_clicked(self):
        self.text += "÷"
        self.expression_label.setText(self.text)

    def calc_answer(self):
        pass



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
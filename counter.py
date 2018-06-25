import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from functools import partial

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'People Counter'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 200
        self.sum = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMinimumSize(300,300)
        self.createLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.outputGroupBox)
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(self.horizontalGroupBox2)
        self.setLayout(windowLayout)

        self.show()

    def createLayout(self):
        layout = QHBoxLayout()

        self.outputGroupBox = QGroupBox("Number of People")
        self.textDisplay = QLabel(str(self.sum))
        layout.addWidget(self.textDisplay)

        self.outputGroupBox.setLayout(layout)

        layout = QHBoxLayout()

        self.horizontalGroupBox = QGroupBox("Press + to increase by 1, Press - to decrease by 1")

        plusButton = QPushButton("+",self)
        plusButton.clicked.connect(partial(self.calc,1))
        layout.addWidget(plusButton)

        negButton = QPushButton("-", self)
        negButton.clicked.connect(partial(self.calc,-1))
        layout.addWidget(negButton)

        self.horizontalGroupBox.setLayout(layout)

        layout = QHBoxLayout()

        self.horizontalGroupBox2 = QGroupBox("Press +2 to increase by 2, Press -2 to decrease by 2")

        plus2Button = QPushButton("+2",self)
        plus2Button.clicked.connect(partial(self.calc,2))
        layout.addWidget(plus2Button)

        neg2Button = QPushButton("-2", self)
        neg2Button.clicked.connect(partial(self.calc,-2))
        layout.addWidget(neg2Button)

        self.horizontalGroupBox2.setLayout(layout)



    @pyqtSlot(int)
    def calc(self, num):
        self.sum += num
        if self.sum < 0:
            self.sum = 0
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Cant go lower than 0")
            msg.exec()
        print(self.sum)
        self.textDisplay.setText(str(self.sum))
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
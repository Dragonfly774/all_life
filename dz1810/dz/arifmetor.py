import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit
from mak import Ui_MainWindow
from PyQt5 import uic


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        ans = 'Ваш заказ:\n'
        summ1 = int(self.lineEdit.text()) * 10

        summ2 = int(self.lineEdit.text()) * 15
        summ3 = int(self.lineEdit.text()) * 5
        summ4 = int(self.lineEdit.text()) * 9
        if self.checkBox.isChecked():
            ans = ans + f'{self.checkBox.text()}----{self.lineEdit.text()}----{summ1}\n'
        if self.checkBox_2.isChecked():
            ans = ans + f'{self.checkBox.text()}----{self.lineEdit.text()}----{summ2}\n'
        if self.checkBox_3.isChecked():
            ans = ans + f'{self.checkBox.text()}----{self.lineEdit.text()}----{summ3}\n'
        if self.checkBox_4.isChecked():
            ans = ans + f'{self.checkBox.text()}----{self.lineEdit.text()}----{summ4}\n'
        self.plainTextEdit.setPlainText(ans)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())












'''        if self.checkBox.isChecked():
            self.lineEdit.setText('1')
        else:
            self.lineEdit.setText('')
        if self.checkBox_2.isChecked():
            self.lineEdit_2.setText('1')
        else:
            self.lineEdit_2.setText('')
        if self.checkBox_3.isChecked():
            self.lineEdit_3.setText('1')
        else:
            self.lineEdit_3.setText('')
        if self.checkBox_4.isChecked():
            self.lineEdit_4.setText('1')
        else:
            self.lineEdit_4.setText('')
'''

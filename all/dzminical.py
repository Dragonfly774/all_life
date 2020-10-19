import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from popa import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBox_1.stateChanged.connect(self.run)
        self.checkBox_2.stateChanged.connect(self.run)
        self.checkBox_3.stateChanged.connect(self.run)

    def run(self):
        if self.sender().text() == 'edit1':
            self.lineEdit_1.show() if self.statusbar == Qt.Checked else self.lineEdit_1.hide()

        elif self.sender().text() == 'edit2':
            self.lineEdit_2.show() if self.statusbar == Qt.Checked else self.lineEdit_2.hide()
        else:
            self.lineEdit_3.show() if self.statusbar == Qt.Checked else self.lineEdit_3.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

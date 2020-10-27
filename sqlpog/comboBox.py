# бла
import sqlite3
def __init__(self):
    self.comboBox.addItem('бла бла', '')
    self.bth.cliced.connect(self.run)

def run(self):
    find_str = self.comboBox.currenData()
    where_str = self.lineEdit.text()
    if where_str == 'title':
        x = f'title LIKE "%{find_str}%"'
    else:
        x = f'{where_str} = {find_str}'
    con = sqlite3.connect(input())

    cur = con.cursor()

    result = cur.execute(f'SELECT * FROM Films, genres WHERE Films.{x} AND Films.genre = genres.id ORDER BY Films.id').fetchall()
    if res := result.fetchall():
        self.lineEdit_2.setText(str(res[0]))
        self.lineEdit_3.setText(str(res[1]))
        self.lineEdit_4.setText(str(res[2]))

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PayForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


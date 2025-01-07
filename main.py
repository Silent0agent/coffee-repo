import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Эспрессо')
        self.conn = sqlite3.connect('coffee.sqlite')
        self.cur = self.conn.cursor()
        self.load_table()

    def load_table(self):
        res = self.cur.execute("SELECT * FROM Coffee").fetchall()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        for i in range(len(res)):
            for j in range(len(res[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(res[i][j])))
        self.tableWidget.resizeColumnsToContents()


def main():
    app = QApplication(sys.argv)
    window = Coffee()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

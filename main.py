import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Эспрессо')
        self.conn = sqlite3.connect('coffee.sqlite')
        self.cur = self.conn.cursor()
        self.load_table()
        self.pushButton.clicked.connect(self.open_win)

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

    def open_win(self):
        self.win = addEdit(self)
        self.win.show()


class addEdit(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Добавление/редактирование кофе')
        self.conn = sqlite3.connect('coffee.sqlite')
        self.cur = self.conn.cursor()
        self.loadButton.clicked.connect(self.load_coffee)
        self.addButton.clicked.connect(self.add_coffee)
        self.redactButton.clicked.connect(self.redact_coffee)

    def load_coffee(self):
        try:
            coffeeid = self.redactId.text()
            if not coffeeid:
                raise Exception
            coffee = self.cur.execute("SELECT * FROM Coffee WHERE id = ?", (coffeeid,)).fetchone()
            self.redactName.setText(str(coffee[1]))
            self.redactRoasting.setText(str(coffee[2]))
            self.redactGrounding.setText(str(coffee[3]))
            self.redactFlavour.setPlainText(str(coffee[4]))
            self.redactPrice.setText(str(coffee[5]))
            self.redactVolume.setText(str(coffee[6]))
            self.error_label.setText('')
        except Exception:
            self.error_label.setText('Введите корректные данные')

    def add_coffee(self):
        try:
            coffeeid = self.addId.text()
            name = self.addName.text()
            roasting = self.addRoasting.text()
            grounding = self.addGrounding.text()
            flavour = self.addFlavour.toPlainText()
            price = self.addPrice.text()
            volume = self.addVolume.text()
            if not name or not roasting or not grounding or not flavour or not price or not volume:
                raise Exception
            if not coffeeid:
                self.cur.execute(
                    "INSERT INTO Coffee ( name, roasting, ground_or_beans, flavour, price, volume) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, roasting, grounding, flavour, price, volume))
            else:
                self.cur.execute(
                    "INSERT INTO Coffee (id, name, roasting, ground_or_beans, flavour, price, volume) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (coffeeid, name, roasting, grounding, flavour, price, volume))
            self.conn.commit()
            self.error_label.setText('Кофе успешно добавлен')
            self.parent.load_table()

        except Exception:
            self.error_label.setText('Введите корректные данные')

    def redact_coffee(self):
        try:
            coffeeid = self.redactId.text()
            name = self.redactName.text()
            roasting = self.redactRoasting.text()
            grounding = self.redactGrounding.text()
            flavour = self.redactFlavour.toPlainText()
            price = self.redactPrice.text()
            volume = self.redactVolume.text()
            if not coffeeid or not name or not roasting or not grounding or not flavour or not price or not volume:
                raise Exception
            self.cur.execute(
                "UPDATE Coffee SET name = ?, roasting = ?, ground_or_beans = ?, flavour = ?, price = ?, volume = ? WHERE id = ?",
                (name, roasting, grounding, flavour, price, volume, coffeeid))
            self.conn.commit()
            self.error_label.setText('Кофе успешно изменен')
            self.parent.load_table()
        except Exception:
            self.error_label.setText('Введите корректные данные')


def main():
    app = QApplication(sys.argv)
    window = Coffee()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

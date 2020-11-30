import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class CoffeeInfo(QMainWindow):
    def __init__(self):
        super(CoffeeInfo, self).__init__()
        uic.loadUi('main.ui', self)

        self.connection = sqlite3.connect('coffee.db')
        self.cursor = self.connection.cursor()
        result = self.cursor.execute('''SELECT *
                                         FROM Coffee''').fetchall()
        self.connection.commit()
        self.connection.close()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]) - 1)
        self.tableWidget.setRowHeight(0, 250)
        self.tableWidget.setHorizontalHeaderLabels(['Название сорта',
                                                    'степень обжарки',
                                                    'Состояние',
                                                    'Описание вкуса',
                                                    'Цена',
                                                    'Объём упаковки'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem[1:]):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = CoffeeInfo()
    wnd.show()
    sys.exit(app.exec())

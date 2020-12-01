import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class CoffeeInfo(QMainWindow):
    def __init__(self):
        super(CoffeeInfo, self).__init__()
        uic.loadUi('main.ui', self)

        result = []
        self.connection = sqlite3.connect('coffee.db')
        self.cursor = self.connection.cursor()
        for i in self.cursor.execute('''SELECT *
                                        FROM Coffee''').fetchall():
            result.append(list(i))
        for i in range(len(result)):
            for j in range(len(result[i])):
                if j == 1 and result[i][j] == 1:
                    result[i][j] = 'робуста'
                if j == 1 and result[i][j] == 2:
                    result[i][j] = 'арабика'
                if j == 1 and result[i][j] == 3:
                    result[i][j] = 'либерика'
                if j == 2 and result[i][j] == 1:
                    result[i][j] = 'светлая'
                if j == 2 and result[i][j] == 2:
                    result[i][j] = 'средняя'
                if j == 2 and result[i][j] == 3:
                    result[i][j] = 'тёмная'
        print(result)
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

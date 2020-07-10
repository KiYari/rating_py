import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget, QHBoxLayout
import csv

from PyQt5.uic.properties import QtGui


class Rating(QWidget):
    def __init__(self):
        super().__init__()

        self.loadUI()

        self.loadTable('src/rating.csv')

    def loadUI(self):
        self.setGeometry(100, 100, 1240, 768)
        self.lay = QHBoxLayout()
        self.table = QTableWidget()
        self.lay.addWidget(self.table)
        self.setLayout(self.lay)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            title = next(reader)

            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)
            self.table.setRowCount(0)
            for i, row in enumerate(reader):
                self.table.setRowCount(self.table.rowCount() + 1)
                if i >= 1:
                    tasks = 9 * float(row[2].replace(',', '.')) // 100\
                                  + 6 * float(row[3].replace(',', '.')) // 100 \
                                  + 6 * float(row[4].replace(',', '.')) // 100 \
                                  + 8 * float(row[5].replace(',', '.')) // 100 \
                                  + 4 * float(row[6].replace(',', '.')) // 100 \
                                  + 8 * float(row[7].replace(',', '.')) // 100 \
                                  + 3 * float(row[8].replace(',', '.')) // 100 \
                                  + 7 * float(row[9].replace(',', '.')) // 100

                    rating = "%.2f" % (tasks * 100 / 51)
                    row.append(rating)
                for j, elem in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(elem))
                    if j == 12:
                        self.table.setItem(i, j, QTableWidgetItem(elem))
                        if float(row[11]) > 60.0:
                            self.table.item(i, j).setBackground(QColor(250, 128, 114))
                        if float(row[11]) > 80.0:
                            self.table.item(i, j).setBackground(QColor(255, 215, 0))
                        if float(row[11]) > 95.0:
                            self.table.item(i, j).setBackground(QColor(144, 238, 144))
            self.table.resizeColumnsToContents()


app = QApplication(sys.argv)
ex = Rating()
ex.show()
sys.exit(app.exec_())

import sys

from Zadacha1 import LogicTable
from Zadacha2 import LogicTable2
from Zadacha3 import LogicTable3
from Zadacha4 import LogicTable4
from Zadacha5 import LogicTable5

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget
)


class CaseMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Меню задач')

        layout = QVBoxLayout()
        self.task1 = None
        self.task2 = None
        self.task3 = None
        self.task4 = None
        self.task5 = None



        for i in range(1, 6):
            btn = QPushButton(f'Задача {i}')
            btn.clicked.connect(lambda checked, i=i: self.open_task(i))
            layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_task(self, task_num):
        if task_num == 1:
            self.task1 = LogicTable()
            self.task1.show()
        elif task_num == 2:
            self.task2 = LogicTable2()
            self.task2.show()
        elif task_num == 3:
            self.task3 = LogicTable3()
            self.task3.show()
        elif task_num == 4:
            self.task4 = LogicTable4()
            self.task4.show()
        elif task_num == 5:
            self.task5 = LogicTable5()
            self.task5.show()


app = QApplication(sys.argv)

menu = CaseMenu()
menu.show()

app.exec_()
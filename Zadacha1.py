import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QRadioButton, QButtonGroup, QFileDialog
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox)


class LogicTable(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        # При нажатии на кнопку
        self.check_btn.clicked.connect(self.check_answers)
        self.save_btn.clicked.connect(self.save_screenshot)

    def initUI(self):
        # Текст задачи
        self.task_text = QLabel("""
    В кафе встретились три друга: скульптор Белов, скрипач Чернов и художник Рыжов. 
    “Замечательно, что один из нас имеет белые, один черные и один рыжие волосы, 
    но ни у одного из нас нет волос того цвета, на который указывает его фамилия”, 
    - заметил черноволосый. 
    “Ты прав”, - сказал Белов. 
    Какой цвет волос у художника?
            """)

        # Таблица
        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(4)

        # Заполняем заголовки
        self.table.setItem(0, 1, QTableWidgetItem("Белов"))
        self.table.setItem(0, 2, QTableWidgetItem("Чернов"))
        self.table.setItem(0, 3, QTableWidgetItem("Рыжов"))

        self.table.setItem(1, 0, QTableWidgetItem("Блондин"))
        self.table.setItem(2, 0, QTableWidgetItem("Брюнет"))
        self.table.setItem(3, 0, QTableWidgetItem("Рыжий"))

        item = QTableWidgetItem("Белов")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 1, item)

        # Устанавливаем "Чернов" только для чтения
        item = QTableWidgetItem("Чернов")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 2, item)

        # Устанавливаем "Рыжов" только для чтения
        item = QTableWidgetItem("Рыжов")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 3, item)

        # Устанавливаем "Блондин" только для чтения
        item = QTableWidgetItem("Блондин")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(1, 0, item)

        # Устанавливаем "Брюнет" только для чтения
        item = QTableWidgetItem("Брюнет")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(2, 0, item)

        # Устанавливаем "Рыжий" только для чтения
        item = QTableWidgetItem("Рыжий")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(3, 0, item)



        # Создаем группы для каждой строки
        self.group1 = QButtonGroup()
        self.group2 = QButtonGroup()
        self.group3 = QButtonGroup()


        self.radio1 = QRadioButton()
        self.radio1.setAutoExclusive(False)
        self.radio2 = QRadioButton()
        self.radio2.setAutoExclusive(False)
        self.radio3 = QRadioButton()
        self.radio3.setAutoExclusive(False)
        self.radio4 = QRadioButton()
        self.radio4.setAutoExclusive(False)
        self.radio5 = QRadioButton()
        self.radio5.setAutoExclusive(False)
        self.radio6 = QRadioButton()
        self.radio6.setAutoExclusive(False)
        self.radio7 = QRadioButton()
        self.radio7.setAutoExclusive(False)
        self.radio8 = QRadioButton()
        self.radio8.setAutoExclusive(False)
        self.radio9 = QRadioButton()
        self.radio9.setAutoExclusive(False)

        self.group1.addButton(self.radio1)
        self.group1.addButton(self.radio2)
        self.group1.addButton(self.radio3)
        self.group2.addButton(self.radio4)
        self.group2.addButton(self.radio5)
        self.group2.addButton(self.radio6)
        self.group3.addButton(self.radio7)
        self.group3.addButton(self.radio8)
        self.group3.addButton(self.radio9)

        self.table.setCellWidget(1, 1, self.radio1)
        self.table.setCellWidget(1, 2, self.radio2)
        self.table.setCellWidget(1, 3, self.radio3)
        self.table.setCellWidget(2, 1, self.radio4)
        self.table.setCellWidget(2, 2, self.radio5)
        self.table.setCellWidget(2, 3, self.radio6)
        self.table.setCellWidget(3, 1, self.radio7)
        self.table.setCellWidget(3, 2, self.radio8)
        self.table.setCellWidget(3, 3, self.radio9)

        # Кнопка проверки
        self.check_btn = QPushButton("Проверить")
        # Кнопка Сохранения
        self.save_btn = QPushButton("Сохранить")

        # Размещаем в вертикальном layout
        layout = QVBoxLayout()

        # Текст задачи
        layout.addWidget(self.task_text)

        # Таблица и кнопка в горизонтальном layout
        table_layout = QHBoxLayout()
        table_layout.addWidget(self.table)
        table_layout.addWidget(self.check_btn)
        table_layout.addWidget(self.save_btn)

        layout.addLayout(table_layout)

        self.resize(610, 300)
        self.setWindowTitle("Логическая задача")
        self.setLayout(layout)

    def check_answers(self):

        radio_1_2 = self.table.cellWidget(1, 2)
        radio_2_3 = self.table.cellWidget(2, 3)
        radio_3_1 = self.table.cellWidget(3, 1)

        if radio_1_2.isChecked() and radio_2_3.isChecked() and radio_3_1.isChecked():
            QMessageBox.information(self, "Результат", "Ответ верный!")
        else:
            QMessageBox.warning(self, "Результат", "Ответ неверный")

    def save_screenshot(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить скриншот", "",
                                                   "Images (*.png *.jpg);;All Files (*)", options=options)

        if file_name:
            screenshot = QPixmap(self.size())
            self.render(screenshot)
            screenshot.save(file_name, "PNG")




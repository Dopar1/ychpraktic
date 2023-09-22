import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QRadioButton, QButtonGroup, QFileDialog
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox)


class LogicTable5(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        # При нажатии на кнопку
        self.check_btn.clicked.connect(self.check_answers)
        self.save_btn.clicked.connect(self.save_screenshot)

    def initUI(self):
        # Текст задачи
        self.task_text = QLabel("""
По кругу сидят Иванов, Петров, Марков и Карпов. 
Их имена Андрей, Сергей, Тимофей, Алексей. 
Известно, что Иванов не Андрей и не Алексей. 
Сергей сидит между Марковым и Тимофеем. 
Петров сидит между Карповым и Андреем. 
Как зовут Иванова, Петрова, Маркова и Карпова?
            """)

        # Таблица
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(5)

        # Заполняем заголовки
        self.table.setItem(0, 1, QTableWidgetItem("Андрей"))
        self.table.setItem(0, 2, QTableWidgetItem("Сергей"))
        self.table.setItem(0, 3, QTableWidgetItem("Тимофей"))
        self.table.setItem(0, 4, QTableWidgetItem("Алексей"))

        self.table.setItem(1, 0, QTableWidgetItem("Иванов"))
        self.table.setItem(2, 0, QTableWidgetItem("Петров"))
        self.table.setItem(3, 0, QTableWidgetItem("Марков"))
        self.table.setItem(4, 0, QTableWidgetItem("Карпов"))

        item = QTableWidgetItem("Андрей")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 1, item)

        # Устанавливаем "Сергей" только для чтения
        item = QTableWidgetItem("Сергей")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 2, item)

        # Устанавливаем "Тимофей" только для чтения
        item = QTableWidgetItem("Тимофей")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 3, item)

        # Устанавливаем "Алексей" только для чтения
        item = QTableWidgetItem("Алексей")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 4, item)

        # Устанавливаем "Иванов" только для чтения
        item = QTableWidgetItem("Иванов")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(1, 0, item)

        # Устанавливаем "Петров" только для чтения
        item = QTableWidgetItem("Петров")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(2, 0, item)

        # Устанавливаем "Марков" только для чтения
        item = QTableWidgetItem("Марков")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(3, 0, item)

        # Устанавливаем "Карпов" только для чтения
        item = QTableWidgetItem("Карпов")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(4, 0, item)

        # Создаем группы для каждой строки
        self.group1 = QButtonGroup()
        self.group2 = QButtonGroup()
        self.group3 = QButtonGroup()
        self.group4 = QButtonGroup()


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
        self.radio10 = QRadioButton()
        self.radio10.setAutoExclusive(False)
        self.radio11 = QRadioButton()
        self.radio11.setAutoExclusive(False)
        self.radio12 = QRadioButton()
        self.radio12.setAutoExclusive(False)
        self.radio13 = QRadioButton()
        self.radio13.setAutoExclusive(False)
        self.radio14 = QRadioButton()
        self.radio14.setAutoExclusive(False)
        self.radio15 = QRadioButton()
        self.radio15.setAutoExclusive(False)
        self.radio16 = QRadioButton()
        self.radio16.setAutoExclusive(False)

        self.group1.addButton(self.radio1)
        self.group1.addButton(self.radio2)
        self.group1.addButton(self.radio3)
        self.group1.addButton(self.radio4)
        self.group2.addButton(self.radio5)
        self.group2.addButton(self.radio6)
        self.group2.addButton(self.radio7)
        self.group2.addButton(self.radio8)
        self.group3.addButton(self.radio9)
        self.group3.addButton(self.radio10)
        self.group3.addButton(self.radio11)
        self.group3.addButton(self.radio12)
        self.group4.addButton(self.radio13)
        self.group4.addButton(self.radio14)
        self.group4.addButton(self.radio15)
        self.group4.addButton(self.radio16)



        self.table.setCellWidget(1, 1, self.radio1)
        self.table.setCellWidget(1, 2, self.radio2)
        self.table.setCellWidget(1, 3, self.radio3)
        self.table.setCellWidget(1, 4, self.radio4)
        self.table.setCellWidget(2, 1, self.radio5)
        self.table.setCellWidget(2, 2, self.radio6)
        self.table.setCellWidget(2, 3, self.radio7)
        self.table.setCellWidget(2, 4, self.radio8)
        self.table.setCellWidget(3, 1, self.radio9)
        self.table.setCellWidget(3, 2, self.radio10)
        self.table.setCellWidget(3, 3, self.radio11)
        self.table.setCellWidget(3, 4, self.radio12)
        self.table.setCellWidget(4, 1, self.radio13)
        self.table.setCellWidget(4, 2, self.radio14)
        self.table.setCellWidget(4, 3, self.radio15)
        self.table.setCellWidget(4, 4, self.radio16)

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

        self.resize(730, 320)
        self.setWindowTitle("Логическая задача")
        self.setLayout(layout)

    def check_answers(self):

        radio_1_2 = self.table.cellWidget(1, 2)
        radio_2_4 = self.table.cellWidget(2, 4)
        radio_3_1 = self.table.cellWidget(3, 1)
        radio_4_3 = self.table.cellWidget(4, 3)

        if radio_1_2.isChecked() and radio_2_4.isChecked() and radio_3_1.isChecked() and radio_4_3.isChecked():
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

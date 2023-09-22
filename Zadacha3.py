import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QRadioButton, QButtonGroup, QFileDialog
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox)


class LogicTable3(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        # При нажатии на кнопку
        self.check_btn.clicked.connect(self.check_answers)
        self.save_btn.clicked.connect(self.save_screenshot)


    def initUI(self):

        # Текст задачи
        self.task_text = QLabel("""
После соревнований бегунов на табло появилась надпись:
• Рустам не был вторым.
• Эдуард отстатл от Рустама на два места.
• Яков не был первым.
• Галина не была не первой ни последней.
• Карина финишировала сразу за Яковом.
Кто же победил в этих соревнованиях? Каково было распределение бегунов на финише?
            """)

        # Таблица
        self.table = QTableWidget()
        self.table.setRowCount(6)
        self.table.setColumnCount(6)

        # Заполняем заголовки
        self.table.setItem(0, 1, QTableWidgetItem("Рустам"))
        self.table.setItem(0, 2, QTableWidgetItem("Эдуард"))
        self.table.setItem(0, 3, QTableWidgetItem("Карина"))
        self.table.setItem(0, 4, QTableWidgetItem("Галина"))
        self.table.setItem(0, 5, QTableWidgetItem("Яков"))

        self.table.setItem(1, 0, QTableWidgetItem("Первый"))
        self.table.setItem(2, 0, QTableWidgetItem("Второй"))
        self.table.setItem(3, 0, QTableWidgetItem("Третий"))
        self.table.setItem(4, 0, QTableWidgetItem("Четвертый"))
        self.table.setItem(5, 0, QTableWidgetItem("Пятый"))

        # Устанавливаем "Рустам" только для чтения
        item = QTableWidgetItem("Рустам")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 1, item)

        # Устанавливаем "Эдуард" только для чтения
        item = QTableWidgetItem("Эдуард")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 2, item)

        # Устанавливаем "Карина" только для чтения
        item = QTableWidgetItem("Карина")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 3, item)

        # Устанавливаем "Галина" только для чтения
        item = QTableWidgetItem("Галина")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 4, item)

        # Устанавливаем "Яков" только для чтения
        item = QTableWidgetItem("Яков")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(0, 5, item)

        # Устанавливаем "Первый" только для чтения
        item = QTableWidgetItem("Первый")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(1, 0, item)

        # Устанавливаем "Второй" только для чтения
        item = QTableWidgetItem("Второй")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(2, 0, item)

        # Устанавливаем "Третий" только для чтения
        item = QTableWidgetItem("Третий")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(3, 0, item)

        # Устанавливаем "Четвертый" только для чтения
        item = QTableWidgetItem("Четвертый")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(4, 0, item)

        # Устанавливаем "Пятый" только для чтения
        item = QTableWidgetItem("Пятый")
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.table.setItem(5, 0, item)

        # Создаем группы для каждой строки
        self.group1 = QButtonGroup()
        self.group2 = QButtonGroup()
        self.group3 = QButtonGroup()
        self.group4 = QButtonGroup()
        self.group5 = QButtonGroup()


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
        self.radio17 = QRadioButton()
        self.radio17.setAutoExclusive(False)
        self.radio18 = QRadioButton()
        self.radio18.setAutoExclusive(False)
        self.radio19 = QRadioButton()
        self.radio19.setAutoExclusive(False)
        self.radio20 = QRadioButton()
        self.radio20.setAutoExclusive(False)
        self.radio21 = QRadioButton()
        self.radio21.setAutoExclusive(False)
        self.radio22 = QRadioButton()
        self.radio22.setAutoExclusive(False)
        self.radio23 = QRadioButton()
        self.radio23.setAutoExclusive(False)
        self.radio24 = QRadioButton()
        self.radio24.setAutoExclusive(False)
        self.radio25 = QRadioButton()
        self.radio25.setAutoExclusive(False)

        self.group1.addButton(self.radio1)
        self.group1.addButton(self.radio2)
        self.group1.addButton(self.radio3)
        self.group1.addButton(self.radio4)
        self.group1.addButton(self.radio5)
        self.group2.addButton(self.radio6)
        self.group2.addButton(self.radio7)
        self.group2.addButton(self.radio8)
        self.group2.addButton(self.radio9)
        self.group2.addButton(self.radio10)
        self.group3.addButton(self.radio11)
        self.group3.addButton(self.radio12)
        self.group3.addButton(self.radio13)
        self.group3.addButton(self.radio14)
        self.group3.addButton(self.radio15)
        self.group4.addButton(self.radio16)
        self.group4.addButton(self.radio17)
        self.group4.addButton(self.radio18)
        self.group4.addButton(self.radio19)
        self.group4.addButton(self.radio20)
        self.group5.addButton(self.radio21)
        self.group5.addButton(self.radio22)
        self.group5.addButton(self.radio23)
        self.group5.addButton(self.radio24)
        self.group5.addButton(self.radio25)



        self.table.setCellWidget(1, 1, self.radio1)
        self.table.setCellWidget(1, 2, self.radio2)
        self.table.setCellWidget(1, 3, self.radio3)
        self.table.setCellWidget(1, 4, self.radio4)
        self.table.setCellWidget(1, 5, self.radio5)
        self.table.setCellWidget(2, 1, self.radio6)
        self.table.setCellWidget(2, 2, self.radio7)
        self.table.setCellWidget(2, 3, self.radio8)
        self.table.setCellWidget(2, 4, self.radio9)
        self.table.setCellWidget(2, 5, self.radio10)
        self.table.setCellWidget(3, 1, self.radio11)
        self.table.setCellWidget(3, 2, self.radio12)
        self.table.setCellWidget(3, 3, self.radio13)
        self.table.setCellWidget(3, 4, self.radio14)
        self.table.setCellWidget(3, 5, self.radio15)
        self.table.setCellWidget(4, 1, self.radio16)
        self.table.setCellWidget(4, 2, self.radio17)
        self.table.setCellWidget(4, 3, self.radio18)
        self.table.setCellWidget(4, 4, self.radio19)
        self.table.setCellWidget(4, 5, self.radio20)
        self.table.setCellWidget(5, 1, self.radio21)
        self.table.setCellWidget(5, 2, self.radio22)
        self.table.setCellWidget(5, 3, self.radio23)
        self.table.setCellWidget(5, 4, self.radio24)
        self.table.setCellWidget(5, 5, self.radio25)

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

        self.resize(820, 400)
        self.setWindowTitle("Логическая задача")
        self.setLayout(layout)

    def check_answers(self):

        radio_1_1 = self.table.cellWidget(1, 1)
        radio_2_4 = self.table.cellWidget(2, 4)
        radio_3_2 = self.table.cellWidget(3, 2)
        radio_4_5 = self.table.cellWidget(4, 5)
        radio_5_3 = self.table.cellWidget(5, 3)

        if radio_1_1.isChecked() and radio_2_4.isChecked() and radio_3_2.isChecked() and radio_4_5.isChecked() and radio_5_3.isChecked():
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


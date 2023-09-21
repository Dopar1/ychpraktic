import sys
from PyQt5.QtWidgets import QRadioButton, QButtonGroup
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox)


class LogicTable2(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        # При нажатии на кнопку
        self.check_btn.clicked.connect(self.check_answers)

    def initUI(self):
        # Текст задачи
        self.task_text = QLabel("""
В бутылке, стакане, кувшине и банке находятся молоко, лимонад, квас и вода. 
Известно, что вода и молоко не в бутылке, сосуд с лимонадом стоит между кувшином и сосудом с квасом, 
в банке – не лимонад и не вода. 
Стакан стоит около банки и сосуда с молоком.
Куда налита каждая жидкость?
            """)

        # Таблица
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(5)

        # Заполняем заголовки
        self.table.setItem(0, 1, QTableWidgetItem("Бутылка"))
        self.table.setItem(0, 2, QTableWidgetItem("Стакан"))
        self.table.setItem(0, 3, QTableWidgetItem("Кувшин"))
        self.table.setItem(0, 4, QTableWidgetItem("Банка"))

        self.table.setItem(1, 0, QTableWidgetItem("Молоко"))
        self.table.setItem(2, 0, QTableWidgetItem("Лимонад"))
        self.table.setItem(3, 0, QTableWidgetItem("Квас"))
        self.table.setItem(4, 0, QTableWidgetItem("Вода"))

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

        # Размещаем в вертикальном layout
        layout = QVBoxLayout()

        # Текст задачи
        layout.addWidget(self.task_text)

        # Таблица и кнопка в горизонтальном layout
        table_layout = QHBoxLayout()
        table_layout.addWidget(self.table)
        table_layout.addWidget(self.check_btn)

        layout.addLayout(table_layout)

        self.resize(620, 300)
        self.setWindowTitle("Логическая задача")
        self.setLayout(layout)

    def check_answers(self):

        radio_1_3 = self.table.cellWidget(1, 3)
        radio_2_1 = self.table.cellWidget(2, 1)
        radio_3_4 = self.table.cellWidget(3, 4)
        radio_4_2 = self.table.cellWidget(4, 2)

        if radio_1_3.isChecked() and radio_2_1.isChecked() and radio_3_4.isChecked() and radio_4_2.isChecked():
            QMessageBox.information(self, "Результат", "Ответ верный!")
        else:
            QMessageBox.warning(self, "Результат", "Ответ неверный")


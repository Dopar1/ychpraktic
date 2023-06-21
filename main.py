import sys # импортируем модуль sys

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QRegion
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFileDialog, QMessageBox, QScrollArea, QLabel, QGridLayout, QCheckBox, QTextEdit)

class LogicHelperApp(QMainWindow): 
    def __init__(self): 
        super().__init__()  

        self.setWindowTitle("Logic Helper")   

        main_layout = QVBoxLayout()  

        self.task_description = QTextEdit() 
        self.task_description.setPlaceholderText("Введите задачу здесь...")
        main_layout.addWidget(self.task_description)   

        button_layout = QHBoxLayout()   

        self.add_variable_a_button = QPushButton("+ Создать переменную A")
        self.add_variable_a_button.clicked.connect(self.add_variable_a) 
        button_layout.addWidget(self.add_variable_a_button) 

        self.add_variable_b_button = QPushButton("+ Создать переменную B")
        self.add_variable_b_button.clicked.connect(self.add_variable_b)
        button_layout.addWidget(self.add_variable_b_button)

        main_layout.addLayout(button_layout)

        self.grid_layout = QGridLayout()
        main_layout.addLayout(self.grid_layout)

        self.save_button = QPushButton("Сохранить решение")
        self.save_button.clicked.connect(self.save_solution)
        main_layout.addWidget(self.save_button)

        central_widget = QWidget() 
        central_widget.setLayout(main_layout)   

        scroll_area = QScrollArea() 
        scroll_area.setWidgetResizable(True)  
        scroll_area.setWidget(central_widget)

        self.setCentralWidget(scroll_area)  

        self.variable_a_count = 0 
        self.variable_b_count = 0  

    def add_variable_a(self):
        variable_a_input = QLineEdit()
        variable_a_input.setPlaceholderText(f"Введите переменную A{self.variable_a_count + 1} здесь...")
        self.grid_layout.addWidget(variable_a_input, self.variable_a_count + 1, 0)
        self.variable_a_count += 1

        for i in range(self.variable_b_count):
            checkbox = QCheckBox()
            self.grid_layout.addWidget(checkbox, self.variable_a_count, i + 1)

    def add_variable_b(self):  
        variable_b_input = QLineEdit()  
        variable_b_input.setPlaceholderText(f"Введите переменную B{self.variable_b_count + 1} здесь...")
        self.grid_layout.addWidget(variable_b_input, 0, self.variable_b_count + 1) 
        self.variable_b_count += 1  

        for i in range(self.variable_a_count):
            checkbox = QCheckBox()
            self.grid_layout.addWidget(checkbox, i + 1, self.variable_b_count) 

    def save_solution(self):  
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить решение", "", "PNG файл (*.png)") 
        if file_name:  
            if not file_name.endswith(".png"): 
                file_name += ".png"

           
            screenshot = QPixmap(self.size())
            self.render(screenshot, QPoint(), QRegion(self.rect()))

            
            screenshot.save(file_name, "PNG")
            QMessageBox.information(self, "Сохранено", f"Решение сохранено в файле {file_name}")  
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось сохранить решение") 

def main():
    app = QApplication(sys.argv)  
    logic_helper_app = LogicHelperApp()
    logic_helper_app.show()  
    sys.exit(app.exec_()) 

if __name__ == "__main__": 
    main()
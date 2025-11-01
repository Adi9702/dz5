
# Тема: Десктопные приложения 1 ч.  Знакомство PyQt6. Понятия Декомпозици

# Десктопные приложения - это
# PyQt6 - это библиотека декстопных программ

# python3 -m venv venv - чтобы открыть венв
# source venv/bin/activate - активировать венв 

# pip freeze > "и название файла" - это чтобы импортировать на случай если случайно удалим, короче резеврное копирование
# ppi install -r. "и название файла" - чтобы разом скачать библиотеку которую удалил

# бэкаб - это резервное копирование 

# д композиция - это разделение кода на мелкие

# два вида расположения Q / H 

# GUI - 


import sys
# это чтобы передавайть аргументы 

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication(sys.argv)
# здесь мы запускаем

window = QWidget()
# импорт окна 
window.setWindowTitle("Простое окно")

label = QLabel("Привет, PyQt6!")
# это надпись в окне
button = QPushButton("Нажми меня")
# компановщик вертикально и горизонтально

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

window.show()
# это значит показать окно
sys.exit(app.exec())
# тут запускаем главный цикл событий (exec завершаем коректно) 


import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно с декомпозицией")
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Привет, группа 32-1В")
        self.button = QPushButton("Нажми меня!")
        self.button.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        self.label.setText("Кнопка нажата!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
if __name__ == "__main__":
    main()

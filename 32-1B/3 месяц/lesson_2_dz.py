
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout 

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Введите тест:")
        self.line = QLineEdit()
        self.button = QPushButton("Нажмите кнопку")
        self.button.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        text = self.line.text() 
        self.label.setText(f"Вы ввели: {text}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
if __name__ == "__main__":
    main()

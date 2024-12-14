from PySide6 import QtWidgets
import sys
from db.database import Database

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()

# Установка заголовка главного окна
window.setWindowTitle("PySide6 Application")

# Установка размеров главного окна
window.resize(300, 250)

conn = Database()

sum = conn.get_sum_sales("База Строитель")

# Создание метки (надписи) с текстом "Hello World!"
lbl = QtWidgets.QLabel(f"{sum}")


# Создание кнопки с надписью "Close"
btn = QtWidgets.QPushButton("Close")

# Создание вертикального блока для размещения метки и кнопки
# Вертикальный блок из себя представляет контейнер в который мы помещаем элементы
box = QtWidgets.QVBoxLayout()

# Добавление метки и кнопки в вертикальный блок
box.addWidget(lbl)
box.addWidget(btn)

# Установка вертикального блока в качестве компоновщика главного окна
window.setLayout(box)

# Подключение обработчика события "clicked" кнопки к методу app.quit, вызывающему завершение приложения
btn.clicked.connect(app.quit)

# Отображение главного окна
window.show()

# Запуск основного цикла обработки событий приложения
sys.exit(app.exec())
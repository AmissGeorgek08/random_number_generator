from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Random Number Generator')
button = QPushButton('Generate')
text = QLabel('Click to generate a random number (0 - 99)')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)

def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Number:')

button.clicked.connect(show_winner)

main_win.resize(425, 250)
main_win.show()
app.exec_()
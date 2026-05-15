from PyQt6.QtWidgets import (QApplication,
                             QGridLayout,
                             QHBoxLayout,
                             QWidget,
                             QLabel
                             )
from PyQt6.QtGui import QPixmap
from pathlib import Path

logo_path = Path(__file__).parent / 'photo' / 'logo.png'
logo_label  = QLabel()
logo = QPixmap(str(logo_path))

app = QApplication([])
window = QWidget()

layout = QGridLayout()
switch_layout =  QHBoxLayout()

window.setLayout(layout)
layout.addLayout(switch_layout, 2, 0)

window.resize(500, 700)


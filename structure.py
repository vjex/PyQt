from PyQt4.QtCore import *
from PyQt4.QtGui import  *
import sys

class Helloworld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()

        label = QLabel("Hello World")
        line_edit= QLineEdit()
        button = QPushButton("close")

        layout.addWidget(label,0,0)
        layout.addWidget(line_edit,0,1)
        layout.addWidget(button,1,1)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(label.setText)
app = QApplication(sys.argv)
dialog=Helloworld()
dialog.show()
app.exec_()

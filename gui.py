import random
import sys
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from uic5 import Ui_Form


class Example(QWidget):

    def __init__(self, data, nrows):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.nrows = nrows
        self.data = data

        # Button Connections
        self.ui.generate_button.clicked.connect(self.getRandomRecipe)
        self.ui.quit_button.clicked.connect(self.close)

    def getRandomRecipe(self):
        randNum = random.randint(0, self.nrows - 1)
        data = self.data

        print(randNum)
        self.ui.recipe_label.setText(f"""
            <div>
            <b>{data["title"][randNum]}</b><br><br>
            <b>Ingredients: </b> \n {data["ingredients"][randNum]}<br><br>
            <b>Directions:</b> \n {data["directions"][randNum]}<br><br>
            <b>Link to Recipe: </b> {data["link"][randNum]}<br><br>
            <b>Tags: </b>{data["NER"][randNum]}<br><br>
            <b>Home Website: </b>{data["site"][randNum]}<br><br>
        </div> """)


def main(data, nrows):
    app = QApplication(sys.argv)
    window = Example(data, nrows)
    window.setWindowIcon(QIcon("chicken.JPG"))
    window.setStyleSheet("""
    QWidget {
        background-color: #36393e;
        color: white;
    }
    QPushButton {
        border: 3px solid #858AE3;
        border-radius: 20px;
        padding: 20px;
    }
    QPushButton:hover{
        background-color: #858AE3;
        border: 3px solid #858AE3;
        border-radius: 20px;
        padding: 20px;
    }
    """)


    window.show()

    sys.exit(app.exec_())

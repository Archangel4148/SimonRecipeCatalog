
#To get updated gui:
#pyuic5 '.\heck yeah.ui' -o uic5.py




import random
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

from SimonRecipeCatalog.uic5 import Ui_Form


class RecipeGenerator(QWidget):

    def __init__(self, data, nrows, recipeCount, currentIndex, recipeCache):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.nrows = nrows
        self.data = data
        self.recipeCount = recipeCount
        self.currentIndex = currentIndex
        self.recipeCache = recipeCache


        # Button Connections
        self.ui.generate_button.clicked.connect(self.getRandomRecipe)
        self.ui.previous_button.clicked.connect(self.getPreviousRecipe)
        self.ui.quit_button.clicked.connect(self.close)

    def getRandomRecipe(self):

        #if we are at the end of the list:
        if self.currentIndex == self.recipeCount - 1:
            randNum = random.randint(0, self.nrows - 1)
            self.currentIndex += 1
            self.recipeCount += 1
            self.recipeCache.append(randNum)
        #if we are at a previous recipe:
        else:
            self.currentIndex += 1
            randNum = self.recipeCache[self.currentIndex]

        data = self.data


        self.printRecipe(data, randNum)


    def getPreviousRecipe(self):
        if self.currentIndex < 1:
            pass
        else:
            self.currentIndex -= 1
            self.printRecipe(self.data, self.recipeCache[self.currentIndex])

    def printRecipe(self, data, randNum):
        # print(randNum)
        self.ui.recipe_label.setText(f"""
                    <div>
                    <b>{data["title"][randNum]}</b><br><br>
                    <b>Ingredients: </b> \n {data["ingredients"][randNum]}<br><br>
                    <b>Directions:</b> \n {data["directions"][randNum]}<br><br>
                    <b>Link to Recipe: </b> {data["link"][randNum]}<br><br>
                    <b>Tags: </b>{data["NER"][randNum]}<br><br>
                    <b>Home Website: </b>{data["site"][randNum]}<br><br>
                    
                </div> """)



def main(data, nrows, recipeIndex, currentIndex, recipeCache):
    app = QApplication(sys.argv)
    window = RecipeGenerator(data, nrows, recipeIndex, currentIndex, recipeCache)
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

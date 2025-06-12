import ast
import sys

import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from recipe_generator import RecipeCatalogWindow

# Load and pre-process the data
nrows = 1000
data = pd.read_csv("recipes_data.csv", nrows=nrows)
data.drop(columns=["source"])

# Stringified lists
data["ingredients"] = data["ingredients"].apply(ast.literal_eval).apply(lambda x: '\n'.join(x))
data["directions"] = data["directions"].apply(ast.literal_eval).apply(lambda x: '\n'.join(x))
data["NER"] = data["NER"].apply(ast.literal_eval).apply(lambda x: ', '.join(x))

# Create the application
app = QApplication(sys.argv)
window = RecipeCatalogWindow(data)
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

# Show the application
window.show()
sys.exit(app.exec_())

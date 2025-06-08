import ast
import sys

import pandas as pd
import random

from PyQt5.QtWidgets import QApplication

from gui import main, Example


def main(data, nrows):
    app = QApplication(sys.argv)
    ex = Example(data, nrows)

    # print(ex.label.text())

    # ex.label.setText(recipe)

    sys.exit(app.exec_())

nrows = 20000
data = pd.read_csv("recipe catalog raw/recipes_data.csv", nrows=nrows)
data.drop(columns=["source"])
#Stringified lists

data["ingredients"] = data["ingredients"].apply(ast.literal_eval)
data["directions"] = data["directions"].apply(ast.literal_eval)
data["NER"] = data["NER"].apply(ast.literal_eval)

data["ingredients"] = data["ingredients"].apply(lambda x: '\n'.join(x))
data["directions"] = data["directions"].apply(lambda x: '\n'.join(x))
data["NER"] = data["NER"].apply(lambda x: ', '.join(x))



# main(f'{data["title"][0]} \n {data["ingredients"][0]}' )

main(data, nrows)
#Check for Source
# source_data = pd.read_csv("recipe catalog raw/recipes_data.csv", nrows=2000000)
# source_data = source_data["source"]
# i = 0
# while i < len(source_data):
#     if source_data[i] != "Gathered":
#         print(source_data[i])
#     i += 1
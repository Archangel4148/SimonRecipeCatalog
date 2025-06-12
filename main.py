import ast

import pandas as pd

from gui import main

nrows = 1000
data = pd.read_csv("recipe catalog raw/recipes_data.csv", nrows=nrows)
data.drop(columns=["source"])

# Stringified lists
data["ingredients"] = data["ingredients"].apply(ast.literal_eval)
data["directions"] = data["directions"].apply(ast.literal_eval)
data["NER"] = data["NER"].apply(ast.literal_eval)

data["ingredients"] = data["ingredients"].apply(lambda x: '\n'.join(x))
data["directions"] = data["directions"].apply(lambda x: '\n'.join(x))
data["NER"] = data["NER"].apply(lambda x: ', '.join(x))

recipeCount = 0
#This is -1 because the first item saved is saved in recipeCache[currentIndex+1], or zero
currentIndex = -1
recipeCache = []
main(data, nrows, recipeCount, currentIndex, recipeCache)

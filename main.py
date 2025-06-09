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

main(data, nrows)

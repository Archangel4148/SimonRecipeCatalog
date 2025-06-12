import random

from PyQt5.QtWidgets import QWidget

from uic5 import Ui_Form


class RecipeCatalogWindow(QWidget):

    def __init__(self, data, max_cache_size=None):
        super().__init__()

        # Create the UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Data
        self.data = data
        self.max_cache_size = max_cache_size
        self.nrows: int = self.data.shape[0]  # Length of the data
        self.currentIndex: int = -1  # Start at -1 because the first item is saved in recipeCache[currentIndex+1]
        self.recipeCache: list = []  # Storage for loaded recipe indices

        # Button Connections
        self.ui.generate_button.clicked.connect(self.handle_generate_button)
        self.ui.previous_button.clicked.connect(self.handle_previous_button)
        self.ui.quit_button.clicked.connect(self.close)

    def get_random_index(self) -> int | None:
        # Get a random number that is not in the cache
        random_index = None

        if len(self.recipeCache) == self.nrows:
            # If we have loaded all recipes, return None
            return None

        while random_index is None or random_index in self.recipeCache:
            random_index = random.randint(0, self.nrows - 1)

        return random_index

    def handle_generate_button(self):
        if self.currentIndex == len(self.recipeCache) - 1:
            # Get a new random index
            new_index = self.get_random_index()

            if new_index is None:
                # If we have loaded all recipes, do nothing
                return

            # Add the new index to the cache and display
            self.recipeCache.append(new_index)
            # Limit the size of the cache
            if self.max_cache_size is not None and len(self.recipeCache) > self.max_cache_size:
                self.recipeCache.pop(0)
                self.currentIndex -= 1
            self.display_recipe(new_index)

        else:
            # Display the next recipe in the cache
            self.display_recipe(self.recipeCache[self.currentIndex + 1])

        # Increment the current index
        self.currentIndex += 1

    def handle_previous_button(self):
        # Go to the previous recipe and display
        if self.currentIndex < 1:
            # Ignore presses if we are at the first recipe
            pass
        else:
            self.currentIndex -= 1
            self.display_recipe(self.recipeCache[self.currentIndex])

    def display_recipe(self, recipe_index: int):
        # Display the recipe at the given index
        self.ui.recipe_label.setText(
            f"""
            <div>
            <b>{self.data["title"][recipe_index]}</b><br><br>
            <b>Ingredients: </b> \n {self.data["ingredients"][recipe_index]}<br><br>
            <b>Directions:</b> \n {self.data["directions"][recipe_index]}<br><br>
            <b>Link to Recipe: </b> {self.data["link"][recipe_index]}<br><br>
            <b>Tags: </b>{self.data["NER"][recipe_index]}<br><br>
            <b>Home Website: </b>{self.data["site"][recipe_index]}<br><br>
            </div> """
        )

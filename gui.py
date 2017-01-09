################################
# gui.py
# Noah Ansel
# 2017-01-08
# ------------------------------
# GUI interface for recipes file.
################################

from tkinter import *
from recipes import *

class MainView(Frame):

  def __init__(self, master, recipeBook = None):
    super().__init__(master)
    if recipeBook == None:
      self._recipeBook = RecipeBook()
    else:
      self._recipeBook = recipeBook
    self._create_widgets()
    self._update()

  def _create_widgets(self):
    self._bookDisplay = Text(self, state = DISABLED, width = 70)
    self._weekDisplay = Text(self, state = DISABLED, width = 70)
    self._getWeekRecipesButton = Button(self,
                                        text = "Get Week Recipes",
                                        command = self._on_getWeekRecipes_click)
    self._recipeBookLabel = Label(self,
                                  justify = LEFT,
                                  text = "Recipes: {}".format(len(self._recipeBook.recipes)))

    # place widgets
    self._bookDisplay.grid(row = 0, column = 0, sticky = N+S)
    self._weekDisplay.grid(row = 0, column = 1)
    self._getWeekRecipesButton.grid(row = 1, column = 1, sticky = W+E)
    self._recipeBookLabel.grid(row = 1, column = 0, sticky = W)

  def _update(self):
    self._bookDisplay.config(state = NORMAL)
    self._bookDisplay.delete(1.0, END)
    self._bookDisplay.insert(END, str(self._recipeBook))
    self._bookDisplay.config(state = DISABLED)

  def _on_getWeekRecipes_click(self):
    ret = self._recipeBook.getWeekRecipes()
    retStr = ""
    for item in ret:
      retStr += str(item) + "\n"

    self._weekDisplay.config(state = NORMAL)
    self._weekDisplay.delete(1.0, END)
    self._weekDisplay.insert(END, retStr)
    self._weekDisplay.config(state = DISABLED)

    self._recipeBookLabel.config(text = "Recipes: {}".format(len(self._recipeBook.recipes)))

    self._update()


if __name__ == "__main__":
  sampleBook = RecipeBook([Recipe("Pork Chops", RecipeCatagory.pork, True, yesterday),
                           Recipe("Spaghetti", RecipeCatagory.groundBeef),
                           Recipe("Baked Lasagna", RecipeCatagory.groundBeef),
                           Recipe("Mushroom Meatballs", RecipeCatagory.groundBeef, True, lastUsed = today),
                           Recipe("Sloppy Joes", RecipeCatagory.groundBeef, lastUsed = today),
                           Recipe("Beef Ragu with Ravioli", RecipeCatagory.groundBeef),
                           Recipe("Hamburger Cutlets", RecipeCatagory.groundBeef, True),
                           Recipe("Chili con Carne", RecipeCatagory.groundBeef),
                           Recipe("Spinach Pesto Manicotti", RecipeCatagory.groundBeef),
                           Recipe("Tomato Meatloaf", RecipeCatagory.groundBeef, lastUsed = today),
                           Recipe("Sloppy BBQ Joes", RecipeCatagory.groundBeef),
                           Recipe("Meatball Garden Skillet", RecipeCatagory.groundBeef),
                           Recipe("Sicilian Meat Roll", RecipeCatagory.groundBeef),
                           Recipe("Mommy's Surprise", RecipeCatagory.groundBeef),
                           Recipe("One-Pot Pasta", RecipeCatagory.groundBeef),
                           Recipe("Beef & Macaroni Casserole", RecipeCatagory.groundBeef),
                           Recipe("Somethin' Good", RecipeCatagory.groundBeef),
                           Recipe("Chicken with Cider and Bacon Sauce", RecipeCatagory.groundBeef),
                           Recipe("Goat Cheese Stuffed Chicken Breasts", RecipeCatagory.poultry, True),
                           Recipe("Tandoori-Style Chicken", RecipeCatagory.poultry),
                           Recipe("Prosciutto Chicken Cacciatore", RecipeCatagory.poultry),
                           Recipe("Mexican Party Wings", RecipeCatagory.poultry),
                           Recipe("Chicken in a Skillet"),
                           Recipe("Turkey with a Twist"),
                           Recipe("Stuffed Chicken Rolls", lastUsed = lastWeek),
                           Recipe("Chicken Tetrazzini", favorite = True, lastUsed = lastMonth),
                           Recipe("Chicken au Poivre"),
                           Recipe("Baked Chicken with Orzo", favorite = True),
                           Recipe("Chicken-Rice Casserole", lastUsed = lastMonth),
                           Recipe("Asian Turkey Lettuce Wraps", favorite = True, lastUsed = yesterday),
                           Recipe("Cornish Hens A'L'Orange", RecipeCatagory.poultry, lastUsed = today),
                           Recipe("Pork Cacciatore", favorite = True),
                           Recipe("Pork Stew"),
                           Recipe("Pork Stew in Green Salsa (Guisado de Puerco con Tomatillos)"),
                           Recipe("Stromboli", RecipeCatagory.pork, favorite = True, lastUsed = lastMonth),
                           Recipe("Modenese Pork Chops"),
                           Recipe("Orange Pork with Scallions"),
                           Recipe("Easy Smoked Sausage Skillet", RecipeCatagory.pork),
                           Recipe("Chipotle's Steak Marinade", RecipeCatagory.pork),
                           Recipe("Chow Mein", RecipeCatagory.pork),
                           Recipe("Pear and Pork Stir-Fry"),
                           Recipe("Upside-Down Pizza", RecipeCatagory.pork),
                           Recipe("Sweet and Sour Pork")])

  root = Tk()
  root.title("Recipe Generator")
  mv = MainView(root, sampleBook)
  mv.pack()

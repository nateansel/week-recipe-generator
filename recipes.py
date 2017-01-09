#
#
#
#
#
#
#

import datetime
import random
from enum import Enum

threeWeeks = 60 * 60 * 24 * 7 * 3 # number of seconds in 3 weeks

class RecipeCatagory(Enum):
    groundBeef = "Ground Beef"
    beef       = "Beef"
    pork       = "Pork"
    fish       = "Fish"
    poultry    = "Poultry"
    vegetarian = "Vegetarian"
recipeCatagories = [RecipeCatagory.groundBeef,
                    RecipeCatagory.beef,
                    RecipeCatagory.pork,
                    RecipeCatagory.fish,
                    RecipeCatagory.poultry,
                    RecipeCatagory.vegetarian]

class RecipeCatagoryPreference:
    def __init__(self, catagory = None, number = 0):
        self.catagory = catagory
        self.number   = number

    def __str__(self):
        return str(number) + " x " + catagory.value

class Recipe:
    def __init__(self, title = "", catagory = None, favorite = False, lastUsed = None):
        self.title    = title
        self.catagory = catagory
        self.favorite = favorite
        self.lastUsed = lastUsed
        if self.catagory == None and self.title:
            lowerTitle = self.title.lower()
            if "chicken" in lowerTitle or "turkey" in lowerTitle:
                self.catagory = RecipeCatagory.poultry
            if "pork" in lowerTitle:
                self.catagory = RecipeCatagory.pork
            if "beef" in lowerTitle:
                self.catagory = RecipeCatagory.beef
            if "fish" in lowerTitle or "salmon" in lowerTitle or "mahi mahi" in lowerTitle or "flounder" in lowerTitle:
                self.catagory = RecipeCatagory.fish
            if "vegetarian" in lowerTitle:
                self.catagory = RecipeCatagory.vegetarian

    def __str__(self):
        string = ""
        if self.favorite:
            string += "* "
        else:
            string += "  "
        string += self.title
        if self.lastUsed:
            string += self.lastUsed.strftime("\n    %b %d, %Y")
        return string

class RecipeBook:
    def __init__(self, recipes = []):
        self.recipes = recipes

    def __str__(self):
        toReturn = ""
        for i in range(len(self.recipes)):
            toReturn += str(self.recipes[i])
            if i != len(self.recipes) - 1:
                toReturn += "\n"
        return toReturn

    def getFavorites(self):
        return [item for item in self.recipes if item.favorite]

    def getRegulars(self):
        return [item for item in self.recipes if not item.favorite]

    def getContentsOfCatagory(self, catagory = None):
        if catagory:
            recipesInCatagory = []
            for recipe in self.recipes:
                if recipe.catagory == catagory:
                    recipesInCatagory.append(recipe)
            return recipesInCatagory
        else:
            print("Error, no catagory provided.")

    def printByCatagory(self):
        toPrint = ""
        printedRecipes = []
        for each in recipeCatagories:
            recipesInCatagory = self.getContentsOfCatagory(each)
            printedRecipes += recipesInCatagory
            if len(recipesInCatagory) > 0:
                toPrint += each.value + "\n"
                for i in range(len(recipesInCatagory)):
                    toPrint += str(recipesInCatagory[i]) + "\n"
                toPrint += "\n"
        excludedRecipes = [item for item in self.recipes if item not in printedRecipes]
        if len(excludedRecipes) > 0:
            toPrint += "No Catagory\n"
            for i in range(len(excludedRecipes)):
                toPrint += str(excludedRecipes[i]) + "\n"
        else:
            toPrint.strip()
        if toPrint == "":
            print("Empty RecipeBook")
        else:
            print(toPrint)

    def getRandomFavorites(self, count = 1):
        return self.__getRandomRecipes(self.getFavorites(), count)

    def getRandomRegulars(self, count = 1):
        return self.__getRandomRecipes(self.getRegulars(), count)

    def __getRandomRecipes(self, recipes = [], count = 0):
        if count == 0:
            return []
        toReturn = []
        recentRecipes = []
        random.shuffle(recipes)
        while len(recipes) > 0:
            recipe = recipes.pop()
            if recipe.lastUsed and (datetime.date.today() - recipe.lastUsed).days > 21:
                toReturn.append(recipe)
            elif recipe.lastUsed == None:
                toReturn.append(recipe)
            else:
                recentRecipes.append(recipe)
            if len(toReturn) == count:
                break
        if len(toReturn) < count:
            recentRecipes.sort(key=lambda recipe: recipe.lastUsed)
            recentRecipes.reverse()
            while len(recentRecipes) > 0:
                toReturn.append(recentRecipes.pop())
                if len(toReturn) == count:
                    break
        return toReturn

    def getWeekRecipes(self):
        favorites = self.getRandomFavorites(2)
        regulars = self.getRandomRegulars(7 - len(favorites))
        weekRecipes = favorites + regulars
        random.shuffle(weekRecipes)
        return weekRecipes

    def repickRecipeAtIndex(self, recipes, index):
        recipeToReplace = recipes[index]
        if recipeToReplace.favorite:
            found = False
            while not found:
                newRecipe = self.getRandomFavorites(1)[0]
                if newRecipe not in recipes:
                    found = True
                    recipes[index] = newRecipe
        else:
            found = False
            while not found:
                newRecipe = self.getRandomRegulars(1)[0]
                if newRecipe not in recipes:
                    found = True
                    recipes[index] = newRecipe

today     = datetime.date.today()
yesterday = datetime.date(today.year, today.month, today.day - 1)
lastWeek  = datetime.date(today.year, today.month, today.day - 7)
lastMonth = datetime.date(today.year - 1, 12, today.day)

def getDate(days = 0):
    today = datetime.date.today()
    if days == 0:
        return today
    if days < 0:
        print("Error: Cannot generate date with negative days.")
        return
    minusYears  = 0
    minusMonths = 0
    minusDays   = days
    if today.day < days:
        minusDays -= today.day
        minusMonths += 1

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

sampleBook.printByCatagory()
print("")

preferences = []
while True:
    if len(preferences) > 0:
        print("Current Preferences:")
        for i in range(len(preferenses)):
            print(str(i + 1) + " " + str(preference))
        print("")
    print("")

week = sampleBook.getWeekRecipes()
weekBook = RecipeBook(week)
print("This week's dishes:")
weekBook.printByCatagory()
# for i in range(len(week)):
#     print(str(i + 1) + " " + str(week[i]))
# j = int(input("change selection (0 for no change): "))
# if j != 0:
#     if j > 0 and j < len(week):
#         sampleBook.repickRecipeAtIndex(week, j - 1)
# print("This week's dishes:")
# for i in range(len(week)):
#     print(str(i + 1) + " " + str(week[i]))

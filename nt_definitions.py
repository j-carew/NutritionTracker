# nt_definitions.py
# This module houses the collection of classes, functions, etc. used in the
# NutritionTracker project.

class Food:

# This class provides the framework for each food that is kept track of in the
# project.  The class will have properties for macronutrients, micronutrients, etc.
# about each food.

    def __init__(self, calories, fat, carbs, protein):
        # This initialization is basic for now.  It only contains macronutrients for the foods.
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def printNutrition(self):
        # This is a class function that displays the macronutrient amounts in the terminal.
        print("\033[92m"+"Calories: "+"\033[0m", self.calories,
              "\nTotal Fat: ", self.fat, "g",
              "\n  Total Carbs: ", self.carbs, "g",
              "\nProtein: ", self.protein, "g")


def addFood(food1, food2):
    # This is a function that allows the addition of nutrients between foods for an aggregation
    # of nutrients between multiple foods.
    sum_calories = food1.calories + food2.calories
    sum_fat = food1.fat + food2.fat
    sum_carbs = food1.carbs + food2.carbs
    sum_protein = food1.protein + food2.protein
    return Food(sum_calories, sum_fat, sum_carbs, sum_protein)

def mult(food1, scalar):
    # This is a multiplication function for foods. It will allow, for example, the addition of
    # multiple servings of a food without repetitive use of the "addFood" function.
    mult_calories = food1.calories * scalar
    mult_fat = food1.fat * scalar
    mult_carbs = food1.carbs * scalar
    mult_protein = food1.protein * scalar
    return Food(mult_calories, mult_fat, mult_carbs, mult_protein)

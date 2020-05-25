cookbook = {'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
            'meal': 'lunch', 'prep_time': 10},
            'cake': {'ingredients': ['flour', 'sugar', 'eggs'],
                     'meal': 'dessert', 'prep_time': 60},
            'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes',
                      'spinach'], 'meal': 'lunch', 'prep_time': 15}}


def print_recipe(name):
    if name not in cookbook:
        print("\nNot a recipe\n")
        return
    print("\nRecipe for cake:")
    print("Ingredients list: ", cookbook[name]['ingredients'])
    print("To be eaten for", cookbook[name]['meal'])
    print("Takes", cookbook[name]['prep_time'], "minutes of cooking.\n")


def del_recipe(name):
    if name not in cookbook:
        print("\nNot a recipe\n")
        return
    del cookbook[name]
    print("Recipe : " + name + " removed from the cookbook\n")


def add_recipe(name):
    if name in cookbook:
        print("\nalready in this cookbook\n")
        return
    cookbook[name] = {}
    prep_time = input("Write the preparation time of this recipe\n>> ")
    cookbook[name]['prep_time'] = prep_time
    meal = input("What is its type of meal ?\n>> ")
    cookbook[name]['meal'] = meal
    cookbook[name]['ingredients'] = []
    ingredients = ""
    while (not ingredients.isnumeric()):
        ingredients = input("Type an ingredient, enter any number to end\n>> ")
        if ingredients and not ingredients.isnumeric():
            cookbook[name]['ingredients'].append(ingredients)


def list_recipe():
    print('-' * 70)
    print("List of all the recipes of this cookbook:\n")
    for i in cookbook:
        print("--> " + i)
    print('-' * 70)


def main():
    choice = 0
    while (choice != 5):
        print("Please select an option by typing the corresponding number")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the the cookbook")
        print("5: Quit")
        choice = input(">> ")
        while (not choice.isnumeric() or
               (choice.isnumeric() and (int(choice) < 1 or int(choice) > 5))):
            print("This option does not exist, please type
                  the corresponding number.\nTo exit, enter 5.")
            choice = input(">> ")
        if int(choice) == 1:
            recipe = ""
            while (recipe == ""):
                recipe = input("Enter the recipe's name you want to add\n>> ")
            add_recipe(recipe)
        if int(choice) == 2:
            recipe = input("Enter the recipe's name to delete:\n>> ")
            del_recipe(recipe)
        if int(choice) == 3:
            recipe = input("Enter the recipe's name to get its details:\n>> ")
            print_recipe(recipe)
        if int(choice) == 4:
            list_recipe()
        if int(choice) == 5:
            print("Cookbook closed.")
            exit(0)


if __name__ == "__main__":
    main()

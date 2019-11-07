import sys
import time

sandwich_dic = {
    "ingredients": ["ham", "bread", "cheese", "tomatoes"],
    "meal": "lunch",
    "prep_time": "10"
}

cake_dic = {
    "ingredients": ["flour", "sugar", "eggs"],
    "meal": "dessert",
    "prep_time": "60"
}

salad_dic = {
    "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
    "meal": "lunch",
    "prep_time": "15"
}

cookbook = {
    "sandwich" : sandwich_dic,
    "cake" : cake_dic,
    "salad" : salad_dic
}

def printCookbook() :
    for x in cookbook :
        print (x)

# def printDicValue(dicName) :
#     for x in dicName :
#         print(dicName[x])

def printRecipe(recipeName) :
    print("Recipe for " + recipeName + ":")
    print("ingredients list:", cookbook[recipeName]["ingredients"])
    print("To be eaten for" , cookbook[recipeName]["meal"] + ".")
    print("Take" , cookbook[recipeName]["prep_time"] , "minutes of cooking.")

def addRecipe(recipeName, ingredientsList, mealType, prepTime) :
    dicName = recipeName+"_dic"
    dicName = dict(ingredients = ingredientsList, meal= mealType,
                        prep_time = prepTime)
    cookbook[recipeName] = dicName

def deleteRecipe(recipeName) :
    cookbook.pop(recipeName)


addRecipe('grec', ["meat", "tomatoes"], 'lunch', '15')
# printCookbook()
# printRecipe("grec")
# deleteRecipe("grec")
# printCookbook()

while 1 :
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    choice = input()
    if choice == "1" :
        # add recipe
        print("choix :", choice )
        print("Please enter the name of recipe:")
        recipeName = input()
        while cookbook.get(recipeName) :
            print("Please enter an other name of recipe:")
            recipeName = input()
        print("Please enter the type of dish:")
        mealType = input()
        print("Please entre the ingredients list separated by a comma',':")
        ingredientsList = input().split(',')
        
        addRecipe(recipeName, ingredientsList, mealType, prepTime)


    elif choice == "2":
        # delete recipe
        print("choix :", choice )
        print("Please enter the recipe's name to delete it:")
        recipe = input()
        if cookbook.get(recipe) :
            deleteRecipe(recipe)
            print("The recipe are deleted")
        else :
            print("Sorry the recipe does not existe")

    elif choice == "3":
        #  print recipe
        print("choix :", choice )
        print("Please enter the recipe's name to get its details:")
        recipe = input()
        if cookbook.get(recipe):
            printRecipe(recipe)
        else :
            print("Sorry the recipe does not exist")
    elif choice == "4":
        #  print cookbook
        printCookbook()

    elif choice == "5":
        print("Cookbook closed.")
        sys.exit()
        # quit
    else :
        print("Desole, aucune fonction ne correspond a votre choix,"
                    "veillez choisir un choix dans la list")
    time.sleep(2)
    print("###########################################################")
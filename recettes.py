def add_recipes(dictionnaire: dict) -> None:
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Entrez le nom de votre recette?\n")
    ingredients = input("Entrez la liste d'ingrédiants de la recette, svp séparer les ingrédiants par une ,\n").split(",")
    dictionnaire[name] = ingredients


def print_recipe(ingredients: dict) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Entrez le nom d'une recette?\n")

    if name in ingredients:
        print(ingredients[name])
    else:
        print("La recette demandée n'existe pas!")
        print(f"Les recettes existantes sont: {list(ingredients.keys())}")


def delete_recipe(dictionnaire: dict) -> None:
    name = input("Entrez le nom d'une recette?\n")
    if name in dictionnaire:
        del dictionnaire[name]
        print("Recette supprimée")
    else:
        print("La recette demandée n'existe pas!")
        print(f"Les recettes existantes sont: {list(dictionnaire.keys())}")

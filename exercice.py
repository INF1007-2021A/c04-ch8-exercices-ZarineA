#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from recettes import add_recipes, print_recipe, delete_recipe
import os

# TODO: Définissez vos fonction ici


def comparer_fichiers(nom_fichier1: str, nom_fichier2: str) -> str:
    difference = ""
    with open(nom_fichier1, 'r') as f1, open(nom_fichier2, 'r') as f2:
        while difference == "":
            car1 = f1.read(1)
            car2 = f2.read(1)
            if car1 == '' or car2 == '':
                difference = "Aucune différence"
            elif car1 != car2:
                difference = car1 + " / " + car2 + " à la position " + str(f1.tell())

    return difference


def recopier_fichier(nom_fichier: str) -> None:
    nom_copie = nom_fichier.removesuffix(".txt") + "-copie.txt"
    with open(nom_fichier, 'r') as original, open(nom_copie, 'w') as copie:
        for caractere in original.read():
            if caractere == ' ':
                copie.write(caractere * 3)
            else:
                copie.write(caractere)


def ecrire_mentions(nom_fichier: str) -> None:
    with open(nom_fichier, 'r') as notes, open("mentions.txt", 'w') as mentions:
        for note in notes:
            for mention in PERCENTAGE_TO_LETTER:
                bornes = PERCENTAGE_TO_LETTER[mention]
                if bornes[0] <= int(note) < bornes[1]:
                    mentions.write(mention + "\n")


def lire_fichier_recettes(nom_fichier_recettes: str) -> dict:
    if os.path.exists(nom_fichier_recettes):
        with open(nom_fichier_recettes, 'r') as fichier:
            livre_recettes = {}
            for recette in fichier:
                recette = recette.removesuffix("\n")
                pos_deux_points = recette.find(':')
                ingredients = recette[pos_deux_points + 1:].split(',')
                livre_recettes[recette[:pos_deux_points]] = ingredients
        return livre_recettes
    else:
        return {}


def ecrire_fichier_recettes(nom_fichier_recettes: str, livre_recettes: dict) -> None:
    with open(nom_fichier_recettes, 'w') as fichier:
        for numero, recette in enumerate(livre_recettes):
            fichier.write(recette + ":")
            for num, ingredient in enumerate(livre_recettes[recette]):
                fichier.write(ingredient)
                if num < len(livre_recettes[recette]) - 1:
                    fichier.write(",")
            if numero < len(livre_recettes) - 1:
                fichier.write("\n")


def consulter_livre_recettes(nom_fichier_recettes: str) -> None:
    livre = lire_fichier_recettes(nom_fichier_recettes)
    continuer = True
    print("\nLIVRE DE RECETTES\n")
    while continuer:
        print("\nQue voulez vous faire ?")
        print("- Ajouter une recette (a)")
        print("- Lire une recette (l)")
        print("- Supprimer une recette (s)")
        print("- Quitter (q)")
        choix = input("--> ")
        if choix == 'a':
            print()
            add_recipes(livre)
        elif choix == 'l':
            print()
            print_recipe(livre)
        elif choix == 's':
            print()
            delete_recipe(livre)
        elif choix == 'q':
            continuer = False
            print("\nAu revoir!\n")
        else:
            print("Saisie invalide")
    ecrire_fichier_recettes(nom_fichier_recettes, livre)


def lister_nombres(nom_fichier: str) -> list:
    with open(nom_fichier, 'r') as fichier:
        nombres = []
        nombre_courant = ""
        caractere = fichier.read(1)
        while caractere != '':
            if caractere.isdigit():
                nombre_courant += caractere
            else:
                if nombre_courant != "":
                    nombres.append(int(nombre_courant))
                    nombre_courant = ""
            caractere = fichier.read(1)
        nombres.sort()

        return nombres


def copier_moitie(nom_fichier: str) -> None:
    nom_copie = nom_fichier.removesuffix(".txt") + "-copie2.txt"
    with open(nom_fichier, 'r') as original, open(nom_copie, 'w') as copie:
        copier = True
        for ligne in original:
            if copier:
                copie.write(ligne)
                copier = False
            else:
                copier = True


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    # 1)
    premiere_difference = comparer_fichiers("exemple.txt", "exemple2.txt")
    print("La première différence entre les deux fichiers est :", premiere_difference)

    # 2)
    recopier_fichier("exemple.txt")

    # 3)
    ecrire_mentions("notes.txt")

    # 4)
    consulter_livre_recettes("recettes.txt")

    # 5)
    print("Les nombres présents dans le fichier sont :")
    print(lister_nombres("exemple.txt"))

    # 6)
    copier_moitie("exemple.txt")

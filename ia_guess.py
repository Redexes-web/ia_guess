from random import randint


# Fonction permetant de trouver la valeur moyenne entre deux autres valeur
def middle(n1, n2):
    if n1 < n2:
        diff = n2 - n1
        middle_ = round(diff/2) + n1
    else:
        diff = n1-n2
        middle_ = round(diff/2)+ n2
    return middle_


# my_range contient la valeur minimal et maximal du nombre aleatoire
my_range = [0, 100]
#rand represente le  nombre choisi aleatoirement
rand = randint(my_range[0], my_range[1])
#guesses est le tableau des suggestions faite par l'algo
guesses = [middle(my_range[0], my_range[1])]
#answer est la reponse courante de l'algo, elle a pour valeur initiale la moyenne de la valeur minimal et maximal
answer = middle(my_range[0], my_range[1])
#tries est le nombre d'essais realisé par l'algo pour trouver le nombre aleatoire
tries = 1

#find_nearest sert  a trouver le nombre le plus proche d'une valeur donné dans un tableau soit au dessus soit en dessous
#needle est la valeur donné
#haystack est le tableau dans lequel on va efectuer notre recherche
#range_ est un tableau qui sert a definir deux valeur minimale ou maximale pour rechercher la valeur needle
#below_or_above dois contenir la string:
#         "below" si on veux le chiffre inferieur le plus proche.
#         "above" si on veux le nombre superieur le plus proche
def find_nearest(needle, haystack, range_, below_or_above):
    nearest_value = (range_[0], range_[1])[below_or_above == "above"]
    if below_or_above == "below":
        for item in haystack:
            if needle > item > nearest_value:
                nearest_value = item
    else:
        for item in haystack:
            if needle < item < nearest_value:
                nearest_value = item
    return nearest_value


#tant que la reponse donné n'est pas la bonne
while answer != rand:
    #on incremente le compteur d'essais
    tries += 1
    #on definit below_above selon si la reponse est plus grande ou plus petite que le nombre donné precedament
    below_above = ("above", "below")[answer > rand]
    #on trouve le nombre le plus proche de notre reponse dans la liste de nombre deja essayés
    nearest = find_nearest(answer, guesses, my_range,  below_above)
    #on trouve la valeur moyenne entre notre ancienne reponse et la valeur la plus proche de cette derniere pour l'affecter a notre nouvelle reponse
    answer = middle(nearest, answer)
    #enfin on ajoute cette nouvelle reponse aux suppositions
    guesses.append(answer)
    #on retourne au debut de la boucle pour tester notre nouvelle reponse!

print("nombre d'essais: ",tries)
print("nombre aleatoire: ",rand)
print("derniere reponse donnée: ",answer)
print("liste de tous les essais: ", guesses)

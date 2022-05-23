"""
5.4.10. Exercice UpyLaB 5.14 - Parcours vert bleu rouge
(D’après une idée de Jacky Trinh - 11/02/2018)

Nous pouvons définir la distance entre deux mots de même longueur (c’est-à-dire ayant le même nombre de lettres) mot_1 et mot_2 comme le nombre minimum de fois où il faut modifier une lettre de mot_1 pour obtenir mot_2, sans changer leur place (distance de Hamming).

Par exemple, les mots « lire » et « bise » sont à une distance de 2, puisqu’il faut changer le “l” et le “r” du mot « lire » pour obtenir « bise ».

Écrire une fonction distance_mots(mot_1, mot_2) qui retourne la distance entre deux mots.
Vous pouvez supposer que les deux mots sont de même longueur, et sont écrits sans accents.
Exemple 1
L’appel suivant de la fonction :
distance_mots("lire", "bise")
doit retourner :
2
Exemple 2
L’appel suivant de la fonction :
distance_mots("Python", "Python")
doit retourner :
0
Exemple 3
L’appel suivant de la fonction :
distance_mots("merci", "adieu")
doit retourner :
5
Exemple 4
L’appel suivant de la fonction :
distance_mots("chien", "niche")
doit retourner :
5
Consignes
Dans cet exercice, il vous est demandé d’écrire seulement la fonction distance_mots.
Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en
 particulier aucun appel à input ou à print.

"""




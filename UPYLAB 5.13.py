"""5.4.9. Exercice UpyLaB 5.13 - Parcours rouge
L’exercice est le même que le précédent, mais ici, si les paramètres ont le type attendu, la fonction modifie la liste
en place et ne retourne rien. Si les paramètres ne sont pas valides, une erreur se produit à l’exécution.

Exemple 1
L’exécution du code suivant :
l = [1, 3, 5]
my_insert(l, 4)
print(l)
doit afficher :
[1, 3, 4, 5]
Exemple 2
L’exécution du code suivant :

l = [1, 3, 5]
my_insert(l, 'a')
print(l)
doit provoquer une exception Python, par exemple :

AssertionError
Consignes
Attention, le code que vous soumettez à UpyLaB ne doit contenir que la définition de la fonction. N’y déclarez donc pas
 de variable l, ni n’y faites d’appel à print comme dans les exemples ci-dessus.
Pour tester le type des paramètres, vous pouvez utiliser les verbes assert, type ou isinstance.
l’instruction assert condition laisse continuer l’exécution du code si la condition évaluée est vraie, mais provoque
 une erreur (appelée exception en Python) si la condition est fausse.

type(v) donne le type de v.

isinstance(v, typ) teste si v est de type typ."""

def my_insert (lst,n):
    """Cette fonction reçoit comme premier paramètre une liste d’entiers relatifs triée par ordre croissant
 et comme deuxième paramètre un entier relatif n, et qui renvoie une liste correspondant à la liste reçue, mais dans
 laquelle le nombre n a été inséré à la bonne place"""
    assert (isinstance(n, int))
    for i in range(len(lst)):
        if max(lst) < n:
            lst.append(n)
            break
        elif lst[i] >= n:
            lst.insert(i,n)
            break
        else:
            continue

l = [1, 3, 5]
my_insert(l, 'a')
print(l)
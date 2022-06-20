# noinspection LanguageDetectionInspection
"""
5.4.11. Exercice UpyLaB 5.15 - Parcours rouge
(D’après une idée de Jacky Trinh - 11/02/2018)
Joao vient d’arriver dans notre pays depuis le Portugal. Il a encore du mal avec la langue française. Malgré ses efforts
 considérables, il fait une faute d’orthographe quasi à chaque mot. Son souci est qu’il n’arrive pas toujours à écrire
 un mot correctement sans se tromper à une lettre près. Ainsi pour écrire « bonjour », il peut écrire « binjour ». Pour
  remédier à ce problème, Joao utilise un correcteur orthographique. Malheureusement, Joao a un examen aujourd’hui et
  il a oublié son petit correcteur.
Afin de l’aider, nous vous demandons d’écrire une fonction correcteur(mot, liste_mots) où mot est le mot que Joao
écrit et liste_mots est une liste qui contient les mots (ayant la bonne orthographe) que Joao est susceptible d’utiliser.
Cette fonction doit retourner le mot dont l’orthographe a été corrigée.

Exemple 1
L’appel suivant de la fonction :
correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
doit retourner :
"bonjour"
Exemple 2
L’appel suivant de la fonction :
correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
doit retourner :

"chat"
Consignes
Pour cet exercice, vous pourrez utiliser la fonction distance_mots(mot_1, mot_2) que vous avez précédemment codée
et qui donne la distance entre deux mots de même longueur. N’oubliez pas alors de mettre aussi le code de cette
 fonction dans votre solution.Le correcteur orthographique demandé est une version simple ; les mots en paramètre auront
  au maximum une seule lettre qui diffère par rapport à la bonne orthographe.
Nous ne prenons pas en compte les mots avec accents, ni les mots composés de tiret, d’apostrophes, d’espace,..
liste_mots ne contient pas de mots qui se ressemblent ; si Joao écrit le mot « liee », il se peut en effet que cela
représente le mot « lire » ou « lier ». Afin d’éviter cette confusion, deux mots de même longueur de la liste sont au
moins à une distance de 3. Il n’y aura ainsi qu’un seul mot dans liste_mots répondant au problème.
Vous pouvez supposer que Joao soit arrive à écrire des mots sans fautes, soit fait au plus une erreur.
"""
def distance_mots(mot1,mot2):
    '''Cette fonction calcule le nombre minimum de fois où il faut modifier une
    lettre de mot_1 pour obtenir mot_2, sans changer leur ordre (distance de Hamming)'''
    cont = 0
    for i,j in zip(mot2,range(len(mot1))):
        if i != mot1[j] :
            cont +=1
        else:
            continue
    return cont

print(distance_mots('merci','mrcia'))

def correcteur(mot, liste_mots):
    """ Cette fonction est un utilise un correcteur orthographique"""
    v =[]
    v1 = []
    for j in liste_mots :
        if len(mot) == len(j):
            v.append(distance_mots(mot,j))
            v1.append(j)
        else:
            continue
    c = min(v)
    for i,a in enumerate (v):
        if c == v[i]:
            return v1[i]
            break



#print (correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
#print(correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
print(correcteur("ancomada", ["chien", "chat", "train", "voiture", "bonjour", "merci",'remettre','anacondi']))





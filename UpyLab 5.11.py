"""def intersection2(v, w):
    res =''
    k= 0
    while k <=len(v)+1:
        for i in range(len(v)):
             if str(v[k:len(v)-i]) in w:
                res = res + v[k:len(v)-i] + ';'
             else:
                 continue
        k+=1
    if res !='':
        long = []
        c= res.rsplit(sep=';')
        h =[]
        m =[]
        '''for k in c:
            if k != '':
                m.append(k)
            else:
                continue'''
        for i in range(len(c)):
            if c[i] !='':
                h.append(c[i])
                long.append(len(c[i]))
            else:
                continue
        resultat = max(long)
        if resultat == 0:
            l = 'Rien '
            return l
        else:
            for j in range(len(h)):
                if len(h[j]) == resultat:
                    l= h[j]
                    break
                else:
                    continue
            return l
    else:
        l = ' '
        return l
"""
"print(intersection2('salut','merci'))"
#print(intersection2('merci', 'adieu'))
#print(intersection2('thierry','sébastien'))
#print(intersection2('bbaacc', 'aabb'))

##########################

"""def intersection(v, w):
    res =''
    k= 0
    long = []
    while k <=len(v)+1:
        for i in range(len(v)):
             if str(v[k:len(v)-i]) in w:
                res = res + v[k:len(v)-i]+ ';'
             else:
                 continue
        k+=1
    c= res.rsplit(sep=';')
    for i in range(len(c)):
        long.append(len(c[i]))
    resultat = max(long)
    if resultat == 0:
        l = 'Rien'
        return l
    else:
        for j in range(len(c)):
            if len(c[j]) == resultat:
                l= c[j]
            else:
                continue
        return l

    return l"""

#print(intersection('aimer', 'marie'))


####
"""v = 'salut'
w = 'merci'
res =''
k= 0
long = []
while k <=len(v)+1:
    for i in range(len(v)):
         if str(v[k:len(v)-i]) in w:
            res = res + v[k:len(v)-i]+ ' '
         else:
             continue
    k+=1
c= res.split(sep=' ')
t = []
longeur = []
for i in c:
    if i != '':
        t.append(i)
        longeur.append(len(i))
    else:
        continue
print(c)
print (t)
print (longeur)

for j in t:
    if len(j) == max(longeur):
        l = j
        break
    else:
        continue
print(l)"""
# Enoncé de l'exercice

"""5.4.7. Exercice UpyLaB 5.11 - Parcours bleu rouge
Écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.
On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots.
 Par exemple, l’intersection de « programme » et « grammaire » est « gramm ».
Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.
Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v.
 Par exemple, intersection('bbaacc', 'aabb') renvoie 'bb'.

Exemple 1
L’appel suivant de la fonction :
intersection('programme', 'grammaire')
doit retourner :
'gramm'
Exemple 2
L’appel suivant de la fonction :
intersection('salut', 'merci')
doit retourner :
''
Exemple 3
L’appel suivant de la fonction :
intersection('merci', 'adieu')
doit retourner :
'e'
"""
# intersection
def intersection (v,w):
    """Cette fonction permet de calculer l’intersection entre deux chaînes de caractères v et w"""
    res =''
    k= 0
    long = []
    while k <=len(v)+1:
        for i in range(len(v)):
             if str(v[k:len(v)-i]) in w:
                res = res + v[k:len(v)-i]+ ' '
             else:
                 continue
        k+=1
    c= res.split(sep=' ')
    t = []
    longeur = []
    for i in c:
        if i != '':
            t.append(i)
            longeur.append(len(i))
        else:
            continue
    if len(t) == 0 :
       l = ''
       return l
    else:
        for j in t:
            if len(j) == max(longeur):
                l = j
                break
            else:
                continue
        return l


print(intersection('salut', 'merci'))
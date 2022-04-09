def dupliques(a):
    "la foction détecte les valeurs en double"
    resl =[0]
    for i in a:
        k = a.count(i)
        resl.append(k)
    if max(resl) > 1:
        resultat = True
    else:
        resultat = False
    return resultat

print(dupliques('abcda'))

#5.4.7 Exercice UpyLaB 5.11 (Parcours Bleu et Rouge)
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

    return res

print(intersection('bbaacc', 'aabb'))"""


#  Exercice UpyLaB 5.14
"""def distance_mots(mot1,mot2):
    '''Cette fonction calcule le nombre minimum de fois où il faut modifier une
    lettre de mot_1 pour obtenir mot_2, sans changer leur ordre (distance de Hamming)'''
    cont = 0
    for i,j in zip(mot2,range(len(mot1))):
        if i != mot1[j] :
            cont +=1
        else:
            continue
    return cont

print(distance_mots('programme', 'grammaire'))"""

""""""""""""#############"""
def intersection(v, w):
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

    return l

print(intersection('programme', 'grammaire'))


#  Exercice UpyLaB 5.14
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

print(distance_mots('programme', 'grammaire'))

"""#########################################"""
def intersection2(v, w):
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

print(intersection2('salut','merci'))
#print(intersection2('merci', 'adieu'))
#print(intersection2('thierry','sébastien'))
#print(intersection2('bbaacc', 'aabb'))

""" lien github: https://github.com/cedson22/Exercices-cours-coder-en-Python-Fun-mooc.git"""
print('hello world!')
def anagrammes(v, w):
    " Ce programme permet de savoir si v et w sont des annagramme"
    if len(v) != len(w):
        a = False
        return a
    else:
        v1 = sorted(v)
        w1 = sorted(w)
        for i in v1:
            if i not in w1:
                a = False
                break
            else:
                if v1.count(i) != w1.count(i):
                    a = False
                    break
                else:
                    a = True
                    continue
                continue
        return a

print(anagrammes('aabc', 'cacb'))

def duplicates(a):
    "la foction détecte les valeurs en double"
    res =[]
    for letter in a:
        if letter not in res:
            res.append(letter)
        else:
           continue
    if len(res) == 0:
         resultat = False
    else:
         resultat = True
    return resultat

dupliques([1, 2, 3, 4])


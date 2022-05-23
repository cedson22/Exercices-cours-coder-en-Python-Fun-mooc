'''print("hello!")
a = [19,20,19,"malanda","malanda",19,20, "Cédric","Makosso","Cédric"]
print(a,len(a), sep='\n')
c= {"malanda":a.count("malanda"),"Cédric": a.count("Cédric"),"Makosso":a.count("Makosso"), 19:a.count(19),20:a.count(20) }

print(c.values(), c.keys(), sep='\n')
print("malanda".upper().count("A"))'''

def premier(n):
    """Cette fonction vérifie si l'entier n est premier ou non"""
    if n in range (2):
        return False
    else:
        for i in range (2,n):
            if (n % i) == 0:
                return False
    return True

'''x = int(input())
for i in range(2,x):
    if (premier(i) == True) :
        print(i)'''


def prime_numbers(nb):
    ''' Cette fonction permet de recevoir  un nombre entier nb et renvoie la liste des nb premiers nombres premiers.'''

    if type(nb) is int and nb >= 0:
        a = []
        i= 2
        while len(a) < nb :
            if premier (i)== True:
                a.append(i)
                i +=1
            else :
                i +=1
        return a
    else:
        c = 'None'
        return c


print(prime_numbers(-1))

# anagramme
def anagrammes(v, w):
    " Ce programme permet de savoir si v et w sont des annagramme"
    if len(v) != len(w):
        return 'False'
    else:
        for i in v:
            if i not in w:
                return 'False'
                break
            else:
                continue
            return 'True'

print(anagrammes('marion', 'romina'))
#%
print('hello!')

#%%
tex = ['Née vers 1942','née vers 1938','née vers 1934'       'père né vers 1943',  'mère née vers 1946',  'vers 1956',
'née vers 1961', 'Née vers 1954', 'née vers 1954','intéressée est né vers 1949', ' née vers 1942']
#%%
print (tex)
#%%


#%%
file = open('GFG.txt', 'w')
data ='née vers 1942'
file.write(data)
file.close()






#%%
h = open('GFG.txt', 'r')

content = h.readlines()

a = ""

for line in content:
    for i in line:
        if i.isdigit() == True:
            a +=i

print("The sum is:", a)
#%%


for i in tex:
    if i.isdigit() == True:
        annee.append(int(i))
    else:
        continue
print(annee)
#%%

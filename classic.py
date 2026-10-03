"""
def secti(a,b,c):
    # funkce secte 3 cisla a, b, c a vratil vysledek pomocí return
    vysledek = a + b + c
    return vysledek

def je_delitelne_3(x):
    zbytek = x % 3
    if zbytek == 0:
        return True
    else:
        return False
    


if __name__ == "__main__":
    x = je_delitelne_3(6)
    print ("je delitelne", x)
    #x = secti(1,2,3)
    #print ("Vysledek je", x)
"""
#if __name__ == "__main__":
#   vstup = int(vstup)
#    vysledek = vstup
#    print (vysledek)
"""
seznam = [1,2,3, "čtyři"] #list
seznam = (1,2,3, "čtyři") #n-tice
seznam = {"jmeno": "Alice", "vek":30, "mesto":"Praha"} #slovník
mnozina = {1, 2, 3, 4, 5} #množina
mnozina.add(6)
"""
a = (1,2,3,4,5)

if __name__ == "__main__":
    len(a)==6
    return True
else:
    return False

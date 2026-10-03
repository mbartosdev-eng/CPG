"""
print("Hello World!")

def vypis_hodnotu_x(x):
    
    #Tato funkce vipisuje hodnotu x. 
    
    print ("----------------")
    print ("Hodnota x je", x)

vypis_hodnotu_x(1)
vypis_hodnotu_x(2)
vypis_hodnotu_x(3)

x = 1

type (x)
print (type(x))

x = "abc"
type (x)
print (type(x))
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


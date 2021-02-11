Z =['1','2','3','4','5','6','7','8','9'] 
a='1'
b='2'
c='3'
d='4'
e='5'
f='6'
g='7'
h='8'
l='9'
drp=True
print('******** - Jeux de X O - *********')
for i in range (5):
    print("          *************")
    print('',a,'|',b,'|',c,)
    print('---|---|---')
    print('',d,'|',e,'|',f,)
    print('---|---|---')
    print('',g,'|',h,'|',l,)
    if Z == []:# ila Z lli lfo9 khwat break w drp ayb9a true, w aymchi ykteb egalite
        break
    choix=(input("joueur n ° '1' Vous devez choisir un nombre present dans le tableau : "))
    if choix not in Z:    
        while choix not in Z: # hadi ila choix lli dkhl lutilisateur makainch ftableau
            print("          *************")
            print('',a,'|',b,'|',c,)
            print('---|---|---')
            print('',d,'|',e,'|',f,)
            print('---|---|---')
            print('',g,'|',h,'|',l,)
            choix=input(("veuillez choisir un nombre appartenant du tableau: "))
    if(choix=='1') and choix in Z: # had z3ma lakan choix == valeur, et dak choix nit ba9i mat3zlch
        a="x"
        Z.remove('1')
    elif(choix=='2') and choix in Z:
        b="x"
        Z.remove('2')
    elif(choix=='3') and choix in Z:
        c="x"
        Z.remove('3')
    elif(choix=='4') and choix in Z:
        d="x"
        Z.remove('4')
    elif(choix=='5') and choix in Z:
        e="x"
        Z.remove('5')
    elif(choix=='6') and choix in Z:
        f="x"
        Z.remove('6')
    elif(choix=='7') and choix in Z:
        g="x"
        Z.remove('7')
    elif(choix=='8') and choix in Z:
        h="x"
        Z.remove('8')
    elif(choix=='9') and choix in Z:
        l="x"
        Z.remove('9')
    if (a=="x" and b=="x" and c=="x")or(d== "x"and e=="x" and f=="x")or(g=="x" and e=="x" and f=="x")or(a== "x"and e=="x" and l=="x")or(c=="x" and e=="x" and g=="x")or(a== "x"and d=="x" and g=="x")or(b=="x" and e=="x" and h=="x")or(c== "x"and f=="x" and l=="x"):
        print("          *************")
        print('',a,'|',b,'|',c,)
        print('---|---|---')
        print('',d,'|',e,'|',f,)
        print('---|---|---')
        print('',g,'|',h,'|',l,)
        print("félicitations pour le joueur n ° '1'")
        drp=False
        break
    print("          *************")
    print('',a,'|',b,'|',c,)
    print('---|---|---')
    print('',d,'|',e,'|',f,)
    print('---|---|---')
    print('',g,'|',h,'|',l,)
    if Z == []: # si Z est une liste vide
        break
    choix=(input("le joueur n ° '2' Vous devez choisir un nombre present dans le tableau : "))
    if choix not in Z:    
        while choix not in Z:
            print("          *************")
            print('',a,'|',b,'|',c,)
            print('---|---|---')
            print('',d,'|',e,'|',f,)
            print('---|---|---')
            print('',g,'|',h,'|',l,)
            choix=input(("veuillez choisir un nombre appartenant du tableau: "))
    if(choix=='1') and choix in Z:
        a="o"
        Z.remove('1')
    elif(choix=='2') and choix in Z:
        b="o"
        Z.remove('2')
    elif(choix=='3') and choix in Z:
        c="o"
        Z.remove('3')
    elif(choix=='4') and choix in Z:
        d="o"
        Z.remove('4')
    elif(choix=='5') and choix in Z:
        e="o"
        Z.remove('5')
    elif(choix=='6') and choix in Z:
        f="o"
        Z.remove('6')
    elif(choix=='7') and choix in Z:
        g="o"
        Z.remove('7')
    elif(choix=='8') and choix in Z:
        h="o"
        Z.remove('8')
    elif(choix=='9') and choix in Z:
        l="o"
        Z.remove('9')

    if (a=="o" and b=="o" and c=="o")or(d== "o"and e=="o" and f=="o")or(g=="o" and e=="o" and f=="o")or(a== "o"and e=="o" and l=="o")or(c=="o" and e=="o" and g=="o")or(a== "o"and d=="o" and g=="o")or(b=="o" and e=="o" and h=="o")or(c== "o"and f=="o" and l=="o"):
        print("          *************")
        print('',a,'|',b,'|',c,)
        print('---|---|---')
        print('',d,'|',e,'|',f,)
        print('---|---|---')
        print('',g,'|',h,'|',l,)
        print("félicitations pour le joueur n ° '2'")
        drp=False
        break

if (drp==True):
    print("égalité")

from PIL import Image
import random
import os
random.seed()
n=23
k=12
e=2
g=[1,0,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]
nom_image = r'mario.jpg'
path = r'images/' + nom_image
img = Image.open(path)
image_blank=Image.new('RGB',(img.size[0],img.size[1]))
pixels = img.load()
pixel_sans_code = image_blank.load()
Image.new('RGB',(500,5))
def conversion(n,tab,i):
    if n > 1:
        conversion(n // 2,tab,i-1)
    tab[i]=n%2

def decimale_binaire(k):
    tab =[0 for i in range(n)]
    conversion(k,tab,n-1)
    q = [tab[n-i-1] for i in range(n)]
    return q

def binaire_decimale(binaire):
    k=1
    resultat=0
    for i in range(n):
        resultat=resultat+k*binaire[i]
        k=k*2
    return resultat

def ajout_erreur(p):
    for i in range(n):
        if(random.randint(0,99)==0):
            if(p[i]==1):
                p[i]=0
            else:
                p[i]=1
    return p
            
def decalage(q,k):
    p=[q[i] for i in range(n)]
    for j in range(k):
        stock = p[0]
        p[0]=p[n-1]
        for i in range(len(p)-2):
            p[n-i-1]=p[n-i-2]
        p[1]=stock
    return p

def multiplication(p,q):
    resultat = [0 for i in range(n)]
    for i in range(n):
        r = decalage(q,i)
        resultat = [resultat[j]+r[j]*p[i] for j in range(n)]
    return resultat

def modulo(p):
    resultat= [p[i]%2 for i in range(n)]
    return resultat

def deg(p):
    for i in range(len(p)):
        if(p[len(p)-1-i]!=0):
            return len(p)-1-i
    return 0

def division_euclid(a,b): # a = bq+r
    r = a
    q = [0 for i in range(n)]
    while(deg(r)>=deg(b)):
        q[deg(r)-deg(b)]=r[deg(r)]
        t=decalage(b,deg(r)-deg(b))
        r=[r[i]-r[deg(r)]*t[i] for i in range(len(a))]
    return (q,r)

def reste(a,b):
    (q,r) = division_euclid(a,b)
    return r

def quotient(a,b):
    (q,r) = division_euclid(a,b)
    return q

def poids(w):
    total = 0
    for i in range(len(w)):
        if(w[i]!=0):
            total = total+1
    return total

def encodage(m,g):
    return modulo(multiplication(m,g))

def calcul(g,s):
    if (deg(s)<n-k-1):
        return decalage(s,1)
    else:
        a = decalage(s,1)
        b = [a[i]-g[i] for i in range(n)]
        return modulo(b)

def decodage_naif(w,g):
    (a,s) = division_euclid(w,g)
    zero=[0 for i in range(n)]
    if(poids(modulo(s))==0):
        return modulo(a)
    return zero

def decodage(w,g):
    (a,s) = division_euclid(w,g)
    zero=[0 for i in range(n)]
    if(poids(modulo(s))==0):
        return modulo(a)
    for i in range(n):
        if(poids(modulo(s))<=e):
            erreur = decalage(s,n-i)
            m = [w[i]-erreur[i] for i in range(n)]
            return modulo(quotient(m,g))
        else:
            s=calcul(g,s)
    return zero
        

nombre = 0
for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):  # For every row
            nombre=nombre+1
            print(nombre)
            (p1,p2,p3)=pixels[i,j]
            b1=decimale_binaire(p1)
            b2=decimale_binaire(p2)
            b3=decimale_binaire(p3)
            b1=encodage(b1,g)
            b2=encodage(b2,g)
            b3=encodage(b3,g)
            ajout_erreur(b1)
            ajout_erreur(b2)
            ajout_erreur(b3)
            pixel_sans_code[i,j]=(binaire_decimale(decodage_naif(b1,g)),binaire_decimale(decodage_naif(b2,g)),binaire_decimale(decodage_naif(b3,g)))
            b1=decodage(b1,g)
            b2=decodage(b2,g)
            b3=decodage(b3,g)
            pixels[i,j]=(binaire_decimale(b1),binaire_decimale(b2),binaire_decimale(b3))

base_name, ext = os.path.splitext(nom_image)
img.save(r'image_resultat/' + base_name + '_code' + ext)
image_blank.save(r'image_resultat/' + base_name + '_sans_code' + ext)


















    
from PIL import Image
import random
import os

random.seed()
n=15
k=7
e=2
g=465
nom_image = r'mario.jpg'
path = r'images/' + nom_image
img = Image.open(path)
pixels = img.load()
image_blank=Image.new('RGB',(img.size[0],img.size[1]))
pixel_sans_code = image_blank.load()

def decalage(p, d):
    d=d%n
    return (p << d)|(p >> (n - d))

def multiplication(p,q):
    s = 0
    j = len(bin(p))
    for i in range(j-2):
        if(bin(p)[j-i-1]=='1'):
            s = s ^ (q<<i)
    return s

def deg(n):
    return len(bin(n))-3

def division_euclid(a,b): # a = bq+r
    r = a
    q = 0
    while(deg(r)>=deg(b)):
        q=q+2**(deg(r)-deg(b))
        t=b<<(deg(r)-deg(b))
        r=r ^ t
    return (q,r)

def reste(a,b):
    (q,r) = division_euclid(a,b)
    return r

def quotient(a,b):
    (q,r) = division_euclid(a,b)
    return q

def poids(w):
    total = 0
    j = len(bin(w))
    for i in range(j-2):
        if(bin(w)[j-i-1]=='1'):
            total = total+1
    return total

def encodage(m,g):
    return multiplication(m,g)

def calcul(g,s):
    if (deg(s)<n-k-1):
        return decalage(s,1)
    else:
        a = decalage(s,1)
        return a^g

def decodage_naif(w,g):
    (a,s) = division_euclid(w,g)
    if(poids(s)==0):
        return a
    return 0

def decodage(w,g):
    (a,s) = division_euclid(w,g)
    if(poids(s)==0):
        return a
    for i in range(n):
        if(poids(s)<=e):
            erreur = decalage(s,n-i)
            m = w^erreur
            return quotient(m,g)
        else:
            s=calcul(g,s)
    return a

def set_bit(v, index, x):
  
  mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
  v &= ~mask          # Clear the bit indicated by the mask (if x is False)
  if x:
    v |= mask         # If x was True, set the bit indicated by the mask.
  return v  

def ajout_erreur(w):
    p=w
    for k in range(n):
        if(random.randint(0,20)==0):
            p=set_bit(p,k,True)
        if(random.randint(0,20)==1):
            p=set_bit(p,k,False)
    return p
nombre = 0
for i in range(img.size[0]):    
    for j in range(img.size[1]):
            nombre=nombre+1
            print(nombre) 
            (p1,p2,p3)=pixels[i,j]
            p1=p1>>1
            p2=p2>>1
            p3=p3>>1
            p1=encodage(p1,g)
            p2=encodage(p2,g)
            p3=encodage(p3,g)
            p1=ajout_erreur(p1)
            p2=ajout_erreur(p2)
            p3=ajout_erreur(p3)
            pixel_sans_code[i,j]=(2*decodage_naif(p1,g),2*decodage_naif(p2,g),2*decodage_naif(p3,g))
            pixels[i,j]=(2*decodage(p1,g),2*decodage(p2,g),2*decodage(p3,g))

base_name, ext = os.path.splitext(nom_image)
img.save(r'image_resultat/' + base_name + '_code' + ext)
image_blank.save(r'image_resultat/' + base_name + '_sans_code' + ext)

#Semplice somma di bit senza guardare ordine ecc...
def riempi(x,i):#Aggiungo spazi per somma
     j=0
     for j in range(i):
             x=x+[0]
     return x

def sommabit(a,b):#finale
     s=[]
     i=0
     res=0
     if(len(a)<len(b)):
             a=riempi(a,len(b)-len(a))
     elif(len(a)>len(b)):
             b=riempi(b,len(a)-len(b))
     for i in range(len(a)):
             s=s+[(a[i]+b[i]+res)%2]
             res=(a[i]+b[i]+res)//2
     s=s+[res]
     return s

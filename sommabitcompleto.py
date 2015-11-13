def sommabitcompleto(a,b):  #Ritorna la somma giusta di due numeri binari
     s=[]                   #PS alcune funzioni sono già state scritte precedentemente e le trovate nei file precedenti
     i=0
     res=0
     z=contrario(a)
     k=contrario(b)
     if(len(z)<len(k)):
             z=riempi(z,len(k)-len(z))
     elif(len(z)>len(k)):
             k=riempi(k,len(z)-len(k))
     for i in range(len(z)):
             s=s+[(z[i]+k[i]+res)%2]
             res=(z[i]+k[i]+res)//2
     if(res==1):
             s=s+[res]
     return contrario(s)

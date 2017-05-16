import os
import getpass
p="prova"
t=0
def op():
    with open("pwd.txt","w") as f:
        print("Cosa vuoi scrivere?")
        s=input()
        f.write(s)

def dl():
    print("Cancello file mi spiace")
    try:
        os.remove('pwd.txt')
    except FileNotFoundError:
        print("Il file non esiste, non cancello")
        return 0

while t<3:
    print("Digita la password: ")
    a=getpass.getpass()
    if(a!=p):
        print("Riprova!")
        t+=1
    else:
        print("Entro al file...")
        op()
        break
if t>2:
    dl()

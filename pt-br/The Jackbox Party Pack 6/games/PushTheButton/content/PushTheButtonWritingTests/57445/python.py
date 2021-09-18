import os
from googletrans import Translator
from unidecode import unidecode
translator = Translator()

pastas = os.listdir()
numeros= ['0','1','2','3','4','5','6','7','8','9']

fileo = open("data.jet","r")
A = fileo.read()
fileo.close()

B = A.split('"')

num=0

r = open("resultado.txt","w+")

for x in range(0,len(B)):
    if(len(B[x])>3):
        if(B[x].find("Alien")>-1 or B[x].find("Human")>-1 or B[x].find("Diff")>-1 or B[x]=="fields" or B[x]=="false" or B[x]=="true"):
            pass
        else:
            num=0
            
            B[x] = B[x].replace("<i>","")
            B[x] = B[x].replace("<\/i>","")
            B[x] = B[x].replace("\\","")
            B[x] = B[x].replace("u2019","'")
         
            for digito in B[x]:
                if digito in numeros:
                    num+=1
        
            if(num<3):
                translation = translator.translate(B[x],dest="pt")
                print(translation.text)
    
    
    
    
    
import argparse
import os
from fileinput import close
import secrets

parser= argparse.ArgumentParser()
parser.add_argument("-i","--input",required=True,help=" input txt")
parser.add_argument("-o","--output",required=True,help="output txt")
parser.add_argument("-L","--long",required=True,type=int, help="pwd min long ")
parser.add_argument("-S","--security",required=False,type=int,help="security level for 1 to 3 ")
arg = parser.parse_args()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if arg.security != 1 and arg.security != 2 and arg.security != 3 and arg.security !=None :
    print ("security level ist for 1 to 3 ")
    exit()

if not os.path.exists(arg.input):
    print("we dont fund die "+arg.input)
    exit()

if not os.path.exists(arg.output):
    print("we dont fund die "+arg.output)
    exit()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if arg.security==None :
    arg.security=1

level=arg.security
long= arg.long

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

input= open(arg.input,"r")    #es gibt noch hier eine profi methode die besser nutzen kann   um die file offnen und zumachen 
keywort=input.readlines()
input.close()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




if level== 1 :
    wordlist=[]

  
    hauptlist=[]
    for k in keywort:
        hauptlist.append(k.strip())
    hauptlist_V2 = hauptlist.copy()

    for h in hauptlist:
        hauptlist_V2.append(h.upper())
        


    for w in hauptlist_V2 :
        if  len(w) >= long:
            wordlist.append(w)
        for t in hauptlist_V2:
            if len (w+t)>= long:
                wordlist.append(w+t)
            

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if level==2 :
    wordlist=[]
    common_words = [
         "iloveyou", "loveyou", "love", "mylove", "sweetheart", "babygirl", "babyboy",
         "mybaby", "forever", "soulmate", "missyou", "foreveryours", "myheart",
         "truelove", "honeybunny", "cutiepie",
         "password", "123456", "123456789", "qwerty", "qwerty123", "admin", "welcome",
         "letmein", "monkey", "football", "dragon", "master", "sunshine", "princess",
         "superman", "batman", "starwars", "trustno1",  "freedom",
         "family", "mother", "father", "mama", "papa", "baby", "angel", "sweetie",
         "darling", "honey", "wife", "husband", "bestfriend",
         "tiger", "lion", "eagle", "falcon", "phoenix", "shadow", "ninja", "dragon2",
         "summer", "winter", "autumn", "spring","1", "12", "123", "1234", "12345", "123456", "00", "01", "99", "100",
        "2020", "2021", "2022", "2023", "2024", "2025", "2026",
        "!", "!!", "!!!", "@", "#", "$", "%", "&", "*", ".", "_","2","4","3","5","6","7","8","9","10","qwertzuiop","azertiop"]

    hauptlist=[]
    for k in keywort:
        hauptlist.append(k.strip())
    hauptlist+=common_words



    hauptlist_V2 = hauptlist.copy()
   
    

    for h in hauptlist:
        hauptlist_V2.append(h.upper())
    hauptlist_V2=list(set(hauptlist_V2))


    for w in hauptlist_V2 :
        if  len(w) >= long:
            wordlist.append(w)
        for t in hauptlist_V2:
            if len (w+t)>= long:
                wordlist.append(w+t)
            

                    
            
      
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if level== 3 :
    wordlist=[]
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","u","r","s","t","u","v","w","x","y","z","q","Q","W","E","R","T","Z","U","I","O","P","Ü","*","Ä","Ö","L","K","J","H","G","F","D","S","A","Y","X","C","V","B","N","M","1","2","3","4","5","6","7","8","9","0","@","-","_","+","*","#","?","!","§","$","%","&","=","~"]
    for i in range (5000):
        word=""
        while len(word)<= long :
            word+=secrets.choice(alpha)
        wordlist.append(word)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
output=open(arg.output,"w")
for i in wordlist :
    output.write(i+"\n")
output.close(  )         

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

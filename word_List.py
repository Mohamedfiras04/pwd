import argparse
import os
from fileinput import close

parser= argparse.ArgumentParser()
parser.add_argument("-i","--input",required=True,help=" input txt")
parser.add_argument("-o","--output",required=True,help="output txt")
parser.add_argument("-L","--long",required=True,help="pwd min long ")
parser.add_argument("-S","--security",required=False,help="security level for 1 to 3 ")
arg = parser.parse_args()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if arg.security != "1" and arg.security != "2" and arg.security != "3" and arg.security !=None :
    print ("security level ist for 1 to 3 ")
    exit()

if not os.path.exists(arg.input):
    print("we dont fund die "+arg.input)
    exit()

if not os.path.exists(arg.output):
    print("we dont fund die "+arg.output)
    exit()

"fehlt hier noch  die condition vonn die  L "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if arg.security==None :
    arg.security="1"

level=arg.security
long= arg.long

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

input= open(arg.input,"r")
keywort=input.readlines()
input.close()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
wordlist=[]

" hier fhler die logik von die reschnug vonn passeworte  Level 1   "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" hier fhler die logik von die reschnug vonn passeworte  Level 2  "

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" hier fhler die logik von die reschnug vonn passeworte  Level 3   "

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
output=open(arg.output,"w")
for i in wordlist :
    output.write(i)
output.close()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

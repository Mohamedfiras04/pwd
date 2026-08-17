import argparse
parser= argparse.ArgumentParser()
parser.add_argument("-i","--input",required=True,help=" input txt")
parser.add_argument("-o","--output",required=True,help="output txt")
parser.add_argument("-L","--long",required=True,help="pwd min long ")
parser.add_argument("-S","--security",required=False,help="security level for 1 to 3 ")
arg = parser.parse_args()
if arg.security != "1" and arg.security != "2" and arg.security != "3" and arg.security !=None :
    print ("security level ist for 1 to 3 ")
    exit()

print(arg.input)
input= open(arg.input,"r")
inhalt=input.readlines()
input.close()
print(inhalt)
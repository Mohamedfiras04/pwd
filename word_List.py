import argparse
parser= argparse.ArgumentParser()
parser.add_argument("-i","--input",required=True,help="-i input.txt")
parser.add_argument("-o","--output",required=True,help="-o output.txt")
arg = parser.parse_args()
print(arg.input)
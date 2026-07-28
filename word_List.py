def grosekleine (w):
    wordlist=set()
    wordlist.add(w.lower())

    wordlist.add(w.upper())

    wordlist.add(w)
    return wordlist
firas=grosekleine("firas")
print(firas)
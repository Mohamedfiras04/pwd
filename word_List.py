import argparse
import os
import secrets

# ====================================================================
# Argumente von der Kommandozeile einlesen
# ====================================================================
parser = argparse.ArgumentParser(
    description="Wordlist generator for authorized penetration testing."
)
parser.add_argument("-i", "--input", required=True, help="input txt file")
parser.add_argument("-o", "--output", required=True, help="output txt file")
parser.add_argument("-L", "--long", required=True, type=int, help="minimum password length")
parser.add_argument("-S", "--security", required=False, type=int, help="security level from 1 to 3")
arg = parser.parse_args()

# ====================================================================
# Eingaben pruefen
# ====================================================================
# Security-Level darf nur 1, 2, 3 oder leer sein
if arg.security not in (1, 2, 3, None):
    print("security level must be from 1 to 3")
    exit()

# Die Input-Datei muss existieren (die lesen wir)
if not os.path.exists(arg.input):
    print("Input file not found: " + arg.input)
    exit()

# ====================================================================
# Standardwerte setzen
# ====================================================================
# Wenn kein Level angegeben wurde, nehmen wir Level 1
if arg.security is None:
    arg.security = 1

level = arg.security
long = arg.long

# ====================================================================
# Keywords aus der Input-Datei lesen
# "with" schliesst die Datei automatisch, auch bei einem Fehler
# ====================================================================
with open(arg.input, "r") as f:
    keywort = f.readlines()

# ====================================================================
# Level 1: Passwoerter nur aus den eigenen Keywords
# ====================================================================
if level == 1:
    wordlist = []

    # Zeilen einlesen und Leerzeichen/Zeilenumbrueche entfernen
    hauptlist = []
    for k in keywort:
        hauptlist.append(k.strip())

    # Zusaetzlich jede Variante in GROSSBUCHSTABEN hinzufuegen
    hauptlist_V2 = hauptlist.copy()
    for h in hauptlist:
        hauptlist_V2.append(h.upper())

    # Jedes Wort einzeln und jede Kombination aus 2 Woertern bilden
    for w in hauptlist_V2:
        if len(w) >= long:                 # nur wenn lang genug
            wordlist.append(w)
        for t in hauptlist_V2:
            if len(w + t) >= long:
                wordlist.append(w + t)

# ====================================================================
# Level 2: eigene Keywords + Liste haeufiger Passwoerter
# ====================================================================
if level == 2:
    wordlist = []

    # Bekannte, oft benutzte Passwoerter / Bausteine
    common_words = [
        "iloveyou", "loveyou", "love", "mylove", "sweetheart", "babygirl", "babyboy",
        "mybaby", "forever", "soulmate", "missyou", "foreveryours", "myheart",
        "truelove", "honeybunny", "cutiepie",
        "password", "123456", "123456789", "qwerty", "qwerty123", "admin", "welcome",
        "letmein", "monkey", "football", "dragon", "master", "sunshine", "princess",
        "superman", "batman", "starwars", "trustno1", "freedom",
        "family", "mother", "father", "mama", "papa", "baby", "angel", "sweetie",
        "darling", "honey", "wife", "husband", "bestfriend",
        "tiger", "lion", "eagle", "falcon", "phoenix", "shadow", "ninja", "dragon2",
        "summer", "winter", "autumn", "spring", "1", "12", "123", "1234", "12345",
        "123456", "00", "01", "99", "100",
        "2020", "2021", "2022", "2023", "2024", "2025", "2026",
        "!", "!!", "!!!", "@", "#", "$", "%", "&", "*", ".", "_",
        "2", "4", "3", "5", "6", "7", "8", "9", "10", "qwertzuiop", "azertiop"]

    # Eigene Keywords lesen und mit den haeufigen Passwoertern mischen
    hauptlist = []
    for k in keywort:
        hauptlist.append(k.strip())
    hauptlist += common_words

    # GROSSBUCHSTABEN-Varianten hinzufuegen, dann Duplikate entfernen
    hauptlist_V2 = hauptlist.copy()
    for h in hauptlist:
        hauptlist_V2.append(h.upper())
    hauptlist_V2 = list(set(hauptlist_V2))

    # Wieder Einzelwoerter und 2er-Kombinationen bilden
    for w in hauptlist_V2:
        if len(w) >= long:
            wordlist.append(w)
        for t in hauptlist_V2:
            if len(w + t) >= long:
                wordlist.append(w + t)

# ====================================================================
# Level 3: komplett zufaellige, starke Passwoerter
# ====================================================================
if level == 3:
    wordlist = []

    # Alle erlaubten Zeichen (Buchstaben, Zahlen, Sonderzeichen)
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "u", "r", "s", "t", "u", "v", "w", "x", "y", "z", "q",
             "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "*", "Ä", "Ö",
             "L", "K", "J", "H", "G", "F", "D", "S", "A", "Y", "X", "C", "V", "B",
             "N", "M", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@", "-",
             "_", "+", "*", "#", "?", "!", "§", "$", "%", "&", "=", "~"]

    # 5000 zufaellige Passwoerter erzeugen
    
    for i in range(5000):
        word = ""
        while len(word) <= long:
            word += secrets.choice(alpha)
        wordlist.append(word)

# ====================================================================
# Duplikate entfernen und in die Output-Datei schreiben
# ====================================================================
wordlist = list(set(wordlist))       # doppelte Passwoerter loeschen

with open(arg.output, "w") as out:
    for i in wordlist:
        out.write(i + "\n")

print("[+] " + str(len(wordlist)) + " passwords generated.")
print("[+] Saved to: " + arg.output)
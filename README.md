# Wordlist Generator

A simple wordlist generator written in Python for **authorized** penetration testing.
It creates password candidates from target keywords (OSINT), useful for tools like Hydra or John the Ripper.

## Features

- **Level 1** – generates passwords only from your input keywords (+ uppercase variants)
- **Level 2** – combines your keywords with a list of common passwords
- **Level 3** – generates 5000 random strong passwords
- Minimum length filter (`-L`)
- No external libraries needed (only Python standard library)

## Requirements

- Python 3

## Usage

```bash
python3 word_List.py -i input.txt -o output.txt -L 7 -S 1
```

| Option | Description |
|--------|-------------|
| `-i`, `--input`    | input file with keywords (one per line) |
| `-o`, `--output`   | output file for the generated wordlist |
| `-L`, `--long`     | minimum password length |
| `-S`, `--security` | security level: 1, 2 or 3 (default: 1) |

### Example

`input.txt`:
```
firas
mohamed 
max
```

Run:
```bash
python3 word_List.py -i input.txt -o wordlist.txt -L 4 -S 1
```

## Disclaimer

This tool is intended **only** for authorized penetration testing and for use on
systems you own or have explicit permission to test. Any misuse of this tool is the
sole responsibility of the user. The author takes no responsibility for illegal use.

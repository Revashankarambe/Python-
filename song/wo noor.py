import time # Used for adding delays between prints
import sys # Used for character-by-character printing

def print_lyrics():
    lyrics = ["kaisi shaam si\nTere naam si",
              "jo padheya na main ki pegham si?",
              "main hairan si\nNaadan si",
              "kis gallon meri jaan Pareshan si?",
              "tenu hasde vekh ke baar baar Tenu puchivna main kadey tere dil di saar\n tera intezar,meri samjho baar",
              "kidda katey ne tu din metho haar haar?"
    ]
    delays = [
        0.5,0.4,0.7,0.3,0.3,0.3,0.8,
    ]
    print("wo noor :\n")
    time.sleep(1.2)
    # Loop through each lyric line
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print_lyrics()                    
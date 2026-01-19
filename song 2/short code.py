import time

lyrics = [
    "kaisi shaam si\nTere naam si",
    "jo padheya na main ki pegham si?",
    "main hairan si\nNaadan si",
    "kis gallon meri jaan Pareshan si?",
    "tenu hasde vekh ke baar baar Tenu puchivna main kadey tere dil di saar\n tera intezar,meri samjho baar",
    "kidda katey ne tu din metho haar haar?"
]

for l in lyrics:
    [print(c, end="", flush=True) or time.sleep(0.06) for c in l]
    print(); time.sleep(0.5)

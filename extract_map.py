import json

def genera_mappa_comuni(file_json, file_txt):
    with open(file_json) as file:
        dati = json.load(file)["Foglio1"]

    mappa_comuni = {}

    for elemento in dati:
        regione = elemento["regione"]
        provincia = elemento["provincia"]
        comune = elemento["comune"]

        if regione not in mappa_comuni:
            mappa_comuni[regione] = {}

        if provincia not in mappa_comuni[regione]:
            mappa_comuni[regione][provincia] = []

        mappa_comuni[regione][provincia].append(comune)

    with open(file_txt, 'w') as f:
        for regione, province in mappa_comuni.items():
            f.write('"' + regione + '": {\n')
            for provincia, comuni in province.items():
                f.write('    "' + provincia + '": [')
                for idx, comune in enumerate(comuni):
                    f.write('"' + comune + '"')
                    if idx != len(comuni) - 1:
                        f.write(", ")
                f.write("],\n")
            f.write("},\n")

# File JSON creato precedentemente
file_json = 'regioni-province-città.json'
# File di testo dove verrà scritta la mappa dei comuni
file_txt = 'mappa_comuni_dart.txt'

# Generare la mappa dei comuni nel file di testo
genera_mappa_comuni(file_json, file_txt)

print("Mappa dei comuni generata correttamente nel file:", file_txt)

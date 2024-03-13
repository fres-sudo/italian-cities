import json

# Funzione per sostituire le sigle delle province con i nomi delle province
def sostituisci_province(dati):
    for elemento in dati:
        if elemento["provincia"] in provincie:
            elemento["provincia"] = provincie[elemento["provincia"]]
    return dati

# Funzione per eliminare i campi specificati da ogni elemento della lista
def elimina_campi(dati):
    campi_da_eliminare = ["istat", "prefisso", "cod_fisco", "num_residenti", "superficie", "cf"]
    for elemento in dati:
        for campo in campi_da_eliminare:
            if campo in elemento:
                del elemento[campo]
    return dati

# Carica il file JSON
with open('dati.json', encoding='utf-8-sig') as file:
    dati = json.load(file)["Foglio1"]

# Mappa delle province
provincie = {
    "AG": "Agrigento",
    "AL": "Alessandria",
    "AN": "Ancona",
    "AO": "Aosta",
    "AR": "Arezzo",
    "AP": "Ascoli Piceno",
    "AT": "Asti",
    "AV": "Avellino",
    "BA": "Bari",
    "BT": "Barletta-Andria-Trani",
    "BL": "Belluno",
    "BN": "Benevento",
    "BG": "Bergamo",
    "BI": "Biella",
    "BO": "Bologna",
    "BZ": "Bolzano",
    "BS": "Brescia",
    "BR": "Brindisi",
    "CA": "Cagliari",
    "CL": "Caltanissetta",
    "CB": "Campobasso",
    "CI": "Carbonia-Iglesias",
    "CE": "Caserta",
    "CT": "Catania",
    "CZ": "Catanzaro",
    "CH": "Chieti",
    "CO": "Como",
    "CS": "Cosenza",
    "CR": "Cremona",
    "KR": "Crotone",
    "CN": "Cuneo",
    "EN": "Enna",
    "FM": "Fermo",
    "FE": "Ferrara",
    "FI": "Firenze",
    "FG": "Foggia",
    "FC": "Forlì-Cesena",
    "FR": "Frosinone",
    "GE": "Genova",
    "GO": "Gorizia",
    "GR": "Grosseto",
    "IM": "Imperia",
    "IS": "Isernia",
    "SP": "La Spezia",
    "AQ": "L'Aquila",
    "LT": "Latina",
    "LE": "Lecce",
    "LC": "Lecco",
    "LI": "Livorno",
    "LO": "Lodi",
    "LU": "Lucca",
    "MC": "Macerata",
    "MN": "Mantova",
    "MS": "Massa-Carrara",
    "MT": "Matera",
    "ME": "Messina",
    "MI": "Milano",
    "MO": "Modena",
    "MB": "Monza e della Brianza",
    "NA": "Napoli",
    "NO": "Novara",
    "NU": "Nuoro",
    "OG": "Ogliastra",
    "OT": "Olbia-Tempio",
    "OR": "Oristano",
    "PD": "Padova",
    "PA": "Palermo",
    "PR": "Parma",
    "PV": "Pavia",
    "PG": "Perugia",
    "PU": "Pesaro e Urbino",
    "PE": "Pescara",
    "PC": "Piacenza",
    "PI": "Pisa",
    "PT": "Pistoia",
    "PN": "Pordenone",
    "PZ": "Potenza",
    "PO": "Prato",
    "RG": "Ragusa",
    "RA": "Ravenna",
    "RC": "Reggio Calabria",
    "RE": "Reggio Emilia",
    "RI": "Rieti",
    "RN": "Rimini",
    "RM": "Roma",
    "RO": "Rovigo",
    "SA": "Salerno",
    "SS": "Sassari",
    "SV": "Savona",
    "SI": "Siena",
    "SR": "Siracusa",
    "SO": "Sondrio",
    "TA": "Taranto",
    "TE": "Teramo",
    "TR": "Terni",
    "TO": "Torino",
    "TP": "Trapani",
    "TN": "Trento",
    "TV": "Treviso",
    "TS": "Trieste",
    "UD": "Udine",
    "VA": "Varese",
    "VE": "Venezia",
    "VB": "Verbano-Cusio-Ossola",
    "VC": "Vercelli",
    "VR": "Verona",
    "VV": "Vibo Valentia",
    "VI": "Vicenza",
    "VT": "Viterbo"
}

# Sostituisci le sigle delle province con i nomi delle province
dati = sostituisci_province(dati)

# Elimina i campi specificati da ogni elemento della lista
dati = elimina_campi(dati)

# Creazione del nuovo oggetto JSON con le specifiche indicate
nuovo_dati = {"Foglio1": dati}

# Scrivi i dati modificati su un nuovo file JSON
with open('dati_modificati.json', 'w') as file:
    json.dump(nuovo_dati, file, indent=4)

print("File 'dati_modificati.json' creato con successo.")

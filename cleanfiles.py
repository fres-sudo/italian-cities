import json

# Function to replace province abbreviations with province names
def replace_provinces(data):
    for element in data:
        if element["provincia"] in provinces:
            element["provincia"] = provinces[element["provincia"]]
    return data

# Function to remove specified fields from each element of the list
def remove_fields(data):
    fields_to_remove = ["istat", "prefisso", "cod_fisco", "num_residenti", "superficie", "cf"]
    for element in data:
        for field in fields_to_remove:
            if field in element:
                del element[field]
    return data

# Load the JSON file
with open('italy-cities.json', encoding='utf-8-sig') as file:
    data = json.load(file)["Foglio1"]

# Province map
provinces = {
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

# Replace province abbreviations with province names
data = replace_provinces(data)

# Remove specified fields from each element of the list
data = remove_fields(data)

# Creating the new JSON object with the specified specifications
new_data = {"Foglio1": data}

# Write the modified data to a new JSON file
with open('country-province-cities.json', 'w') as file:
    json.dump(new_data, file, indent=4)

print("File 'country-province-cities.json' created successfully.")

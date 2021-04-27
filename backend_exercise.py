# ##########################################################################
# Author: Adrián Bécares ###################################################
############################################################################
# A small script to load a laboratory database in .json format and filter it,
# selecting the school-oriented laboratories.
# Link to the database: https://labsland.com/api/labs?&country=ES&lang=es

import pandas as pd
import json
import urllib.request as ur

# Load the .json file
url = ur.urlopen('https://labsland.com/api/labs?&country=ES&lang=es')
load_json = json.loads(url.read().decode())

# Get the laboratories and initialize the output dictionary
laboratories = load_json["laboratories"]
filtered_labs = {}

# Search through the laboratories and select the ones that are school-oriented
for i, lab in enumerate(laboratories):
    ed_lvl = lab["educationLevels"]
    
    if "hs" in ed_lvl or "ms" in ed_lvl:        
        
        # Create a new entry and append it to the dictionary
        entry = {
            "Nombre":      lab['name'],
            "Descripción": lab['description'],
            "Institución": lab['institution']
        }
        
        filtered_labs[str(i)] = entry

# Generate a new .json file
filtered_json = json.dumps(filtered_labs)


# Output the .json file (testing only)
#f = open("output.json", "w")
#f.write(filtered_json)
#f.close()

# Output the .csv file
df = pd.read_json(filtered_json)
df.to_csv("output.csv")


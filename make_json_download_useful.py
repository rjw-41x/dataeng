# Python program to read json file

import pandas as pd
import json

# Opening JSON file
in_path = '/Users/randywillard/Work/code/'
data_dir = 'json+data/'
file_name = 'electric_veh_WA.json'
f = open( in_path + data_dir + file_name )

# returns JSON object as a dictionary
data = json.load(f)

column_names=[]
# Iterating through the json meta to get the column names from the meta section
for m in data['meta']['view']['columns']:
    # print( m["name"] )
    column_names.append( m["name"].replace(" ","_" ).replace("-",""))

print (column_names )

# Iterating through the json data section
data_df = pd.DataFrame( data=data['data'], columns=column_names )
# write out converted file to csv
data_df.to_csv( in_path + data_dir + "wa_evs_clean.csv", sep="|")

# show user work is complete
print ( data_df.head())

# Closing file
f.close()

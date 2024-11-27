import pandas as pd
import insert_data_csv_to_db as insert_data

def csv_to_json():
    df = pd.read_csv("insertDATA\paraules_temàtica_penjat.csv")
    d = df.to_dict(orient='list')
    
    return d

data = csv_to_json()


for i in range(500):
    insert_data.insert_data_csv_to_db(i, data)

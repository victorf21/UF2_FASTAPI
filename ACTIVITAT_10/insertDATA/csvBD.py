import pandas as pd

df = pd.read_csv("ACTIVITAT_10\insertDATA\paraules_temàtica_penjat.csv")
d = df.to_dict()

for x in range(len(df)):
    p = df['WORD'][x]
    t = df['THEME'][x]
    print(df)
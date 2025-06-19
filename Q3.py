import pandas as pd

df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")

df.columns = df.iloc[1]
df = df[2:]

df = df[['Adrese', 'Pilsēta']].copy()

filtered = df[
    (df['Adrese'] == 'Adulienas iela') &
    (df['Pilsēta'].isin(['Valmiera', 'Saulkrasti']))
]

print(len(filtered))
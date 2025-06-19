import pandas as pd

df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")
df.columns = df.iloc[1]
df = df[2:]

df = df[['Klients', 'Skaits', 'Kopā']].copy()
df['Skaits'] = pd.to_numeric(df['Skaits'], errors='coerce')
df['Kopā'] = pd.to_numeric(df['Kopā'], errors='coerce')
filtered = df[
    (df['Klients'] == 'Korporatīvais') &
    (df['Skaits'] >= 40) &
    (df['Skaits'] <= 50)
]

total_sum = int(filtered['Kopā'].sum())

print(total_sum)
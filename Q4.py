import pandas as pd

df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")
df.columns = df.iloc[1]
df = df[2:]

df = df[['Produkts', 'Cena']].copy()

df['Cena'] = pd.to_numeric(df['Cena'], errors='coerce')

filtered = df[df['Produkts'].str.contains('LaserJet', na=False)]

average_price = int(filtered['Cena'].mean())

print(average_price)
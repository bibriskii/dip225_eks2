import pandas as pd

df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")
df.columns = df.iloc[1]
df = df[2:]
df = df[['Adrese', 'Skaits']].copy()
df['Skaits'] = pd.to_numeric(df['Skaits'], errors='coerce')

filtered = df[df['Adrese'].str.startswith('Ain', na=False) & (df['Skaits'] < 40)]

print(len(filtered))
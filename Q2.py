import pandas as pd


df = pd.read_excel("sagatave_eksamenam.xlsx", sheet_name="Lapa_0")

df.columns = df.iloc[1]
df = df[2:]
df = df[['Prioritāte', 'Piegādes datums']].copy()

df['Piegādes datums'] = pd.to_datetime(df['Piegādes datums'], errors='coerce')

filtered = df[
    (df['Prioritāte'] == 'High') &
    (df['Piegādes datums'].dt.year == 2015)
]

print(len(filtered))
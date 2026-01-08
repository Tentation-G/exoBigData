import pandas as pd
# Data sample Path
data_s = "meteo_paris_2023_2024_dirty.csv"
# Open le data sample avec pandas -> dataframe
df = pd.read_csv(data_s)
# Conversion des dates en datetime
df["date"] = pd.to_datetime(df["date"])
# Supprimer les doublons
df = df.drop_duplicates()
# Remplacement NA de ce champ par 0
df["precipitation_mm"] = df["precipitation_mm"].fillna(0)
# Remplacement des NA de ce champs par median
wind_kmh_median = df["wind_kmh"].median()
df["wind_kmh"] = df["wind_kmh"].fillna(wind_kmh_median)

# Determination des Valeurs Aberrantes
# Intervalle interquartile
Q1 = df["temp_max"].quantile(0.25)
Q3 = df["temp_max"].quantile(0.75)
ITQ = Q3 - Q1
# Filtre entre les val aberrantes
df = df[
    (df["temp_max"] > Q1 - 1.5 * ITQ) &
    (df["temp_max"] < Q3 + 1.5 * ITQ)
]

print(df.info())
print(df.describe())
import pandas as pd
import numpy as np

# Génération des dates
dates = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")

data = []

np.random.seed(42)

for date in dates:
    month = date.month

    # saisonnalité simple
    if month in [12, 1, 2]:  # hiver
        temp_max = np.random.normal(7, 4)
    elif month in [3, 4, 5]:  # printemps
        temp_max = np.random.normal(15, 4)
    elif month in [6, 7, 8]:  # été
        temp_max = np.random.normal(25, 5)
    else:  # automne
        temp_max = np.random.normal(16, 4)

    temp_min = temp_max - np.random.uniform(4, 9)
    precipitation = max(0, np.random.exponential(2))
    wind = np.random.normal(15, 5)

    data.append([
        date,
        round(temp_max, 1),
        round(temp_min, 1),
        round(precipitation, 1),
        round(abs(wind), 1)
    ])

df = pd.DataFrame(data, columns=[
    "date", "temp_max", "temp_min", "precipitation_mm", "wind_kmh"
])

# Ajout volontaire de problèmes réalistes
df.loc[np.random.choice(df.index, 20), "precipitation_mm"] = np.nan
df.loc[np.random.choice(df.index, 10), "wind_kmh"] = np.nan
df.loc[np.random.choice(df.index, 3), "temp_max"] = 58  # aberrations

df.to_csv("meteo_paris_2023_2024_dirty.csv", index=False)

print("Dataset généré :", df.shape)
print(df.head())

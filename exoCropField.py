import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ----- INIT ----- #
ds = "data-set/crop-yield.csv"
df = pd.read_csv(ds)
cytph = df["Crop_Yield_ton_per_hectare"]

# ----- EXO 1 ----- #
print("----- Exo 1 -----")
# Affichages infos + calcule dispertion
# du rendement (tone recup par hectar -> Crop_Yield_ton_per_hectare)

# 1]
print("1]")
cytph_moy = cytph.mean()
cytph_med = cytph.median()
cytph_min = cytph.min()
cytph_max = cytph.max()

print("Moyenne    :", cytph_moy) # 22.34
print("Medianne   :", cytph_med) # 10.27
print("Minimum    :", cytph_min) # 1.76
print("Maximum    :", cytph_max) # 80.99

# 2]
print("\n2]")
# Calcule de la dispertion
cytph_variance   = round(cytph.var(),2)
cytph_ecart_type = round(np.sqrt(cytph_variance),2)
cytph_coef_de_variation = round(cytph_ecart_type/cytph_moy,2)

print("Variance   :", cytph_variance) # 575.33
print("Ecart_type :", cytph_ecart_type) # 23.99
print("Coef_var   :", cytph_coef_de_variation) # (entre 0 et 1) 1.07 -> dispertion tres tres elevé

# ----- EXO 2 ----- #
print("\n----- Exo 1 -----")
# Analyse Univarié et Bivarié

# 1.1] Analyse par culture
print("1.1]")
"""
Calculer le rendement moyen par Crop_Type
-Identifier :
 -la culture la plus productive
 -la moins productive
"""

crop_type_rend_moy = df.groupby("Crop_Type")["Crop_Yield_ton_per_hectare"].mean()

print("Rend moy per crop type :\n",crop_type_rend_moy)

# 1.2] +/- productive
print("\n1.2]")
crop_type_rend_moy_min = round(min(crop_type_rend_moy),2)
idx_crop_type_rend_min = crop_type_rend_moy.idxmin()
crop_type_rend_moy_max = round(max(crop_type_rend_moy),2)
idx_crop_type_rend_max = crop_type_rend_moy.idxmax()

print("Crop type la moins productive :", idx_crop_type_rend_min, crop_type_rend_moy_min)
print("Crop type la plus productive  :", idx_crop_type_rend_max, crop_type_rend_moy_max)

# 2.1] Analyse par Soil_type et Soil_pH
print("\n2.1]")
# Moyenne rend per Soil_type (Enum -> ca chill un coup)
soil_type_rend_moy = df.groupby("Soil_Type")["Crop_Yield_ton_per_hectare"].mean()
soil_type_rend_moy = soil_type_rend_moy.sort_values(ascending=False)
print("Rendement Moyen par",soil_type_rend_moy)

"""
plt.figure()
soil_type_rend_moy.plot(kind="bar")
plt.title("Rendement moyen par type de sol")
plt.xlabel("Soil_Type")
plt.ylabel("Yield (t/ha)")
plt.tight_layout()
plt.show()
"""

# Meilleurs rend ped Soil_pH
bins = [4,5,6,7,8,9]

# Creer une nouvelle colonne
df["pH_bin"] = pd.cut(
    df["Soil_pH"],
    bins=bins,
    include_lowest=True
)
plt.figure()
plt.scatter(df["Soil_pH"], df["Crop_Yield_ton_per_hectare"], alpha=0.2)
plt.title("Soil pH vs Crop Yield")
plt.xlabel("Soil_pH")
plt.ylabel("Yield (t/ha)")
plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np

# ----- INIT ----- #
ds = "data-set/crop-yield.csv"
df = pd.read_csv(ds)
cytph = df["Crop_Yield_ton_per_hectare"]

# ----- EXO 1 ----- #
# Affichages infos + calcule dispertion
# du rendement (tone recup par hectar -> Crop_Yield_ton_per_hectare)

# 1]
cytph_moy = cytph.mean()
cytph_med = cytph.median()
cytph_min = cytph.min()
cytph_max = cytph.max()

print("Moyenne    :", cytph_moy) # 22.34
print("Medianne   :", cytph_med) # 10.27
print("Minimum    :", cytph_min) # 1.76
print("Maximum    :", cytph_max) # 80.99

# 2]
# Calcule de la dispertion
cytph_variance   = round(cytph.var(),2)
cytph_ecart_type = round(np.sqrt(cytph_variance),2)
cytph_coef_de_variation = round(cytph_ecart_type/cytph_moy,2)

print("Variance   :", cytph_variance) # 575.33
print("Ecart_type :", cytph_ecart_type) # 23.99
print("Coef_var   :", cytph_coef_de_variation) # (entre 0 et 1) 1.07 -> dispertion tres tres elevé

# ----- EXO 2 ----- #
#

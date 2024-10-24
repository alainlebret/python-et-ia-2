import numpy as np
import pandas as pd

np.random.seed(42)
n_points = 100

# Génération de données
temps = pd.date_range('08:00', periods=n_points, freq='10T').time  # Période de temps à 10 minutes d'intervalle
temperature = 25 + 5 * np.sin(np.linspace(0, 3 * np.pi, n_points)) + np.random.normal(0, 1, n_points)  # Relation non-linéaire
pression = np.linspace(1000, 1020, n_points) + np.random.normal(0, 1.5, n_points)  # Données avec un peu de bruit

# Humidité corrigée avec une relation polynomiale mais dans des valeurs réalistes
humidite = 50 + 0.2 * temperature + 0.05 * pression + np.random.normal(0, 5, n_points)

# Création du DataFrame
df_donnees = pd.DataFrame({
    'temps': temps,
    'temperature': temperature,
    'pression': pression,
    'humidite': humidite
})

# Sauvegarde du jeu de données
df_donnees.to_csv('jeu_donnees_tp7_corrected.csv', index=False)

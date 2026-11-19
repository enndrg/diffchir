import numpy as np
from scipy.ndimage import maximum_filter

def calculer_fraunhofer(champ_objet: np.ndarray) -> np.ndarray:
    #Calcule I_diff avec FFT
    champ_diffracte = np.fft.fftshift(np.fft.fft2(champ_objet))
    intensite = np.abs(champ_diffracte)**2
    return intensite / np.max(intensite)  # Normalisation

def extraire_pics_bragg(intensite: np.ndarray, seuil_relatif: float = 0.05, taille_voisinage: int = 10):
    # Détecte les coordonnées et intensités des ordres de diffraction.
    max_locaux = (intensite == maximum_filter(intensite, size=taille_voisinage))
    masque_seuil = intensite > (seuil_relatif * np.max(intensite))
    pics = max_locaux & masque_seuil
    
    y_idx, x_idx = np.where(pics)
    valeurs = intensite[y_idx, x_idx]
    return x_idx, y_idx, valeurs

def calculer_dissymetrie(intensite_G: np.ndarray, intensite_D: np.ndarray) -> float:
#Calcule g comme def
    diff = np.abs(intensite_G - intensite_D)
    somme = intensite_G + intensite_D + 1e-12  # Évite la division par zéro
    return float(np.mean(diff / somme))

import os
import numpy as np
import matplotlib.pyplot as plt

def sauvegarder_figure_unique(champ_objet: np.ndarray, intensite: np.ndarray, 
                              L: float, dossier_sortie: str = "results", nom_fichier: str = "diffraction.png"):
    # Comparaison Reel / FFT
    os.makedirs(dossier_sortie, exist_ok=True)
    N = champ_objet.shape[0]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
    
    # Espace réel (Phase)
    extent_um = [-L / 2 * 1e6, L / 2 * 1e6, -L / 2 * 1e6, L / 2 * 1e6]
    im1 = ax1.imshow(np.angle(champ_objet), cmap='twilight', extent=extent_um)
    ax1.set_title("Phase de la surface chirale (µm)")
    ax1.set_xlabel("x (µm)")
    ax1.set_ylabel("y (µm)")
    ax1.set_xlim(-20, 20)
    ax1.set_ylim(-20, 20)
    plt.colorbar(im1, ax=ax1, label="Phase (rad)")
    
    # Espace réciproque (Diffraction)
    im2 = ax2.imshow(np.log1p(intensite * 1e4), cmap='inferno')
    ax2.set_title("Cliché de diffraction (log I)")
    ax2.set_xlabel("Fréquence spatiale u (px)")
    ax2.set_ylabel("Fréquence spatiale v (px)")
    zoom = N // 6
    ax2.set_xlim(N // 2 - zoom, N // 2 + zoom)
    ax2.set_ylim(N // 2 - zoom, N // 2 + zoom)
    plt.colorbar(im2, ax=ax2, label="Intensité (u.a., log)")
    
    plt.tight_layout()
    plt.savefig(os.path.join(dossier_sortie, nom_fichier), dpi=300)
    plt.close()

def sauvegarder_balayage(valeurs_chi: np.ndarray, dissymetries: list, 
                         dossier_sortie: str = "results", nom_fichier: str = "balayage_chiralite.png"):
    # trace g en fonct ion de la disymetrie
    os.makedirs(dossier_sortie, exist_ok=True)
    
    plt.figure(figsize=(7, 4))
    plt.plot(valeurs_chi, dissymetries, marker='o', linewidth=2, color='#d95f02')
    plt.title("Sensibilité de la diffraction à la chiralité géométrique")
    plt.xlabel("Paramètre de chiralité $\chi$")
    plt.ylabel("Facteur de dissymétrie moyen $g$")
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig(os.path.join(dossier_sortie, nom_fichier), dpi=300)
    plt.close()

import numpy as np
from src.geometry import generer_surface_spirale
from src.diffraction import calculer_fraunhofer, calculer_dissymetrie
from src.visualization import sauvegarder_figure_unique, sauvegarder_balayage

def executer_pipeline():
    N = 1024
    L = 100e-6
    profondeur_phase = np.pi / 2

    print("Simulation d'un cas (chi = 1.5)")
    champ_G = generer_surface_spirale(N, L, chiralite=1.5, profondeur_phase=profondeur_phase)
    intensite_G = calculer_fraunhofer(champ_G)
    sauvegarder_figure_unique(champ_G, intensite_G, L, nom_fichier="simulation_nom.png")
    print("ok dans results/simulation_nominale.png")

    print("Balayage paramétrique (Enantiomère G // Enantiomère D)")
    plage_chi = np.linspace(0.0, 3.0, 15)
    facteurs_g = []

    for chi in plage_chi:
        # Génération des deux énantiomères (+chi et -chi)
        c_G = generer_surface_spirale(N, L, chiralite=+chi, profondeur_phase=profondeur_phase)
        c_D = generer_surface_spirale(N, L, chiralite=-chi, profondeur_phase=profondeur_phase)
        
        i_G = calculer_fraunhofer(c_G)
        i_D = calculer_fraunhofer(c_D)
        
        g = calculer_dissymetrie(i_G, i_D)
        facteurs_g.append(g)
        print(f"chi = {chi:.2f} -> Dissymétrie g = {g:.4f}")

    sauvegarder_balayage(plage_chi, facteurs_g)
    print("Courbe de balayage sauvegardée dans results/balayage_chiralite.png")

if __name__ == "__main__":
    executer_pipeline()

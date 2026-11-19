import numpy as np

def creer_grille(N: int, L: float):
    """Génère les grilles de coordonnées spatiales 2+D."""
    x = np.linspace(-L / 2, L / 2, N, endpoint=False)
    return np.meshgrid(x, x)

def generer_surface_spirale(N: int, L: float, n_cell: int = 64, 
                            chiralite: float = 1.0, profondeur_phase: float = np.pi / 2, 
                            w0: float = 30e-6) -> np.ndarray:
                              
    X, Y = creer_grille(N, L)
    
    # maille élémentaire
    xc = np.linspace(-1, 1, n_cell)
    Xc, Yc = np.meshgrid(xc, xc)
    R = np.sqrt(Xc**2 + Yc**2)
    Theta = np.arctan2(Yc, Xc)
    
    # def géo du motif
    motif = np.sin(3 * Theta + chiralite * 5 * R)
    masque_binaire = (motif > 0) & (R < 0.8)
    
    # pavage
    repetitions = N // n_cell
    surface = np.tile(masque_binaire, (repetitions, repetitions))
    
    # transmittance de phase pure
    transmittance = np.exp(1j * profondeur_phase * surface)
    
    # "Enveloppe" du faisceau incident
    faisceau = np.exp(-(X**2 + Y**2) / w0**2)
    
    return transmittance * faisceau

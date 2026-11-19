# Diffchir -Simulation de Diffraction sur Surfaces Chirales (Modèle Scalaire)

Outil numérique en Python qui automatise le calcul de figures de diffraction en champ lointain générées par des surfaces structurées chirales 2D.

## Cadre Physique

Le modèle repose sur l'optique de Fourier scalaire :
* **Diffraction de Fraunhofer :** L'amplitude diffractée $U(u,v)$ dans le plan focal d'une lentille est calculée via la Transformée de Fourier 2D (FFT) de la fonction de transmittance complexe $t(x,y)$ de la surface :
  $$U(u, v) \propto \mathcal{F}\{t(x, y)\}$$
* **Non-Symétrie et Chiralité :** Selon la loi de Friedel, un masque purement réel produit une figure de diffraction centrosymétrique ($I(u,v) = I(-u,-v)$), masquant la chiralité géométrique. Pour rendre la signature chirale observable directement dans l'intensité diffractée, ce code implémente des **masques de phase** ($t(x,y) = e^{i\phi(x,y)}$) simulant un relief gravé sur la surface.
* **Quantification :** L'asymétrie entre ordres de diffraction opposés ou entre deux énantiomères ($G$ et $D$) est mesurée via le facteur de dissymétrie $g$ :
  $$g = \frac{I_G(m,n) - I_D(m,n)}{I_G(m,n) + I_D(m,n)}$$

## Architecture du Projet

A rédiger 


## Utilisation

Exécuter le script principal pour lancer la simulation par défaut et générer les figures dans le dossier `results/` :

```bash
python main.py
```
## Licence
MIT (a finir)

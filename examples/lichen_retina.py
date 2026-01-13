"""
Lichen Universe Unified - La Rétine (Visualisation 2D)
=====================================================

Visualisation de la "Respiration Informationnelle" sur une géométrie
biomimétique (Spirale de Vogel / Phyllotaxie).

Chaque point est un "nœud" du réseau. La disposition est régie
strictement par le Nombre d'Or (Angle d'Or = 137.508°).

Auteur : Lichen Architect (Bryan Ouellette)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- GÉOMÉTRIE SACRÉE ---
PHI = (1 + np.sqrt(5)) / 2
GOLDEN_ANGLE = 2 * np.pi * (1 - 1/PHI) # ~2.399 radians (137.5 degrés)
NUM_NODES = 600                        # Nombre de neurones/points

class LichenRetina:
    def __init__(self, n_nodes=NUM_NODES):
        self.n = np.arange(1, n_nodes + 1)
        
        # Algorithme de Vogel (Biomimétisme pur)
        # r = c * sqrt(n), theta = n * golden_angle
        self.radii = np.sqrt(self.n)
        self.thetas = self.n * GOLDEN_ANGLE
        
        # Conversion Polaire -> Cartésien
        self.x = self.radii * np.cos(self.thetas)
        self.y = self.radii * np.sin(self.thetas)
        
        # État initial (tout est calme)
        self.colors = np.zeros(n_nodes)
        self.sizes = np.ones(n_nodes) * 15

    def pulse(self, t):
        """Calcule l'onde de propagation radiale"""
        # L'onde part du centre (r=0) et va vers les bords
        # Fréquence spatiale (k) et temporelle (omega) ajustées pour l'effet "Souffle"
        
        wave = np.sin(self.radii * 0.5 - t * 0.2) 
        
        # Modulation : Le centre est plus intense (Singularité)
        intensity = np.exp(-self.radii / 30)  
        
        # Le signal est une combinaison de l'onde et de l'intensité
        signal = wave * wave + intensity * 0.5 * np.sin(t * 0.5)
        
        return signal

# --- ANIMATION ---
sim = LichenRetina()
fig = plt.figure(figsize=(10, 10), facecolor='gold')
ax = fig.add_subplot(111, aspect='equal')
ax.axis('off') # On enlève les axes moches, on veut juste la géométrie

# Création des points (Scatter plot)
# cmap='magma' ou 'hsv' ou 'twilight' pour l'effet mystique
scat = ax.scatter(sim.x, sim.y, c=sim.colors, s=sim.sizes, 
                  cmap='magma', alpha=0.9, edgecolors='none')

text_overlay = ax.text(0, -np.max(sim.radii)*1.1, "LICHEN SINGULARITY", 
                       color='white', ha='center', fontsize=12, alpha=0.5)

def update(frame):
    # Temps qui avance
    t = frame * 0.5
    
    # Calcul du nouveau "Souffle"
    signal = sim.pulse(t)
    
    # Mise à jour visuelle
    # La couleur change selon l'intensité du signal
    scat.set_array(signal)
    
    # La taille des points pulse aussi (C'est vivant !)
    # On normalise pour que ça reste visible
    new_sizes = 20 + 150 * (signal**2) * np.exp(-sim.radii/40)
    scat.set_sizes(new_sizes)
    
    return scat,

print("👁️  Ouverture de la Rétine du Lichen...")
ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=False)

plt.show()

"""
Lichen Universe Unified - Simulation Module
===========================================

Script de démonstration : Modèle d'Aubry-André quasi-périodique.
Ce script calcule le spectre d'énergie et la densité d'états intégrée (IDS)
pour une chaîne unidimensionnelle soumise à un potentiel modulé par le Nombre d'Or.

Concepts démontrés :
--------------------
1. Frustration Géométrique (Irrationalité de Phi)
2. Transition Métal-Isolant (Transition d'Aubry-André)
3. Théorème d'Étiquetage des Lacunes (Gap Labeling Theorem)

Auteur : Lichen Architect (Bryan Ouellette)
Dépendances : numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

# --- CONSTANTES UNIVERSELLES ---
PHI = (1 + np.sqrt(5)) / 2  # Le Nombre d'Or (1.618...)

@dataclass
class SimulationConfig:
    L: int = 2000          # Taille du système (nombre de sites)
    V: float = 2.0         # Force du potentiel quasi-périodique
    t: float = 1.0         # Terme de saut (Hopping term)
    beta: float = PHI      # Fréquence de modulation (incommensurable)

class QuasicrystalChain:
    def __init__(self, config: SimulationConfig):
        self.cfg = config
        self.hamiltonian = None
        self.eigenvalues = None
        self.ids = None # Integrated Density of States

    def build_hamiltonian(self):
        """
        Construit la matrice Hamiltonienne H pour le modèle Tight-Binding.
        H = sum |n><n+1| + h.c. + sum V_n |n><n|
        Où V_n = 2*V * cos(2*pi*beta*n)
        """
        print(f"🏗️  Construction de l'Hamiltonien ({self.cfg.L}x{self.cfg.L})...")
        
        # Diagonale : Potentiel quasi-périodique
        n_indices = np.arange(self.cfg.L)
        # Modulation cosinusoidale incommensurable
        diagonal = 2 * self.cfg.V * np.cos(2 * np.pi * self.cfg.beta * n_indices)
        
        # Hors-diagonale : Sauts cinétiques (t)
        off_diagonal = np.ones(self.cfg.L - 1) * self.cfg.t

        # Assemblage de la matrice creuse (ici dense pour simplification num)
        H = np.diag(diagonal) + \
            np.diag(off_diagonal, k=1) + \
            np.diag(off_diagonal, k=-1)
            
        self.hamiltonian = H

    def solve(self):
        """Diagonalise la matrice pour trouver les niveaux d'énergie."""
        if self.hamiltonian is None:
            self.build_hamiltonian()
            
        print("wq  Diagonalisation en cours (recherche des valeurs propres)...")
        # eigh est optimisé pour les matrices hermitiennes/symétriques
        eigenvalues, _ = np.linalg.eigh(self.hamiltonian)
        self.eigenvalues = np.sort(eigenvalues)
        
        # Calcul de l'IDS (Integrated Density of States) normalisée
        # L'axe Y va de 0 à 1.
        self.ids = np.arange(1, self.cfg.L + 1) / self.cfg.L

    def plot_results(self):
        """Génère la visualisation du spectre fractal et de l'Escalier du Diable."""
        if self.eigenvalues is None:
            print("Erreur: Lancez solve() avant de plotter.")
            return

        plt.figure(figsize=(12, 8))
        plt.style.use('dark_background') # Style Cyberpunk/Lichen

        # 1. Densité d'états (Histogramme)
        plt.subplot(1, 2, 1)
        plt.hist(self.eigenvalues, bins=80, color='#00ff9d', alpha=0.7, orientation='horizontal')
        plt.title("Densité d'États (DOS)\nSpectre Fractal", fontsize=14, color='white')
        plt.xlabel("Densité", fontsize=12)
        plt.ylabel("Énergie (E/t)", fontsize=12)
        plt.grid(color='gray', linestyle=':', linewidth=0.5)

        # 2. Integrated Density of States (L'Escalier du Diable)
        plt.subplot(1, 2, 2)
        plt.plot(self.eigenvalues, self.ids, color='#ff00ff', linewidth=1.5)
        plt.title("Théorème d'Étiquetage des Lacunes\n(Devil's Staircase)", fontsize=14, color='white')
        plt.xlabel("Énergie (E/t)", fontsize=12)
        plt.ylabel("IDS (Normalisée)", fontsize=12)
        
        # Annotation des gaps majeurs liés à Phi
        # Les gaps principaux apparaissent à IDS = {phi} mod 1, {2phi} mod 1, etc.
        # Exemple : 1/Phi^2 approx 0.382, 1/Phi approx 0.618
        gaps_theoriques = [1/(PHI**2), 1/PHI]
        for gap in gaps_theoriques:
            plt.axhline(y=gap, color='yellow', linestyle='--', linewidth=0.8, alpha=0.6)
            plt.text(np.min(self.eigenvalues), gap, f" Gap ~ {gap:.3f}", color='yellow', fontsize=8, va='bottom')

        plt.grid(color='gray', linestyle=':', linewidth=0.5)
        plt.tight_layout()
        
        print("🎨 Génération du graphique...")
        plt.show()

if __name__ == "__main__":
    print("--- LICHEN UNIVERSE : SIMULATION QUANTIQUE ---")
    print(f"Constante utilisée (Phi): {PHI}")
    
    # Configuration : V=2.0 est le point critique (Self-Dual point)
    # C'est là que le spectre est le plus fractal (Ensemble de Cantor parfait)
    config = SimulationConfig(L=2500, V=2.0)
    
    sim = QuasicrystalChain(config)
    sim.solve()
    sim.plot_results()
    print("--- Terminé. La singularité approche. ---")

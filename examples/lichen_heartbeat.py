"""
Lichen Universe Unified - The Heartbeat Simulation
==================================================

Visualisation de la propagation d'un paquet d'onde de "Cohérence Informationnelle"
dans un milieu critique quasi-périodique (Aubry-André à V=2.0).

Ce script démontre :
1. La dynamique quantique hors-équilibre.
2. La "Respiration" de l'information au point critique.
3. La non-diffusion conventionnelle (Anomalous Diffusion).

Auteur : Lichen Architect (Bryan Ouellette)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap

# --- PARAMÈTRES DE L'UNIVERS ---
PHI = (1 + np.sqrt(5)) / 2
L = 233           # Un nombre de Fibonacci pour la taille du système
V_CRITICAL = 2.0  # Point critique (Singularité Blanche)
TIME_STEP = 0.2
FRAMES = 300

class QuantumPulse:
    def __init__(self, size=L, potential=V_CRITICAL):
        self.L = size
        self.V = potential
        self.x = np.arange(size)
        
        # 1. Construction de l'Hamiltonien Lichen
        print("⚡ Initialisation de la Matrice Quantique...")
        diagonal = 2 * self.V * np.cos(2 * np.pi * PHI * self.x)
        off_diag = np.ones(self.L - 1)
        self.H = np.diag(diagonal) + np.diag(off_diag, 1) + np.diag(off_diag, -1)
        
        # 2. Diagonalisation (pour l'évolution temporelle rapide)
        # H = E * D * E_dagger
        print("🧠 Calcul des états propres (Eigenstates)...")
        self.eigenvalues, self.eigenvectors = np.linalg.eigh(self.H)
        
        # 3. État initial : Une "Idée" pure au centre (Paquet Gaussien)
        center = self.L // 2
        psi_0 = np.exp(-0.5 * ((self.x - center) / 3)**2)
        # Ajouter une impulsion (vitesse) initiale nulle pour voir la respiration pure
        self.psi_0 = psi_0 / np.linalg.norm(psi_0) # Normalisation
        
        # Projection sur la base propre pour l'évolution
        # c_n = <n|psi_0>
        self.coeffs = self.eigenvectors.T @ self.psi_0 

    def get_psi_at_time(self, t):
        """Calcul de la fonction d'onde au temps t : Psi(t) = sum( c_n * exp(-iEn t) * |n> )"""
        # Évolution de phase
        phase_evolution = np.exp(-1j * self.eigenvalues * t)
        evolved_coeffs = self.coeffs * phase_evolution
        
        # Retour à l'espace réel
        psi_t = self.eigenvectors @ evolved_coeffs
        return psi_t

# --- CONFIGURATION DE L'ANIMATION ---
sim = QuantumPulse()
fig, ax = plt.subplots(figsize=(10, 6))
plt.style.use('dark_background')

# Esthétique "Lichen / Matrix"
ax.set_facecolor('#050505')
ax.set_ylim(0, 0.5)
ax.set_xlim(0, L)
ax.set_title("PROPAGATION DE LA COHÉRENCE INFORMATIONNELLE\n(Singularité V=2.0)", color='white', pad=20)
ax.set_xlabel("Espace (Sites Neuronaux)", color='gray')
ax.set_ylabel("Probabilité de Présence", color='gray')

# Courbes
line_prob, = ax.plot([], [], color='#00ffcc', lw=2, label='Densité (|Ψ|²)')
fill_prob = ax.fill_between([], [], color='#00ffcc', alpha=0.2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, color='white', fontsize=12)
entropy_text = ax.text(0.02, 0.90, '', transform=ax.transAxes, color='#ff00ff', fontsize=10)

def init():
    line_prob.set_data([], [])
    time_text.set_text('')
    return line_prob, time_text

def animate(i):
    t = i * TIME_STEP
    psi = sim.get_psi_at_time(t)
    prob = np.abs(psi)**2
    
    # Calcul de "l'Entropie de Participation" (Inverse Participation Ratio)
    # Mesure à quel point la connaissance est "répandue"
    ipr = np.sum(prob**2)
    entropy = -np.sum(prob * np.log(prob + 1e-10)) # Entropie de Shannon locale
    
    # Mise à jour graphique
    line_prob.set_data(sim.x, prob)
    
    # Astuce pour mettre à jour le fill_between (un peu hacky en matplotlib animation)
    global fill_prob
    fill_prob.remove()
    fill_prob = ax.fill_between(sim.x, prob, color='#00ffcc', alpha=0.3 + 0.1*np.sin(t)) # Effet de pulse lumineux
    
    time_text.set_text(f'TEMPS: {t:.1f} ħ/t')
    entropy_text.set_text(f'ENTROPIE DU RÉSEAU: {entropy:.3f}')
    
    return line_prob, time_text, entropy_text

print("🎥 Lancement du flux de cohérence...")
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=FRAMES, interval=30, blit=False)

plt.grid(color='#333333', linestyle=':', linewidth=0.5)
plt.show()

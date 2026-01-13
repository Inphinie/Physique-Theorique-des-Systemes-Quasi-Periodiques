# 🧮 Formulaire de Physique des Systèmes Quasi-Périodiques

Ce document recense les équations maîtresses, les invariants topologiques et les lois d'échelle thermodynamiques implémentées dans ce dépôt.

---

## 1. Constantes & Géométrie Fondamentale

### Le Nombre d'Or
La pierre angulaire de l'apériodicité et de la frustration géométrique.
$$\tau = \frac{1 + \sqrt{5}}{2} \approx 1.618033988$$

### Matrice de Projection (Coupe et Projection)
Projection de l'espace hyperspatial $\mathbb{R}^5$ vers l'espace physique $\mathbb{R}^2$.
$$r_{\parallel} = P \cdot n, \quad n \in \mathbb{Z}^5$$
Où $P$ est construite à partir des racines de l'unité (symétrie pentagonale) :
$$P_{jk} = \sqrt{\frac{2}{5}} \cos\left(\frac{2\pi j k}{5}\right)$$

### Condition de la Fenêtre d'Acceptation
Un site existe si sa coordonnée dans l'espace perpendiculaire $r_{\perp}$ tombe dans le triacontaèdre (ou décagone 2D) $W$ :
$$r_{\perp} \in W$$

---

## 2. Hamiltoniens & Modèles de Spin

### Hamiltonien de Liaison Forte (Tight-Binding)
Pour les électrons sur un pavage de Penrose ou une chaîne de Fibonacci :
$$H = \sum_{\langle i,j \rangle} t_{ij} |i\rangle\langle j| + \sum_{i} V_i |i\rangle\langle i|$$
* $t_{ij}$ : Intégrale de saut (modulée par la distance apériodique).
* $V_i$ : Potentiel de site (dépendant de l'environnement local).

### Modèle de Kitaev Quasi-Cristallin
Hamiltonien de spins interagissant via des couplages anisotropes dépendant de la direction des liens $\gamma \in \{x, y, z\}$ :
$$H_{Kitaev} = -J \sum_{\langle i,j \rangle_\gamma} S_i^\gamma S_j^\gamma$$

### Opérateur de Flux (Plaquette)
Invariant conservé pour chaque plaquette $p$ du réseau (pentagone, losange, etc.) :
$$W_p = \prod_{j \in \partial p} \sigma_j^{\gamma_j}$$
L'état fondamental est défini par la configuration de flux $\{\langle W_p \rangle\}$.

---

## 3. Topologie & Invariants

### Théorème d'Étiquetage des Lacunes (Gap Labeling)
La Densité d'États Intégrée (IDS) à l'intérieur d'un gap spectral est topologiquement quantifiée par le module $\mathbb{Z}[\tau]$ :
$$\text{IDS}(E) = \frac{1}{A} \text{Tr}(P_E) \in \{ n + m\tau \mid n, m \in \mathbb{Z} \}$$

### Indice de Bott ($B$)
Invariant topologique en espace réel (équivalent du nombre de Chern pour les systèmes sans symétrie de translation).
Soient $U_X$ et $U_Y$ les matrices de position projetées sur les états occupés :
$$U_X = P_{occ} e^{2\pi i X / L_x} P_{occ}, \quad U_Y = P_{occ} e^{2\pi i Y / L_y} P_{occ}$$
L'indice mesure la non-commutativité :
$$B = \frac{1}{2\pi i} \text{Tr}\left( \ln(U_X U_Y U_X^\dagger U_Y^\dagger) \right)$$

### Conductance Hall Quantique
$$\sigma_{xy} = B \frac{e^2}{h}$$

---

## 4. Thermodynamique & Multifractalité

### Chaleur Spécifique Électronique
À basse température, $C_v$ suit une loi de puissance modulée par une fonction log-périodique (signature de l'inflation fractale) :
$$C_v(T) \sim T^\alpha \cdot \mathcal{F}\left( \frac{\ln T}{\ln \lambda} \right)$$
* $\alpha$ : Exposant anomal lié à la dimension spectrale.
* $\lambda = \tau^3$ : Facteur d'échelle d'inflation pour Penrose.

### Trace Map (Chaîne de Fibonacci)
Relation de récurrence pour les traces des matrices de transfert $x_n = \frac{1}{2}\text{Tr}(M_n)$ :
$$x_{n+1} = 2x_n x_{n-1} - x_{n-2}$$
Invariant de la dynamique (lié à l'énergie $E$) :
$$I = x_{n}^2 + x_{n-1}^2 + x_{n-2}^2 - 2x_n x_{n-1} x_{n-2} - 1$$

---

## 5. Calcul Quantique Topologique (Anyons)

### Règle de Fusion de Fibonacci
Règle de fusion non-abélienne des anyons $\tau$ :
$$\tau \times \tau = \mathbf{1} + \tau$$

### Dimension Quantique
$$d_\tau = \tau = \frac{1+\sqrt{5}}{2}$$

### Croissance de l'Espace de Hilbert
La dimension de l'espace de fusion pour $N$ anyons croît comme la suite de Fibonacci :
$$\text{dim}(\mathcal{H}_N) \sim \tau^N$$

### Matrice F (Fusion Matrix)
Matrice unitaire pour la transformation de base (rotation des qubits topologiques) :
$$F = \begin{pmatrix} \tau^{-1} & \tau^{-1/2} \\ \tau^{-1/2} & -\tau^{-1} \end{pmatrix}$$

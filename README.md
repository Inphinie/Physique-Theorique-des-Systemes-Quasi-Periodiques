# Physique Théorique des Systèmes Quasi-Périodiques : Topologie, Frustration et Émergence

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Physics: Condensed Matter](https://img.shields.io/badge/Physics-Condensed%20Matter-blue.svg)](https://arxiv.org/archive/cond-mat)

##  🌌 Introduction

Ce dépôt héberge une formalisation canonique et falsifiable de la physique des systèmes quasi-périodiques (pavages de Penrose, chaînes de Fibonacci). Ce travail synthétise l'héritage géométrique de Penrose et de Bruijn avec les outils modernes de la topologie quantique et de la thermodynamique computationnelle.

L'objectif est de démontrer comment l'irrationalité du Nombre d'Or ($\phi$), lorsqu'elle est encodée dans la structure même de la matière, engendre des phénomènes émergents exotiques : liquides de spins chiraux, spectres multifractals et potentiel pour le calcul quantique topologique.

## 📐 Fondements Géométriques : L'Ordre Caché

La théorie repose sur l'axiome de **Coupe et Projection** (Cut-and-Project). L'ordre apériodique observé dans l'espace physique est interprété comme la projection d'une structure hypercubique parfaite résidant dans un super-espace de dimension $N=5$.

* **Matrice de Projection :** Utilisation des racines de l'unité associées à la symétrie d'ordre 5.
* **Fenêtre d'Acceptation :** Sélection des sites via un triacontaèdre rhombique dans l'espace interne ("perpendiculaire").
* **Hyperuniformité :** Suppression anormale des fluctuations de densité à grande échelle ($S(k) \to 0$ quand $k \to 0$).

## 🧩 Frustration Géométrique en forme de $\phi$

Nous explorons les conséquences physiques de l'imposition d'une frustration géométrique sur une structure régie par $\phi$.

### Squelette Rigide vs Clusters Fluctuants
Contrairement aux réseaux périodiques, la frustration sur un pavage de Penrose induit une séparation de phase intrinsèque :
1.  **Squelette Rigide :** ~75% des spins se gèlent dans une configuration a-périodique stable.
2.  **Entropie Résiduelle :** Des clusters décagonaux conservent une liberté de retournement ("flippable clusters"), générant une entropie résiduelle spécifique à $\ln \tau$.

### Glaces de Spin Artificielles (ASI)
Analyse de la topologie des vertex (coordinence $z=3, 5$) qui force l'émergence de **monopôles magnétiques** comme défauts topologiques inévitables, plutôt que comme simples excitations thermiques.

## ⚛️ Dynamique Quantique et Topologie

L'application des modèles de spins quantiques (Heisenberg, Kitaev) sur ces géométries révèle des phases de la matière hautement intriquées.

### 1. Théorème d'Étiquetage des Lacunes (Gap Labeling)
Les valeurs de la Densité d'États Intégrée (IDS) à l'intérieur des lacunes spectrales sont quantifiées par le $\mathbb{Z}$-module engendré par le nombre d'or :
$$\mathcal{M} = \{ n + m\tau \mid n, m \in \mathbb{Z} \}$$
Toute mesure expérimentale de conductance déviant de ce module invalide la structure quasi-cristalline idéale.

### 2. Indice de Bott et Effet Hall
En l'absence de zone de Brillouin, nous utilisons l'**Indice de Bott** (commutativité approximative des matrices de position) comme invariant topologique en espace réel, relié directement à la conductance Hall $\sigma_{xy}$.

### 3. Modèle de Kitaev Quasi-Cristallin
L'état fondamental sur un réseau de Penrose tri-coordonné est un **Liquide de Spin Chiral** qui brise spontanément la symétrie par renversement du temps (TRS) sans champ magnétique externe, supportant des fermions de Majorana critiques.

## 🔥 Thermodynamique Falsifiable

La théorie propose des prédictions expérimentales précises basées sur la structure fractale du spectre d'énergie (Ensemble de Cantor).

**Chaleur Spécifique Électronique :**
$$C_v(T) \sim T^{\alpha} \cdot P(\ln T / \ln \lambda)$$
* Une loi de puissance anormale ($\alpha \neq 1$).
* Des **oscillations log-périodiques** $P(x)$ de faible amplitude, signature directe de l'auto-similarité discrète et de l'inflation ($\lambda = \phi^3$).

## 💻 Applications : Calcul Quantique Topologique

La frustration géométrique $\phi$ est identifiée comme un catalyseur pour la stabilisation des **Anyons de Fibonacci**.
* **Fusion Dorée :** $\tau \times \tau = 1 + \tau$
* **Universalité :** Ces quasi-particules permettent le calcul quantique universel via le tressage (braiding), le quasi-cristal agissant comme un piège naturel empêchant leur cristallisation conventionnelle.

---

### Références Principales
Ce travail s'appuie sur et étend les travaux de :
* **R. Penrose & N.G. de Bruijn :** Pavages et méthode de projection.
* **J. Bellissard :** $C^*$-algèbres et Gap Labeling Theorem.
* **A. Kitaev :** Liquides de spins et modèles exactement solubles.

---
*Ce dépôt contient les formalisations théoriques et les résultats de simulations computationnelles (Tensor Networks / Monte Carlo).*

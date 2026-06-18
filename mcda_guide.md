# 🧭 Guide MCDA — Méthodes, équations & application

> Document de référence consolidé. Toutes les méthodes MCDA classiques et récentes (2024–2026),  
> avec liens, équations, avantages, limites et un exemple d'application complet.

---

## Table des matières

1. [Vue d'ensemble — Classification des méthodes](#1-vue-densemble)
2. [Nouveaux algorithmes MCDA (2024–2026)](#2-nouveaux-algorithmes-mcda-20242026)
3. [Méthodes classiques influentes](#3-méthodes-classiques-influentes)
4. [Tableau comparatif global](#4-tableau-comparatif-global)
5. [Application : sélection d'une méthode de correction de données](#5-application--sélection-dune-méthode-de-correction-de-données)

---

# 1. Vue d'ensemble

## 1.1 Classification des méthodes

| Méthode | Famille | Horizon | Idée clé | Cas d'usage |
|---------|---------|---------|----------|-------------|
| **MAUT/MAVT** | Value | Classique | Fonctions d'utilité multi-attributs | Base théorique |
| **AHP** | Value | Classique | Comparaisons par paires hiérarchiques | Décision générale |
| **ANP** | Value | Classique | AHP avec dépendances et boucles | Systèmes interdépendants |
| **SMART/SMARTER** | Value | Classique | Pondération simple par ratio | Industrie, rapidité |
| **TOPSIS** | Distance | Classique | Distance à l'idéal et à l'anti-idéal | Classement robuste |
| **VIKOR** | Distance/Compromis | Classique | Compromis utilité–regret | Décision collective |
| **COPRAS** | Distance | Classique | Rapport proportionnel direct | Simplicité, transparence |
| **ELECTRE** | Outranking | Classique | Surclassement avec seuils et veto | Critères hétérogènes |
| **PROMETHEE** | Outranking | Classique | Fonctions de préférence + flux | Préférences continues |
| **MOORA/MULTIMOORA** | Ratio | Classique | Trois formes combinées | Industrie, robustesse |
| **BWM** | Pairwise | Classique | Meilleur/Pire critère uniquement | Cohérence maximale |
| **Stratified MCDA** | Hiérarchique | 2024 | Critères en strates | Systèmes complexes |
| **SBWM** | Pairwise/Stratifié | 2024 | BWM par strates | Décisions expertes |
| **Reference-Model MCDA** | Distance | 2024 | Distance à un profil cible | Remplacement d'équipement |
| **AI-Augmented MCDA** | Hybride | 2024 | ML + MCDA | Optimisation automatisée |
| **SLoS** | Agrégation | 2024 | Pénalise les valeurs extrêmes | Santé, risques |

---

# 2. Nouveaux algorithmes MCDA (2024–2026)

## 2.1 Stratified MCDA

🔗 [Recherche](ca://s?q=Explain_Stratified_MCDA)  
**Famille :** Hiérarchique  

### Description
Méthode récente qui structure les critères en **strates hiérarchiques**. Elle permet de gérer des critères hétérogènes (physiques, économiques, qualitatifs) en couches. On regroupe les critères en strates $S_1, S_2, \dots, S_k$, puis on agrège par strate avant d'agréger globalement.

### Équation clé

$$
V = \sum_{i=1}^k W_i \cdot f_i(\text{critères de la strate } S_i)
$$

### ✅ Avantages
- Très adaptée aux systèmes complexes (industrie, énergie, santé)
- Permet des pondérations différentes par strate

---

## 2.2 Stratified Best–Worst Method (SBWM)

🔗
**Famille :** Pairwise / Stratifié  

### Description
Extension stratifiée du [Best–Worst Method(BWM)](https://en.wikipedia.org/wiki/Best_worst_method) . On applique BWM **dans chaque strate**, puis on combine les résultats. Voir §3.11 pour le détail de BWM.

### Équation BWM classique

$$
\min_{\mathbf{w}} \max_j \left| \frac{w_B}{w_j} - a_{Bj} \right|,\quad
\left| \frac{w_j}{w_W} - a_{jW} \right|
$$

SBWM ajoute une couche hiérarchique au-dessus de cette formulation.

---

## 2.3 Reference‑Model MCDA (2024)

**Famille :** Distance  

### Description
Méthode basée sur la **distance à un modèle de référence** défini par l'utilisateur. Contrairement à **TOPSIS** (distance à l'idéal/anti‑idéal), on compare ici à un **profil cible** concret.

### Équation

$$
D_i = \sqrt{\sum_{k} w_k (x_{ik} - r_k)^2}
$$

où $r_k$ = valeur de référence du critère $k$.

### ✅ Avantages
- Très intuitif quand on remplace un produit ou un système existant
- Plus flexible que TOPSIS

---

## 2.4 AI‑Augmented MCDA

**Famille :** Hybride  

### Description
Méthodes hybrides combinant MCDA + IA (ML, modèles tensoriels, modèles probabilistes).

**Exemples :**
- MCDA pour sélectionner un modèle ML
- MCDA + réseaux neuronaux pour pondérer automatiquement les critères
- MCDA + modèles stochastiques pour gérer l'incertitude

### Forme générale

$$
V_i = g_{\theta}(\mathbf{x}_i, \mathbf{w})
$$

où $g_{\theta}$ est un modèle appris.

---

## 2.5 Scale‑Loss Score (SLoS)

**Famille :** Agrégation  

### Description
Nouvelle fonction d'agrégation pénalisant fortement les valeurs extrêmes. Une valeur très faible sur un critère fait chuter fortement le score global.

**Utilisé en :** évaluation bénéfice–risque, santé, industrie pharmaceutique.

### Forme multiplicative

$$
S = \prod_{k} x_k^{w_k}
$$

### Variante logarithmique

$$
\log S = \sum_k w_k \log x_k
$$

---

# 3. Méthodes classiques influentes

## 3.1 [MAUT / MAVT](https://en.wikipedia.org/wiki/Multi-attribute_utility)

**Famille :** Value  

### Description
Fondation théorique de tout MCDA. Chaque critère est transformé en une **fonction d'utilité** $u_k(x)$, puis agrégé par somme pondérée ou produit.

---

## 3.2 [AHP — Analytic Hierarchy Process](https://en.wikipedia.org/wiki/Analytic_hierarchy_process)

**Famille :** Value  

### Description
Méthode la plus enseignée au monde. Décompose le problème en **hiérarchie** (objectif → critères → alternatives), puis effectue des **comparaisons par paires** pour dériver les poids.

---

## 3.3 [ANP — Analytic Network Process](https://en.wikipedia.org/wiki/Analytic_network_process)

**Famille :** Value / Network  

### Description
Extension de l'**AHP** qui permet des **dépendances** et **boucles** entre critères et alternatives.

### Étapes
1. Comparaisons par paires (comme AHP) pour chaque cluster.
2. Construction d'une **super‑matrice** $W$ qui contient toutes les influences.
3. Calcul de la **super‑matrice pondérée**, puis de la **super‑matrice limite** $W^\infty$.
4. Les poids finaux sont extraits de $W^\infty$.

Mathématiquement, on cherche le vecteur propre stationnaire de la super‑matrice.

---

## 3.4 SMART / SMARTER

**Famille :** Value  

### Description
Méthodes simples et très utilisées en industrie. SMARTER ajoute une procédure de pondération par rang (rank-order centroid weights).

---

## 3.5 [TOPSIS](https://en.wikipedia.org/wiki/TOPSIS)

**Famille :** Distance  

### Description
Technique de classement par distance à l'idéal. Une bonne alternative est **proche** de la solution idéale et **loin** de la solution anti‑idéale.

### Étapes

**1. Normalisation**
$$
r_{ik} = \frac{x_{ik}}{\sqrt{\sum_i x_{ik}^2}}
$$

**2. Pondération**
$$
v_{ik} = w_k \, r_{ik}
$$

**3. Idéal et anti‑idéal** (critère à maximiser)
$$
v_k^+ = \max_i v_{ik}, \quad v_k^- = \min_i v_{ik}
$$

**4. Distances**
$$
D_i^+ = \sqrt{\sum_k (v_{ik} - v_k^+)^2}, \quad
D_i^- = \sqrt{\sum_k (v_{ik} - v_k^-)^2}
$$

**5. Score de proximité**
$$
C_i = \frac{D_i^-}{D_i^+ + D_i^-}
$$

Plus $C_i$ est grand, meilleure est l'alternative.

---

## 3.6 [VIKOR](https://en.wikipedia.org/wiki/VIKOR)

**Famille :** Distance / Compromis  

### Description
Cherche une solution de **compromis** entre utilité de groupe (performance globale) et regret individuel (pire critère).

### Meilleur et pire pour chaque critère

$$
f_k^* = \max_i f_{ik}, \quad f_k^- = \min_i f_{ik}
$$

### Mesures $S_i$ (utilité) et $R_i$ (regret)

$$
S_i = \sum_k w_k \frac{f_k^* - f_{ik}}{f_k^* - f_k^-}
$$

$$
R_i = \max_k \left[ w_k \frac{f_k^* - f_{ik}}{f_k^* - f_k^-} \right]
$$

### Indice VIKOR

$$
Q_i = v \cdot \frac{S_i - S^*}{S^- - S^*} + (1-v) \cdot \frac{R_i - R^*}{R^- - R^*}
$$

avec $v \in [0,1]$ (souvent $v = 0.5$). On classe les alternatives par $Q_i$.

---

## 3.7 COPRAS

**Famille :** Distance  

### Description
Méthode proportionnelle simple et efficace. Calcule un rapport entre la somme des critères bénéfices et la somme des critères coûts, de façon directement lisible.

---

## 3.8 [ELECTRE](https://en.wikipedia.org/wiki/ELECTRE)

**Famille :** Outranking  

### Description
Famille de méthodes qui compare les alternatives **par paires** pour décider si l'une **surclasse** l'autre, en utilisant un **indice de concordance**, un **indice de discordance** et des **seuils de veto**.

### Concordance

Pour deux alternatives $a$ et $b$ :

- Ensemble des critères où $a$ est au moins aussi bon que $b$ :
$$
J^+(a,b) = \{ k \mid x_{ak} \ge x_{bk} \}
$$

- Indice de concordance :
$$
C(a,b) = \frac{\sum_{k \in J^+(a,b)} w_k}{\sum_{k} w_k}
$$

### Discordance (version simple)

$$
D(a,b) = \max_{k} \frac{x_{bk} - x_{ak}}{\text{plage}_k}
$$

On dit que $a$ surclasse $b$ si $C(a,b)$ dépasse le seuil de concordance, $D(a,b)$ est sous le seuil de discordance, et aucun veto n'est activé.

---

## 3.9 [PROMETHEE](https://en.wikipedia.org/wiki/Preference_ranking_organization_method_for_enrichment_evaluation)

**Famille :** Outranking  

### Description
Pour chaque critère, on définit une **fonction de préférence** $P_k(a,b)$ qui mesure à quel point $a$ est préféré à $b$. Très utilisé en Europe.

### Préférence unitaire

$$
P_k(a,b) = F_k(x_{ak} - x_{bk})
$$

où $F_k$ est une fonction (usuelle, linéaire, gaussienne, etc.).

### Préférence globale

$$
\pi(a,b) = \sum_k w_k \, P_k(a,b)
$$

### Flux de préférence

$$
\phi^+(a) = \frac{1}{n-1} \sum_{b \ne a} \pi(a,b) \quad \text{(flux sortant)}
$$

$$
\phi^-(a) = \frac{1}{n-1} \sum_{b \ne a} \pi(b,a) \quad \text{(flux entrant)}
$$

$$
\phi(a) = \phi^+(a) - \phi^-(a) \quad \text{(flux net)}
$$

**PROMETHEE II :** trier les alternatives par $\phi(a)$.

---

## 3.10 MOORA / MULTIMOORA

**Famille :** Ratio  

### Description
MULTIMOORA combine **trois formes** pour plus de robustesse.

**Ratio System**
$$
y_i = \sum_{k \in B} w_k \frac{x_{ik}}{x_k^{\max}} - \sum_{k \in C} w_k \frac{x_{ik}}{x_k^{\max}}
$$
où $B$ = critères à maximiser, $C$ = à minimiser.

**Reference Point** — compare chaque alternative au meilleur sur chaque critère.

**Full Multiplicative Form**
$$
U_i = \prod_{k \in B} x_{ik}^{w_k} \Big/ \prod_{k \in C} x_{ik}^{w_k}
$$

MULTIMOORA agrège les classements issus de ces trois formes.

---

## 3.11 [BWM — Best–Worst Method](https://en.wikipedia.org/wiki/Best%E2%80%93worst_method)

**Famille :** Pairwise  

### Description
L'expert choisit un **meilleur** critère (Best) et un **pire** (Worst), compare le Best à tous les autres, puis tous les autres au Worst. Moins de comparaisons qu'AHP, résultat très cohérent.

### Formulation

On cherche les poids $w_k$ qui minimisent l'incohérence :

$$
\min_{\mathbf{w}, \xi} \ \xi
$$

sous contraintes :

$$
\left| \frac{w_B}{w_j} - a_{Bj} \right| \le \xi,\quad
\left| \frac{w_j}{w_W} - a_{jW} \right| \le \xi,\quad
\sum_k w_k = 1,\quad
w_k \ge 0
$$

où :
- $B$ = critère Best, $W$ = critère Worst
- $a_{Bj}$ = préférence du Best sur $j$
- $a_{jW}$ = préférence de $j$ sur le Worst

---

# 4. Tableau comparatif global

| Méthode | Famille | Force principale | Complexité | Gère l'incertitude | Cas d'usage typique |
|---------|---------|-----------------|------------|-------------------|---------------------|
| MAUT/MAVT | Value | Base théorique solide | Élevée | Oui (utilité) | Décision stratégique |
| AHP | Value | Intuitif, universel | Moyenne | Non | Tout domaine |
| ANP | Value | Dépendances entre critères | Élevée | Non | Systèmes interdépendants |
| SMART | Value | Simple et rapide | Faible | Non | Industrie |
| TOPSIS | Distance | Très populaire, robuste | Faible | Non | Classement multi-critères |
| VIKOR | Distance | Compromis optimal | Faible | Non | Décision collective |
| COPRAS | Distance | Proportionnel, transparent | Faible | Non | Évaluation comparative |
| ELECTRE | Outranking | Gère les veto | Élevée | Partielle | Critères hétérogènes |
| PROMETHEE | Outranking | Préférences continues | Moyenne | Non | Europe, ingénierie |
| MOORA | Ratio | Ultra rapide | Faible | Non | Industrie |
| MULTIMOORA | Ratio | Très robuste (3 formes) | Moyenne | Non | Industrie |
| BWM | Pairwise | Cohérence élevée, peu de données | Faible | Non | Pondération experte |
| Stratified MCDA | Hiérarchique | Critères hétérogènes en strates | Moyenne | Non | Systèmes complexes |
| SBWM | Pairwise/Stratifié | BWM hiérarchisé | Moyenne | Non | Décisions expertes |
| Reference-Model MCDA | Distance | Distance à un profil cible | Faible | Non | Remplacement d'équipement |
| AI-Augmented MCDA | Hybride | Automatisation des poids | Élevée | Oui (ML) | Optimisation automatisée |
| SLoS | Agrégation | Pénalise les extrêmes | Faible | Non | Santé, risques |

---

# 5. Application : sélection d'une méthode de correction de données

> Exemple complet d'application MCDA avec intégration d'un **score de plausibilité métier**.

---

## 5.1 🎯 Alternatives (méthodes de correction)

| Méthode | Description |
|--------|-------------|
| M1 | Règles métier + interpolation simple |
| M2 | Modèle statistique (ARIMA / Kalman) |
| M3 | Modèle ML (LSTM / autre réseau) |

---

## 5.2 🎛️ Critères MCDA

| Critère | Objectif | Type |
|--------|----------|------|
| C1 : Plausibilité métier | Respect des règles métier | Maximiser |
| C2 : Cohérence temporelle | Continuité, dérivées réalistes | Maximiser |
| C3 : Qualité de reconstruction | RMSE sur données masquées | Minimiser |
| C4 : Robustesse aux anomalies | Détection correcte, peu de faux positifs | Maximiser |
| C5 : Coût opérationnel | Temps de calcul, complexité | Minimiser |

---

## 5.3 📊 Tableau de décision

| Méthode | C1 Plausibilité (↑) | C2 Cohérence (↑) | C3 RMSE (↓) | C4 Robustesse (↑) | C5 Coût (↓) |
|---------|---------------------|------------------|-------------|-------------------|-------------|
| M1 | 0.85 | 0.70 | 1.2 | 0.60 | 1.0 |
| M2 | 0.90 | 0.80 | 0.9 | 0.75 | 1.5 |
| M3 | 0.95 | 0.85 | 0.7 | 0.80 | 3.0 |

---

## 5.4 🔧 Normalisation des critères

**Critères à maximiser**
$$
x'_{ij} = \frac{x_{ij}}{\max_j x_{ij}}
$$

**Critères à minimiser**
$$
x'_{ij} = \frac{\min_j x_{ij}}{x_{ij}}
$$

**Résultat normalisé**

| Méthode | C1 | C2 | C3 | C4 | C5 |
|---------|----|----|----|----|-----|
| M1 | 0.895 | 0.824 | 0.583 | 0.750 | 0.333 |
| M2 | 0.947 | 0.941 | 0.778 | 0.938 | 0.500 |
| M3 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

---

## 5.5 ⚖️ Pondération des critères

Poids proposés (somme = 1) :

| Critère | Poids | Justification |
|---------|-------|---------------|
| C1 : Plausibilité métier | **0.30** | Critique en contexte industriel |
| C2 : Cohérence temporelle | 0.20 | — |
| C3 : Qualité RMSE | 0.20 | — |
| C4 : Robustesse anomalies | 0.20 | — |
| C5 : Coût opérationnel | 0.10 | — |

---

## 5.6 🧮 Score global (somme pondérée)

$$
\text{Score}_i = \sum_k w_k \cdot x'_{ik}
$$

| Méthode | Calcul | Score |
|---------|--------|-------|
| M1 | 0.30·0.895 + 0.20·0.824 + 0.20·0.583 + 0.20·0.750 + 0.10·0.333 | **0.724** |
| M2 | 0.30·0.947 + 0.20·0.941 + 0.20·0.778 + 0.20·0.938 + 0.10·0.500 | **0.872** |
| M3 | 0.30·1.000 + 0.20·1.000 + 0.20·1.000 + 0.20·1.000 + 0.10·1.000 | **1.000** |

---

## 5.7 🏆 Classement final

| Rang | Méthode | Score |
|------|---------|-------|
| 🥇 1 | M3 — Modèle ML | 1.000 |
| 🥈 2 | M2 — Modèle statistique | 0.872 |
| 🥉 3 | M1 — Règles métier | 0.724 |

---

## 5.8 🎯 Rôle du score de plausibilité métier (C1)

Le critère C1 influence fortement le classement car :

- il capture les règles métier (monotonie, plages physiques, cohérence multi‑capteurs)
- il pénalise les méthodes qui produisent des corrections non crédibles
- il est pondéré à **30 %**, ce qui reflète son importance dans un contexte industriel

> Sans ce critère, une méthode « mathématiquement bonne » mais « métier incohérente » pourrait gagner — ce qui serait dangereux.

---

## 5.9 📌 Résumé de l'application

- Le score de plausibilité métier devient un **critère MCDA clé**.
- Il est intégré dans un tableau de décision avec normalisation + pondération.
- Le MCDA permet de **justifier objectivement** le choix d'une méthode de correction.
- Le modèle ML gagne ici, mais uniquement parce qu'il respecte mieux les règles métier dans cet exemple.

---

*Fin du guide — généré depuis `criteria.md`*

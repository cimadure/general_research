# 🆕 Nouveaux algorithmes MCDA (2024–2026)  
Ce bloc regroupe **toutes les nouveautés MCDA récentes**, avec :  
- explications claires  
- équations utiles  
- liens Wikipédia (quand disponibles)  
- tableau récapitulatif  
- puis la liste des **méthodes MCDA les plus influentes** de la littérature

---

# 1. ⭐ Nouveaux algorithmes MCDA (2024–2026)

## 1.1 **[Stratified MCDA](ca://s?q=Explain_Stratified_MCDA)**  
Méthode récente qui structure les critères en **strates hiérarchiques**.  
Elle permet de gérer des critères hétérogènes (physiques, économiques, qualitatifs) en couches.

### Idée clé  
On regroupe les critères en strates $ S_1, S_2, \dots, S_k $, puis on agrège par strate avant d’agréger globalement.

$$
V = \sum_{i=1}^k W_i \cdot f_i(\text{critères de la strate } S_i)
$$

### Avantages  
- Très adaptée aux systèmes complexes (industrie, énergie, santé).  
- Permet des pondérations différentes par strate.

---

## 1.2 **Stratified Best–Worst Method (SBWM)**  
Extension stratifiée du **Best–Worst Method** (BWM).  
BWM classique : https://en.wikipedia.org/wiki/Best%E2%80%93worst_method

### Idée  
On applique BWM **dans chaque strate**, puis on combine les résultats.

### Équation BWM classique  
$$
\min_{\mathbf{w}} \max_j \left| \frac{w_B}{w_j} - a_{Bj} \right|,\quad
\left| \frac{w_j}{w_W} - a_{jW} \right|
$$

SBWM ajoute une couche hiérarchique.

---

## 1.3 **Reference‑Model MCDA (2024)**  
Méthode basée sur la **distance à un modèle de référence** défini par l’utilisateur.  
Contrairement à **TOPSIS** (distance à l’idéal/anti‑idéal), ici on compare à un **profil cible**.

### Formule  
$$
D_i = \sqrt{\sum_{k} w_k (x_{ik} - r_k)^2}
$$

où $ r_k $ = valeur de référence du critère $k$.

### Avantages  
- Très intuitif quand on remplace un produit ou un système existant.  
- Plus flexible que TOPSIS.

---

## 1.4 **AI‑Augmented MCDA**  
Méthodes hybrides combinant MCDA + IA (ML, modèles tensoriels, modèles probabilistes).

### Exemples  
- MCDA pour sélectionner un modèle ML  
- MCDA + réseaux neuronaux pour pondérer automatiquement les critères  
- MCDA + modèles stochastiques pour gérer l’incertitude

### Forme générale  
$$
V_i = g_{\theta}(\mathbf{x}_i, \mathbf{w})
$$

où $ g_{\theta} $ est un modèle appris.

---

## 1.5 **Scale‑Loss Score (SLoS)**  
Nouvelle fonction d’agrégation pénalisant fortement les valeurs extrêmes.

### Formule simplifiée  
$$
S = \prod_{k} x_k^{w_k}
$$

ou une variante logarithmique :

$$
\log S = \sum_k w_k \log x_k
$$

### Utilisé en  
- évaluation bénéfice–risque  
- santé  
- industrie pharmaceutique

---

# 2. 📊 Tableau récapitulatif des nouveaux algorithmes

| Méthode | Type | Nouveauté | Cas d’usage |
|--------|------|-----------|-------------|
| **[Stratified MCDA](ca://s?q=Explain_Stratified_MCDA)** | Hiérarchique | Critères en strates | Systèmes complexes |
| **SBWM** | Pairwise | BWM stratifié | Décisions expertes |
| **Reference‑Model MCDA** | Distance | Distance à un modèle cible | Remplacement d’équipement |
| **AI‑Augmented MCDA** | Hybride | ML + MCDA | Sélection de modèles, optimisation |
| **SLoS** | Agrégation | Pénalisation des extrêmes | Santé, risques |

---

# 3. 📚 Méthodes MCDA les plus influentes (classiques)

Voici les méthodes qui dominent la littérature depuis 40 ans.  
Liens Wikipédia inclus quand disponibles.

---

## 3.1 **Méthodes Value‑Based / Scoring**

### **MAUT / MAVT**  
https://en.wikipedia.org/wiki/Multi-attribute_utility  
Fondation théorique de tout MCDA.

### **AHP — Analytic Hierarchy Process**  
https://en.wikipedia.org/wiki/Analytic_hierarchy_process  
Méthode la plus enseignée au monde.

### **ANP — Analytic Network Process**  
https://en.wikipedia.org/wiki/Analytic_network_process  
Extension de AHP avec dépendances.

### **SMART / SMARTER**  
Méthodes simples et très utilisées en industrie.

---

## 3.2 **Méthodes Distance‑Based**

### **TOPSIS**  
https://en.wikipedia.org/wiki/TOPSIS  
Technique de classement par distance à l’idéal.

$$
C_i = \frac{D_i^-}{D_i^+ + D_i^-}
$$

### **VIKOR**  
https://en.wikipedia.org/wiki/VIKOR  
Recherche d’un compromis entre utilité et regret.

### **COPRAS**  
Méthode proportionnelle simple et efficace.

---

## 3.3 **Méthodes Outranking**

### **ELECTRE**  
https://en.wikipedia.org/wiki/ELECTRE  
Famille de méthodes avec seuils, veto, surclassement.

### **PROMETHEE**  
https://en.wikipedia.org/wiki/Preference_ranking_organization_method_for_enrichment_evaluation  
Préférences continues, très utilisé en Europe.

---

## 3.4 **Méthodes Ratio‑Based**

### **MOORA / MULTIMOORA**  
Méthodes rapides et robustes pour l’industrie.

---

## 3.5 **Méthodes Pairwise Optimization**

### **BWM — Best–Worst Method**  
https://en.wikipedia.org/wiki/Best%E2%80%93worst_method  
Moins de comparaisons qu’AHP, très cohérent.

---

# 4. 🧠 Tableau récapitulatif des méthodes influentes

| Méthode | Famille | Pourquoi elle est influente |
|--------|---------|-----------------------------|
| **MAUT/MAVT** | Value | Base théorique du MCDA |
| **AHP** | Value | Intuitif, universel |
| **ANP** | Value | Gère les dépendances |
| **SMART** | Value | Simple et industriel |
| **TOPSIS** | Distance | Très populaire, robuste |
| **VIKOR** | Distance | Compromis optimal |
| **COPRAS** | Distance | Proportionnel, transparent |
| **ELECTRE** | Outranking | Gère les veto |
| **PROMETHEE** | Outranking | Préférences continues |
| **MOORA** | Ratio | Ultra rapide |
| **MULTIMOORA** | Ratio | Très robuste |
| **BWM** | Pairwise | Cohérence élevée |

---

# 5. 🎯 Résumé final

- Les **nouveaux algorithmes MCDA** (2024–2026) apportent :  
  - hiérarchisation (Stratified MCDA)  
  - distance à un modèle cible (Reference‑Model MCDA)  
  - hybridation IA (AI‑Augmented MCDA)  
  - nouvelles fonctions d’agrégation (SLoS)

- Les **méthodes influentes** restent :  
  **AHP, TOPSIS, ELECTRE, PROMETHEE, MAUT, VIKOR, BWM, MOORA**.

---


🧱 Tableau MCDA complet + intégration du score de plausibilité métier
Ce bloc contient tout :  
- définition des alternatives  
- critères MCDA  
- tableau de décision  
- normalisation  
- pondération  
- calcul final  
- rôle du score de plausibilité métier  

---

1. 🎯 Alternatives (méthodes de correction)

| Méthode | Description |
|--------|-------------|
| M1 | Règles métier + interpolation simple |
| M2 | Modèle statistique (ARIMA / Kalman) |
| M3 | Modèle ML (LSTM / autre réseau) |

---

2. 🎛️ Critères MCDA (dont le score de plausibilité métier)

| Critère | Objectif | Type |
|--------|----------|------|
| C1 : Plausibilité métier | Respect des règles métier | Maximiser |
| C2 : Cohérence temporelle | Continuité, dérivées réalistes | Maximiser |
| C3 : Qualité de reconstruction | RMSE sur données masquées | Minimiser |
| C4 : Robustesse aux anomalies | Détection correcte, peu de faux positifs | Maximiser |
| C5 : Coût opérationnel | Temps de calcul, complexité | Minimiser |

---

3. 📊 Tableau de décision (valeurs fictives mais réalistes)

| Méthode | C1 Plausibilité (↑) | C2 Cohérence (↑) | C3 RMSE (↓) | C4 Robustesse (↑) | C5 Coût (↓) |
|---------|---------------------|------------------|-------------|-------------------|-------------|
| M1  | 0.85                | 0.70             | 1.2         | 0.60              | 1.0         |
| M2  | 0.90                | 0.80             | 0.9         | 0.75              | 1.5         |
| M3  | 0.95                | 0.85             | 0.7         | 0.80              | 3.0         |

---

4. 🔧 Normalisation des critères

Critères à maximiser
$$
x'{ij} = \frac{x{ij}}{\maxj x{ij}}
$$

Critères à minimiser
$$
x'{ij} = \frac{\minj x{ij}}{x{ij}}
$$

Résultat normalisé

| Méthode | C1 | C2 | C3 | C4 | C5 |
|---------|----|----|----|----|----|
| M1  | 0.85/0.95 = 0.895 | 0.70/0.85 = 0.824 | 0.7/1.2 = 0.583 | 0.60/0.80 = 0.750 | 1.0/3.0 = 0.333 |
| M2  | 0.90/0.95 = 0.947 | 0.80/0.85 = 0.941 | 0.7/0.9 = 0.778 | 0.75/0.80 = 0.938 | 1.5/3.0 = 0.500 |
| M3  | 0.95/0.95 = 1.000 | 0.85/0.85 = 1.000 | 0.7/0.7 = 1.000 | 0.80/0.80 = 1.000 | 3.0/3.0 = 1.000 |

---

5. ⚖️ Pondération des critères

Poids proposés (somme = 1) :

- w1 = 0.30 (plausibilité métier = très important)  
- w2 = 0.20  
- w3 = 0.20  
- w4 = 0.20  
- w5 = 0.10  

---

6. 🧮 Calcul du score global (somme pondérée)

$$
\text{Score}i = \sumk wk \cdot x'{ik}
$$

Résultats

| Méthode | Score |
|---------|--------|
| M1 | 0.30·0.895 + 0.20·0.824 + 0.20·0.583 + 0.20·0.750 + 0.10·0.333 = 0.724 |
| M2 | 0.30·0.947 + 0.20·0.941 + 0.20·0.778 + 0.20·0.938 + 0.10·0.500 = 0.872 |
| M3 | 0.30·1.000 + 0.20·1.000 + 0.20·1.000 + 0.20·1.000 + 0.10·1.000 = 1.000 |

---

7. 🏆 Classement final

1. M3 — Modèle ML (score = 1.000)  
2. M2 — Modèle statistique (score = 0.872)  
3. M1 — Règles métier + interpolation (score = 0.724)

---

8. 🎯 Rôle du score de plausibilité métier (C1)

Le critère C1 influence fortement le classement car :

- il capture les règles métier (monotonie, plages physiques, cohérence multi‑capteurs)  
- il pénalise les méthodes qui produisent des corrections non crédibles  
- il est pondéré à 30 %, ce qui reflète son importance dans un contexte industriel

Sans ce critère, une méthode “mathématiquement bonne” mais “métier incohérente” pourrait gagner — ce qui serait dangereux.

---

9. 📌 Résumé

- Le score de plausibilité métier devient un critère MCDA clé.  
- Il est intégré dans un tableau de décision avec normalisation + pondération.  
- Le MCDA permet de justifier objectivement le choix d’une méthode de correction.  
- Le modèle ML gagne ici, mais uniquement parce qu’il respecte mieux les règles métier dans cet exemple.

---

____

📚 Monobloc MCDA — ELECTRE, PROMETHEE, TOPSIS, VIKOR, ANP, MULTIMOORA, SLoS, SBWM

Ce bloc regroupe, pour chaque méthode :
- définition courte  
- idée clé  
- équations essentielles  
- lien Wikipédia (quand disponible)

---

## 1. ELECTRE (outranking)

**Lien :** https://en.wikipedia.org/wiki/ELECTRE  

**Idée générale :**  
Comparer les alternatives **par paires** et décider si l’une **surclasse** l’autre, en utilisant :
- un **indice de concordance** (où l’alternative est meilleure ou égale)  
- un **indice de discordance** (où elle est nettement pire)  
- des **seuils** et éventuellement des **veto**

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

On dit que $a$ surclasse $b$ si :
- $C(a,b)$ est **au‑dessus** d’un seuil de concordance  
- $D(a,b)$ est **en‑dessous** d’un seuil de discordance  
- et pas de veto activé

---

## 2. PROMETHEE (outranking avec fonctions de préférence)

**Lien :** https://en.wikipedia.org/wiki/Preference_ranking_organization_method_for_enrichment_evaluation  

**Idée générale :**  
Pour chaque critère, on définit une **fonction de préférence** $P_k(a,b)$ qui mesure à quel point $a$ est préféré à $b$ sur ce critère.

### Préférence unitaire

$$
P_k(a,b) = F_k(x_{ak} - x_{bk})
$$

où $F_k$ est une fonction (usuelle, linéaire, gaussienne, etc.).

### Préférence globale

$$
\pi(a,b) = \sum_k w_k \, P_k(a,b)
$$

### Flots de préférence

- **Flux sortant :**  
  $$
  \phi^+(a) = \frac{1}{n-1} \sum_{b \ne a} \pi(a,b)
  $$

- **Flux entrant :**  
  $$
  \phi^-(a) = \frac{1}{n-1} \sum_{b \ne a} \pi(b,a)
  $$

- **Flux net :**  
  $$
  \phi(a) = \phi^+(a) - \phi^-(a)
  $$

Classement PROMETHEE II : trier les alternatives par $\phi(a)$.

---

## 3. TOPSIS (distance à l’idéal)

**Lien :** https://en.wikipedia.org/wiki/TOPSIS  

**Idée générale :**  
Une bonne alternative est :
- **proche** de la solution idéale  
- **loin** de la solution anti‑idéale

### Étapes principales

1. **Normalisation**  
   $$
   r_{ik} = \frac{x_{ik}}{\sqrt{\sum_i x_{ik}^2}}
   $$

2. **Pondération**  
   $$
   v_{ik} = w_k \, r_{ik}
   $$

3. **Idéal et anti‑idéal**

   - Critère à maximiser :  
     $$
     v_k^+ = \max_i v_{ik}, \quad v_k^- = \min_i v_{ik}
     $$

4. **Distances**

   $$
   D_i^+ = \sqrt{\sum_k (v_{ik} - v_k^+)^2}, \quad
   D_i^- = \sqrt{\sum_k (v_{ik} - v_k^-)^2}
   $$

5. **Score de proximité**

   $$
   C_i = \frac{D_i^-}{D_i^+ + D_i^-}
   $$

Plus $C_i$ est grand, meilleure est l’alternative.

---

## 4. VIKOR (compromis)

**Lien :** https://en.wikipedia.org/wiki/VIKOR  

**Idée générale :**  
Chercher une solution de **compromis** entre :
- **utilité de groupe** (performance globale)  
- **regret individuel** (pire critère)

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

avec $v \in [0,1]$ (souvent $v = 0.5$).

On classe les alternatives par $Q_i$.

---

## 5. ANP (Analytic Network Process)

**Lien :** https://en.wikipedia.org/wiki/Analytic_network_process  

**Idée générale :**  
Extension de l’**AHP** qui permet des **dépendances** et **boucles** entre critères et alternatives.

### Étapes

1. Comparaisons par paires (comme AHP) pour chaque cluster (critères, alternatives, etc.).  
2. Construction d’une **super‑matrice** $W$ qui contient toutes les influences.  
3. Calcul de la **super‑matrice pondérée**, puis de la **super‑matrice limite** $W^\infty$.  
4. Les poids finaux sont extraits de $W^\infty$.

Mathématiquement, on cherche le vecteur propre stationnaire de la super‑matrice.

---

## 6. MULTIMOORA (extension de MOORA)

**MOORA / MULTIMOORA** n’ont pas de page Wikipédia dédiée, mais MOORA est souvent décrit dans la littérature.

**Idée générale :**  
MULTIMOORA combine **trois formes** :

1. **Ratio System**  
   $$
   y_i = \sum_{k \in B} w_k \frac{x_{ik}}{x_k^{\max}} - \sum_{k \in C} w_k \frac{x_{ik}}{x_k^{\max}}
   $$
   où $B$ = critères à maximiser, $C$ = à minimiser.

2. **Reference Point**  
   On compare chaque alternative à un point de référence (meilleures performances).

3. **Full Multiplicative Form**  
   $$
   U_i = \prod_{k \in B} x_{ik}^{w_k} \Big/ \prod_{k \in C} x_{ik}^{w_k}
   $$

MULTIMOORA agrège les classements issus de ces trois formes pour plus de robustesse.

---

## 7. SLoS (Scale‑Loss Score)

**Idée générale :**  
Fonction d’agrégation qui **pénalise fortement les valeurs extrêmes** et favorise un profil équilibré.

### Forme multiplicative

Pour des critères normalisés $x_k \in (0,1]$ :

$$
S = \prod_k x_k^{w_k}
$$

ou en log :

$$
\log S = \sum_k w_k \log x_k
$$

Une valeur très faible sur un critère fait chuter fortement le score global → utile en **bénéfice–risque**, sécurité, santé.

---

## 8. SBWM (Stratified Best–Worst Method)

**BWM classique (Best–Worst Method) :**  
https://en.wikipedia.org/wiki/Best%E2%80%93worst_method  

**Idée générale :**  
- L’expert choisit un **meilleur** critère (Best) et un **pire** (Worst).  
- Il compare le Best à tous les autres, puis tous les autres au Worst.  
- On résout un problème d’optimisation pour obtenir les poids.

### Formulation BWM

On cherche les poids $w_k$ qui minimisent l’incohérence :

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
- $B$ = critère Best  
- $W$ = critère Worst  
- $a_{Bj}$ = préférence du Best sur $j$  
- $a_{jW}$ = préférence de $j$ sur le Worst  

**SBWM (Stratified BWM)** :  
On applique BWM **par strate de critères** (groupes hiérarchiques), puis on agrège les poids des strates et des critères internes.

---

## 9. Résumé rapide

| Méthode | Famille | Idée clé |
|--------|---------|----------|
| ELECTRE | Outranking | Concordance + discordance + veto |
| PROMETHEE | Outranking | Fonctions de préférence + flots |
| TOPSIS | Distance | Proche de l’idéal, loin de l’anti‑idéal |
| VIKOR | Distance/Compromis | Compromis utilité–regret |
| ANP | Hiérarchique/Network | Dépendances entre critères |
| MULTIMOORA | Ratio/Hybrid | Trois formes combinées |
| SLoS | Agrégation | Pénalise les extrêmes |
| SBWM | Pairwise/Stratified | BWM hiérarchisé |

---


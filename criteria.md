`markdown

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
\[
x'{ij} = \frac{x{ij}}{\maxj x{ij}}
\]

Critères à minimiser
\[
x'{ij} = \frac{\minj x{ij}}{x{ij}}
\]

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

\[
\text{Score}i = \sumk wk \cdot x'{ik}
\]

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


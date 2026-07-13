# Exercice 2 — Cartographier des composants

**Module associé :** [Module 4 — Méthode de construction](../04-methode-construction.md)  
**Durée estimée :** 30 minutes  
**Niveau :** Intermédiaire

## Partie A — Exemple guidé : application de gestion de stock

Appliquez la méthode en 7 étapes sur l'application **StockPro**, une solution de gestion de stock pour des commerces de détail.

### Contexte

- **Utilisateur :** Gérant d'un magasin de détail (50-500 références)
- **Besoins :**
  1. Suivre les niveaux de stock en temps réel
  2. Être alerté quand un produit est en rupture
  3. Analyser les ventes pour anticiper les commandes
- **Équipe :** 3 développeurs, lancement dans 4 mois
- **Budget infra :** 300€/mois max

### Votre mission

Suivez les 7 étapes de la méthode et complétez les tableaux ci-dessous.

#### Étape 1-2 — Utilisateur et besoins

Déjà fournis ci-dessus. Validez-les ou proposez des améliorations.

#### Étape 3 — Lister les composants

Listez au moins **12 composants** nécessaires pour satisfaire les 3 besoins.

| # | Composant | Besoin(s) associé(s) |
|---|-----------|----------------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |
| 10 | | |
| 11 | | |
| 12 | | |

#### Étape 4-5 — Positionner sur la map

| # | Composant | Vertical (H/M/B) | Horizontal (G/C/P/Co) |
|---|-----------|-------------------|------------------------|
| 1 | | | |
| 2 | | | |
| ... | | | |

#### Étape 6 — Dépendances

Dessinez le diagramme de dépendances (Mermaid ou schéma) pour au moins 8 composants.

#### Étape 7 — Mouvement

| Composant | Mouvement prévu ? | Vers quel stade ? | Délai estimé |
|-----------|-------------------|-------------------|--------------|
| | | | |

### Questions de réflexion

1. Quel composant est le **différenciateur** de StockPro ?
2. Quels composants sont en zone **Buy automatique** (bas-droite) ?
3. Y a-t-il un composant dont le mouvement rapide devrait influencer votre stratégie ?

---

## Partie B — Votre application

Appliquez la même méthode sur **votre** application en utilisant la [fiche application](../templates/fiche-application.md) remplie.

### Instructions de personnalisation

1. **Remplissez** la [fiche application](../templates/fiche-application.md) si ce n'est pas déjà fait
2. **Copiez** le [template Wardley Map vierge](../templates/wardley-map-vierge.md)
3. **Suivez les 7 étapes** du [Module 4](../04-methode-construction.md)
4. **Comparez** votre map avec le corrigé de StockPro (Partie A) — les structures seront différentes, mais la méthode est la même

### Grille d'auto-évaluation

| Critère | Oui / Non |
|---------|-----------|
| J'ai un utilisateur principal clairement identifié | |
| Mes besoins sont en langage métier (pas technique) | |
| J'ai 10-20 composants (pas des technos) | |
| Chaque composant est positionné sur les 2 axes | |
| Les dépendances vont du haut vers le bas | |
| J'ai identifié au moins 2 composants en mouvement | |
| J'ai identifié le différenciateur (haut-gauche) | |
| J'ai identifié les commodités (bas-droite) | |

### Livrable Partie B

- Fiche application remplie
- Wardley Map complétée (template ou dessin)
- Réponses à la grille d'auto-évaluation

---

## Correction

→ [Corrigé de l'exercice 2 — StockPro](corriges/ex02-corrige.md)  
→ [Guide de personnalisation pour votre application](corriges/ex02-corrige.md#partie-b--guide-de-personnalisation)

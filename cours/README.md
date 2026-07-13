# Cours Wardley Maps — Choix technologiques et ressources externes

Ce cours vous apprend à utiliser les **Wardley Maps** pour cartographier une application informatique et prendre des décisions éclairées : construire en interne, acheter un SaaS, ou externaliser.

## Public visé

Chefs de projet, architectes, tech leads et fondateurs techniques.

## Prérequis

- Notions de base d'une application web ou mobile (frontend, API, base de données, authentification, hébergement)
- Aucune connaissance préalable des Wardley Maps requise

## Durée estimée

**4 à 6 heures** (théorie + atelier pratique)

## Parcours recommandé

| Étape | Module | Durée | Exercice |
|-------|--------|-------|----------|
| 1 | [Introduction](01-introduction.md) | 30 min | — |
| 2 | [Concepts fondamentaux](02-concepts-fondamentaux.md) | 45 min | — |
| 3 | [Lire une Wardley Map](03-lecture-d-une-map.md) | 45 min | [Exercice 1](exercices/ex01-lire-une-map.md) |
| 4 | [Méthode de construction](04-methode-construction.md) | 60 min | [Exercice 2](exercices/ex02-cartographier-composants.md) |
| 5 | [Décisions technologiques](05-decisions-technologiques.md) | 60 min | [Exercice 3](exercices/ex03-build-buy-outsource.md) |
| 6 | [Atelier : votre application](06-atelier-votre-application.md) | 90 min | Fiche application |
| 7 | [Cas pratiques](07-cas-pratiques.md) | 45 min | — |

## Structure du dossier

```
cours/
├── README.md                         ← Vous êtes ici
├── 01-introduction.md
├── 02-concepts-fondamentaux.md
├── 03-lecture-d-une-map.md
├── 04-methode-construction.md
├── 05-decisions-technologiques.md
├── 06-atelier-votre-application.md
├── 07-cas-pratiques.md
├── exercices/
│   ├── ex01-lire-une-map.md
│   ├── ex02-cartographier-composants.md
│   ├── ex03-build-buy-outsource.md
│   └── corriges/
├── templates/
│   ├── fiche-application.md
│   ├── grille-decision.md
│   └── wardley-map-vierge.md
└── annexes/
    ├── glossaire.md
    ├── erreurs-frequentes.md
    └── ressources.md
```

## Livrables attendus

À la fin du cours, vous aurez produit :

1. Une **Wardley Map** de votre application (composants, dépendances, évolution)
2. Un **tableau de décisions** build / buy / outsource pour chaque composant stratégique
3. Un **plan d'action** avec 3 décisions prioritaires justifiées

## Avant l'atelier (module 6)

Remplissez la [fiche application](templates/fiche-application.md) avec la description de votre projet. C'est le prérequis indispensable pour l'atelier pratique.

## Annexes

- [Glossaire](annexes/glossaire.md)
- [Erreurs fréquentes](annexes/erreurs-frequentes.md)
- [Ressources complémentaires](annexes/ressources.md)

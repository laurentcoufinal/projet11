# Analyse des dépendances du système d'information

Ce document étudie les interactions entre les composants du SI du Groupe Retail Sphère : échanges de données, dépendances fonctionnelles et techniques, couplages structurants et leurs impacts.

## Diagrammes de référence

- [Architecture composants](diagrammes/architecture-composants.drawio) — vue globale du SI en 3 couches
- [Flux de dépendances](diagrammes/flux-dependances.drawio) — 4 parcours principaux numérotés par priorité

![Architecture composants](diagrammes/architecture-composants.png)

![Flux de dépendances](diagrammes/flux-dependances.png)

---

## Tableau des dépendances structurantes

| Source | Cible | Type | Nature | Impact |
|--------|-------|------|--------|--------|
| Front-end e-commerce | Service Catalogue | Fonctionnelle | Appel REST synchrone | Dépendance directe pour l'affichage catalogue ; lenteur catalogue impacte l'expérience client |
| Front-end e-commerce | Service Commandes | Fonctionnelle | Appel REST synchrone | Parcours commande bloquant si le service est lent en pic de charge |
| Back-office interne | Service Catalogue | Fonctionnelle | Appel REST synchrone | Gestion produits dépendante de la disponibilité du service |
| Back-office interne | Service Commandes | Fonctionnelle | Appel REST synchrone | Suivi et gestion des commandes centralisés via un seul service |
| Back-office interne | Service Stock | Fonctionnelle | Appel REST synchrone | Gestion des stocks opérationnelle dépendante du service PHP |
| Service Catalogue | Base de données principale | Technique | Lecture/écriture BDD partagée | Couplage fort à la BDD centrale ; évolutions schéma impactent le service |
| Service Commandes | Base de données principale | Technique | Lecture/écriture BDD partagée | Point central du parcours commande ; pic de charge sur BDD et service |
| Service Commandes | Service Stock | Fonctionnelle + technique | Appel REST synchrone | Synchronisation stock/commandes ; source d'écarts de données documentés |
| Service Commandes | API externe de paiement | Fonctionnelle + technique | Appel vers service tiers | Transaction bloquante ; dépendance externe pour chaque paiement |
| Service Stock | Base de données principale | Technique | Lecture/écriture BDD partagée | Même BDD que Commandes ; risque d'incohérence stock/commandes |
| Service Stock | Service Commandes | Fonctionnelle + technique | Appel REST synchrone (bidirectionnel) | Couplage fort entre les deux services critiques du SI |
| Base de données principale | Outil de reporting | Technique | Lecture batch (ETL) | Données non temps réel ; reporting décalé par rapport à l'opérationnel |

---

## Composants fortement couplés

### 1. Ensemble des services ↔ Base de données centrale

Tous les services métier (Catalogue, Commandes, Stock) partagent une base PostgreSQL unique. Ce choix architectural concentre les lectures et écritures sur un point unique, ce qui :

- crée un goulet d'étranglement en période de pic (performances commandes et catalogue) ;
- rend toute évolution de schéma transversale à plusieurs services ;
- empêche un découpage clair des responsabilités de persistance.

### 2. Service Commandes ↔ Service Stock

Ces deux services interagissent de manière synchrone pour synchroniser les niveaux de stock avec les commandes. Ce couplage fonctionnel direct est à l'origine :

- des écarts constatés entre données de stock et commandes ;
- d'une synchronisation parfois complexe entre services ;
- d'une dépendance mutuelle qui complique les évolutions indépendantes de chaque service.

### 3. Multi-services avec règles métier dupliquées

Certaines règles métier sont dupliquées dans plusieurs services (constat rapport métier). Ce couplage logique, bien que non visible dans le schéma d'architecture, a pour conséquence :

- des modifications coordonnées sur plusieurs composants pour une seule évolution ;
- un risque d'incohérence entre les implémentations ;
- une dégradation de la maintenabilité globale du SI.

---

## Analyse par flux principal

### Flux 1 — Parcours client (priorité haute)

Le parcours client enchaîne Front-end → Catalogue/Commandes → API Paiement → BDD. C'est le flux le plus critique car il impacte directement les clients finaux et le chiffre d'affaires. Les appels synchrones en cascade amplifient les latences en pic de charge : une lenteur sur Commandes ou la BDD bloque l'ensemble du parcours d'achat.

### Flux 2 — Gestion des stocks (priorité haute)

Le flux Commandes → Stock → BDD est le second flux structurant. Il conditionne la cohérence entre les commandes passées et les niveaux de stock disponibles. Les écarts documentés entre ces deux domaines de données trouvent leur origine dans ce couplage synchrone entre services hétérogènes (Node.js et PHP).

### Flux 3 — Back-office

Le back-office centralise l'accès aux trois services métier. Toute indisponibilité d'un service impacte une fonction de gestion interne. Ce point d'entrée unique multiplie les dépendances fonctionnelles côté équipes opérationnelles.

### Flux 4 — Reporting (batch)

Le reporting lit la BDD en mode batch via des scripts ETL Python. Ce découplage partiel (lecture seule, asynchrone) limite l'impact sur l'opérationnel mais explique l'absence de données en temps réel pour le pilotage métier.

---

## Conséquences des dépendances

| Dépendance | Impact sur la performance | Impact sur la maintenabilité | Impact sur la cohérence |
|------------|--------------------------|------------------------------|------------------------|
| BDD centrale partagée | Goulet d'étranglement en pic de charge | Évolutions multi-composants | Risque d'écritures concurrentes incohérentes |
| Commandes ↔ Stock synchrone | Latence cumulée sur le parcours commande | Deux stacks (Node.js/PHP) à maintenir | Écarts stock/commandes documentés |
| Règles métier dupliquées | — | Modifications sur plusieurs services | Incohérences entre implémentations |
| Reporting batch | Données non temps réel | Stack Python supplémentaire | Décalage entre opérationnel et pilotage |
| API paiement externe | Dépendance réseau sur chaque transaction | Intégration à maintenir avec le tiers | — |

---

## Synthèse

Les dépendances les plus structurantes du SI sont la centralisation des données dans une BDD unique et le couplage synchrone entre les services Commandes et Stock. Ces deux facteurs expliquent la majorité des limites documentées en performance, cohérence des données et maintenabilité. La réduction de ces dépendances constitue un axe prioritaire d'évolution, conformément aux attentes du Groupe Retail Sphère.

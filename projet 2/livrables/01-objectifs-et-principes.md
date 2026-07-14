# Objectifs et principes d'architecture — Groupe Retail Sphère

Document de cadrage de l'architecture cible, issu de l'audit du SI existant ([`projet/livrables/rapport-audit-si.md`](../../projet/livrables/rapport-audit-si.md)).

---

## Méthode — Synergetic Blueprint

Le **Synergetic Blueprint** est un processus structuré d'application du **Domain-Driven Design (DDD)**, de l'intention métier jusqu'à une architecture et un plan d'intégration traçables. Il organise les techniques DDD (capabilities, Domain Storytelling, EventStorming, Context Map, modèle de domaine, Example Mapping…) en un fil conducteur cohérent, publié par Michael Junker (*Mastering Domain-Driven Design*, 2025) et étendu dans *DDD Toolbox* (2026).

### Les 4 zones et 12 étapes

| Zone | Étapes | Techniques / outputs |
|------|--------|----------------------|
| **Design stratégique — Idéation** | 1 à 3 | North Star, Business Model Canvas, capability map, premières frontières de domaine |
| **Design stratégique — Exigences** | 4 à 7 | Domain Storytelling, Visual Glossary, EventStorming, Event Modeling, user stories |
| **Design stratégique — Solution Design** | 8 | Context Map, patterns d'intégration, spécification architecturale |
| **Design tactique** | 9 à 12 | Modèle de domaine, contrats API/événements, Example Mapping, implémentation et documentation |

Les numéros d'étapes indiquent un **ordre de lecture**, pas une exécution séquentielle rigide. Les découvertes en aval (par exemple un EventStorming) peuvent remettre en cause les artefacts amont (par exemple la capability map).

### Application au projet Groupe Retail Sphère

| Phase projet | Étapes Blueprint | Livrable(s) |
|---|---|---|
| Phase 0 — Cadrage | Amont (pré-Blueprint) | [`01-objectifs-et-principes.md`](01-objectifs-et-principes.md) |
| Phase 1 — Idéation | 1-3 | [`02-ideation-capabilities.md`](02-ideation-capabilities.md) |
| Phase 2 — Exigences | 4-7 | [`03-glossaire-domaine.md`](03-glossaire-domaine.md), [`04-user-stories.md`](04-user-stories.md), [`05-event-storming.md`](05-event-storming.md) |
| Phase 3 — Solution Design | 8 | [`06-context-map.drawio`](06-context-map.drawio) |
| Phases 4-5 — Architecture | Complément besoin2 | [`07`](07-architecture-applicative.drawio) à [`10`](10-architecture-deploiement.drawio) |
| Phase 6 — Design tactique | 9-11 | [`11-modele-domaine.md`](11-modele-domaine.md), [`12-contrats-api.md`](12-contrats-api.md) |
| Phase 7 — Intégration | 12 | [`13-plan-integration.md`](13-plan-integration.md), [`document-architecture-cible.md`](document-architecture-cible.md) |

Le détail opérationnel des phases est décrit dans [`roadmap.md`](roadmap.md).

```mermaid
flowchart LR
    cadrage["Phase0 Cadrage"]
    ideation["Etapes1-3 Ideation"]
    exigences["Etapes4-7 Exigences"]
    solution["Etape8 ContextMap"]
    archi["Architecture cible"]
    tactique["Etapes9-11 Design tactique"]
    integration["Etape12 Integration"]

    cadrage --> ideation --> exigences --> solution --> archi --> tactique --> integration
```

Les **objectifs (O1-O5)** et **principes d'architecture** définis ci-dessous servent de fondation aux étapes Blueprint suivantes — en particulier le principe 4 (langage ubiquitaire), qui prépare directement l'étape 5 (Visual Glossary).

---

## Problèmes principaux identifiés

| # | Problème | Source audit |
|---|----------|--------------|
| P1 | Écarts entre les données de stock et les commandes | Cohérence des données |
| P2 | Dégradation des performances en pic de charge sur le parcours commande | Performance |
| P3 | Hétérogénéité technologique (Java, Node.js, PHP, Python) | Maintenabilité |
| P4 | Forte dépendance à une base de données unique partagée | Architecture |
| P5 | Reporting non temps réel, décalé par rapport à l'opérationnel | Performance / pilotage |

### Reformulation synthétique

Le SI actuel remplit ses fonctions métier mais souffre de couplages structurels : une base de données centralisée, des communications synchrones entre services critiques, et une diversité technologique qui complexifie chaque évolution. Ces facteurs limitent la cohérence des données, la performance en croissance et la capacité à faire évoluer le système de manière maîtrisée.

---

## Objectifs de l'architecture cible

Chaque objectif est directement relié à un problème identifié.

| Objectif | Problème adressé | Formulation |
|----------|------------------|-------------|
| **O1 — Cohérence inter-domaines** | P1 | Garantir l'alignement fiable entre les données de commandes et de stock |
| **O2 — Résilience en charge** | P2 | Absorber la croissance des volumes sans dégradation du parcours client |
| **O3 — Simplicité de maintenance** | P3 | Réduire la complexité liée à la multiplicité des technologies |
| **O4 — Responsabilités clarifiées** | P4 | Délimiter clairement les périmètres de responsabilité de chaque domaine |
| **O5 — Pilotage actualisé** | P5 | Permettre aux équipes métiers de disposer d'indicateurs fiables et récents |

---

## Principes d'architecture structurants

Ces principes guident la conception sans prescrire de solutions techniques à ce stade.

### Principe 1 — Séparation des responsabilités par domaine métier

Chaque domaine fonctionnel (catalogue, commandes, stock, reporting) possède un périmètre de responsabilité clairement délimité. Aucun composant ne doit porter des règles métier appartenant à un autre domaine.

*Relié à : O4, P4*

### Principe 2 — Découplage temporel des flux critiques

Les interactions entre domaines à fort enjeu (notamment commandes et stock) ne doivent pas créer de chaînes de dépendances bloquantes. Le traitement peut être différé lorsque la cohérence métier le permet.

*Relié à : O2, P2*

### Principe 3 — Évolutivité progressive

L'architecture cible se met en place par étapes, sans interruption du service existant et sans refonte globale immédiate. Chaque évolution doit pouvoir être validée indépendamment avant de passer à la suivante.

*Relié à : O3, contraintes métier du rapport d'audit*

### Principe 4 — Langage ubiquitaire partagé

Les termes métier (Produit, Commande, Stock, Réservation, Paiement) sont définis une seule fois et utilisés de manière cohérente par les équipes métier et IT, de la spécification à l'implémentation.

*Relié à : O1, toutes les phases de conception DDD*

---

## Contraintes à respecter

| Contrainte | Origine |
|------------|---------|
| Le système existant reste opérationnel pendant les évolutions | Rapport métier |
| Pas de refonte complète immédiate | Rapport métier |
| Appropriation progressive par les équipes | Rapport métier |
| Cohérence avec les solutions identifiées lors de l'audit | Benchmark technologique |

---

## Traçabilité problèmes → objectifs → principes

| Problème | Objectif | Principe(s) |
|----------|----------|-------------|
| P1 Écarts stock/commandes | O1 Cohérence | P1, P4 |
| P2 Pics de charge | O2 Résilience | P2 |
| P3 Hétérogénéité techno | O3 Maintenance | P3 |
| P4 BDD unique | O4 Responsabilités | P1, P3 |
| P5 Reporting décalé | O5 Pilotage | P1, P3 |

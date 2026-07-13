# Document d'architecture cible — Groupe Retail Sphère

**Date** : juillet 2026  
**Contexte** : suite à l'audit du SI existant ([`projet/livrables/rapport-audit-si.md`](../../projet/livrables/rapport-audit-si.md))  
**Méthode** : Synergetic Blueprint (DDD) — 12 étapes en 4 zones  
**Contraintes** : migration progressive, SI opérationnel pendant les évolutions, pas de refonte big-bang

---

## Table des matières

1. [Contexte et objectifs](#1-contexte-et-objectifs)
2. [Principes d'architecture](#2-principes-darchitecture)
3. [Capabilities et idéation](#3-capabilities-et-idéation)
4. [User stories et critères d'acceptation](#4-user-stories-et-critères-dacceptation)
5. [Glossaire et événements domaine](#5-glossaire-et-événements-domaine)
6. [Context Map](#6-context-map)
7. [Architecture applicative](#7-architecture-applicative)
8. [Justification d'architecture](#8-justification-darchitecture)
9. [Choix technologiques](#9-choix-technologiques)
10. [Architecture de déploiement](#10-architecture-de-déploiement)
11. [Modèle de domaine et contrats API](#11-modèle-de-domaine-et-contrats-api)
12. [Plan d'intégration](#12-plan-dintégration)
13. [Synthèse et traçabilité](#13-synthèse-et-traçabilité)

---

## 1. Contexte et objectifs

Le Groupe Retail Sphère souhaite moderniser son SI pour améliorer la cohérence, la maintenabilité et l'évolutivité, tout en maintenant la plateforme opérationnelle.

### Problèmes identifiés (audit)

| # | Problème |
|---|----------|
| P1 | Écarts entre données de stock et commandes |
| P2 | Dégradation des performances en pic de charge |
| P3 | Hétérogénéité technologique (Java, Node.js, PHP, Python) |
| P4 | Forte dépendance à une BDD unique partagée |
| P5 | Reporting non temps réel |

### Objectifs de l'architecture cible

| Objectif | Problème | Formulation |
|----------|----------|-------------|
| O1 | P1 | Garantir la cohérence des données inter-domaines |
| O2 | P2 | Absorber la croissance sans dégradation du parcours client |
| O3 | P3 | Réduire la complexité de maintenance |
| O4 | P4 | Clarifier les responsabilités de chaque domaine |
| O5 | P5 | Permettre un pilotage métier fiable et actualisé |

---

## 2. Principes d'architecture

1. **Séparation des responsabilités** par bounded context (Catalogue, Commandes, Stock, Reporting)
2. **Découplage temporel** des flux critiques (Commandes → Stock par événements async)
3. **Évolutivité progressive** (Strangler Fig Pattern, migration par vagues)
4. **Langage ubiquitaire partagé** (Produit, Commande, Stock, Réservation, Paiement)

---

## 3. Capabilities et idéation

**North Star** : *« Plateforme retail omnicanale fiable, évolutive et maintenable »*

| Capability | Priorité |
|------------|----------|
| TraitementCommandes | Haute |
| GestionStock | Haute |
| GestionCatalogue | Moyenne |
| PilotagePerformance | Moyenne |
| PaiementClient | Haute (intégration) |

---

## 4. User stories et critères d'acceptation

### US-1 — Consultation catalogue (client final)

- [ ] Catalogue consultable avec référence, prix, description
- [ ] Chargement < 2 s en conditions normales
- [ ] Données exclusivement du contexte Catalogue

### US-2 — Passage de commande (client final)

- [ ] Commande créée à partir du catalogue
- [ ] Paiement via API externe uniquement
- [ ] Confirmation client avant réservation stock (async)
- [ ] Réponse < 3 s en pic de charge

### US-3 — Gestion stocks (équipe interne)

- [ ] Consultation et modification des niveaux de stock
- [ ] Stock = source unique de vérité des quantités
- [ ] Réservation automatique sur `CommandeConfirmee`
- [ ] Écarts stock/commandes < 1 % sur 24 h

### US-4 — Pilotage activité (équipe métier)

- [ ] Tableaux de bord accessibles
- [ ] Fraîcheur indicateurs < 15 minutes
- [ ] Reporting en lecture seule, sans impact transactionnel

---

## 5. Glossaire et événements domaine

### Termes clés

| Terme | Contexte |
|-------|----------|
| Produit | Catalogue |
| Commande | Commandes |
| Stock / Réservation | Stock |
| Paiement | Commandes / externe |
| Indicateur | Reporting |

### Événements domaine principaux

| Événement | Émetteur | Consommateur |
|-----------|----------|--------------|
| `CommandeConfirmee` | Commandes | Stock (RabbitMQ) |
| `StockReserve` | Stock | Reporting (CDC) |
| `StockInsuffisant` | Stock | Commandes |
| `PaiementValide` | Commandes | — (interne) |

---

## 6. Context Map

Fichier éditable : [`06-context-map.drawio`](06-context-map.drawio)

| Relation | Pattern DDD | Intégration |
|----------|-------------|-------------|
| Catalogue → Commandes | Customer-Supplier | REST sync |
| Commandes → Stock | Customer-Supplier | Événements async (RabbitMQ) |
| Commandes → Paiement | Anti-Corruption Layer | REST sync |
| Domaines → Reporting | Published Language | CDC read-only |

---

## 7. Architecture applicative

Fichier éditable : [`07-architecture-applicative.drawio`](07-architecture-applicative.drawio)

### Stack cible

```
[React] [Angular] → API Gateway → [Catalogue | Commandes | Stock] (Spring Boot)
                                        ↓ RabbitMQ
                              [PostgreSQL × 3] + [API Paiement]
                                        ↓ Debezium CDC
                              [Metabase] (+ ETL Python transition)
```

### Composants

| Couche | Composants |
|--------|------------|
| Présentation | Front-end React, Back-office Angular |
| Point d'entrée | API Gateway (Spring Cloud Gateway) |
| Services métier | Catalogue, Commandes, Stock (Spring Boot) |
| Infrastructure | RabbitMQ, PostgreSQL × 3, Debezium, Metabase |
| Externe | API Paiement |

---

## 8. Justification d'architecture

### Microservices par bounded context — RETENU

Évolution progressive depuis l'existant, migration par vagues, responsabilités clarifiées.

### Monolithe — ÉCARTÉ

Refonte complète incompatible avec les contraintes.

### Microservices big-bang — ÉCARTÉ

Risque opérationnel trop élevé.

### MVC/API front — RETENU

React/Angular conservés ; API Gateway centralise l'accès aux services backend.

---

## 9. Choix technologiques

| Composant | Technologie | Objectif | Statut |
|-----------|-------------|----------|--------|
| Front e-commerce | React | Continuité | Conservé |
| Back-office | Angular | Continuité | Conservé |
| Services métier | Java Spring Boot | O3 | Migré |
| API Gateway | Spring Cloud Gateway | O4 | Nouveau |
| Messaging | RabbitMQ | O1, O2 | Nouveau |
| BDD | PostgreSQL par service | O1, O4 | Migré |
| CDC / BI | Debezium + Metabase | O5 | Nouveau |
| Paiement | API externe | Sécurité | Conservé |
| Conteneurisation | Docker | O3 | Nouveau |

---

## 10. Architecture de déploiement

Fichier éditable : [`10-architecture-deploiement.drawio`](10-architecture-deploiement.drawio)

### Zones de déploiement

| Zone | Composants |
|------|------------|
| Client | Navigateur (React / Angular) |
| Applicative (Docker) | Gateway, 3 services, RabbitMQ, Debezium, Metabase |
| Données | PostgreSQL Catalogue, Commandes, Stock |
| Externe | API Paiement |

### Building blocks

Docker · PostgreSQL · RabbitMQ · Debezium · Metabase · Spring Cloud Gateway

---

## 11. Modèle de domaine et contrats API

### Agrégats

| Contexte | Agrégat | Règle clé |
|----------|---------|-----------|
| Catalogue | Produit | Référence unique, prix > 0 |
| Commandes | Commande | Confirmée après paiement validé |
| Stock | NiveauStock | Quantité ≥ 0 ; réservation sur `CommandeConfirmee` |

### API REST (extraits)

| Service | Endpoint clé |
|---------|--------------|
| Catalogue | `GET /api/catalogue/produits` |
| Commandes | `POST /api/commandes`, `POST /api/commandes/{id}/paiement` |
| Stock | `GET /api/stock/niveaux`, `PUT /api/stock/niveaux/{ref}` |

### Événements RabbitMQ

- `CommandeConfirmee` → routing key `commandes.confirmee`
- `StockReserve` → routing key `stock.reserve`
- `StockInsuffisant` → routing key `stock.insuffisant`

Détail complet : [`11-modele-domaine.md`](11-modele-domaine.md), [`12-contrats-api.md`](12-contrats-api.md)

---

## 12. Plan d'intégration

Migration en 4 vagues (7-9 mois), système opérationnel à chaque étape.

| Vague | Durée | Solution | Critère de succès |
|-------|-------|----------|-------------------|
| **V1** | 6-8 sem. | RabbitMQ async Commandes/Stock | Latence stable en pic ; 0 perte événements |
| **V2** | 8-10 sem. | Stock → Spring Boot | Parité PHP validée ; PHP décommissionné |
| **V3** | 4-6 sem. | Debezium + Metabase | Indicateurs < 15 min de fraîcheur |
| **V4** | 10-12 sem. | BDD/service + API Gateway | 3 BDD indépendantes ; pas de régression US |

Détail complet : [`13-plan-integration.md`](13-plan-integration.md)

---

## 13. Synthèse et traçabilité

### Fonctionnement cible

Le SI cible conserve les interfaces utilisateur existantes (React, Angular) et réorganise le backend en microservices alignés sur les bounded contexts DDD. La communication critique Commandes/Stock passe par des événements asynchrones (RabbitMQ). Chaque service possède sa propre base PostgreSQL. Le reporting est alimenté en quasi temps réel par CDC (Debezium) vers Metabase.

### Limites adressées

| Limite audit | Solution architecture |
|--------------|----------------------|
| Écarts stock/commandes | Événements traçables + BDD Stock dédiée |
| Pics de charge | Async Commandes/Stock |
| Hétérogénéité | Spring Boot unifié |
| BDD unique | PostgreSQL par service |
| Reporting décalé | CDC + Metabase |

### Traçabilité audit → architecture → migration

```
Audit (P1-P5) → Objectifs (O1-O5) → Principes → Blueprint 12 étapes
    → Architecture cible → 4 vagues d'intégration (V1-V4)
```

### Artefacts modulaires sources

| Artefact | Contenu |
|----------|---------|
| `01-objectifs-et-principes.md` | Problèmes, objectifs, principes |
| `02-ideation-capabilities.md` | North Star, capabilities |
| `03-glossaire-domaine.md` | Langage ubiquitaire |
| `04-user-stories.md` | 4 US + critères |
| `05-event-storming.md` | Événements domaine |
| `06-context-map.drawio` | Relations DDD |
| `07-architecture-applicative.drawio` | UML composants |
| `08-justification-architecture.md` | Microservices vs monolithe |
| `09-choix-technologiques.md` | Stack justifiée |
| `10-architecture-deploiement.drawio` | UML déploiement |
| `11-modele-domaine.md` | Agrégats |
| `12-contrats-api.md` | REST + événements |
| `13-plan-integration.md` | 4 vagues migration |
| `roadmap.md` | Roadmap détaillée complète |

---

*Document assemblé conformément au Synergetic Blueprint et à la demande [`besoin2.md`](../besoin2.md).*

# Rapport d'audit du système d'information — Groupe Retail Sphère

**Date** : juillet 2026  
**Périmètre** : audit du SI existant (modélisation, analyse fonctionnelle et technique, dépendances, benchmark technologique)  
**Sources** : rapport métier haut niveau, description technique du système existant

---

## Table des matières

1. [Contexte et périmètre fonctionnel](#1-contexte-et-périmètre-fonctionnel)
2. [Critères d'audit](#2-critères-daudit)
3. [Modélisation du système existant](#3-modélisation-du-système-existant)
4. [Analyse des composants](#4-analyse-des-composants)
5. [Analyse des dépendances](#5-analyse-des-dépendances)
6. [Benchmark technologique](#6-benchmark-technologique)
7. [Synthèse](#7-synthèse)

---

## 1. Contexte et périmètre fonctionnel

### Présentation du groupe

Le Groupe Retail Sphère est un éditeur de solutions logicielles destiné aux entreprises du secteur de la distribution. Sa plateforme permet à ses clients de gérer leurs activités omnicanales, incluant la vente en ligne, la gestion des stocks et le pilotage des opérations commerciales.

L'entreprise connaît une forte croissance depuis plusieurs années, avec une augmentation du nombre de clients et des volumes de données traités.

### Activités principales

| Usage | Description |
|-------|-------------|
| Consultation catalogue | Consultation d'un catalogue produit en ligne par les clients finaux |
| Gestion des commandes | Prise en charge du cycle de vie des commandes clients |
| Gestion des stocks | Suivi des niveaux de stock en entrepôts et magasins |
| Reporting | Pilotage des performances via des tableaux de bord et indicateurs métiers |

### Utilisateurs du système

| Type d'utilisateur | Rôle | Interface / canal |
|--------------------|------|-------------------|
| Clients finaux | Consultent les produits et passent des commandes | Site e-commerce (front-end) |
| Équipes internes | Gèrent les produits, les commandes et les stocks | Back-office interne |
| Équipes métiers | Pilotent l'activité commerciale | Tableaux de bord de reporting |

### Rôle global du système d'information

Le système d'information du Groupe Retail Sphère constitue la plateforme centrale sur laquelle reposent les activités omnicanales de l'éditeur et de ses clients distributeurs. Il met à disposition des interfaces adaptées à chaque profil d'utilisateur — site e-commerce pour les clients finaux, back-office pour les équipes opérationnelles, reporting pour le pilotage métier — et orchestre les flux métier essentiels : consultation du catalogue, traitement des commandes, gestion des stocks et production d'indicateurs de performance. Dans un contexte de forte croissance, ce SI doit supporter l'augmentation des volumes de clients et de données tout en restant l'outil de travail quotidien des différentes équipes.

### Contexte actuel

Le système d'information s'est construit progressivement, au fil des besoins métier et des évolutions de l'entreprise. Cette croissance organique a conduit à une architecture composée de plusieurs composants interconnectés, développés avec des technologies différentes.

Aujourd'hui, le système montre certaines limites en termes de cohérence, d'évolutivité et de maintenabilité. Le Groupe Retail Sphère souhaite améliorer la structuration de son architecture, réduire les dépendances entre composants et clarifier les responsabilités des services, tout en maintenant le système opérationnel pendant les évolutions.

---

## 2. Critères d'audit

Les critères d'évaluation s'inscrivent dans les objectifs d'évolution du groupe : améliorer la maintenabilité, faciliter l'évolution des fonctionnalités, améliorer la cohérence des données et les performances globales.

| Critère | Objectif d'évaluation |
|---------|----------------------|
| Performance | Capacité du SI à traiter les charges et fournir des réponses dans des délais acceptables |
| Maintenabilité | Facilité de maintenance et d'évolution du code et des composants |
| Cohérence des données | Fiabilité et synchronisation des données entre les services |
| Architecture | Qualité de la structuration, du découpage et des responsabilités |
| Évolutivité | Capacité à faire évoluer le système sans refonte complète |
| Sécurité | Fiabilité des échanges sensibles, notamment les transactions financières |

### Performance

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Temps de traitement des commandes augmentant en pic de charge ; requêtes catalogue lentes ; reporting non temps réel |
| **Indicateur** | Temps de réponse commandes en pic ; temps de chargement catalogue ; fraîcheur des données de reporting |

### Maintenabilité

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Service Stock sur une technologie différente ; règles métier dupliquées ; évolutions multi-composants |
| **Indicateur** | Nombre de technologies distinctes ; composants impactés par évolution ; logique métier dupliquée |

### Cohérence des données

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Écarts entre données de stock et commandes ; synchronisation inter-services complexe |
| **Indicateur** | Fréquence des écarts stock/commandes ; complexité des mécanismes de synchronisation |

### Architecture

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Forte dépendance à la BDD centrale ; interactions nombreuses ; responsabilités peu claires |
| **Indicateur** | Couplage BDD ; lisibilité du graphe d'interactions ; clarté des frontières de responsabilité |

### Évolutivité

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Construction progressive sans architecture unifiée ; pas de refonte complète immédiate possible |
| **Indicateur** | Capacité d'évolution progressive composant par composant sans interruption de service |

### Sécurité

| Élément | Détail |
|---------|--------|
| **Constats documentés** | API externe de paiement (service tiers) ; Service Commandes seul point d'interaction |
| **Indicateur** | Fiabilité de l'intégration paiement ; isolation des flux de transaction |

---

## 3. Modélisation du système existant

Le SI repose sur 8 composants organisés en 3 couches : présentation (front-end, back-office), services métier (Catalogue, Commandes, Stock) et données/intégration (PostgreSQL, reporting, API paiement). Les communications s'effectuent principalement via des API REST synchrones.

### Vue d'architecture

Fichier source éditable : [diagrammes/architecture-composants.drawio](diagrammes/architecture-composants.drawio)

![Architecture composants](diagrammes/architecture-composants.png)

### Flux principaux

Fichier source éditable : [diagrammes/flux-dependances.drawio](diagrammes/flux-dependances.drawio)

![Flux de dépendances](diagrammes/flux-dependances.png)

| Flux | Parcours | Priorité |
|------|----------|----------|
| 1 — Parcours client | Front-end → Catalogue / Commandes → API Paiement → BDD | Haute |
| 2 — Gestion stocks | Commandes → Stock → BDD | Haute |
| 3 — Back-office | Back-office → Catalogue / Commandes / Stock | Moyenne |
| 4 — Reporting | BDD → Outil reporting (batch) | Basse |

---

## 4. Analyse des composants

### 1. Front-end e-commerce

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Interface web pour consulter le catalogue et passer des commandes |
| **Responsabilité technique** | Présentation des données ; appels REST aux services backend |
| **Technologie** | React |
| **Usages métier liés** | Consultation catalogue ; passage de commande |
| **Interactions principales** | Service Catalogue ; Service Commandes |
| **Points de vigilance** | Requêtes catalogue lentes |

### 2. Back-office interne

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Gestion des produits, commandes et stocks par les équipes internes |
| **Responsabilité technique** | Interface d'administration ; orchestration via REST |
| **Technologie** | Angular |
| **Usages métier liés** | Gestion produits, commandes, stocks |
| **Interactions principales** | Service Catalogue ; Service Commandes ; Service Stock |
| **Points de vigilance** | Point d'accès unique vers trois services |

### 3. Service Catalogue

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Gestion des produits (références, prix, descriptions) |
| **Responsabilité technique** | API REST ; persistance en BDD |
| **Technologie** | Java Spring Boot |
| **Usages métier liés** | Consultation catalogue ; gestion produits |
| **Interactions principales** | BDD ; Front-end ; Back-office |
| **Points de vigilance** | Requêtes lentes ; dépendance BDD centrale |

### 4. Service Commandes

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Cycle de vie des commandes (création, validation, suivi) |
| **Responsabilité technique** | Orchestration commande ; coordination stock et paiement |
| **Technologie** | Node.js |
| **Usages métier liés** | Passage de commande ; gestion commandes |
| **Interactions principales** | BDD ; Stock ; API Paiement ; Front-end ; Back-office |
| **Points de vigilance** | Pic de charge ; composant le plus connecté ; écarts stock/commandes |

### 5. Service Stock

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Gestion des niveaux de stock et synchronisation avec les commandes |
| **Responsabilité technique** | Suivi des quantités ; synchronisation avec Commandes |
| **Technologie** | PHP |
| **Usages métier liés** | Gestion stocks ; synchronisation stock/commandes |
| **Interactions principales** | BDD ; Service Commandes ; Back-office |
| **Points de vigilance** | Technologie hétérogène ; écarts de données ; sync complexe |

### 6. Base de données principale

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Stockage centralisé (produits, commandes, clients, stocks) |
| **Responsabilité technique** | Persistance relationnelle ; BDD unique partagée |
| **Technologie** | PostgreSQL |
| **Usages métier liés** | Tous les usages |
| **Interactions principales** | Catalogue ; Commandes ; Stock ; Reporting |
| **Points de vigilance** | Couplage fort ; point de défaillance unique |

### 7. Outil de reporting

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Tableaux de bord et indicateurs métiers |
| **Responsabilité technique** | ETL batch depuis la BDD |
| **Technologie** | Python (scripts ETL) |
| **Usages métier liés** | Pilotage des performances |
| **Interactions principales** | BDD (lecture batch) |
| **Points de vigilance** | Données non temps réel ; stack hétérogène |

### 8. API externe de paiement

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Gestion des transactions de paiement |
| **Responsabilité technique** | Service tiers ; intégration via Service Commandes |
| **Technologie** | Service tiers (externe) |
| **Usages métier liés** | Passage de commande (paiement) |
| **Interactions principales** | Service Commandes |
| **Points de vigilance** | Dépendance prestataire externe |

---

## 5. Analyse des dépendances

### Dépendances structurantes

| Source | Cible | Type | Impact |
|--------|-------|------|--------|
| Front-end | Catalogue / Commandes | Fonctionnelle (REST) | Expérience client dépendante de la performance backend |
| Back-office | Catalogue / Commandes / Stock | Fonctionnelle (REST) | Opérations internes multi-dépendantes |
| Services métier | BDD centrale | Technique | Goulet d'étranglement ; évolutions transversales |
| Commandes | Stock | Fonctionnelle + technique | Source des écarts stock/commandes |
| Commandes | API Paiement | Fonctionnelle + technique | Transaction bloquante |
| BDD | Reporting | Technique (batch) | Données de pilotage décalées |

### Composants fortement couplés

1. **Services ↔ BDD centrale** — couplage fort, goulet d'étranglement en pic de charge
2. **Commandes ↔ Stock** — synchronisation synchrone, écarts documentés, stacks hétérogènes (Node.js/PHP)
3. **Règles métier dupliquées** — évolutions coordonnées sur plusieurs services, risque d'incohérence

---

## 6. Benchmark technologique

| Problème | Techno actuelle | Alternative recommandée | Solutions existantes | Objectif |
|----------|----------------|------------------------|----------------------|----------|
| Couplage Commandes/Stock | REST synchrone | Messagerie asynchrone par événements | **RabbitMQ**, **Apache Kafka** | Performance, cohérence |
| Hétérogénéité (PHP) | Service Stock en PHP | Alignement Java Spring Boot | **Spring Boot**, **Quarkus** | Maintenabilité |
| BDD unique | PostgreSQL partagée | BDD par service (Stock, Commandes) | **PostgreSQL** (instances dédiées), **MySQL** | Cohérence, évolutivité |
| Reporting batch | Python ETL | CDC + outil BI en complément | **Debezium**, **Metabase** | Pilotage temps réel |

### Comparaison des solutions concrètes

#### Messagerie — RabbitMQ vs Apache Kafka

| Critère | RabbitMQ | Apache Kafka |
|---------|----------|--------------|
| Complexité | Faible à modérée | Élevée (cluster, topics, retention) |
| Volumes | Adapté aux volumes actuels Commandes→Stock | Orienté très haut débit / log d'événements |
| Compétences | Courbe d'apprentissage raisonnable | Expertise ops plus lourde |
| Migration progressive | Intégration progressive simple | Plus lourd à introduire |

**Recommandation** : **RabbitMQ** — volumes et contrainte de migration progressive ne justifient pas Kafka.

#### Stack Java — Spring Boot vs Quarkus

| Critère | Spring Boot | Quarkus |
|---------|-------------|---------|
| Continuité | Déjà utilisé (Service Catalogue) | Nouveau socle à apprendre |
| Écosystème | Mature, large documentation | Cloud-native, démarrage rapide |
| Migration Stock | Capitalisation compétences existantes | Double courbe (framework + migration PHP) |
| Maintenabilité | Unifie Catalogue / Stock / Commandes | Risque de nouvelle hétérogénéité |

**Recommandation** : **Spring Boot** — alignement sur l'existant Catalogue.

#### BDD par service — PostgreSQL vs MySQL

| Critère | PostgreSQL (instances dédiées) | MySQL |
|---------|--------------------------------|-------|
| Continuité | Déjà en production | Changement de moteur |
| Compétences | Équipes déjà formées | Nouvelle expertise |
| Isolation | Une instance / schéma par service | Équivalent possible |
| Risque migration | Principalement découpage données | Découpage + conversion techno |

**Recommandation** : **PostgreSQL** (instances dédiées) — continuité et moindre risque.

#### Reporting — Debezium (CDC) et Metabase (BI)

Ces deux solutions sont **complémentaires** (pas concurrentes) : Debezium capture les changements, Metabase les visualise.

| Critère | Debezium | Metabase |
|---------|----------|----------|
| Rôle | CDC — capture des changements BDD | BI — tableaux de bord métier |
| Fraîcheur | Quasi temps réel | Consomme le flux CDC |
| Impact transactionnel | Lecture seule (logs/replication) | Aucun (lecture) |
| Transition | Complète l'ETL, ne le remplace pas d'emblée | Interface équipes métiers |

**Recommandation** : **Debezium + Metabase** en complément de l'ETL Python pendant la transition.

#### Synthèse des solutions retenues

| Domaine | Solution retenue |
|---------|------------------|
| Messagerie | RabbitMQ |
| Stack services | Spring Boot |
| BDD | PostgreSQL par service |
| Reporting | Debezium + Metabase |

Toutes les recommandations respectent les contraintes : système opérationnel pendant les évolutions, pas de refonte complète immédiate, appropriation progressive par les équipes.

---

## 7. Synthèse

### 7.1 Fonctionnement global du SI

Le SI du Groupe Retail Sphère est une plateforme omnicanale composée de 8 éléments interconnectés. Les clients finaux accèdent au catalogue et passent des commandes via un front-end React ; les équipes internes gèrent l'opérationnel via un back-office Angular ; les équipes métiers pilotent l'activité via des rapports générés en batch. Trois services métier (Catalogue en Java, Commandes en Node.js, Stock en PHP) orchestrent les flux principaux, avec une persistance centralisée dans une base PostgreSQL unique et un paiement externalisé via une API tierce.

### 7.2 Limites principales par critère d'audit

| Critère | Limite principale |
|---------|-------------------|
| Performance | Dégradation en pic de charge sur le parcours commande ; catalogue lent ; reporting non temps réel |
| Maintenabilité | 4 langages (Java, Node.js, PHP, Python) ; règles métier dupliquées ; évolutions multi-composants |
| Cohérence des données | Écarts stock/commandes ; synchronisation complexe entre services hétérogènes |
| Architecture | BDD unique partagée ; interactions nombreuses ; responsabilités peu délimitées |
| Évolutivité | Architecture construite progressivement sans vision unifiée ; couplages limitant l'évolution indépendante |
| Sécurité | Dépendance à un prestataire externe pour les paiements (seul constat documenté) |

### 7.3 Pistes d'amélioration

1. **Découpler Commandes et Stock** via une communication asynchrone par événements, pour réduire la latence en pic de charge et améliorer la traçabilité de la synchronisation des données.
2. **Uniformiser le Service Stock** sur Java Spring Boot pour réduire l'hétérogénéité technologique et faciliter la maintenance.
3. **Introduire des bases dédiées** pour les domaines Stock et Commandes, en commençant par le découplage des données de stock.
4. **Moderniser le reporting** en complétant l'ETL batch par un mécanisme CDC pour des indicateurs proches du temps réel.
5. **Centraliser les règles métier dupliquées** pour limiter les modifications coordonnées sur plusieurs services.

### 7.4 Recommandations prioritaires

| Priorité | Action | Impact attendu | Contrainte respectée |
|----------|--------|----------------|---------------------|
| 1 | Messagerie asynchrone Commandes → Stock | Performance + cohérence | Migration progressive |
| 2 | Migration Service Stock vers Java Spring Boot | Maintenabilité | Service par service |
| 3 | CDC + outil BI pour le reporting | Pilotage amélioré | Faible impact opérationnel |
| 4 | BDD par service (Stock, Commandes) | Évolutivité + cohérence | Long terme, par étapes |

Le SI actuel remplit son rôle fonctionnel (catalogue, commandes, stock, reporting) mais atteint ses limites structurelles face à la croissance du groupe. Les recommandations proposées constituent une trajectoire d'évolution progressive, alignée sur les objectifs et contraintes du Groupe Retail Sphère, sans remettre en cause la continuité opérationnelle du système.

---

*Artefacts modulaires sources : `01-contexte-fonctionnel.md`, `02-criteres-audit.md`, `03-analyse-composants.md`, `04-analyse-dependances.md`, `05-benchmark-technologique.md`, `diagrammes/*.drawio`*

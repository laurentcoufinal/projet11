# Choix technologiques — Architecture cible

Chaque choix est justifié par un objectif d'architecture défini dans [`01-objectifs-et-principes.md`](01-objectifs-et-principes.md) et cohérent avec le benchmark de l'audit ([`projet/livrables/05-benchmark-technologique.md`](../../projet/livrables/05-benchmark-technologique.md)).

---

## Stack cible synthétique

```
[React] [Angular] → API Gateway (Spring Cloud Gateway)
                         ↓
              [Catalogue | Commandes | Stock] (Spring Boot)
                         ↓ RabbitMQ
              [PostgreSQL × 3] + [API Paiement externe]
                         ↓ Debezium CDC
              [Metabase] (+ ETL Python en transition)
```

---

## Tableau des choix technologiques

| Composant | Technologie retenue | Objectif servi | Statut | Justification |
|-----------|---------------------|----------------|--------|---------------|
| Front e-commerce | **React** | Continuité UX | Conservé | Pas de problème identifié sur le frontend ; évite une rupture utilisateur |
| Back-office | **Angular** | Continuité UX | Conservé | Idem ; équipes opérationnelles formées |
| Services métier | **Java Spring Boot** | O3 — Maintenance | Migré (Stock, Commandes) / Conservé (Catalogue) | Réduction hétérogénéité ; capitalisation sur l'existant Catalogue |
| API Gateway | **Spring Cloud Gateway** | O4 — Responsabilités | Nouveau | Point d'entrée unique, routage, sécurité centralisée |
| Messaging | **RabbitMQ** | O1, O2 — Cohérence, résilience | Nouveau | Découplage async Commandes/Stock ; traçabilité événements |
| Base de données | **PostgreSQL (par service)** | O1, O4 — Cohérence, responsabilités | Migré progressivement | Découplage données ; évolutions schéma indépendantes |
| CDC | **Debezium** | O5 — Pilotage | Nouveau | Capture changements sans impact transactionnel |
| BI / Reporting | **Metabase** + ETL Python | O5 — Pilotage | Complété | Fraîcheur données ; ETL batch conservé en transition |
| Conteneurisation | **Docker** | O3 — Maintenance | Nouveau | Déploiement modulaire, reproductibilité |
| Paiement | **API externe** (inchangée) | Sécurité transactions | Conservé | Périmètre tiers stable ; ACL dans Service Commandes |

---

## Détail par couche

### Couche présentation

| Choix | Alternative écartée | Raison |
|-------|---------------------|--------|
| React (conservé) | Refonte Next.js | Hors périmètre audit ; coût sans gain objectif |
| Angular (conservé) | Refonte Vue.js | Idem |

### Couche services

| Choix | Alternative écartée | Raison |
|-------|---------------------|--------|
| Spring Boot unifié | Conserver Node.js (Commandes) + PHP (Stock) | Hétérogénéité documentée ; maintenance complexe |
| Spring Boot unifié | Node.js pour tous | Catalogue déjà en Java ; migration inutile |

### Couche données

| Choix | Alternative écartée | Raison |
|-------|---------------------|--------|
| PostgreSQL par service | BDD unique partagée (actuel) | Couplage fort documenté ; goulet d'étranglement |
| PostgreSQL par service | MongoDB par service | Changement de paradigme non justifié ; équipes PostgreSQL |

### Couche intégration

| Choix | Alternative écartée | Raison |
|-------|---------------------|--------|
| RabbitMQ | Kafka | Volumes actuels ne justifient pas la complexité Kafka |
| RabbitMQ | REST synchrone (actuel) | Latence en pic documentée |
| Debezium CDC | Polling ETL seul | Fraîcheur insuffisante pour le pilotage |

---

## Cohérence globale de la stack

| Critère | Évaluation |
|---------|------------|
| Nombre de langages backend cible | 1 (Java) vs 4 actuellement |
| Technologies nouvelles | 4 (Gateway, RabbitMQ, Debezium, Metabase) — introduites progressivement |
| Technologies conservées | 4 (React, Angular, PostgreSQL, API Paiement) |
| Risque de dispersion | Faible — socle Spring Boot + PostgreSQL |

---

## Traçabilité benchmark → choix

| Recommandation audit | Choix retenu | Vague d'intégration |
|---------------------|--------------|---------------------|
| Messagerie async Commandes/Stock | RabbitMQ | V1 |
| Migration Stock → Spring Boot | Java Spring Boot | V2 |
| CDC + BI | Debezium + Metabase | V3 |
| BDD par service | PostgreSQL × 3 | V4 |
| API Gateway | Spring Cloud Gateway | V4 |

---

## Technologies explicitement hors périmètre

| Technologie | Raison d'exclusion |
|-------------|-------------------|
| Kubernetes | Complexité opérationnelle non justifiée à ce stade ; Docker suffit |
| Kafka | Volumes de messages actuels ne le justifient pas |
| Refonte frontend | Pas de problème identifié sur les interfaces |
| Nouveau prestataire paiement | Périmètre stable, intégration existante fonctionnelle |

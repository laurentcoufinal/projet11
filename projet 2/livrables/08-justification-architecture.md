# Justification d'architecture

## Choix architectural principal : microservices par bounded context

### Option retenue — Microservices par bounded context (évolution progressive)

L'architecture cible organise le SI en services autonomes alignés sur les bounded contexts DDD (Catalogue, Commandes, Stock, Reporting). Chaque service possède sa propre base de données et expose des API REST. La communication inter-domaines critique (Commandes → Stock) s'effectue par événements asynchrones.

**Justification** :
- Aligné sur l'existant (déjà organisé en services métier)
- Permet une migration progressive (Strangler Fig Pattern) sans refonte complète
- Répond aux objectifs O1 (cohérence), O4 (responsabilités) et O3 (maintenabilité)
- Compatible avec la contrainte de maintien opérationnel pendant les évolutions

### Option écartée — Monolithe

Un regroupement de toute la logique métier dans une application unique simplifierait le déploiement initial mais nécessiterait une refonte complète du SI existant.

**Raisons d'écart** :
- Incompatible avec la contrainte « pas de refonte complète immédiate »
- Risque opérationnel élevé (big-bang)
- Ne résout pas la problématique de migration progressive

### Option écartée — Microservices big-bang

Une décomposition immédiate de tous les services avec bases de données séparées et stack unifiée dès le départ.

**Raisons d'écart** :
- Risque opérationnel trop élevé pour une plateforme en production
- Courbe d'apprentissage simultanée sur plusieurs technologies nouvelles
- Non conforme à l'appropriation progressive attendue par les équipes

---

## Pattern de présentation : MVC / API côté front

### Option retenue — SPA (React/Angular) + API REST via API Gateway

Les interfaces utilisateur existantes (React pour l'e-commerce, Angular pour le back-office) sont conservées. Elles communiquent avec les services backend via une API Gateway centralisée.

| Couche | Rôle | Technologie |
|--------|------|-------------|
| **Vue** | Affichage et interaction utilisateur | React, Angular |
| **Contrôleur** | Logique de présentation côté client | Composants React/Angular |
| **Modèle** | Données et règles métier | Services backend (Spring Boot) |

**Justification** :
- Continuité pour les utilisateurs (pas de changement d'interface)
- Séparation claire entre présentation et logique métier
- API Gateway centralise routage, authentification et monitoring

### Option écartée — Server-Side Rendering (SSR) unifié

Remplacement des SPA par un framework SSR unique (ex. Next.js).

**Raisons d'écart** :
- Rupture pour les équipes front existantes
- Hors périmètre de l'audit (pas de problème identifié sur les frontends)
- Coût de migration sans gain sur les objectifs prioritaires

---

## Patterns d'intégration inter-services

| Relation | Pattern retenu | Alternative écartée | Raison |
|----------|---------------|---------------------|--------|
| Commandes → Stock | Événements async (RabbitMQ) | REST synchrone (actuel) | Performance, découplage |
| Commandes → Paiement | Anti-Corruption Layer + REST | Intégration directe sans couche | Isolation du modèle externe |
| Reporting → domaines | CDC read-only (Debezium) | Accès direct BDD partagée | Découplage, pas d'impact transactionnel |
| Front → Services | API Gateway | Appels directs multi-services | Point d'entrée unique, sécurité |

---

## Décisions d'architecture (ADR synthèse)

| # | Décision | Statut | Objectif |
|---|----------|--------|----------|
| ADR-1 | Microservices par bounded context | Retenu | O4 |
| ADR-2 | Messagerie async Commandes/Stock | Retenu | O1, O2 |
| ADR-3 | PostgreSQL par service (progressif) | Retenu | O1, O4 |
| ADR-4 | Conservation React/Angular | Retenu | Continuité |
| ADR-5 | API Gateway Spring Cloud Gateway | Retenu | O4 |
| ADR-6 | Monolithe | Écarté | Contrainte refonte |
| ADR-7 | Big-bang microservices | Écarté | Risque opérationnel |

---

## Traçabilité objectifs → décisions

| Objectif | Décision architecturale |
|----------|------------------------|
| O1 Cohérence | BDD par service + événements traçables |
| O2 Résilience | Async Commandes/Stock + API Gateway |
| O3 Maintenance | Stack unifiée Spring Boot (migration progressive) |
| O4 Responsabilités | Bounded contexts + API Gateway |
| O5 Pilotage | CDC + Metabase (lecture seule découplée) |

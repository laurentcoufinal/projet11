# Critères d'audit du système d'information

Ce document définit les critères utilisés pour évaluer l'adéquation du SI du Groupe Retail Sphère. Les constats proviennent du rapport métier haut niveau ; les indicateurs d'évaluation permettent de mesurer l'écart par rapport aux objectifs d'évolution du groupe.

## Vue d'ensemble des critères

| Critère | Objectif d'évaluation |
|---------|----------------------|
| Performance | Capacité du SI à traiter les charges et fournir des réponses dans des délais acceptables |
| Maintenabilité | Facilité de maintenance et d'évolution du code et des composants |
| Cohérence des données | Fiabilité et synchronisation des données entre les services |
| Architecture | Qualité de la structuration, du découpage et des responsabilités |
| Évolutivité | Capacité à faire évoluer le système sans refonte complète |
| Sécurité | Fiabilité des échanges sensibles, notamment les transactions financières |

---

## 1. Performance

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Le temps de traitement des commandes augmente lors des pics de charge ; certaines requêtes sur le catalogue sont lentes ; le système de reporting ne fournit pas de données en temps réel |
| **Indicateur d'évaluation** | Temps de réponse des commandes en période de pic ; temps de chargement du catalogue ; délai de fraîcheur des données de reporting |
| **Seuil attendu** | Traitement des commandes stable en pic de charge ; catalogue consultable sans latence perceptible ; reporting aligné sur les besoins de pilotage (actuellement non temps réel) |

---

## 2. Maintenabilité

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Le service Stock est basé sur une technologie différente du reste du système ; certaines règles métier sont dupliquées dans plusieurs services ; les évolutions nécessitent souvent des modifications sur plusieurs composants |
| **Indicateur d'évaluation** | Nombre de technologies distinctes ; nombre de composants impactés par une évolution fonctionnelle ; présence de logique métier dupliquée |
| **Seuil attendu** | Réduction de l'hétérogénéité technologique ; évolutions localisées à un nombre limité de composants ; règles métier centralisées |

---

## 3. Cohérence des données

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Des écarts sont constatés entre les données de stock et les commandes ; la synchronisation des données entre les services est parfois complexe |
| **Indicateur d'évaluation** | Fréquence des écarts stock/commandes ; complexité des mécanismes de synchronisation inter-services |
| **Seuil attendu** | Données de stock et de commandes alignées ; synchronisation prévisible et traçable entre services |

---

## 4. Architecture

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Les services sont fortement dépendants de la base de données centrale ; les interactions entre services sont nombreuses et parfois difficiles à suivre ; le système manque de découpage clair entre les responsabilités |
| **Indicateur d'évaluation** | Degré de couplage à la BDD centrale ; lisibilité du graphe d'interactions ; clarté des frontières de responsabilité par composant |
| **Seuil attendu** | Architecture structurée par couches ; dépendances explicites et limitées ; responsabilités clairement attribuées à chaque service |

---

## 5. Évolutivité

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Le système s'est construit progressivement sans architecture unifiée globale ; une refonte complète immédiate n'est pas envisageable ; le système existant doit rester opérationnel pendant les évolutions |
| **Indicateur d'évaluation** | Capacité à intégrer de nouvelles fonctionnalités sans impact transversal ; possibilité d'évolution progressive composant par composant |
| **Seuil attendu** | Évolutions réalisables par étapes, sans interruption de service ; les équipes peuvent s'approprier progressivement les nouvelles solutions |

---

## 6. Sécurité

| Élément | Détail |
|---------|--------|
| **Constats documentés** | Le système s'appuie sur une API externe de paiement pour la gestion des transactions financières (service tiers) ; aucun autre constat de sécurité n'est documenté dans les sources |
| **Indicateur d'évaluation** | Fiabilité de l'intégration avec le prestataire de paiement ; isolation des flux de transaction du reste du SI |
| **Seuil attendu** | Les paiements transitent exclusivement par le service tiers dédié ; le Service Commandes est le seul point d'interaction avec l'API de paiement |

---

## Objectifs d'évolution associés

Les critères d'audit s'inscrivent dans les objectifs du Groupe Retail Sphère :

- Améliorer la maintenabilité du système
- Faciliter l'évolution des fonctionnalités
- Améliorer la cohérence des données
- Améliorer les performances globales

Les contraintes imposent de maintenir le système opérationnel pendant les évolutions et d'éviter une refonte complète immédiate.

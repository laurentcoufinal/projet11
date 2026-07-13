# Idéation stratégique — Capabilities et North Star

**Synergetic Blueprint** : étapes 1 à 3 (Idéation stratégique).

---

## North Star

> **« Plateforme retail omnicanale fiable, évolutive et maintenable »**

Vision directrice pour la modernisation du SI : supporter la croissance du Groupe Retail Sphère tout en améliorant la cohérence des données, la performance et la capacité d'évolution, sans rupture opérationnelle pour les clients et les équipes internes.

---

## Business capabilities identifiées

| Capability | Description | Utilisateurs | Priorité audit |
|------------|-------------|--------------|----------------|
| **GestionCatalogue** | Consultation et administration des produits (références, prix, descriptions) | Clients finaux, équipes internes | Moyenne |
| **TraitementCommandes** | Cycle de vie des commandes (création, validation, paiement, suivi) | Clients finaux, équipes internes | **Haute** |
| **GestionStock** | Suivi des niveaux de stock, réservations, entrepôts et magasins | Équipes internes | **Haute** |
| **PilotagePerformance** | Production d'indicateurs et tableaux de bord métier | Équipes métiers | Moyenne |
| **PaiementClient** | Traitement des transactions financières lors des commandes | Clients finaux | Haute (intégration) |

---

## Priorisation des capabilities

Basée sur l'analyse des flux critiques de l'audit (parcours client et gestion stocks en priorité).

| Rang | Capability | Justification |
|------|------------|---------------|
| 1 | TraitementCommandes | Flux le plus critique ; impact direct sur le chiffre d'affaires ; dégradation documentée en pic de charge |
| 2 | GestionStock | Couplage fort avec Commandes ; source des écarts de données documentés |
| 3 | GestionCatalogue | Requêtes lentes mais moins critique que le parcours commande |
| 4 | PilotagePerformance | Amélioration souhaitée mais sans impact sur le transactionnel |
| 5 | PaiementClient | Service externe stable ; intégration à préserver, pas à refondre |

---

## Frontières de domaine initiales (bounded contexts candidats)

| Capability | Bounded context candidat | Frontière |
|------------|--------------------------|-----------|
| GestionCatalogue | **Catalogue** | Produits, prix, références |
| TraitementCommandes | **Commandes** | Cycle de vie commande, orchestration paiement |
| GestionStock | **Stock** | Niveaux, réservations, entrepôts/magasins |
| PilotagePerformance | **Reporting** | Indicateurs, tableaux de bord (lecture seule) |
| PaiementClient | **Paiement** (externe) | Transactions financières (système tiers) |

---

## Business Model Canvas simplifié

| Bloc | Élément Retail Sphère |
|------|----------------------|
| **Proposition de valeur** | Plateforme SaaS omnicanale pour distributeurs |
| **Segments clients** | Entreprises de la distribution |
| **Canaux** | Site e-commerce, back-office, reporting |
| **Activités clés** | Catalogue, commandes, stock, pilotage |
| **Ressources clés** | SI modulaire, équipes dev multi-stacks |
| **Partenaires clés** | Prestataire de paiement externe |
| **Structure de coûts** | Maintenance SI, infrastructure, intégrations |
| **Sources de revenus** | Abonnements SaaS clients distributeurs |

---

## Impact Mapping (simplifié)

| Acteur | Objectif | Impacts mesurables |
|--------|----------|-------------------|
| Client final | Passer commande rapidement | Temps de réponse < 3 s en pic |
| Équipe interne | Gérer stocks sans erreur | 0 écart stock/commandes |
| Équipe métier | Piloter l'activité | Indicateurs < 15 min de fraîcheur |
| Équipe technique | Maintenir le SI | Évolutions localisées à 1-2 services max |

---

## Output de la zone Idéation

- North Star définie
- 5 capabilities identifiées et priorisées
- 5 bounded contexts candidats esquissés
- Capabilities **Commandes** et **Stock** identifiées comme leviers prioritaires de la modernisation

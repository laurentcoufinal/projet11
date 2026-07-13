# User stories — Système cible

**Synergetic Blueprint** : étapes 4-7 | **besoin2** : 3 à 5 cas d'usage principaux.

---

## US-1 — Consultation du catalogue

**En tant que** client final,  
**je veux** consulter le catalogue produit en ligne,  
**afin de** identifier les produits disponibles avant de passer commande.

| Attribut | Valeur |
|----------|--------|
| **Capability** | GestionCatalogue |
| **Bounded context** | Catalogue |
| **Principe d'architecture** | Séparation des responsabilités |

### Critères d'acceptation

- [ ] Le client peut parcourir la liste des produits avec référence, prix et description
- [ ] Le temps de chargement de la page catalogue est inférieur à 2 secondes en conditions normales
- [ ] Les données affichées proviennent exclusivement du contexte Catalogue
- [ ] Aucune donnée de stock ou de commande n'est requise pour afficher le catalogue

---

## US-2 — Passage de commande avec paiement

**En tant que** client final,  
**je veux** passer une commande et payer en ligne,  
**afin de** acquérir les produits sélectionnés.

| Attribut | Valeur |
|----------|--------|
| **Capability** | TraitementCommandes, PaiementClient |
| **Bounded context** | Commandes, Paiement (externe) |
| **Principe d'architecture** | Découplage temporel |

### Critères d'acceptation

- [ ] Le client peut créer une commande à partir de produits du catalogue
- [ ] Le paiement transite exclusivement par l'API externe de paiement
- [ ] La commande est confirmée au client avant la réservation stock (traitement asynchrone)
- [ ] En période de pic de charge, le client reçoit une confirmation de commande en moins de 3 secondes
- [ ] La réservation stock est déclenchée par événement après confirmation, sans bloquer la réponse client

---

## US-3 — Gestion des stocks

**En tant que** membre de l'équipe interne,  
**je veux** gérer les niveaux de stock des produits en entrepôts et magasins,  
**afin de** garantir la disponibilité des produits commandés.

| Attribut | Valeur |
|----------|--------|
| **Capability** | GestionStock |
| **Bounded context** | Stock |
| **Principe d'architecture** | Séparation des responsabilités, cohérence des données |

### Critères d'acceptation

- [ ] L'équipe interne peut consulter et modifier les niveaux de stock par produit et par lieu
- [ ] Le contexte Stock est la source unique de vérité pour les quantités disponibles
- [ ] Une réservation est automatiquement créée à la réception d'un événement `CommandeConfirmee`
- [ ] Les écarts entre stock affiché et commandes en cours sont inférieurs à 1 % sur une période de 24 h

---

## US-4 — Pilotage de l'activité

**En tant que** membre de l'équipe métier,  
**je veux** consulter des indicateurs de performance actualisés,  
**afin de** piloter l'activité commerciale de manière fiable.

| Attribut | Valeur |
|----------|--------|
| **Capability** | PilotagePerformance |
| **Bounded context** | Reporting |
| **Principe d'architecture** | Évolutivité progressive |

### Critères d'acceptation

- [ ] L'équipe métier accède à des tableaux de bord via l'outil de reporting
- [ ] Les indicateurs (chiffre d'affaires, volume commandes, niveaux stock) ont une fraîcheur inférieure à 15 minutes
- [ ] Le reporting fonctionne en lecture seule, sans impact sur les transactions opérationnelles
- [ ] L'ETL batch existant reste disponible en parallèle pendant la phase de transition

---

## Matrice de traçabilité

| User story | Objectif | Capability | Événements domaine clés |
|------------|----------|------------|------------------------|
| US-1 | O2, O4 | GestionCatalogue | `ProduitConsulte` |
| US-2 | O1, O2 | TraitementCommandes | `CommandeCreee`, `PaiementValide`, `CommandeConfirmee` |
| US-3 | O1, O4 | GestionStock | `StockReserve`, `StockMisAJour` |
| US-4 | O5 | PilotagePerformance | — (lecture CDC) |

---

## Example Mapping (Synergetic Blueprint étape 11)

### US-2 — Exemples

| Règle | Exemple concret |
|-------|----------------|
| Commande confirmée avant réservation stock | Client paie → reçoit « Commande confirmée » → stock réservé 2 s plus tard |
| Paiement via API externe uniquement | Aucun traitement carte bancaire dans le service Commandes |
| Réponse < 3 s en pic | 500 commandes simultanées : 95e percentile < 3 s |

| Contre-exemple | Comportement attendu |
|----------------|---------------------|
| Paiement refusé | Commande reste « En attente », pas de réservation stock |
| Stock insuffisant après confirmation | Événement `StockInsuffisant` → alerte équipe interne |

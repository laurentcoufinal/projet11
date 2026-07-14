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

```gherkin
Fonctionnalité: Consultation du catalogue
  En tant que client final
  Je veux consulter le catalogue produit en ligne
  Afin d'identifier les produits disponibles avant de passer commande

  Scénario: Parcourir la liste des produits
    Étant donné que je suis un client final sur le site
    Quand j'accède à la page catalogue
    Alors je vois pour chaque produit sa référence, son prix et sa description

  Scénario: Temps de chargement acceptable
    Étant donné des conditions normales de charge
    Quand j'accède à la page catalogue
    Alors la page s'affiche en moins de 2 secondes

  Scénario: Données issues du contexte Catalogue uniquement
    Étant donné que le catalogue contient des produits publiés
    Quand j'accède à la page catalogue
    Alors les données affichées proviennent exclusivement du contexte Catalogue

  Scénario: Affichage sans dépendance aux contextes Stock et Commandes
    Étant donné que les contextes Stock et Commandes sont indisponibles
    Quand j'accède à la page catalogue
    Alors le catalogue s'affiche correctement sans requête de stock ni de commande
```

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

```gherkin
Fonctionnalité: Passage de commande avec paiement
  En tant que client final
  Je veux passer une commande et payer en ligne
  Afin d'acquérir les produits sélectionnés

  Scénario: Créer une commande à partir du catalogue
    Étant donné que j'ai sélectionné des produits du catalogue
    Quand je valide ma commande
    Alors une commande est créée avec les produits sélectionnés

  Scénario: Paiement via l'API externe uniquement
    Étant donné que j'ai une commande en attente de paiement
    Quand je procède au paiement
    Alors le paiement transite exclusivement par l'API externe de paiement
    Et aucun traitement de carte bancaire n'est effectué dans le service Commandes

  Scénario: Confirmation client avant réservation stock
    Étant donné que j'ai validé le paiement de ma commande
    Quand le paiement est accepté
    Alors je reçois immédiatement le message « Commande confirmée »
    Et la réservation stock est effectuée environ 2 secondes plus tard

  Scénario: Temps de réponse en période de pic
    Étant donné une période de pic avec 500 commandes simultanées
    Quand je valide ma commande et mon paiement
    Alors je reçois une confirmation de commande en moins de 3 secondes
    Et le 95e percentile des temps de réponse est inférieur à 3 secondes

  Scénario: Réservation stock déclenchée par événement
    Étant donné que ma commande est confirmée
    Quand l'événement CommandeConfirmee est publié
    Alors la réservation stock est déclenchée de manière asynchrone
    Et la réponse au client n'est pas bloquée par la réservation

  Scénario: Paiement refusé
    Étant donné que j'ai une commande en attente de paiement
    Quand le paiement est refusé par l'API externe
    Alors ma commande reste au statut « En attente »
    Et aucune réservation stock n'est créée

  Scénario: Stock insuffisant après confirmation
    Étant donné que ma commande est confirmée
    Quand le stock disponible est insuffisant pour honorer la commande
    Alors l'événement StockInsuffisant est publié
    Et l'équipe interne reçoit une alerte
```

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

```gherkin
Fonctionnalité: Gestion des stocks
  En tant que membre de l'équipe interne
  Je veux gérer les niveaux de stock des produits en entrepôts et magasins
  Afin de garantir la disponibilité des produits commandés

  Scénario: Consulter et modifier les niveaux de stock
    Étant donné que je suis un membre de l'équipe interne authentifié
    Quand j'accède à la gestion des stocks pour un produit et un lieu donnés
    Alors je peux consulter le niveau de stock actuel
    Et je peux modifier ce niveau de stock

  Scénario: Stock comme source unique de vérité
    Étant donné qu'un produit est référencé dans plusieurs contextes
    Quand une quantité disponible est consultée pour ce produit
    Alors la quantité provient exclusivement du contexte Stock

  Scénario: Réservation automatique à la confirmation de commande
    Étant donné qu'un événement CommandeConfirmee est reçu pour une commande
    Quand le contexte Stock traite cet événement
    Alors une réservation est automatiquement créée pour les produits commandés

  Scénario: Cohérence stock et commandes en cours
    Étant donné une période de 24 heures d'activité normale
    Quand les écarts entre le stock affiché et les commandes en cours sont mesurés
    Alors ces écarts sont inférieurs à 1 %
```

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

```gherkin
Fonctionnalité: Pilotage de l'activité
  En tant que membre de l'équipe métier
  Je veux consulter des indicateurs de performance actualisés
  Afin de piloter l'activité commerciale de manière fiable

  Scénario: Accès aux tableaux de bord
    Étant donné que je suis un membre de l'équipe métier authentifié
    Quand j'accède à l'outil de reporting
    Alors je peux consulter les tableaux de bord de pilotage

  Scénario: Fraîcheur des indicateurs
    Étant donné que des transactions opérationnelles ont eu lieu récemment
    Quand je consulte les indicateurs de chiffre d'affaires, de volume de commandes et de niveaux de stock
    Alors ces indicateurs ont une fraîcheur inférieure à 15 minutes

  Scénario: Reporting en lecture seule
    Étant donné que le reporting est consulté pendant une période de charge opérationnelle
    Quand l'équipe métier consulte les tableaux de bord
    Alors les transactions opérationnelles ne sont pas impactées par la consultation

  Scénario: ETL batch disponible en parallèle
    Étant donné que le système est en phase de transition
    Quand l'équipe métier utilise l'outil de reporting
    Alors l'ETL batch existant reste disponible en parallèle
```

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

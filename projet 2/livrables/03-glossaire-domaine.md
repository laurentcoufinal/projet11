# Glossaire du domaine — Langage ubiquitaire

**Synergetic Blueprint** : étape 5 (Visual Glossary).

Ce glossaire définit les termes métier partagés entre les équipes métier et IT. Chaque terme est utilisé de manière identique dans les user stories, les événements domaine et les contrats d'API.

---

## Termes du domaine

| Terme | Définition | Bounded context | Exemple d'usage |
|-------|------------|-----------------|-----------------|
| **Produit** | Article commercialisé avec une référence unique, un prix et une description | Catalogue | « Le Produit REF-1234 est affiché au catalogue » |
| **Commande** | Demande d'achat d'un ou plusieurs Produits par un Client, avec un cycle de vie défini | Commandes | « La Commande CMD-5678 est en attente de paiement » |
| **Client** | Utilisateur final qui consulte le catalogue et passe des Commandes | Commandes | « Le Client authentifie sa Commande » |
| **Stock** | Quantité disponible d'un Produit dans un entrepôt ou un magasin | Stock | « Le Stock du Produit REF-1234 est de 42 unités » |
| **Réservation** | Blocage temporaire d'une quantité de Stock suite à une Commande validée | Stock | « Une Réservation de 2 unités est créée pour la Commande CMD-5678 » |
| **Paiement** | Transaction financière associée à une Commande, traitée par un prestataire externe | Commandes / Paiement | « Le Paiement de la Commande CMD-5678 est validé » |
| **Indicateur** | Mesure agrégée permettant le pilotage de l'activité commerciale | Reporting | « L'Indicateur de chiffre d'affaires journalier est consulté » |

---

## Cycle de vie de la Commande

| État | Description | Événement déclencheur |
|------|-------------|----------------------|
| Créée | Commande initiée par le Client | `CommandeCreee` |
| En attente de paiement | Commande enregistrée, paiement non encore validé | — |
| Payée | Paiement validé par le prestataire externe | `PaiementValide` |
| Confirmée | Commande validée, réservation stock déclenchée | `CommandeConfirmee` |
| Annulée | Commande annulée avant ou après paiement | `CommandeAnnulee` |

---

## Règles métier clés (langage métier)

| Règle | Domaine |
|-------|---------|
| Un Produit possède une référence unique | Catalogue |
| Le prix d'un Produit est strictement positif | Catalogue |
| Une Commande ne peut être confirmée qu'après validation du Paiement | Commandes |
| Le Stock d'un Produit ne peut pas être négatif | Stock |
| Une Réservation est créée uniquement sur `CommandeConfirmee` | Stock |
| Les Paiements transitent exclusivement par le prestataire externe | Commandes |

---

## Correspondance termes existants → termes cibles

| Terme actuel (SI) | Terme ubiquitaire | Changement |
|-------------------|-------------------|------------|
| Référence produit | Produit | Unification |
| Niveau de stock | Stock | Simplification |
| Transaction | Paiement | Clarification |
| Tableau de bord | Indicateur | Précision du périmètre |

---

## Anti-patterns linguistiques à éviter

| À éviter | Utiliser à la place | Raison |
|----------|---------------------|--------|
| « Article » et « Produit » interchangeables | **Produit** uniquement | Cohérence |
| « Order » dans les APIs métier | **Commande** | Langage français métier |
| « Inventory » | **Stock** | Terme du rapport métier source |

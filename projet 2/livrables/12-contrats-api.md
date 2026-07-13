# Contrats d'API — REST et événements domaine

**Synergetic Blueprint** : étape 10 (API Product Canvas simplifié).

---

## API REST — Service Catalogue

**Base URL** : `/api/catalogue`

| Méthode | Endpoint | Description | User story |
|---------|----------|-------------|------------|
| GET | `/produits` | Liste des produits actifs | US-1 |
| GET | `/produits/{reference}` | Détail d'un produit | US-1 |
| POST | `/produits` | Créer un produit (back-office) | US-1 |
| PUT | `/produits/{reference}` | Modifier un produit (back-office) | US-1 |

**Exemple réponse GET `/produits/{reference}`** :
```json
{
  "reference": "REF-1234",
  "libelle": "Produit exemple",
  "description": "Description du produit",
  "prix": 29.99,
  "statut": "ACTIF"
}
```

---

## API REST — Service Commandes

**Base URL** : `/api/commandes`

| Méthode | Endpoint | Description | User story |
|---------|----------|-------------|------------|
| POST | `/commandes` | Créer une commande | US-2 |
| GET | `/commandes/{id}` | Détail d'une commande | US-2 |
| POST | `/commandes/{id}/paiement` | Initier le paiement (ACL vers API externe) | US-2 |
| POST | `/commandes/{id}/annulation` | Annuler une commande | US-2 |
| GET | `/commandes` | Liste des commandes (back-office) | US-2 |

**Exemple requête POST `/commandes`** :
```json
{
  "clientId": "CLI-001",
  "lignes": [
    { "referenceProduit": "REF-1234", "quantite": 2, "prixUnitaire": 29.99 }
  ]
}
```

**Exemple réponse POST `/commandes/{id}/paiement`** :
```json
{
  "commandeId": "CMD-5678",
  "statut": "CONFIRME",
  "message": "Commande confirmée. Réservation stock en cours."
}
```

---

## API REST — Service Stock

**Base URL** : `/api/stock`

| Méthode | Endpoint | Description | User story |
|---------|----------|-------------|------------|
| GET | `/niveaux/{referenceProduit}` | Niveau de stock par produit | US-3 |
| GET | `/niveaux` | Liste des niveaux (back-office) | US-3 |
| PUT | `/niveaux/{referenceProduit}` | Ajuster un niveau (back-office) | US-3 |
| GET | `/reservations/{commandeId}` | Réservation liée à une commande | US-3 |

---

## Schémas d'événements domaine (RabbitMQ)

**Exchange** : `retail-sphere.events` (topic)

### CommandeConfirmee

| Champ | Type | Description |
|-------|------|-------------|
| `eventType` | string | `"CommandeConfirmee"` |
| `commandeId` | string | Identifiant de la commande |
| `lignes` | array | `[{ referenceProduit, quantite }]` |
| `timestamp` | ISO 8601 | Horodatage de l'événement |

**Routing key** : `commandes.confirmee`  
**Consommateur** : Service Stock

### CommandeAnnulee

| Champ | Type | Description |
|-------|------|-------------|
| `eventType` | string | `"CommandeAnnulee"` |
| `commandeId` | string | Identifiant de la commande |
| `timestamp` | ISO 8601 | Horodatage |

**Routing key** : `commandes.annulee`  
**Consommateur** : Service Stock

### StockReserve

| Champ | Type | Description |
|-------|------|-------------|
| `eventType` | string | `"StockReserve"` |
| `commandeId` | string | Commande source |
| `referenceProduit` | string | Produit réservé |
| `quantite` | integer | Quantité réservée |
| `timestamp` | ISO 8601 | Horodatage |

**Routing key** : `stock.reserve`  
**Consommateur** : Reporting (CDC)

### StockInsuffisant

| Champ | Type | Description |
|-------|------|-------------|
| `eventType` | string | `"StockInsuffisant"` |
| `commandeId` | string | Commande concernée |
| `referenceProduit` | string | Produit en rupture |
| `quantiteDemandee` | integer | Quantité demandée |
| `quantiteDisponible` | integer | Quantité réellement disponible |

**Routing key** : `stock.insuffisant`  
**Consommateur** : Service Commandes (alerte)

---

## Anti-Corruption Layer — API Paiement externe

Le Service Commandes traduit le modèle interne (`Paiement`) vers le modèle du prestataire externe.

| Modèle interne | Modèle externe (API Paiement) |
|----------------|-------------------------------|
| `commandeId` | `order_ref` |
| `montant` | `amount` |
| `statut: PAYE` | `status: succeeded` |
| `statut: ECHEC` | `status: failed` |

---

## Traçabilité contrats → user stories → événements

| User story | API REST | Événement async |
|------------|----------|-----------------|
| US-1 | GET `/produits` | `ProduitConsulte` (optionnel) |
| US-2 | POST `/commandes`, POST `/paiement` | `CommandeConfirmee` → Stock |
| US-3 | GET/PUT `/niveaux` | `StockReserve`, `StockMisAJour` |
| US-4 | — (Metabase) | CDC depuis tous les contextes |

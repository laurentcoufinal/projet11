# Exercice 1 — Lire une Wardley Map

**Module associé :** [Module 3 — Lire une Wardley Map](../03-lecture-d-une-map.md)  
**Durée estimée :** 20 minutes  
**Niveau :** Débutant

## Contexte

Vous rejoignez l'équipe de **ShopLocal**, une marketplace qui met en relation des artisans locaux et des acheteurs. L'équipe a produit la Wardley Map suivante avant votre arrivée.

## La map à analyser

```text
                    Genesis    Custom      Product      Commodity
                 ┌──────────┬───────────┬────────────┬────────────┐
                 │          │           │            │            │
  Utilisateur    │  [Ache-  │           │            │            │
  (Acheteur      │  teur    │           │            │            │
   local)        │  local]  │           │            │            │
                 │          │           │            │            │
                 ├──────────┼───────────┼────────────┼────────────┤
                 │          │           │            │            │
  Besoins        │          │[Découvrir │[Acheter   │            │
                 │          │ artisans  │ un produit│            │
                 │          │ locaux]   │]           │            │
                 │          │           │            │            │
                 ├──────────┼───────────┼────────────┼────────────┤
                 │          │           │            │            │
  Métier         │          │[Moteur de │[Catalogue │            │
                 │          │ matching  │ produits] │            │
                 │          │ géoloc]   │           │            │
                 │          │     →     │           │            │
                 ├──────────┼───────────┼────────────┼────────────┤
                 │          │           │            │            │
  Technique      │          │           │[Panier /  │[Paiement   │
                 │          │           │ commande] │ Stripe]    │
                 │          │           │            │            │
                 ├──────────┼───────────┼────────────┼────────────┤
                 │          │           │            │            │
  Infra          │          │           │[Auth      │[Hébergement│
                 │          │           │ Keycloak] │ AWS]       │
                 │          │           │[BDD       │[CDN        │
                 │          │           │ Postgres] │ Cloudflare]│
                 └──────────┴───────────┴────────────┴────────────┘
```

## Questions

### Question 1 — Utilisateur et besoins

a) Qui est l'utilisateur principal de cette map ?  
b) Les besoins sont-ils exprimés correctement (en langage métier, pas technique) ? Justifiez.

### Question 2 — Zones stratégiques

a) Quel composant est le **différenciateur** de ShopLocal ? Où se situe-t-il sur la map ?  
b) Citez **3 composants** qui devraient être achetés (Buy) plutôt que construits. Justifiez leur position.

### Question 3 — Mouvement

a) Quel composant a un mouvement anticipé ? Vers quel stade évolue-t-il ?  
b) Quelle implication stratégique cela a-t-il pour ShopLocal ?

### Question 4 — Incohérences

La map contient au moins **2 incohérences** ou choix discutables. Identifiez-les et proposez une correction.

### Question 5 — Décisions

Pour chaque composant ci-dessous, indiquez la décision recommandée (Build / Buy / Outsource / Don't build) et justifiez en une phrase :

| Composant | Votre décision | Justification |
|-----------|---------------|---------------|
| Moteur de matching géoloc | | |
| Paiement (Stripe) | | |
| Auth (Keycloak self-hosted) | | |
| Catalogue produits | | |
| Hébergement AWS | | |

## Livrable

Rédigez vos réponses dans un document ou directement ci-dessous chaque question.

## Correction

→ [Corrigé de l'exercice 1](corriges/ex01-corrige.md)

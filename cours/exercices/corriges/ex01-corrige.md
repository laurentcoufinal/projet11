# Corrigé — Exercice 1 — Lire une Wardley Map

## Question 1 — Utilisateur et besoins

### a) Utilisateur principal

L'utilisateur principal est l'**acheteur local** — la personne qui cherche à acheter des produits d'artisans près de chez elle.

### b) Qualité des besoins

**Oui**, les besoins sont correctement exprimés :

- « Découvrir artisans locaux » — verbe d'action, orienté utilisateur
- « Acheter un produit » — besoin métier clair

Ils ne mentionnent aucune technologie (pas de « API », « React », « base de données »). C'est la bonne pratique.

**Point d'amélioration possible :** on pourrait ajouter un besoin « Suivre ma commande » ou « Évaluer un artisan », mais 2 besoins suffisent pour une première map.

---

## Question 2 — Zones stratégiques

### a) Différenciateur

Le **moteur de matching géolocalisé** est le différenciateur. Il se situe en **zone Custom, au niveau métier** (milieu-haut de la map, côté gauche).

C'est ce composant qui distingue ShopLocal d'une marketplace générique : la capacité de connecter un acheteur avec des artisans **proches géographiquement**.

### b) Trois composants à acheter

| Composant | Position | Pourquoi Buy |
|-----------|----------|--------------|
| **Paiement (Stripe)** | Commodity | Standard universel, interchangeble, ne jamais construire |
| **Hébergement AWS** | Commodity | Infrastructure pure, aucune valeur à opérer soi-même |
| **CDN Cloudflare** | Commodity | Service utilitaire standardisé |

On pourrait aussi accepter : Auth (devrait être un SaaS, pas self-hosted), BDD Postgres managée (RDS).

---

## Question 3 — Mouvement

### a) Composant en mouvement

Le **moteur de matching géolocalisé** a une flèche `→` indiquant un mouvement vers **Product**.

### b) Implication stratégique

Le matching géoloc va se standardiser (des librairies et services de géolocalisation/proximité existent déjà). ShopLocal doit :

1. **Court terme** : capitaliser sur son avantage actuel (investir dans la qualité du matching)
2. **Moyen terme** : préparer un **nouveau différenciateur** car le matching ne sera plus un argument de vente
3. **Ne pas sur-investir** : éviter de construire une usine à gaz — rester lean

**Question clé :** quand le matching sera banal, sur quoi ShopLocal se différenciera-t-il ? (ex. qualité artisanale, communauté, logistique locale)

---

## Question 4 — Incohérences

### Incohérence 1 : Auth en Keycloak self-hosted (Product, mais mal positionné)

Keycloak est un produit open-source qu'on **auto-héberge**. C'est un choix Product, mais pour une startup/marketplace, **Auth0 ou Firebase Auth** (SaaS managé) serait plus adapté :

- Moins de maintenance opérationnelle
- Time-to-market plus rapide
- Positionné en Commodity/Product côté droit

**Correction :** remplacer par Auth0 (Buy, Commodity) ou au minimum Keycloak managé.

### Incohérence 2 : BDD Postgres en Product alors qu'elle devrait être Commodity

PostgreSQL en tant que composant « persistance » est une **commodité**. L'auto-héberger sur AWS EC2 est un choix Custom inutile. Il faudrait utiliser une **BDD managée** (RDS, Supabase) en zone Commodity.

**Correction :** déplacer vers Commodity avec RDS ou Supabase.

### Incohérence 3 (bonus) : Pas d'utilisateur « artisan »

La map ne montre que l'acheteur. Or une marketplace a **deux côtés**. Il manque potentiellement une seconde map pour l'artisan (besoin : « Vendre mes produits en ligne »).

---

## Question 5 — Décisions

| Composant | Décision | Justification |
|-----------|----------|---------------|
| Moteur de matching géoloc | **Build** | Différenciateur en zone Custom — c'est le cœur de la valeur ShopLocal |
| Paiement (Stripe) | **Buy** | Commodity — Stripe est le standard, ne jamais construire son propre processeur de paiement |
| Auth (Keycloak self-hosted) | **Buy** (Auth0) | Product/Commodity — le self-hosting ajoute de la complexité ops sans valeur. Préférer Auth0 ou Firebase Auth |
| Catalogue produits | **Buy** ou Build léger | Product — des solutions existent (Shopify headless, Snipcart). Si le catalogue est simple, un CRUD maison suffit |
| Hébergement AWS | **Buy** | Commodity — utiliser le cloud sans réinventer l'infrastructure |

---

## Points clés à retenir

- Le différenciateur se lit en **haut-gauche**
- Les commodités se lisent en **bas-droite** → Buy systématique
- Le **mouvement** change la donne : un avantage temporaire ne justifie pas un investissement permanent
- Une map peut révéler des **incohérences** entre la position stratégique et les choix techniques actuels

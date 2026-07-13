# Analyse des composants du système d'information

Ce document décrit chaque composant du SI du Groupe Retail Sphère selon une structure identique : rôle métier, responsabilité technique, technologie, usages métier liés, interactions principales et points de vigilance.

---

## 1. Front-end e-commerce

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Interface web permettant aux clients finaux de consulter le catalogue produit et de passer des commandes en ligne |
| **Responsabilité technique** | Présentation des données catalogue et commandes ; collecte des actions utilisateur ; appels aux services backend via API REST |
| **Technologie** | React |
| **Usages métier liés** | Consultation catalogue ; passage de commande |
| **Interactions principales** | Service Catalogue (consultation produits) ; Service Commandes (création et suivi de commandes) |
| **Points de vigilance** | Certaines requêtes sur le catalogue sont lentes (impact performance perçue par les clients finaux) |

---

## 2. Back-office interne

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Interface utilisée par les équipes internes pour gérer les produits, les commandes et les stocks |
| **Responsabilité technique** | Interface d'administration ; orchestration des opérations de gestion via appels REST vers les services métier |
| **Technologie** | Angular |
| **Usages métier liés** | Gestion des produits ; gestion des commandes ; gestion des stocks |
| **Interactions principales** | Service Catalogue ; Service Commandes ; Service Stock |
| **Points de vigilance** | Point d'accès unique vers trois services distincts, ce qui concentre les dépendances fonctionnelles côté opérations internes |

---

## 3. Service Catalogue

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Gestion des produits : références, prix et descriptions du catalogue |
| **Responsabilité technique** | Exposition d'API REST pour la consultation et la modification des données produit ; persistance en base de données |
| **Technologie** | Java Spring Boot |
| **Usages métier liés** | Consultation catalogue ; gestion des produits (back-office) |
| **Interactions principales** | Base de données principale ; Front-end e-commerce ; Back-office interne |
| **Points de vigilance** | Requêtes lentes sur le catalogue ; dépendance directe à la BDD centrale partagée |

---

## 4. Service Commandes

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Gestion du cycle de vie des commandes : création, validation et suivi |
| **Responsabilité technique** | Orchestration du parcours commande ; coordination avec le stock et le paiement ; persistance des commandes en base |
| **Technologie** | Node.js |
| **Usages métier liés** | Passage de commande ; gestion des commandes (back-office) |
| **Interactions principales** | Base de données principale ; Service Stock ; API externe de paiement ; Front-end e-commerce ; Back-office interne |
| **Points de vigilance** | Temps de traitement augmentant en pic de charge ; composant le plus connecté du SI (5 interactions) ; écarts possibles entre données de stock et commandes |

---

## 5. Service Stock

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Gestion des niveaux de stock (entrepôts et magasins) et synchronisation avec les commandes |
| **Responsabilité technique** | Suivi et mise à jour des quantités en stock ; synchronisation avec le Service Commandes ; persistance en base |
| **Technologie** | PHP |
| **Usages métier liés** | Gestion des stocks ; synchronisation stock/commandes |
| **Interactions principales** | Base de données principale ; Service Commandes ; Back-office interne |
| **Points de vigilance** | Technologie différente du reste du système (impact maintenabilité) ; écarts constatés entre données de stock et commandes ; synchronisation parfois complexe |

---

## 6. Base de données principale

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Stockage centralisé de l'ensemble des données métier : produits, commandes, clients et stocks |
| **Responsabilité technique** | Persistance relationnelle ; point de stockage unique partagé par tous les services |
| **Technologie** | PostgreSQL |
| **Usages métier liés** | Tous les usages (catalogue, commandes, stock, reporting) |
| **Interactions principales** | Service Catalogue ; Service Commandes ; Service Stock ; Outil de reporting (lecture) |
| **Points de vigilance** | Base unique partagée : couplage fort de tous les services ; point de défaillance unique ; forte dépendance documentée de l'architecture |

---

## 7. Outil de reporting

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Génération de tableaux de bord et d'indicateurs métiers pour le pilotage de l'activité |
| **Responsabilité technique** | Extraction et transformation des données (ETL) depuis la base principale ; production de rapports batch |
| **Technologie** | Python (scripts ETL) |
| **Usages métier liés** | Pilotage des performances ; consultation des tableaux de bord par les équipes métiers |
| **Interactions principales** | Base de données principale (lecture batch) |
| **Points de vigilance** | Ne fournit pas de données en temps réel ; technologie hétérogène (Python) au sein d'un SI multi-stacks |

---

## 8. API externe de paiement

| Attribut | Description |
|----------|-------------|
| **Rôle métier** | Gestion des transactions de paiement lors du passage de commande |
| **Responsabilité technique** | Traitement des paiements via un service tiers externe ; intégration exclusivement via le Service Commandes |
| **Technologie** | Service tiers (externe) |
| **Usages métier liés** | Passage de commande (paiement) |
| **Interactions principales** | Service Commandes |
| **Points de vigilance** | Dépendance à un prestataire externe ; seul point d'échange pour les transactions financières documenté dans le SI |

---

## Synthèse par usage métier

| Usage métier | Composants impliqués |
|--------------|---------------------|
| Consultation catalogue | Front-end e-commerce, Service Catalogue |
| Passage de commande | Front-end e-commerce, Service Commandes, API externe de paiement |
| Gestion produits / commandes / stocks | Back-office interne, Service Catalogue, Service Commandes, Service Stock |
| Pilotage de l'activité | Outil de reporting, Base de données principale |

Description technique du système existant
Groupe Retail Sphère
Vue d’ensemble 2
Liste des composants 2
1. Front-end e-commerce 2
2. Back-office interne 2
3. Service Catalogue 2
4. Service Commandes 3
5. Service Stock 3
6. Base de données principale 3
7. Outil de reporting 3
8. API externe de paiement 3
Interactions principales 4
Parcours client 4
Gestion des stocks 4
Back-office 4
Reporting 4
Observations générales 4
Vue d’ensemble
Le système d’information du Groupe Retail Sphère repose sur plusieurs composants applicatifs interconnectés.
L’architecture actuelle est organisée autour de services métiers, d’interfaces utilisateurs et d’un système de stockage centralisé.
Liste des composants
1. Front-end e-commerce
● Rôle : interface web utilisée par les clients pour consulter le catalogue et passer des commandes
● Technologie : React
● Interactions :
○ Service Catalogue
○ Service Commandes
2. Back-office interne
● Rôle : interface utilisée par les équipes internes pour gérer les produits, les commandes et les stocks
● Technologie : Angular
● Interactions :
○ Service Catalogue
○ Service Commandes
○ Service Stock
3. Service Catalogue
● Rôle : gestion des produits (références, prix, descriptions)
● Technologie : Java Spring Boot
● Interactions :
○ Base de données
○ Frontend
○ Back-office
4. Service Commandes
● Rôle : gestion du cycle de vie des commandes (création, validation, suivi)
● Technologie : Node.js
● Interactions :
○ Base de données
○ Service Stock
○ API de paiement
○ Frontend
○ Back-office
5. Service Stock
● Rôle : gestion des niveaux de stock et synchronisation avec les commandes
● Technologie : PHP
● Interactions :
○ Base de données
○ Service Commandes
○ Back-office
6. Base de données principale
● Rôle : stockage des données (produits, commandes, clients, stocks)
● Technologie : PostgreSQL
● Particularité :
○ base unique partagée par tous les services
7. Outil de reporting
● Rôle : génération de tableaux de bord et d’indicateurs métiers
● Technologie : Python (scripts ETL)
● Interactions :
○ lecture des données depuis la base principale
8. API externe de paiement
● Rôle : gestion des transactions de paiement
● Type : service tiers
● Interactions :
○ Service Commandes
Interactions principales
Le système fonctionne principalement via des appels synchrones entre les services.
Parcours client
● Frontend → Service Catalogue
● Frontend → Service Commandes
● Service Commandes → API paiement
● Service Commandes → Base de données
Gestion des stocks
● Service Commandes → Service Stock
● Service Stock → Base de données
Back-office
● Back-office → Catalogue
● Back-office → Commandes
● Back-office → Stock
Reporting
● Base de données → Outil de reporting (batch)
Observations générales
● Les services communiquent principalement via des API REST synchrones
● Les données sont centralisées dans une base unique
● Certaines technologies sont hétérogènes (Java, Node.js, PHP, Python)
● Le système s’est construit progressivement, sans architecture unifiée globale
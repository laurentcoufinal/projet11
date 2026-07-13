Rapport métier haut niveau
Groupe Retail Sphère
Présentation du SI et contexte métier 2
Présentation du Groupe Retail Sphère 2
Activités principales 2
Utilisateurs du système 2
Contexte actuel 2
Rapport d’état du système d’information 3
Performance 3
Maintenabilité 3
Cohérence des données 3
Architecture 3
Contraintes et objectifs d’évolution 3
Objectifs 3
Contraintes 4
Attentes 4
Présentation du SI et contexte métier
Présentation du Groupe Retail Sphère
Le Groupe Retail Sphère est un éditeur de solutions logicielles destiné aux entreprises du secteur de la distribution. Sa plateforme permet à ses clients de gérer leurs activités omnicanales, incluant la vente en ligne, la gestion des stocks et le pilotage des opérations commerciales.
L’entreprise connaît une forte croissance depuis plusieurs années, avec une augmentation du nombre de clients et des volumes de données traitées.
Activités principales
La plateforme couvre les principaux usages suivants :
● consultation d’un catalogue produit en ligne ;
● gestion des commandes clients ;
● gestion des stocks (entrepôts et magasins) ;
● pilotage des performances via des outils de reporting.
Utilisateurs du système
Le système est utilisé par plusieurs types d’acteurs :
● Clients finaux : utilisent le site e-commerce pour consulter les produits et passer des commandes ;
● Équipes internes : utilisent le back-office pour gérer les produits, les commandes et les stocks ;
● Équipes métiers : consultent les tableaux de bord pour piloter l’activité.
Contexte actuel
Le système d’information s’est construit progressivement, au fil des besoins métier et des évolutions de l’entreprise. Cette croissance a conduit à une architecture composée de plusieurs composants interconnectés, développés avec des technologies différentes.
Aujourd’hui, le système montre certaines limites en termes de cohérence, d’évolutivité et de maintenabilité.
Rapport d’état du système d’information
Performance
● Le temps de traitement des commandes augmente lors des pics de charge
● Certaines requêtes sur le catalogue sont lentes
● Le système de reporting ne fournit pas de données en temps réel
Maintenabilité
● Le service Stock est basé sur une technologie différente du reste du système
● Certaines règles métier sont dupliquées dans plusieurs services
● Les évolutions nécessitent souvent des modifications sur plusieurs composants
Cohérence des données
● Des écarts sont constatés entre les données de stock et les commandes
● La synchronisation des données entre les services est parfois complexe
Architecture
● Les services sont fortement dépendants de la base de données centrale
● Les interactions entre services sont nombreuses et parfois difficiles à suivre
● Le système manque de découpage clair entre les responsabilités
Contraintes et objectifs d’évolution
Objectifs
Le Groupe Retail Sphère souhaite :
● améliorer la maintenabilité du système
● faciliter l’évolution des fonctionnalités
● améliorer la cohérence des données
● améliorer les performances globales
Contraintes
● Le système existant doit rester opérationnel pendant les évolutions
● Une refonte complète immédiate n’est pas envisageable
● Les équipes doivent pouvoir s’approprier progressivement les nouvelles solutions
Attentes
Une attention particulière est attendue sur :
● la structuration de l’architecture
● la réduction des dépendances entre composants
● la clarification des responsabilités des services
# Benchmark technologique

Ce benchmark compare des alternatives technologiques en réponse aux problèmes observés dans le SI du Groupe Retail Sphère. Chaque comparaison est limitée à des solutions pertinentes pour les besoins identifiés, sans veille technologique générale.

## Problèmes observés et périmètre du benchmark

| Problème observé | Besoin métier associé | Technologie actuelle |
|------------------|----------------------|---------------------|
| Hétérogénéité des stacks (Java, Node.js, PHP, Python) | Améliorer la maintenabilité | Multi-stacks |
| BDD unique partagée par tous les services | Améliorer la cohérence des données et l'évolutivité | PostgreSQL monolithique |
| Reporting non temps réel | Améliorer les performances de pilotage | Python ETL batch |
| Appels synchrones inter-services en pic de charge | Améliorer les performances globales | API REST synchrone |

---

## Comparaison 1 — Uniformisation des stacks de services

**Problème** : Le service Stock (PHP) et l'outil de reporting (Python) utilisent des technologies différentes du reste (Java, Node.js), ce qui complique la maintenance et les évolutions multi-composants.

| Critère | Situation actuelle (multi-stacks) | Alternative : stack unifiée (Java Spring Boot) |
|---------|-----------------------------------|--------------------------------------------------|
| Maintenabilité | Faible — 4 langages, compétences dispersées | Élevée — un socle commun pour Catalogue, Commandes et Stock |
| Courbe d'apprentissage | Élevée — chaque service nécessite une expertise distincte | Modérée — capitalisation sur l'existant Java Spring Boot |
| Risque de migration | — | Modéré — migration progressive possible (contrainte : pas de refonte complète) |
| Impact opérationnel | — | Le système reste opérationnel si migration service par service |

**Recommandation** : À terme, aligner le Service Stock sur Java Spring Boot (déjà utilisé par le Service Catalogue) pour réduire l'hétérogénéité. Migration progressive en commençant par le service le plus couplé (Stock), conformément à la contrainte d'évolution sans interruption.

---

## Comparaison 2 — Découpage de la base de données

**Problème** : La base PostgreSQL unique est partagée par tous les services, créant un couplage fort et des risques d'incohérence entre stock et commandes.

| Critère | Situation actuelle (BDD unique) | Alternative : BDD par service |
|---------|----------------------------------|-------------------------------|
| Cohérence des données | Faible — écarts stock/commandes documentés | Améliorée — chaque service maîtrise son périmètre de données |
| Performance | Dégradée en pic — goulet d'étranglement central | Améliorée — charges réparties par service |
| Évolutivité | Faible — évolutions de schéma transversales | Élevée — évolutions indépendantes par service |
| Complexité de mise en œuvre | — | Élevée — nécessite une stratégie de synchronisation inter-services |

**Recommandation** : Introduire progressivement des bases dédiées pour les domaines les plus critiques (Stock et Commandes), en commençant par découpler les données de stock. Cela répond directement aux écarts documentés et à l'objectif de cohérence des données, tout en respectant la contrainte de non-refonte immédiate.

---

## Comparaison 3 — Reporting temps réel

**Problème** : L'outil de reporting (Python ETL batch) ne fournit pas de données en temps réel, limitant le pilotage métier.

| Critère | Situation actuelle (ETL batch) | Alternative : pipeline de données en flux (ex. change data capture + outil BI) |
|---------|-------------------------------|-------------------------------------------------------------------------------|
| Fraîcheur des données | Faible — données décalées (batch) | Élevée — données proches du temps réel |
| Performance du pilotage | Limitée — décisions sur données anciennes | Améliorée — indicateurs actualisés |
| Complexité | Faible — scripts ETL existants | Modérée — infrastructure de flux à mettre en place |
| Impact sur l'opérationnel | Aucun (lecture seule) | Faible — lecture seule, pas d'impact sur les transactions |

**Recommandation** : Compléter l'ETL batch existant par un mécanisme de capture des changements sur la BDD (CDC) alimentant un outil de visualisation. Cette évolution progressive améliore le pilotage sans impacter le système transactionnel, en accord avec la contrainte de maintien opérationnel.

---

## Comparaison 4 — Communication inter-services

**Problème** : Les appels REST synchrones entre services amplifient les latences en pic de charge, notamment sur le parcours commande (Commandes → Stock → BDD).

| Critère | Situation actuelle (REST synchrone) | Alternative : messagerie asynchrone (ex. file de messages) |
|---------|-------------------------------------|-----------------------------------------------------------|
| Performance en pic de charge | Faible — chaîne synchrone bloquante | Améliorée — découplage temporel des traitements |
| Découplage des services | Faible — dépendance directe Commandes/Stock | Élevé — communication par événements |
| Cohérence des données | Risque d'écarts (sync synchrone défaillante) | Améliorée si événements ordonnés et traçables |
| Complexité de mise en œuvre | Faible — pattern existant | Modérée — infrastructure de messaging à ajouter |

**Recommandation** : Pour le flux critique Commandes → Stock, introduire une communication asynchrone par événements (ex. « commande validée » → « mise à jour stock »). Cela réduit la latence perçue en pic de charge et améliore la traçabilité de la synchronisation stock/commandes, répondant aux deux constats documentés (performance et cohérence).

---

## Tableau de synthèse des recommandations

| Priorité | Problème | Solution recommandée | Objectif métier | Faisabilité |
|----------|----------|---------------------|-----------------|-------------|
| 1 | Couplage Commandes/Stock + écarts de données | Messagerie asynchrone + découplage progressif des BDD | Cohérence des données, performance | Migration progressive possible |
| 2 | Hétérogénéité PHP (Service Stock) | Alignement sur Java Spring Boot | Maintenabilité | Migration service par service |
| 3 | Reporting non temps réel | CDC + outil BI en complément de l'ETL | Performance de pilotage | Faible impact opérationnel |
| 4 | BDD unique partagée | BDD par service (Stock, Commandes en priorité) | Évolutivité, cohérence | Long terme, par étapes |

Toutes les recommandations respectent les contraintes du projet : le système reste opérationnel pendant les évolutions, aucune refonte complète immédiate, et les équipes peuvent s'approprier progressivement les nouvelles solutions.

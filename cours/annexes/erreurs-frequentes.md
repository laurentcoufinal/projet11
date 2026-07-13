# Erreurs fréquentes — Wardley Maps

Ce document recense les pièges les plus courants lors de la création et de l'utilisation de Wardley Maps pour des applications informatiques.

---

## 1. Cartographier des technologies au lieu de composants

**Erreur :** placer « React », « PostgreSQL », « Kubernetes » sur la map.

**Pourquoi c'est faux :** une Wardley Map cartographie des **capacités**, pas des implémentations. La technologie est un choix qui vient **après** la map.

**Correction :**

| Incorrect | Correct |
|-----------|---------|
| React | Interface utilisateur |
| PostgreSQL | Persistance des données |
| Kubernetes | Orchestration de conteneurs |
| Redis | Cache |
| Docker | Conteneurisation |

Le choix React vs Vue se fait **après** avoir positionné « Interface utilisateur » en Product.

---

## 2. Commencer par la technique, pas par l'utilisateur

**Erreur :** démarrer la map par la stack technique (« On a un backend Node.js, une BDD Mongo... »).

**Pourquoi c'est faux :** la map doit être **ancrée par le besoin utilisateur**. Sinon, on optimise la technique sans savoir si elle crée de la valeur.

**Correction :** toujours commencer par « Qui est mon utilisateur ? » et « De quoi a-t-il besoin ? »

---

## 3. Map trop détaillée

**Erreur :** 40-50 composants avec chaque micro-service, chaque table, chaque endpoint.

**Pourquoi c'est faux :** la map devient illisible et perd son pouvoir stratégique. On ne voit plus la forêt pour les arbres.

**Correction :**
- Première passe : 10-15 composants larges
- Deuxième passe (optionnelle) : zoomer sur **un** composant critique
- Règle : si un composant n'influence pas une décision build/buy/outsource, il est trop détaillé

---

## 4. Ignorer le mouvement

**Erreur :** traiter la map comme un snapshot figé sans anticiper l'évolution.

**Pourquoi c'est faux :** le mouvement (genesis → commodity) est le principe le plus puissant des Wardley Maps. Un composant en genesis aujourd'hui sera product demain.

**Correction :**
- Ajouter des flèches `→` pour les composants en mouvement
- Se demander : « Dans 2 ans, ce composant sera où ? »
- Ne pas sur-investir dans ce qui va se commoditiser

---

## 5. Construire ce qui est déjà commoditisé

**Erreur :** développer son propre système d'authentification, de paiement, d'envoi d'emails, ou d'hébergement.

**Pourquoi c'est faux :** ces composants sont en bas-droite de toute map. Les construire gaspille du temps et introduit des risques (sécurité, fiabilité).

**Correction :** en zone bas-droite, la décision par défaut est **Buy**. Toujours.

**Exemples de composants à ne jamais construire :**
- Authentification (Auth0, Firebase Auth, Clerk)
- Paiement (Stripe, PayPal)
- Email transactionnel (SendGrid, SES)
- Hébergement (AWS, GCP, Railway)
- CDN (Cloudflare)
- Certificats TLS (Let's Encrypt)

---

## 6. Acheter du genesis

**Erreur :** utiliser un outil immature ou mal adapté pour un besoin unique en zone genesis/custom haut.

**Pourquoi c'est faux :** les produits en genesis n'ont pas encore la maturité pour des besoins spécialisés. Le fit sera mauvais.

**Correction :** en zone genesis haut, **construire** (ou attendre que le marché mature). N'achetez pas un SaaS qui promet de tout faire si votre besoin est unique.

---

## 7. Confondre features et besoins

**Erreur :** lister des fonctionnalités techniques comme besoins.

| Feature (incorrect) | Besoin (correct) |
|--------------------|------------------|
| « API REST » | « Intégrer mes données avec d'autres outils » |
| « Dashboard temps réel » | « Voir l'état de mon activité instantanément » |
| « Export CSV » | « Analyser mes données dans Excel » |
| « Mode sombre » | « Utiliser l'app confortablement le soir » |

**Correction :** reformulez chaque feature en posant la question « Pourquoi l'utilisateur veut-il ça ? »

---

## 8. Une seule map pour tous les utilisateurs

**Erreur :** mélanger les besoins de l'admin, du client final et du développeur API sur une seule map.

**Pourquoi c'est faux :** chaque persona a des besoins et des chaînes de valeur différents. La map devient incohérente.

**Correction :** une map par persona principal. Si nécessaire, montrez les composants partagés entre maps.

---

## 9. Ne pas impliquer l'équipe

**Erreur :** créer la map seul dans son coin, sans validation métier ou produit.

**Pourquoi c'est faux :** la map reflète une vision partielle. Le positionnement des composants sur l'axe d'évolution est subjectif et bénéficie de perspectives multiples.

**Correction :** atelier de 1-2h avec 2-4 personnes (métier + technique + produit). La discussion **est** la valeur, pas le dessin.

---

## 10. Ne jamais mettre à jour la map

**Erreur :** créer la map une fois au lancement et ne plus y toucher.

**Pourquoi c'est faux :** le paysage évolue. Ce qui était custom devient product. De nouveaux composants apparaissent (IA, nouvelles réglementations).

**Correction :**
- Dater chaque map
- Réviser tous les 6-12 mois
- Réviser à chaque pivot stratégique (levée de fonds, nouveau marché, refonte)

---

## 11. Utiliser la map comme diagramme d'architecture

**Erreur :** confondre Wardley Map et diagramme C4 / UML / architecture technique.

**Différences :**

| Wardley Map | Diagramme d'architecture |
|-------------|-------------------------|
| Orientée stratégie | Orientée implémentation |
| Axe d'évolution | Pas d'axe d'évolution |
| Composants = capacités | Composants = services/modules |
| But : décider build/buy | But : documenter le système |
| 10-15 éléments | Autant que nécessaire |

**Correction :** utilisez les deux, mais pour des objectifs différents. La Wardley Map précède les choix techniques.

---

## 12. Outsourcer le cœur métier

**Erreur :** confier à un prestataire le développement de l'algorithme ou de la logique qui constitue l'avantage compétitif.

**Pourquoi c'est faux :** le savoir-faire part avec le prestataire. Le différenciateur doit rester en interne.

**Correction :** outsourcez le **custom non différenciant** (back-office, CRUD admin, refonte UI). Gardez le **genesis/custom haut** en interne.

---

## Checklist anti-erreurs

Avant de finaliser votre map, vérifiez :

- [ ] J'ai un utilisateur principal clairement identifié
- [ ] Mes besoins sont en langage métier (pas technique)
- [ ] J'ai 10-20 composants (pas 50)
- [ ] Mes composants sont des capacités (pas des technos)
- [ ] J'ai marqué le mouvement des composants clés
- [ ] Je n'ai rien en « Build » en bas-droite
- [ ] J'ai impliqué au moins une autre personne dans la création
- [ ] J'ai daté la map et planifié une révision

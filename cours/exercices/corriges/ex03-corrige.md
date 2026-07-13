# Corrigé — Exercice 3 — Build / Buy / Outsource

## Question 1 — Décisions rapides

| # | Composant | Décision | Justification |
|---|-----------|----------|---------------|
| 1 | Moteur de parcours adaptatif | **Build** | Genesis, haut de la map — c'est le différenciateur EdTech, le cœur de la proposition de valeur |
| 5 | Authentification / SSO | **Buy** | Commodity — Auth0, Firebase Auth ou Clerk, ne jamais construire |
| 8 | Chatbot tuteur IA | **Build** (avec API) | Genesis, haut — différenciant, mais construire sur des API existantes (OpenAI, Anthropic), pas from scratch |
| 10 | Hébergement / infra | **Buy** | Commodity — AWS, GCP ou Railway, aucune raison d'opérer soi-même |

**Note sur le chatbot (#8) :** « Build » ici signifie construire la logique métier du tuteur (prompts, contexte pédagogique, intégration au parcours) en s'appuyant sur une API IA (Buy). On ne construit pas son propre modèle de langage.

---

## Question 2 — Grille pour Analytics d'apprentissage (#7)

| # | Critère | Évaluation | Oriente vers |
|---|---------|------------|--------------|
| 1 | Différenciation métier | **Partiellement** — les analytics basiques sont communs, mais l'analyse adaptative liée au parcours (#1) est différenciante | Build pour la partie adaptative |
| 2 | Stade d'évolution | **Custom** — des dashboards existent (Mixpanel, Amplitude) mais pas l'analyse pédagogique adaptative | Build pour le custom, Buy pour le tracking de base |
| 3 | Coût total (3 ans) | Build : ~3 semaines dev + maintenance / Buy (Mixpanel) : ~300€/mois = ~10 800€ | Build la partie custom, Buy le tracking |
| 4 | Compétences internes | **Partiellement** — l'équipe backend peut construire l'API analytics, mais pas de data engineer | Build léger + Buy pour le stockage/visualisation |
| 5 | Risque de lock-in | **Moyen** si Mixpanel / **Faible** si on stocke dans sa propre BDD | Préférer stockage interne + outil de viz |
| 6 | Conformité | **Modérée** — données d'apprentissage personnelles (RGPD) | Héberger les données soi-même |
| 7 | Time-to-market | **Normal** — pas bloquant pour le lancement | Build possible |

**Décision : Build (hybride)**

- **Buy** Mixpanel ou Posthog pour le tracking d'événements basique
- **Build** la couche d'analyse adaptative qui connecte les analytics au moteur de parcours (#1)
- Justification : le tracking basique est une commodité, mais l'analyse pédagogique personnalisée est liée au différenciateur

---

## Question 3 — Cas limites

### a) Back-office admin (#9) — Outsource

**Décision : Outsource**

Justification :
- Le back-office est en zone Custom mais **non différenciant** — les utilisateurs ne le voient pas
- L'équipe frontend est surchargée (lecteur vidéo prioritaire)
- Un prestataire peut livrer un CRUD admin en 2-3 semaines avec React Admin ou Retool
- L'équipe interne se concentre sur le moteur de parcours (#1) et le chatbot (#8)

**Risque à mitiger :** documenter l'API admin pour la maintenance future.

### b) Chatbot tuteur IA (#8) — Adapter la stratégie

**Décision : Build rapide sur API (Buy l'IA, Build le métier) — accélérer**

Justification :
- Le composant passe de Genesis à Custom/Product — le mouvement est rapide
- Le concurrent a validé le marché — le besoin est réel
- Construire sur l'API OpenAI/Anthropic (Buy) + couche métier pédagogique (Build) = 2-3 semaines
- Ne PAS construire son propre modèle IA (ce serait du Genesis pur, trop coûteux)
- **Ne pas attendre** — le mouvement rapide signifie que dans 1 an, ce sera banal

**Action :** lancer un MVP chatbot en 3 semaines, itérer sur la qualité pédagogique (le vrai différenciateur).

### c) Streaming vidéo (#6) — Buy (Vimeo OTT)

**Décision : Buy (Vimeo OTT ou équivalent)**

Justification :
- 500€/mois vs 2 mois de dev (coût opportunité : 2 devs × 2 mois = bien plus que 500€/mois sur 1 an)
- Le streaming vidéo est en Product — des solutions matures existent (Vimeo, Mux, Cloudflare Stream)
- Construire avec AWS MediaConvert ajoute de la complexité ops (encodage, CDN, DRM) sans valeur
- Avec 4 mois avant le lancement, 2 mois de dev streaming retardent tout le projet
- **Coût sur 3 ans :** Vimeo ~18 000€ vs Build ~80 000€+ (salaires + maintenance)

**Alternative acceptable :** Mux ou Cloudflare Stream si le coût Vimeo est trop élevé à terme.

---

## Question 4 — Plan d'action

### 3 décisions prioritaires immédiates

| Priorité | Composant | Décision | Action concrète |
|----------|-----------|----------|-----------------|
| **P1** | Authentification (#5) | Buy | Intégrer Auth0 ou Clerk cette semaine — bloquant pour tout le reste |
| **P1** | Moteur de parcours adaptatif (#1) | Build | Démarrer le développement — c'est le différenciateur, le plus risqué |
| **P2** | Streaming vidéo (#6) | Buy | Choisir Vimeo OTT ou Mux et commencer l'intégration — bloquant pour le contenu |

### 3 composants à ne surtout pas construire

| Composant | Pourquoi ne pas construire | Alternative |
|-----------|---------------------------|-------------|
| **Authentification (#5)** | Commodity, risque sécurité, 3-4 semaines de dev inutiles | Auth0, Clerk, Firebase Auth |
| **Hébergement (#10)** | Commodity pure, ops non core | Railway, AWS, Fly.io |
| **Lecteur vidéo (#2)** | Product — des lecteurs existent (Video.js, Plyr, ou intégré à Vimeo) | Buy/intégrer un lecteur existant |

### Bonus — ce qu'il ne faut pas faire

- **Ne pas construire** son propre modèle IA pour le chatbot — utiliser des API
- **Ne pas auto-héberger** PostgreSQL — utiliser une BDD managée
- **Ne pas construire** un système de paiement — Stripe si monétisation

---

## Points clés à retenir

- La **zone de la map** oriente la décision, mais le **contexte** (équipe, délai, budget) affine
- **Buy + Build** est souvent la bonne combinaison : acheter les commodités, construire le différenciant
- Le **mouvement** accélère ou retarde les décisions : un genesis qui devient product rapidement = agir vite
- L'**outsource** est pertinent pour le custom non différenciant quand l'équipe est saturée

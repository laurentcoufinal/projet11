# Module 7 — Cas pratiques

**Durée estimée :** 45 minutes

## Objectifs

À la fin de ce module, vous saurez :

- Appliquer la méthode Wardley Map dans 3 contextes réels différents
- Comparer les décisions avant/après la cartographie
- Tirer des leçons transférables à votre propre projet

---

## Cas 1 — Startup MVP : « Tout construire » vs « S'appuyer sur l'existant »

### Contexte

**FitTrack** est une startup qui veut lancer une application de suivi fitness personnalisé. L'équipe : 2 développeurs, budget 200€/mois, lancement dans 3 mois.

Le CTO veut tout construire « pour garder le contrôle ».

### Map initiale (vision du CTO)

```text
                    Genesis    Custom      Product      Commodity
                 ┌──────────┬───────────┬────────────┬────────────┐
  Besoins        │          │[Suivre   │[Voir mes  │            │
                 │          │ mon      │ progrès]  │            │
                 │          │ activité]│            │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Métier         │          │[Algo     │[Dashboard│            │
                 │          │ personna-│ progrès]  │            │
                 │          │ lisation]│  BUILD    │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Technique      │          │[Auth     │[Notifs]   │[Email]     │
                 │          │  BUILD]  │  BUILD    │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Infra          │          │[BDD      │[Héberge-  │            │
                 │          │  BUILD]  │ ment BUILD│            │
                 └──────────┴───────────┴────────────┴────────────┘
```

**Problème :** tout est en « BUILD » — estimation : 8-10 mois, pas 3.

### Map corrigée (après Wardley Mapping)

```text
                    Genesis    Custom      Product      Commodity
                 ┌──────────┬───────────┬────────────┬────────────┐
  Besoins        │          │[Suivre   │[Voir mes  │            │
                 │          │ mon      │ progrès]  │            │
                 │          │ activité]│            │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Métier         │          │[Algo     │[Dashboard│            │
                 │          │ personna-│ progrès]  │            │
                 │          │ lisation]│  BUILD    │            │
                 │          │  BUILD   │           │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Technique      │          │           │[Auth0]    │[SendGrid]  │
                 │          │           │[BUY]     │[BUY]       │
                 ├──────────┼───────────┼────────────┼────────────┤
  Infra          │          │           │[Supabase] │[Railway]   │
                 │          │           │[BUY]      │[BUY]       │
                 └──────────┴───────────┴────────────┴────────────┘
```

### Décisions prises

| Composant | Avant | Après | Gain |
|-----------|-------|-------|------|
| Auth | Build (4 sem.) | Buy Auth0 (2 jours) | 3,5 semaines |
| Notifications | Build (2 sem.) | Buy Firebase (1 jour) | 2 semaines |
| Email | Build (1 sem.) | Buy SendGrid (1 jour) | 1 semaine |
| BDD | Build (1 sem.) | Buy Supabase (1 jour) | 1 semaine |
| Hébergement | Build (2 sem.) | Buy Railway (1 jour) | 2 semaines |
| Algo personnalisation | Build | Build (inchangé) | — |
| Dashboard | Build | Build (inchangé) | — |

**Résultat :** lancement en 3 mois au lieu de 8. Budget infra : 150€/mois.

### Leçons

- Un MVP ne doit construire **que le différenciateur** (algo de personnalisation)
- Tout le reste en bas-droite = Buy sans discussion
- « Garder le contrôle » sur l'auth est une illusion coûteuse

---

## Cas 2 — Scale-up : Remplacer le custom par du Product

### Contexte

**DataPipe** est une scale-up (30 personnes, 5M€ ARR) qui a construit son propre **moteur de recherche** il y a 3 ans (Elasticsearch auto-hébergé + couche custom). L'équipe de 3 ingénieurs dédiée coûte 300K€/an à maintenir.

### Map actuelle

```text
                    Genesis    Custom      Product      Commodity
                 ┌──────────┬───────────┬────────────┬────────────┐
  Besoins        │          │           │[Rechercher│            │
                 │          │           │ des données│            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Métier         │          │           │[Filtres  │            │
                 │          │           │ avancés]  │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Technique      │          │[Moteur    │           │            │
                 │          │ recherche │           │            │
                 │          │ CUSTOM    │           │            │
                 │          │ 3 ing.    │           │            │
                 │          │     →     │           │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Infra          │          │[ES cluster│           │            │
                 │          │ CUSTOM]   │           │            │
                 └──────────┴───────────┴────────────┴────────────┘
```

**Le mouvement `→`** indique que le moteur de recherche custom évolue vers Product (Algolia, Meilisearch, Elasticsearch managé).

### Map cible

```text
                    Genesis    Custom      Product      Commodity
                 ┌──────────┬───────────┬────────────┬────────────┐
  Besoins        │          │           │[Rechercher│            │
                 │          │           │ des données│            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Métier         │          │           │[Filtres  │            │
                 │          │           │ avancés]  │            │
                 │          │           │  BUILD    │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Technique      │          │           │[Meilisearch│           │
                 │          │           │  BUY]     │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Infra          │          │           │           │[ES Cloud]  │
                 │          │           │           │[BUY]       │
                 └──────────┴───────────┴────────────┴────────────┘
```

### Décisions prises

| Action | Détail | Impact |
|--------|--------|--------|
| Migrer vers Meilisearch Cloud | Remplacer le cluster ES custom | -2 ingénieurs recherche réaffectés |
| Garder les filtres avancés en Build | Logique métier spécifique au domaine | Différenciation préservée |
| Libérer 200K€/an | Coût Meilisearch ~100K€/an vs 300K€ maintenance | Budget réinvesti dans le produit |

### Leçons

- Ce qui était un avantage (custom) devient un **boulet** quand le marché mature
- La map révèle le **mouvement** : agir avant que le coût de migration augmente
- Libérer les ressources des commodités pour réinvestir dans le différenciateur

---

## Cas 3 — Legacy : Cartographier la dette et prioriser la migration

### Contexte

**BankSoft** est un éditeur de logiciel bancaire vieux de 15 ans. Monolithe Java, base Oracle, pas de CI/CD, déploiements manuels. L'équipe veut moderniser mais ne sait pas par où commencer.

### Map de l'existant

```text
                    Genesis    Custom      Product      Commodity
                 ┌──────────┬───────────┬────────────┬────────────┐
  Besoins        │          │           │[Gérer    │            │
                 │          │           │ comptes]  │            │
                 │          │           │[Virements]│            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Métier         │          │[Moteur   │[Interface│            │
                 │          │ règles   │ web      │            │
                 │          │ bancaire │ legacy]  │            │
                 │          │ CUSTOM]  │          │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Technique      │          │[Auth     │           │            │
                 │          │ session  │           │            │
                 │          │ CUSTOM]  │           │            │
                 ├──────────┼───────────┼────────────┼────────────┤
  Infra          │          │[Oracle   │[Serveurs │            │
                 │          │ CUSTOM]  │ physiques│            │
                 │          │          │ CUSTOM]  │            │
                 └──────────┴───────────┴────────────┴────────────┘
```

**Constat :** tout est en Custom, beaucoup devrait être en Product/Commodity.

### Plan de migration (map cible, par phases)

**Phase 1 (3 mois) — Quick wins :**

| Composant | Action | De → Vers |
|-----------|--------|-----------|
| Auth session custom | Buy Auth0 + OIDC | Custom → Product |
| Serveurs physiques | Buy cloud (AWS) | Custom → Commodity |
| CI/CD (inexistant) | Buy GitHub Actions | Rien → Product |

**Phase 2 (6 mois) — Migration données :**

| Composant | Action | De → Vers |
|-----------|--------|-----------|
| Oracle | Buy PostgreSQL managé (RDS) | Custom → Commodity |
| Interface web legacy | Outsource refonte React | Custom → Product |

**Phase 3 (12 mois) — Cœur métier :**

| Composant | Action | De → Vers |
|-----------|--------|-----------|
| Moteur de règles bancaire | Build progressivement (strangler fig) | Custom → Custom (modernisé) |
| Interface web | Build (reprise de l'outsource) | Product → Product (maîtrisé) |

### Priorisation

```text
Impact élevé + Effort faible = FAIRE EN PREMIER
├── Auth → Auth0 (sécurité critique, effort faible)
├── CI/CD → GitHub Actions (qualité, effort faible)
└── Hébergement → Cloud (coût, effort moyen)

Impact élevé + Effort élevé = PLANIFIER
├── Oracle → PostgreSQL (risque données, effort élevé)
└── Interface web → Refonte (UX, effort élevé)

Impact faible = NE PAS FAIRE MAINTENANT
└── Moteur de règles (fonctionne, custom justifié)
```

### Leçons

- La map du legacy **révèle** ce qui devrait déjà être en commodity
- Migrer par **phases** : infra d'abord, données ensuite, métier en dernier
- Le moteur de règles bancaire reste en Custom (justifié) — ne pas tout migrer aveuglément
- L'outsource est utile pour la refonte UI (custom non différenciant visuellement)

---

## Synthèse transversale

| Cas | Situation | Erreur initiale | Décision clé | Résultat |
|-----|-----------|-----------------|--------------|----------|
| FitTrack (MVP) | Tout construire | Sur-développement | Buy les commodités | Lancement 3 mois au lieu de 8 |
| DataPipe (scale-up) | Custom devenu banal | Ignorer le mouvement | Migrer vers Meilisearch | 200K€/an économisés |
| BankSoft (legacy) | Tout en custom | Pas de priorisation | Migrer par phases | Modernisation structurée |

### Questions à vous poser

Après ces 3 cas, appliquez à votre projet :

1. **Construisez-vous des choses qui existent déjà en Product/Commodity ?** (cas FitTrack)
2. **Maintenez-vous du custom qui a migré vers Product ?** (cas DataPipe)
3. **Avez-vous une vision par phases de votre modernisation ?** (cas BankSoft)

## Résumé du cours

Vous avez maintenant tous les outils pour :

1. **Cartographier** votre application (modules 2-4)
2. **Lire** une map existante (module 3)
3. **Décider** build / buy / outsource (module 5)
4. **Appliquer** sur votre projet (module 6)
5. **Vous inspirer** de cas réels (module 7)

**Prochaine étape :** remplissez votre [fiche application](templates/fiche-application.md) et réalisez l'[atelier](06-atelier-votre-application.md).

## Annexes

- [Glossaire](annexes/glossaire.md)
- [Erreurs fréquentes](annexes/erreurs-frequentes.md)
- [Ressources complémentaires](annexes/ressources.md)

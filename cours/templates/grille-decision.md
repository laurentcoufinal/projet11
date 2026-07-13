# Template — Grille de décision Build / Buy / Outsource

Utilisez ce template pour chaque composant en **zone d'arbitrage** (milieu de la map).

---

## Composant évalué

| Champ | Valeur |
|-------|--------|
| **Nom du composant** | _[ex. Système de notifications]_ |
| **Besoin associé** | _[ex. Informer l'utilisateur en temps réel]_ |
| **Position sur la map** | Vertical : _[Haut / Milieu / Bas]_ — Horizontal : _[Genesis / Custom / Product / Commodity]_ |
| **Date d'évaluation** | _[JJ/MM/AAAA]_ |

## Évaluation des 7 critères

| # | Critère | Évaluation | Oriente vers |
|---|---------|------------|--------------|
| 1 | **Différenciation métier** — Ce composant est-il un avantage concurrentiel ? | ☐ Oui ☐ Non | Oui → Build / Non → Buy-Outsource |
| 2 | **Stade d'évolution** — Genesis/Custom ou Product/Commodity ? | ☐ Genesis ☐ Custom ☐ Product ☐ Commodity | Gauche → Build / Droite → Buy |
| 3 | **Coût total (3 ans)** — Build + maintenance vs SaaS vs prestataire ? | Build : _[€]_ / Buy : _[€]_ / Outsource : _[€]_ | Le moins cher n'est pas toujours le bon choix |
| 4 | **Compétences internes** — L'équipe maîtrise-t-elle cette techno ? | ☐ Oui ☐ Partiellement ☐ Non | Oui → Build possible / Non → Buy-Outsource |
| 5 | **Risque de lock-in** — Peut-on changer de fournisseur ? | ☐ Faible ☐ Moyen ☐ Élevé | Élevé sur composant critique → prudence |
| 6 | **Conformité / sécurité** — Données sensibles, RGPD, secteur régulé ? | ☐ Aucune contrainte ☐ Contrainte modérée ☐ Contrainte forte | Forte → Build ou fournisseur certifié |
| 7 | **Time-to-market** — Délai pour livrer ? | ☐ Urgent (< 1 mois) ☐ Normal (1-3 mois) ☐ Long (> 3 mois) | Urgent → Buy |

## Mouvement anticipé

| Question | Réponse |
|----------|---------|
| Ce composant va-t-il évoluer vers la droite ? | ☐ Non ☐ Lent (3-5 ans) ☐ Rapide (1-2 ans) |
| Si oui, vers quel stade ? | _[Product / Commodity]_ |
| Impact sur la décision ? | _[ex. Ne pas investir massivement, préparer la transition]_ |

## Décision

| Champ | Valeur |
|-------|--------|
| **Décision** | ☐ Build ☐ Buy ☐ Outsource ☐ Don't build |
| **Solution retenue** | _[ex. Firebase Cloud Messaging]_ |
| **Justification** | _[2-3 phrases expliquant le choix]_ |
| **Risques identifiés** | _[ex. Dépendance Google, limites du plan gratuit]_ |
| **Plan de mitigation** | _[ex. Abstraire derrière une interface NotificationService]_ |
| **Date de révision** | _[JJ/MM/AAAA — réévaluer dans 6 mois]_ |

---

## Tableau récapitulatif (pour tous les composants)

| Composant | Zone map | Décision | Solution | Priorité |
|-----------|----------|----------|----------|----------|
| _[Nom]_ | _[Haut-Custom]_ | _[Build]_ | _[Interne]_ | _[P1]_ |
| _[Nom]_ | _[Bas-Commodity]_ | _[Buy]_ | _[AWS S3]_ | _[P2]_ |
| _[Nom]_ | _[Milieu-Custom]_ | _[Outsource]_ | _[Agence X]_ | _[P3]_ |
| | | | | |
| | | | | |

**Légende priorité :** P1 = critique / P2 = important / P3 = peut attendre

# Exercice 3 — Build / Buy / Outsource

**Module associé :** [Module 5 — Décisions technologiques](../05-decisions-technologiques.md)  
**Durée estimée :** 30 minutes  
**Niveau :** Intermédiaire

## Contexte

Vous êtes tech lead d'une **startup EdTech** qui développe une plateforme de formation en ligne pour les professionnels. L'équipe compte 4 développeurs (2 backend, 1 frontend, 1 fullstack). Budget limité, lancement prévu dans 4 mois.

Voici les composants identifiés sur votre Wardley Map, avec leur position :

| # | Composant | Besoin associé | Vertical | Horizontal |
|---|-----------|----------------|----------|------------|
| 1 | Moteur de parcours adaptatif | Personnaliser la formation | Haut | Genesis |
| 2 | Lecteur vidéo interactif | Suivre un cours vidéo | Haut | Product |
| 3 | Système de quiz / évaluation | Valider ses acquis | Haut | Product |
| 4 | Génération de certificats | Obtenir une certification | Milieu | Product |
| 5 | Authentification / SSO | Se connecter | Bas | Commodity |
| 6 | Streaming vidéo | Héberger les vidéos de cours | Bas | Product |
| 7 | Analytics d'apprentissage | Mesurer la progression | Milieu | Custom |
| 8 | Chatbot tuteur IA | Poser des questions au tuteur | Haut | Genesis |
| 9 | Back-office admin | Gérer les cours et utilisateurs | Milieu | Custom |
| 10 | Hébergement / infra | Faire tourner l'application | Bas | Commodity |

## Questions

### Question 1 — Décisions rapides

Pour les composants en zone **évidente** (haut-gauche ou bas-droite), indiquez directement la décision :

| # | Composant | Décision | Justification (1 phrase) |
|---|-----------|----------|---------------------------|
| 1 | Moteur de parcours adaptatif | | |
| 5 | Authentification / SSO | | |
| 8 | Chatbot tuteur IA | | |
| 10 | Hébergement / infra | | |

### Question 2 — Grille de décision complète

Pour le composant **Analytics d'apprentissage** (#7, zone d'arbitrage), remplissez la grille complète en utilisant le [template](../templates/grille-decision.md).

### Question 3 — Cas limites

Pour chaque situation, choisissez la meilleure décision et justifiez :

**a)** Le **back-office admin** (#9) : l'équipe frontend est déjà surchargée par le lecteur vidéo. Faut-il Build, Buy ou Outsource ?

**b)** Le **chatbot tuteur IA** (#8) : un concurrent vient de lancer une fonctionnalité similaire basée sur l'API OpenAI. Le composant passe de Genesis à Custom/Product. Que faites-vous ?

**c)** Le **streaming vidéo** (#6) : Vimeo OTT coûte 500€/mois, construire avec AWS MediaConvert coûterait 2 mois de dev. Que choisissez-vous ?

### Question 4 — Plan d'action

Identifiez les **3 décisions prioritaires** à prendre immédiatement et les **3 composants à ne surtout pas construire**.

## Livrable

- Tableaux remplis pour les questions 1 et 2
- Réponses argumentées pour la question 3
- Plan d'action pour la question 4

## Correction

→ [Corrigé de l'exercice 3](corriges/ex03-corrige.md)

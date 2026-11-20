# Human-Activity-Recognition-UCI-HAR-MLP : étude progressive de réseaux MLP

## Contexte

On cherche à reconnaître l'activité d'une personne à partir des capteurs de son smartphone. Le jeu de données est *Human Activity Recognition Using Smartphones* (UCI) : 30 volontaires ont porté un téléphone à la taille en réalisant six activités, pendant que l'accéléromètre et le gyroscope enregistraient leurs mouvements à 50 Hz.

L'objectif du projet n'est pas d'obtenir la meilleure accuracy possible. Il s'agit de comprendre comment la taille du réseau, les fonctions d'activation, les optimiseurs et la régularisation influencent les performances, en suivant une méthode rigoureuse.

## Données

- Une ligne correspond à une fenêtre de 2,56 s (128 mesures, avec 50 % de chevauchement), décrite par 561 caractéristiques calculées à partir des signaux.
- Cible : `Activity`, six classes (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING).
- `subject` identifie le volontaire. Cette colonne ne sert pas d'entrée au modèle : elle sert uniquement à découper les données.
- `train.csv` contient 21 volontaires, `test.csv` en contient 9 autres. Le modèle est donc évalué sur des personnes qu'il n'a jamais vues.

Source : [Kaggle, UCI ML Human Activity Recognition](https://www.kaggle.com/datasets/uciml/human-activity-recognition-with-smartphones)

## Démarche

1. **Validation par volontaires.** Quelques volontaires entiers de `train.csv` sont mis de côté pour la validation. Comme les fenêtres consécutives se chevauchent, un tirage aléatoire de lignes donnerait une validation trop optimiste.
2. **Référence simple.** Une régression logistique multiclasse sert de point de comparaison pour tous les réseaux.
3. **Plusieurs graines.** Les comparaisons importantes sont répétées avec plusieurs graines aléatoires et reportées en moyenne ± écart-type. Un écart inférieur à cette variabilité n'est pas interprété.
4. **Test utilisé une seule fois**, à la fin, sur les configurations retenues.

Métriques : accuracy, F1 macro et par classe, matrice de confusion.

## Structure du repository

```
.
├── data/
│   └── raw_har_data/        # train.csv et test.csv (non versionnés)
├── notebooks/
├── README.md
└── requirements.txt
```

## Avancement

- [x] Mise en place du dépôt, de l'environnement et des données
- [x] Étape 1 : exploration des données et choix du prétraitement
- [x] Étape 2 : découpage train / validation par volontaires
- [x] Étape 3 : régression logistique de référence
- [x] Étape 4 : MLP à une couche cachée (activations, optimiseurs, pas d'apprentissage)
- [x] Étape 5 : variabilité entre graines
- [x] Étape 6 : largeur et profondeur du réseau
- [ ] Étape 7 : régularisation (dropout, weight decay, batch normalization, early stopping)
- [ ] Étape 8 : courbes d'apprentissage
- [ ] Étape 9 : évaluation sur le test et matrice de confusion
- [ ] Étape 10 : t-SNE et UMAP sur la dernière couche cachée
- [ ] Étape 11 : ouvertures (optionnel)
- [ ] Rapport (6 pages maximum)

## Résultats

À compléter au fil des étapes.

## Auteur

Asma BAHRINI M2 MALIA .
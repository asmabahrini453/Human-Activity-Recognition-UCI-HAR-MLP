# Reconnaissance d'activités humaines (UCI HAR) : étude progressive de MLP

Classification de 6 activités (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING) à partir de 561 caractéristiques issues des capteurs d'un smartphone (fenêtres de 2,56 s). Le jeu de test contient des volontaires absents de l'entraînement.

## Méthode

- Découpage **par volontaires** (jamais par lignes) : 16 volontaires pour l'entraînement, 5 pour la validation (`data/split_volontaires.json`).
- Référence : régression logistique.
- Choix des modèles par validation croisée groupée par volontaire (5 partitions) et plusieurs graines (moyenne ± écart-type).
- Le **jeu de test n'est utilisé que pour l'évaluation finale**, jamais pour choisir un modèle ni un hyperparamètre.

## Structure

```
.
├── data/
│   ├── raw_har_data/          # train.csv, test.csv (à télécharger, voir ci-dessous)
│   ├── processed_har_data/    # données standardisées (générées par V1)
│   └── split_volontaires.json # volontaires de validation (généré par V1)
├── notebooks/
│   ├── charte_graphique.py          # couleurs et style des figures
│   ├── V1_une_couche_cachee.ipynb   # exploration, découpage, référence, MLP à une couche
│   └── V2_reseau_profond.ipynb      # largeur/profondeur, régularisation, test final, interprétabilité
├── results/                   # tableaux et caches (générés)
├── requirements.txt
└── README.md
```

## Contenu des notebooks

**V1 : une couche cachée**
1. Exploration des données
2. Découpage par volontaires, standardisation, régression logistique de référence
3. MLP à une couche cachée : pas d'apprentissage, activations × optimiseurs, analyse par classe, variabilité entre graines
4. Courbes d'apprentissage et évaluation finale sur le test

**V2 : réseau profond**
1. Largeur et profondeur
2. Régularisation : dropout, weight decay, BatchNorm, arrêt précoce et combinaisons (validation croisée par volontaires)
3. Courbes d'apprentissage et évaluation finale sur le test
4. Interprétabilité : t-SNE et UMAP sur l'espace latent, silhouette, comparaison avec les matrices de confusion

## Installation

pip install -r requirements.txt

## Données

Télécharger le jeu de données sur Kaggle :
https://www.kaggle.com/datasets/uciml/human-activity-recognition-with-smartphones

Placer `train.csv` et `test.csv` dans `data/raw_har_data/`.

## Exécution

1. Ouvrir les notebooks dans VS Code 
2. Lancer **V1 en premier** (*Restart & Run All*) : il crée `data/processed_har_data/` et `data/split_volontaires.json`, dont V2 a besoin.
3. Lancer ensuite **V2** (*Restart & Run All*).

Remarques :
- Les graines sont fixées (0 à 4) : les résultats sont reproductibles.
- Les calculs longs sont mis en cache dans `results/`. Supprimer ces fichiers force le recalcul complet, qui peut prendre plusieurs dizaines de minutes (surtout la partie régularisation de V2).
- Si `results/test_final_v1.csv` ou `results/test_final_v2.csv` existe, le test est simplement recalculé (résultats identiques).

## Résultats principaux (F1 macro sur le test)

| Modèle | F1 test |
|---|---|
| Régression logistique | 0,9555 |
| V1 : 1 couche (64) | 0,9435 ± 0,0035 |
| V2a : 2 couches (128, 64), BatchNorm + dropout | 0,9403 ± 0,0089 |
| V2b : 3 couches (256, 128, 64), BatchNorm + dropout + weight decay | 0,9512 ± 0,0075 |

Les différences entre MLP sont petites par rapport à la variabilité entre volontaires (écart-type ≈ 0,05 en validation croisée), et la régression logistique reste au moins aussi bonne. La confusion principale est SITTING ↔ STANDING.

-------------------------------------------------------------------------------------------------
M2 MALIA - BAHRINI Asma
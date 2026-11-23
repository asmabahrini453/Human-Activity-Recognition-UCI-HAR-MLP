# Reconnaissance d'activités humaines (UCI HAR) : étude progressive de MLP

Classification de 6 activités (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING) à partir de 561 caractéristiques issues des capteurs d'un smartphone (fenêtres de 2,56 s). Le jeu de test contient des volontaires absents de l'entraînement. En ouverture, un réseau convolutif 1D est aussi entraîné sur les signaux bruts des capteurs.

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
│   ├── Inertial Signals/      # signaux bruts, train/ et test/ (à télécharger, pour V3 seulement)
│   ├── processed_har_data/    # données standardisées (générées par V1)
│   └── split_volontaires.json # volontaires de validation (généré par V1)
├── notebooks/
│   ├── charte_graphique.py            # couleurs et style des figures
│   ├── V1_une_couche_cachee.ipynb     # exploration, découpage, référence, MLP à une couche
│   ├── V2_reseau_profond.ipynb        # largeur/profondeur, régularisation, test final, interprétabilité
│   └── V3_signaux_bruts_cnn1d.ipynb   # ouverture : CNN 1D sur signaux bruts (optionnel)
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

**V3 : ouverture, signaux bruts (optionnel)**
1. Chargement des signaux bruts (fenêtres de 128 mesures sur 9 canaux) et contrôle d'alignement avec `train.csv` / `test.csv`
2. CNN 1D (3 convolutions, BatchNorm, 24 838 paramètres) : validation sur les 5 volontaires, puis validation croisée groupée par volontaires
3. Évaluation finale sur le test (5 graines) et comparaison avec le MLP et la régression logistique

## Installation

```bash
pip install -r requirements.txt
```

## Données

- **V1 et V2** : télécharger `train.csv` et `test.csv` sur Kaggle (https://www.kaggle.com/datasets/uciml/human-activity-recognition-with-smartphones) et les placer dans `data/raw_har_data/`.
- **V3** : télécharger `UCI HAR Dataset.zip` sur le dépôt UCI (https://archive.ics.uci.edu/dataset/240) et copier les dossiers `Inertial Signals` de `train` et de `test` dans `data/Inertial Signals/train` et `data/Inertial Signals/test`. V3 lit les classes et les volontaires dans `train.csv` et `test.csv`.

## Exécution

1. Ouvrir les notebooks dans VS Code.
2. Lancer **V1 en premier** (*Restart & Run All*) : il crée `data/processed_har_data/` et `data/split_volontaires.json`, dont V2 et V3 ont besoin.
3. Lancer ensuite **V2**, puis **V3** (*Restart & Run All*).

Remarques :
- Les graines sont fixées (0 à 4) : les résultats sont reproductibles.
- Les calculs longs sont mis en cache dans `results/`. Supprimer ces fichiers force le recalcul complet, qui peut prendre plusieurs dizaines de minutes (surtout la partie régularisation de V2). V3 est plus court (quelques minutes).
- Si `results/test_final_v1.csv`, `test_final_v2.csv` ou `test_final_v3.csv` existe, le test est simplement recalculé (résultats identiques).

## Résultats principaux (F1 macro sur le test)

| Modèle | F1 test |
|---|---|
| Régression logistique | 0,9555 |
| V1 : 1 couche (64) | 0,9435 ± 0,0035 |
| V2a : 2 couches (128, 64), BatchNorm + dropout | 0,9403 ± 0,0089 |
| V2b : 3 couches (256, 128, 64), BatchNorm + dropout + weight decay | 0,9512 ± 0,0075 |
| V3 : CNN 1D sur signaux bruts | 0,9296 ± 0,0095 |

Les différences entre MLP sont petites par rapport à la variabilité entre volontaires (écart-type ≈ 0,05 en validation croisée), et la régression logistique reste au moins aussi bonne. Le CNN 1D égale les MLP en validation croisée mais reste en dessous sur le test. La confusion principale est SITTING ↔ STANDING.

## Sources

- Reyes-Ortiz, Anguita, Ghio, Oneto, Parra (2012). *Human Activity Recognition Using Smartphones*. UCI Machine Learning Repository. https://doi.org/10.24432/C54S4K
- Anguita, Ghio, Oneto, Parra, Reyes-Ortiz (2013). *A Public Domain Dataset for Human Activity Recognition Using Smartphones*. ESANN.

-------------------------------------------------------------------------------------------------
M2 MALIA - BAHRINI Asma
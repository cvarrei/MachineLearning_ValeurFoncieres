# Immo_TD

Pour un [projet orienté sur la programmation Python](https://github.com/asardell/M2-SISE-2023/blob/main/Roadmap.pdf) de notre Master 2 Statistique et Informatique pour la Science des données (SISE) de l'Université Lyon 2, nous avons réalisé une analyse approfondie des valeurs foncières en France de 2018 à 2021. Le but de l'exercice était de proposer un algorithme pour prédire les valeurs foncières de biens vendu en 2022. 

Ce projet a été réalisé par Adrien Castex, Victor Sigogneau et Clovis Varangot-Reille. 

Pour ce faire, nous avons décomposé le projet en différentes étapes: 
1. Exploration des données
2. Création de modèles pour prédire les valeurs foncières
3. Création d'un rapport d'analyse avec des statistiques descriptives des données et les variables majeurs pour les modèles.
4. Création d'un algorithme pour réaliser la prédiction
5. Déploiement en ligne d'une application Dash avec un dashboard et une possibilité de prédiction.

L'application peut se retrouver en ligne à l'adresse suivante: https://immopred-app.onrender.com/ . Le repository de l'application se trouve [ici](https://github.com/cvarrei/repo_test). Plus de détails sur l'application ainsi qu'une documentation utilisateur est présente dans le repository correspondant.


## Dossiers du Repository
1. [Documentation Technique](#documentation-technique)
2. [Datasets](#datasets)
3. [Notebooks](#notebooks)
4. [Modèles sauvegardés](#modèles-sauvegardés)
5. [Rapport d'Analyse](#rapport-danalyse)

## Documentation Technique

Vous pourrez trouver un document technique [ici](https://github.com/cvarrei/immo_TD/tree/main/Documentation%20Technique) présentant le schéma fonctionnel de preprocessing et modélisation des données. Pour une analyse plus approfondie, vous pourrez trouver les notebooks dans les sections correspondantes.

## Datasets

Dans ce dossier, vous trouverez les jeux de données originels (valeursfoncieres-2018.zip à valeursfoncieres-2021.zip). Ceux-ci sont les [ventes de biens réalisées entre 2018 et 2021 en France](https://github.com/asardell/M2-SISE-2023/tree/main/rawdata), des jeux de données de plusieurs millions d'obersvations chacun.  data_train, df_dash_dashboard et df_sansNantypelocal sont des versions nettoyés du dataset originel qui nous ont permis de réaliser différentes étapes pour ne pas à avoir à manipuler le dataset complet (trop gros pour être manipulé quotidiennement).

Nous y ajoutons des variables supplémentaires retrouvées principalement sur les open datasets du gouvernement français ou organismes nationaux: 
- [Les données géographiques des communes](https://github.com/asardell/M2-SISE-2023/blob/main/rawdata/communes-departement-region.csv)
- [Le nombre d'écoles élémentaires par département](https://www.observatoire-des-territoires.gouv.fr/nombre-decoles-elementaires)
- [Le salaire horaire moyen par département](https://www.insee.fr/fr/statistiques/2021266)
- [Le pourcentage de population active par département](https://www.insee.fr/fr/statistiques/2012710#titre-bloc-1)
- [Le prix au m2 et le nombre de ventes par communes aggrégés par département](https://www.data.gouv.fr/fr/datasets/indicateurs-immobiliers-par-commune-et-par-annee-prix-et-volumes-sur-la-periode-2014-2021/)

Nous avons également récupéré [les tracés de chaque region et département français](https://www.data.gouv.fr/fr/datasets/contours-des-communes-de-france-simplifie-avec-regions-et-departement-doutre-mer-rapproches/) sur le site d'opendata du gouvernement français pour faciliter la cartographie. 

## Notebooks

Dans [ce dossier](https://github.com/cvarrei/immo_TD/tree/main/Notebooks), vous retrouverez les différents notebooks qui nous ont permis de réaliser ce projet: 
- notebook_immo_explo: Ce notebook retrace notre processus de preprocessing, de nettoyage et d'exploration initiale. Toutefois une exploration plus détaillée est disponible dans notre rapport d'analyse.
- tree_typelocal: Ce notebook retrace la construction de l'algorithme de classification en cas d'absence d'étiquettage du type de bien.
- notebook_TYPELOCAL_modelisation: Ces quatres notebooks retrace notre processus de preprocessing et modélisation selon les différents types de locaux.
- submission_notebook: La partie modélisation s'est concrétisé par une compétition Kaggle sur un échantillon test qui représentait les ventes de biens de 2022. Ce notebook retrace donc tout le processus de traitement de l'échantillon test puis de prédiction.  

## Modèles sauvegardés

Dans [ce dossier](https://github.com/cvarrei/immo_TD/tree/main/Mod%C3%A8le%20ML), vous pourrez retrouver nos différents pipelines de préprocessing ayant appris sur nos échantillons d'apprentissage ainsi que les modèles de machine learning en format .pkl. Vous pourrez retrouver également notre modèle qui nous permet de classifier le type de bien avant la prédiction final de la valeur foncière en cas d'absence d'étiquettage.

## Rapport d'Analyse

Le [rapport d'analyse](https://github.com/cvarrei/immo_TD/tree/main/Rapport%20d'analyse) est un document pdf expliquant de manière textuelle et simplifiée le processus de préprocessing, puis d'analyse univariée et bivariée des variables présentes dans le dataset originelainsi que des variables open-data ajoutées. Il est complétée par une description rapide des variables importantes pour les différents modèles de prédiciton. Il est accompagné de sa version en JupyterNotebook ainsi que des plots en format png pour le notebook.

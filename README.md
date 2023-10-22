# Immo_TD

Pour un [projet orienté sur la programmation Python](https://github.com/asardell/M2-SISE-2023/blob/main/Roadmap.pdf) de notre Master 2 Statistique et Informatique pour la Science des données (SISE) de l'Université Lyon 2, nous avons réalisé une analyse approfondie des valeurs foncières en France de 2018 à 2021. Le but de l'exercice était de proposer un algorithme pour prédire les valeurs foncières de biens vendu en 2022. 

Ce projet a été réalisé par Adrien Castex, Victor Sigogneau et Clovis Varangot-Reille. 

Pour ce faire, nous avons décomposé le projet en différentes étapes: 
1. Exploration des données
2. Création de modèles pour prédire les valeurs foncières
3. Création d'un rapport d'analyse avec des statistiques descriptives des données et les variables majeurs pour les modèles.
4. Création d'un algorithme pour réaliser la prédiction
5. Déploiement en ligne d'une application Dash avec un dashboard et une possibilité de prédiction.

L'application peut se retrouver en ligne à l'adresse suivante: https://immopred-app.onrender.com/ . Le repository de l'application se trouve [ici](https://github.com/cvarrei/repo_test). 


## Table of Contents
1. [Documentation Technique](#documentation)
2. [Datasets](#datasets)
3. [Notebooks](#notebooks)
   - [Exploratory Analysis](#exploratory-analysis)
   - [Modélisations](#local-modelisation)
   - [Analysis Report](#analysis-report)
   - [Submission Notebook](#submission-notebook)
4. [Rapport d'Analyse](#rapport-analyse)

# Documentation Technique

Vous pourrez trouver un document technique [ici](https://github.com/cvarrei/immo_TD/blob/main/documentation_technique.pdf) présentant le schéma fonctionnel de preprocessing et modélisation des données. Pour une analyse plus approfondie, vous pourrez trouver les notebooks dans les sections correspondantes.

# Datasets

Dans ce dossier, vous trouverez les jeux de données originels (.......). Ceux-ci sont les [ventes de biens réalisées entre 2018 et 2021 en France](https://github.com/asardell/M2-SISE-2023/tree/main/rawdata), des jeux de données de plusieurs millions d'obersvations chacun. 
Nous y ajoutons des variables supplémentaires retrouvées principalement sur les open datasets du gouvernement français ou organismes nationaux: 
- [Les données géographiques des communes](https://github.com/asardell/M2-SISE-2023/blob/main/rawdata/communes-departement-region.csv)
- [Le nombre d'écoles élémentaires par département](https://www.observatoire-des-territoires.gouv.fr/nombre-decoles-elementaires)
- [Le salaire horaire moyen par département](https://www.insee.fr/fr/statistiques/2021266)
- [Le pourcentage de population active par département](https://www.insee.fr/fr/statistiques/2012710#titre-bloc-1)
- [Le prix au m2 et le nombre de ventes par communes aggrégés par département](https://www.data.gouv.fr/fr/datasets/indicateurs-immobiliers-par-commune-et-par-annee-prix-et-volumes-sur-la-periode-2014-2021/)

Nous avons également récupéré [les tracés de chaque region et département français](https://www.data.gouv.fr/fr/datasets/contours-des-communes-de-france-simplifie-avec-regions-et-departement-doutre-mer-rapproches/) sur le site d'opendata du gouvernement français pour faciliter la cartographie. 

# Rapport d'Analyse

Le rapport d'analyse est un document pdf expliquant de manière textuelle et simplifiée le processus de préprocessing, puis d'analyse univariée et bivariée des variables présentes dans le dataset originelainsi que des variables open-data ajoutées. Il est complétée par une description rapide des variables importantes pour les différents modèles de prédiciton. 

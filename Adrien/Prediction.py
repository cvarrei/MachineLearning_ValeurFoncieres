import pandas as pd
import sklearn
import os 
import pickle 



def preproc(nlot,tl,sr,nbpp,st,te,year,month,nom_region):
    # On importe la pipeline de preprocessing et le modèle de régression utilisé pour prédire le prix des dépendances.
    with open("immo_TD/Clovis/dependance_preprocessing.pkl", 'rb') as file_prep:
                preprocessing_dep = pickle.load(file_prep) 
    with open("immo_TD/Clovis/dependance_model.pkl", 'rb') as file_reg:
                regression_dep = pickle.load(file_reg)
    # On importe l'arbre de décision utilisé pour prédire le prix des locaux.
    with open("immo_TD/Clovis/local_model.pkl", 'rb') as file_reg:
                tree_local = pickle.load(file_reg)
    # On importe la pipeline de preprocessing et le modèle de régression utilisé pour prédire le prix des maisons.
    with open("immo_TD/Clovis/maison_preprocessing.pkl", 'rb') as file_prep:
                preprocessing_maison = pickle.load(file_prep)
    with open("immo_TD/Clovis/maison_model.pkl", 'rb') as file_reg:
                regression_maison = pickle.load(file_reg)
    # On importe la pipeline de preprocessing et le modèle de régression utilisé pour prédire le prix des appartements.
    with open("immo_TD/Clovis/appartement_preprocessing.pkl", 'rb') as file_prep:
                preprocessing_appartement = pickle.load(file_prep)
    with open("immo_TD/Clovis/appartement_model.pkl", 'rb') as file_reg:
                regression_appartement = pickle.load(file_reg)
    
    
    
    
    
    
    
    if(te=="y"):
        te=True
    else:
        te=False
    
    data=pd.DataFrame(list(nlot,tl,sr,nbpp,st,te,year,month,nom_region),columns=["Nombre de lots","Type local","Surface reelle bati","Nombre pieces principales","Surface terrain","exterieur","year","month","nom_region"])

    





    return data





def pred():





    predi=0




    return predi
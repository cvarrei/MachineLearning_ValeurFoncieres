from sklearn.base import TransformerMixin
import numpy as np

class Qual_Standardize(TransformerMixin):
        # On standardize les valeurs qualitatives en utilisant la racine carré de p_k.
        def __init__(self):
            self.p_k = None
        # Notre fit calcule la valeur p_k nécessaire à la transformation.
        def fit(self, X, y=None):
            qual_int = X.astype(int)
            # On calcule la valeur p_k comme la proportion de True dans la colonne
            self.p_k = np.sum(qual_int, axis=0) / qual_int.shape[0]
            return self
        def transform(self, X, y=None):
            qual_int = X.astype(int)    
            # On transforme chaque valeur du tableau disjonctif complet par la racine carré de p_k
            qual_trans = qual_int / (np.sqrt(self.p_k))

            return qual_trans
    
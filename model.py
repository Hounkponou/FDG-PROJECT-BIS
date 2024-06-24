def build_model(df):
    import pandas as pd
    from datetime import datetime
    from sklearn.neighbors import KNeighborsClassifier
    import numpy as np
    import io
    # Préparer les features et labels
    features = df[["jour_semaine", "semaine", "mois"]]
    labels = df[["boule_1", "boule_2", "boule_3", "boule_4", "boule_5", "etoile_1", "etoile_2"]]

    # Construire le modèle k-NN
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(features, labels)

    return knn
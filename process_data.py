def process_data(df):
    import pandas as pd
    from datetime import datetime
    from sklearn.neighbors import KNeighborsClassifier
    import numpy as np
    import io
    # Convertir la colonne date en datetime
    df["date_de_tirage"] = pd.to_datetime(df["date_de_tirage"], format='%d/%m/%Y',errors='coerce')
    #df["date_de_tirage"] = pd.to_datetime(df["date_de_tirage"], format='%d/%m/%Y', errors='coerce')
    # Pour les dates qui n'ont pas été converties (NaT), essayer un autre format
    #df["date_de_tirage"] = df["date_de_tirage"].fillna(pd.to_datetime(df["date_de_tirage"], format='%Y-%m-%d', errors='coerce'))
    # Extraire le jour de la semaine, le numéro de la semaine et le mois
    df["jour_semaine"] = df["date_de_tirage"].dt.dayofweek
    df["semaine"] = df["date_de_tirage"].dt.isocalendar().week
    df["mois"] = df["date_de_tirage"].dt.month

    return df
#%%

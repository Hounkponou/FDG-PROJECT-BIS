def load_data():
    import pandas as pd
    import io
    import os
    path = 'data/'
    file_list = []
    List = []

    for root, folders, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))

    for filename in file_list:
        df = pd.read_csv(filename, sep=";", encoding='latin-1')
        List.append(df)

    # Concaténer les fichiers pour créer le DataFrame final
    data = pd.concat(List, ignore_index=True)[['jour_de_tirage', 'date_de_tirage', 'boule_1', 'boule_2', 'boule_3', 'boule_4','boule_5', 'etoile_1','etoile_2']]

    return data

def recommend_numbers(knn, date):
    import pandas as pd
    from datetime import datetime
    from sklearn.neighbors import KNeighborsClassifier
    import numpy as np
    import io
    dates=pd.to_datetime(date, format='%d/%m/%Y')
    jour_semaine=dates.dayofweek
    semaine=dates.isocalendar().week
    mois=dates.month
    input_data = np.array([[jour_semaine, semaine, mois]])
    prediction = knn.predict(input_data)
    return prediction[0]
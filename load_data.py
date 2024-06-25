def load_data():
    import pandas as pd
    d1=pd.read_csv(r' euromillions_2_csv')
    d2=pd.read_csv(r'euromillions_201902.csv')
    d3=pd.read_csv(r'euromillions_202002.csv')
    data_list=[d1,d2,d3]
    # Concatenate the DataFrames to create the final DataFrame
    data = pd.concat(data_list, ignore_index=True)[['jour_de_tirage', 'date_de_tirage', 'boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5', 'etoile_1', 'etoile_2']]

    return data

# Example usage in Streamlit
#st.title('Load Data from GitHub')
#data = load_data()
#st.write(data)


def load_data():
    import pandas as pd
    import requests
    from io import StringIO
    import streamlit as st

    # Base URL for the raw files in the GitHub repository
    base_url = "https://github.com/Hounkponou/FDG-PROJECT-BIS/tree/main/data" #"https://raw.githubusercontent.com/Hounkponou/FDG-PROJECT-BIS/main/data/"
    
    
    # GitHub token (if accessing a private repository)
    github_token = st.secrets["github_token"]
    
    # List of file names in the repository
    file_names = [
        "euromillions_2.csv",
        "euromillions_201902.csv",
        "euromillions_202002.csv"
        # Add more file names as needed
    ]
    
    headers = {"Authorization": f"token {github_token}"}
    data_list = []

    # Download each file and read it into a DataFrame
    for file_name in file_names:
        url = base_url + file_name
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            csv_data = StringIO(response.text)
            df = pd.read_csv(csv_data, sep=";", encoding='latin-1')
            data_list.append(df)
        else:
            print(f"Failed to download {file_name} with status code {response.status_code}")

    # Concatenate the DataFrames to create the final DataFrame
    data = pd.concat(data_list, ignore_index=True)[['jour_de_tirage', 'date_de_tirage', 'boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5', 'etoile_1', 'etoile_2']]

    return data

# Example usage in Streamlit
#st.title('Load Data from GitHub')
#data = load_data()
#st.write(data)


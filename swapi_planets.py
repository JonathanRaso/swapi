#### Planets (fetching + data_to_df) Functions (Adil) ####

planets_data_set = []

def fetch_planets(uri):
    if requests.get(uri).status_code == 200:
        n_planets = requests.get(uri).json().get('count', 'key not found')
        print('Planets count fetching succeded')
    else:
        print('Planets number unknown/Request failed')
    for i in range(n_planets):
        r=requests.get(f'{uri}/{str(i+1)}')
        if r.status_code == 200:
            planets_data = r.json()
            planets_data_set.append(planets_data)
    print('All available planets data fetched and pushed to planets_data_set')

def transform_data(data_set):
    df = pd.DataFrame.from_dict(data_set)
    return df
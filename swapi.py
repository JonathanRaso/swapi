import requests
import pandas as pd

#### People Functions (Jonathan) ####

def fetch_swapi_people(index=1):
    people_api_url = f"https://swapi.dev/api/people/{index}/"
    
    response = requests.get(people_api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "Nothing fetched"
   
    
def create_people_dataframe():
    columns = ["name","height", "mass", 
               "hair_color", "skin_color", 
               "eye_color", "birth_year", "gender", "homeworld", "films", 
              "species", "vehicles", "starships", "created", "edited", "url"]
    people_df = pd.DataFrame(columns=columns)
    
    for i in range(1, 84):
        if fetch_swapi_people(i) == "Nothing fetched":
            continue
        else:    
            people = fetch_swapi_people(i)
            people_df.loc[i,'name'] = people["name"]
            people_df.loc[i,'height'] = people["height"]
            people_df.loc[i,'mass'] = people["mass"]
            people_df.loc[i,'hair_color'] = people["hair_color"]
            people_df.loc[i,'skin_color'] = people["skin_color"]
            people_df.loc[i,'eye_color'] = people["eye_color"]
            people_df.loc[i,'birth_year'] = people["birth_year"]
            people_df.loc[i,'gender'] = people["gender"]
            people_df.loc[i,'homeworld'] = people["homeworld"]
            people_df.loc[i,'films'] = people["films"]
            people_df.loc[i,'species'] = people["species"]
            people_df.loc[i,'vehicles'] = people["vehicles"]
            people_df.loc[i,'starships'] = people["starships"]
            people_df.loc[i,'created'] = people["created"]
            people_df.loc[i,'edited'] = people["edited"]
            people_df.loc[i,'url'] = people["url"]
        
    return people_df    
 
#### Starships Functions (Marianne) ####

def fetch_starships():
    uri = 'https://swapi.dev/api/starships/'
    myDict = {}
    data =[]
    pageMax = range(1,5)
    npage = 1
    for r in pageMax:
        myRequest = requests.get(uri+f"?page={npage}")
        if myRequest.status_code == 200:
            myDict[f"page{npage}"] = myRequest.json()
            data.append(myDict[f"page{npage}"]["results"])
        else:
            print("NO DATA")
            npage +=1
    return data

def transform_starships_data(data):
    columns = ['name','model','starship_class','manufacturer','cost_in_credits','length','crew','passengers','max_atmosphering_speed','hyperdrive_rating','MGLT','cargo_capacity','consumables','films','pilots','url','created','edited']
    starships_df = pd.DataFrame(columns=columns)
    indexDataFrame = 0
    for p in range (0,len(data)):
        for s in range(0,len(data[p])):
            starships_df.loc[indexDataFrame,'name'] = data[p][s]["name"]
            starships_df.loc[indexDataFrame,'model'] = data[p][s]["model"]
            starships_df.loc[indexDataFrame,'starship_class'] = data[p][s]["starship_class"]
            starships_df.loc[indexDataFrame,'manufacturer'] = data[p][s]["manufacturer"]
            starships_df.loc[indexDataFrame,'cost_in_credits'] = data[p][s]["cost_in_credits"]
            starships_df.loc[indexDataFrame,'length'] = data[p][s]["length"]
            starships_df.loc[indexDataFrame,'crew'] = data[p][s]["crew"]
            starships_df.loc[indexDataFrame,'passengers'] = data[p][s]["passengers"]
            starships_df.loc[indexDataFrame,'max_atmosphering_speed'] = data[p][s]["max_atmosphering_speed"]
            starships_df.loc[indexDataFrame,'hyperdrive_rating'] = data[p][s]["hyperdrive_rating"]
            starships_df.loc[indexDataFrame,'MGLT'] = data[p][s]["MGLT"]
            starships_df.loc[indexDataFrame,'cargo_capacity'] = data[p][s]["cargo_capacity"]
            starships_df.loc[indexDataFrame,'consumables'] = data[p][s]["consumables"]
            starships_df.loc[indexDataFrame,'films'] = data[p][s]["films"]
            starships_df.loc[indexDataFrame,'pilots'] = data[p][s]["pilots"]
            starships_df.loc[indexDataFrame,'url'] = data[p][s]["url"]
            starships_df.loc[indexDataFrame,'created'] = data[p][s]["created"]
            starships_df.loc[indexDataFrame,'edited'] = data[p][s]["edited"]
            indexDataFrame +=1
    return starships_df


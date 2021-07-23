# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:26:08 2021

@author: SImplon.co
"""
import requests
import pandas as pd

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
 
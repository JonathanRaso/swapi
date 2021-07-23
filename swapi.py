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
 
    
 
n_page = 4 
uri = "https://swapi.dev/api/vehicles"
    
url = uri
if n_page > 1 : 
    url = f"{uri}/?page={str(n_page)}"
url 


r = requests.get(url)

def fetch_vehicule(n_page):
    url = f"https://swapi.dev/api/vehicles"
    if n_page > 0 :
        url = f"{uri}/?page={str(n_page)}"
    r = requests.get(url)
    if r.status_code == 200 : 
        data = r.json()
        result_list = data["results"]
        return result_list
    else : 
        return None
    
vehicule_list = fetch_vehicule(1)
vehicule_list

columns = ["name" , "model" , "manufacturer" , "cost_in_credits" , "length" ,"max_atmosphering_speed" , "crew" , "passengers" , "cargo_capacity" , "consumables" , "vehicle_class" , "pilots"  ,"films"]
df = pd.DataFrame(columns=columns)
df

for i , row in enumerate(vehicule_list) :
    df.loc[i,"name"] = row["name"]
    df.loc[i,"model"] = row["model"]
    df.loc[i,"manufacturer"] = row["manufacturer"]
    df.loc[i,"cost_in_credits"] = row["cost_in_credits"]
    df.loc[i,"length"] = row["length"]
    df.loc[i,"max_atmosphering_speed"] = row["max_atmosphering_speed"]
    df.loc[i,"crew"] = row["crew"]
    df.loc[i,"passengers"] = row["passengers"]
    df.loc[i,"cargo_capacity"] = row["cargo_capacity"]
    df.loc[i,"consumables"] = row["consumables"]
    df.loc[i,"vehicle_class"] = row["vehicle_class"]
    df.loc[i,"pilots"] = row["pilots"]
    df.loc[i,"films"] = row["films"]
df   
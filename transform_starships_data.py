def transform_starships_data(data):
    import pandas as pd
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
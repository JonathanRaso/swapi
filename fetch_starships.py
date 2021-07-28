def fetch_starships():
    import requests
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

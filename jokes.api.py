import requests
def joke_genarator():
    try:
        url ="https://icanhazdadjoke.com"
        headers ={"Accept":"application/json"}
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        data  = response.json()

        return data
    except:
        print("the data fetching failed")
        return None

joke = joke_genarator()
clean = joke.get('joke')
if joke and clean:
    print(f"{clean}")


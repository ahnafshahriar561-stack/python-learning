import requests

name = input("enter name ")
def predict_age(name):

    try:
        url = "https://api.agify.io"
        params={"name":name}

        response = requests.get(url,params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except:
        print("data can't be fetched")

result = predict_age(name)
if result and result.get('age'):
    age = result.get('age')
    print(f" {name} is {age} year old")
else:
    print(f"the age for{name} is not availabe")

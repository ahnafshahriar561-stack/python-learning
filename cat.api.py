import requests
url="https://catfact.ninja/fact"
find = requests.get(url)
def get():
    if find.status_code == 200:
        d = find.json()
        return d
    else:
        print("data fetching failed")
k = get()
print(f"{k}")
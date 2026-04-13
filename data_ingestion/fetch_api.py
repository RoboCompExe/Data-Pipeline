import requests

def fetch_data():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    data = fetch_data()
    print(data)

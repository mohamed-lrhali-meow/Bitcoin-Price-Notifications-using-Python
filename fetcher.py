import requests

def get_prices(coins):
    try:
        ids = ",".join(coins.keys())
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
        
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print("Error fetching data")
            return None
        
        data = response.json()
        
        return {coin: data[coin]["usd"] for coin in coins}
    
    except Exception as e:
        print("Error:", e)
        return None
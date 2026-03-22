import time
import json
import schedule
from fetcher import get_prices
from monitor import check_prices

with open("config.json") as f:
    config = json.load(f)

coins = config["coins"]
interval = config["interval"]

def job():
    prices = get_prices(coins)
    check_prices(prices, coins)

job()

schedule.every(interval).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
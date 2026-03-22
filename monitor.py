from notifier import send_notification

last_alert = {}

def check_prices(prices, coins):
    global last_alert

    if prices is None:
        return

    if not last_alert:
        last_alert = {coin: None for coin in coins}

    for coin, price in prices.items():
        high = coins[coin]["high"]
        low = coins[coin]["low"]

        print(f"{coin.upper()}: ${price}")

        if price > high and last_alert[coin] != "high":
            last_alert[coin] = "high"
            send_notification(f"{coin.upper()} above ${high}! Current: ${price}")

        elif price < low and last_alert[coin] != "low":
            last_alert[coin] = "low"
            send_notification(f"{coin.upper()} below ${low}! Current: ${price}")
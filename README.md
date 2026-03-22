# 🚀 Bitcoin Price Notifications

Hey there! 👋 

If you're like me and want to stay on top of your crypto without constantly checking prices, then this project is for you. I built this little app to send me notifications whenever Bitcoin or Ethereum crosses certain price thresholds I care about. No more Refreshing, just real-time alerts!

## 💡 What Does It Do?

This app monitors crypto prices 24/7 and sends you Windows notifications when:
- Bitcoin goes **above** or **below** your set limits
- Ethereum goes **above** or **below** your set limits

Perfect for catching those market moves without staring at a screen all day.

## 📦 Installation

1. Clone this repo:
```bash
git clone https://github.com/yourusername/bitcoin-price-notifications.git
cd bitcoin-price-notifications
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

## ⚙️ Setup

Edit `config.json` to set your own price thresholds:

```json
{
    "interval": 1,
    "coins": {
        "bitcoin": { "high": 69000, "low": 68000 },
        "ethereum": { "high": 4000, "low": 3000 }
    }
}
```

- **interval**: How often to check (in minutes)
- **high**: Send alert if price goes above this
- **low**: Send alert if price goes below this

## 🚀 Running It

Just run:
```bash
python main.py
```

That's it! The app will check prices every minute (or whatever interval you set) and notify you when things get interesting.

## 📁 Project Structure

```
.
├── main.py          # The main script that runs everything
├── fetcher.py       # Gets crypto prices from CoinGecko API
├── monitor.py       # Watches for price changes
├── notifier.py      # Sends you notifications
├── config.json      # Your custom price thresholds
└── README.md        # This file!
```

## 🔗 Credits

- Prices powered by [CoinGecko API](https://www.coingecko.com/api)
- Notifications using [win10toast](https://github.com/jalaxy/win10toast)

## 💬 Cool Features

✨ Smart alerts - only notifies you **once** per threshold cross (no spam!)
✨ Easy config - just edit JSON, no coding required
✨ Multiple coins - monitor Bitcoin, Ethereum, or add more!
✨ Lightweight - minimal resource usage

## 🎯 Future Ideas

- Support for more cryptocurrencies
- Email/SMS notifications
- Custom alert sounds
- Store price history in a database

## 📝 License

Do whatever you want with this. It's free!



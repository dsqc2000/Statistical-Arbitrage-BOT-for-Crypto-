"""
    API Documentation
    https://bybit-exchange.github.io/docs/linear/#t-introduction
"""

# API Imports
from pybit import usdt_perpetual
from pybit import HTTP

# CONFIG
mode = "test"
timeframe = 60
kline_limit = 200
z_score_window = 21

# LIVE API
api_key_mainnet = ""
api_secret_mainnet = ""

# TEST API
api_key_testnet = "4OHe8BW78quRIcSAwo"
api_secret_testnet = "ooYY2yCpj3qrBYRtsAxZBsuF45dTLUHOaLLx"

# SELECTED API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

# SELECTED URL
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"
#https://testnet.bybit.com/fr-FR/
# SESSION Activation
session = usdt_perpetual.HTTP(
    endpoint=api_url,
    api_key=api_key,
    api_secret=api_secret
)

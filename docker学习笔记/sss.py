import time

import requests
import json

# url = ['https://api.zan.top/node/v1/eth/mainnet/f3f0feb84b3147b79c0a05fbe9952cf4',
#        'https://api.zan.top/node/v1/eth/goerli/f3f0feb84b3147b79c0a05fbe9952cf4',
#        'https://api.zan.top/node/v1/eth/sepolia/f3f0feb84b3147b79c0a05fbe9952cf4']

# url = ["https://api.zan.top/node/v1/bsc/mainnet/f3f0feb84b3147b79c0a05fbe9952cf4",
#        "https://api.zan.top/node/v1/bsc/testnet/f3f0feb84b3147b79c0a05fbe9952cf4"]

url=['https://api.zan.top/node/v1/polygon/mainnet/f3f0feb84b3147b79c0a05fbe9952cf4',
     'https://api.zan.top/node/v1/polygon/mumbai/f3f0feb84b3147b79c0a05fbe9952cf4']


count = 0
a = 0
methods = ["eth_blockNumber", "eth_blockNumber1", "eth_blockNumber2", "eth_blockNumber3", "eth_blockNumber4",
           "eth_blockNumber5", "eth_blockNumber6"]
while True:
    for method in methods:
        payload = json.dumps({
            "method": method,
            "params": [],
            "id": 1,
            "jsonrpc": "2.0"
        })
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.request("POST", url[a], headers=headers, data=payload)
        print(response.text)
    a += 1
    if a == len(url):
        a = 0
    count += 1
    if count == 30:
        break

    time.sleep(10)

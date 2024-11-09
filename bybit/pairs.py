import argparse
import requests
import sys

parser = argparse.ArgumentParser(description="Bybit tickers")
parser.add_argument("-q", "--quote-asset")

if __name__ == "__main__":
    args = parser.parse_args()

    url = "https://api.bybit.com/v2/public/symbols"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch data, status code {response.status_code}")
        print(f"Response body: {response.text}")
        sys.exit(1)

    symbols = map(lambda x: x["name"], response.json()["result"])

    if args.quote_asset:
        symbols = filter(lambda x: x.endswith(args.quote_asset.upper()), symbols)

    symbols = map(lambda x: "BYBIT:{}".format(x.upper().replace(":", "")), symbols)

    print(",\n".join(sorted(symbols)))

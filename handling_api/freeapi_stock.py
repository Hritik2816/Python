import requests

def fetch_random_stock():
  url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
  respose = requests.get(url)
  data = respose.json()

  if data["success"] and "data" in data:
    stock_data = data["data"]
    comp_name = stock_data["Name"]
    list_comp_date = stock_data["ListingDate"]
    market_cap = stock_data["MarketCap"]
    curr_price = stock_data["CurrentPrice"]
    high_low = stock_data["HighLow"]
    book_value = stock_data["BookValue"]
    return comp_name, list_comp_date, market_cap, curr_price, high_low, book_value
  else:
    raise Exception("Failed to Fetch the stock data")

def main():
    try:
      Name, ListingDate, MarketCap, CurrentPrice, HighLow, BookValue = fetch_random_stock()
      print(f"Company Name: {Name}\nList Company Date: {ListingDate}\nMarket Cap: {MarketCap}\nCurrent Price: {CurrentPrice}\nHigh and Low: {HighLow}\nBookValue: {BookValue}")
    except Exception as e:
      print(e)

if __name__ == "__main__":
  main()      
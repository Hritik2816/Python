import http
import requests

def fetch_random_product():
  url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"

  response = requests.get(url)
  data = response.json()

  if data["success"] and "data" in data:
    product_data = data["data"]
    product_category = product_data["category"]
    product_title = product_data["title"]
    product_description = product_data["description"]
    product_price = product_data["price"]
    return product_category,product_title,product_description,product_price
  else:
    raise Exception("Fail to fetch product data")
  
def main():
  try:
    category, title, description, price = fetch_random_product()
    print(f"Category: {category}\nTitle: {title}\nDescription: {description}\nPrice: {price}")
  except Exception as e:
    print(e)


if __name__ == "__main__":
  main()

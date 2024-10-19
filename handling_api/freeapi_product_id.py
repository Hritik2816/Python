import requests

def fetch_random_product(product_id):
    # Correctly format the URL using an f-string
    url = f'https://api.freeapi.app/api/v1/public/randomproducts/{product_id}'
    response = requests.get(url)
    
    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()
        if data["success"] and "data" in data:
            product_data = data["data"]
            product_category = product_data["category"]
            product_title = product_data["title"]
            product_description = product_data["description"]
            product_price = product_data["price"]
            return product_category, product_title, product_description, product_price
        else:
            raise Exception("Failed to fetch product data: Invalid response structure.")
    else:
        raise Exception(f"Failed to fetch product data: HTTP Status Code {response.status_code}")

def main():
    productId = '20'  # Define the productId here
    try:
        category, title, description, price = fetch_random_product(productId)
        print(f"Category: {category}\nTitle: {title}\nDescription: {description}\nPrice: {price}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
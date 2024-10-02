items = ["apple", "mango", "banana", "apple", "orange"]

unique_item = set()

for item in items:
  if item in unique_item:
    print(item)
    break
  unique_item.add(item)
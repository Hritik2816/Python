chai_types = {"Masala":"Spicy", "Ginger":"Zesty","Green":"Mild"}
print(chai_types["Masala"])
print(chai_types)
print(chai_types.get("Ginger"))
chai_types["Green"] = "Fresh"
print(chai_types)

for chai in chai_types:
    print(chai)
    print(chai, chai_types[chai])


for key, value in chai_types.items():
    print(key,value)

if "Masala" in chai_types:
    print("I have Masala chai ")
    print(len(chai_types))

chai_types["Earl Grey"] = "Citrus"
print(len(chai_types))

chai_types.pop("Ginger")
print(chai_types)
chai_types.popitem()
print(chai_types)
print(len(chai_types))

del chai_types["Green"]
print(chai_types)


chai_types_copy =  chai_types.copy()
print(chai_types_copy)

chai_shop = {
  "Chai":{"Masala":"Spicy", "Ginger":"Strong", "Green":"Mild"},"Coffee":{"Cold":"Yummy","Hot":"Nice"}
  }

print(chai_shop["Chai"]["Masala"])


square_num = {x:x**2 for x in range(10)}
# print(square_num)
square_num.clear()
print(square_num)


keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
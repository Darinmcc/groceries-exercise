# groceries.py

from pprint import pprint




products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

def sort_by_name(any_product):
    return any_product["name"]

#sort prior to loop, need to sort before print
#sorted fucntion -- 2 parameters, list to be sortes 1.product, and 2 the way to sort)
sorted_products = sorted(products, key=sort_by_name)


product_count = len(products)
#print(products["name"])
#num = products["id"]
#name = products["name"]
#price = products["price"]


#print("THERE ARE " +str(product_count) + " PRODUCTS:")
#print("THERE ARE ",product_count," PRODUCTS")
#print(type(products))

print("--------------")
print(f"THERE ARE {product_count} PRODUCTS:")
print("--------------")


# loop through sorted products instead of products

for item in sorted_products:
    #print(type(item))
    #N = item["name"]
    #P = item["price"]
    #print(item["name"])
    #print(N,".....",P)
    price_usd = to_usd(item['price'])
    print(f"+ {item['name']} ... {price_usd}")
    #print(f"{N}...{P}")
    #print(item.get("name"))


# pprint(products)

# TODO: write some Python code here to produce the desired output

#pprint(products)

#products_count = len(products)

#print("THERE ARE 20 PRODUCTS:")
#> "one string" + "another string"
#print("THERE ARE " + str(products_count) + " PRODUCTS:")

#print("--------------")
#print(f"THERE ARE {products_count} PRODUCTS:")
#print("--------------")

# todo: sort the products

#for item in products:
    #print(type(item))
    #print(p["name"])
    #print(item["name"])
    #n = item["name"]
    #price = item["price"]
    #print(f"{item['name']} ... {item['price']}")

    #price_usd = to_usd(item['price'])
    #print(f"{item['name']} ... {price_usd}")


#creating a list
#assembling one list based on the contents of another list
#arr = [1,2,3,4]
#arr2 = []
#for i in arr:
#   arr2.append(i*100)
departments_list = []

for item in products:
    #print(item["department"])
    if item["department"] not in departments_list:
        departments_list.append(item["department"])

#another way to remove dupes

department_count = len(departments_list)

print("--------------")
print(f"THERE ARE {department_count} DEPARTMENTS:")
print("--------------")

departments_list.sort()

for d in departments_list:
    matching_products = [item for item in products if item["department"] == d]
    matching_products_count = len(matching_products)
    if matching_products_count > 1:
        label = "products"
    else:
        label = "product"
    print("+  " + d.title() + f"({matching_products_count} {label})")


#filter function 2 parameters 1 way to sort, and th list to be sorted from
#filter(x, arr)

#list comprehension
#[] starts and end with square
# team for team in teams if team["city"] == city]
#return the item for each item in our list of items if it matches some list of criterea
3
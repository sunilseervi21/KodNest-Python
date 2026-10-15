products={
    "P101": ["key",1200],
    "P102":["mouse",1201]
}

print(products["P101"])#when you know key is present 
print(products.get("p103"))#use when you dont know whether key is present or not
if products is None:
    print("key is not present")
else:
    print("key is present")

#updating
products["P101"][1]=10000
print(products["P101"])
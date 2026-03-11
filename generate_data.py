import pandas as pd
import random

products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard", "Mouse"]
cities = ["Hyderabad", "Bangalore", "Delhi", "Chennai", "Mumbai", "Pune"]

data = []

for i in range(1, 101):
    record = {
        "id": i,
        "product": random.choice(products),
        "city": random.choice(cities),
        "amount": random.randint(200, 2000)
    }
    data.append(record)

df = pd.DataFrame(data)
df.to_csv("sales.csv", index=False)
print("sales.csv with 100 records generated successfully!")
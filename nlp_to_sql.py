import re
from rapidfuzz import process


def generate_sql(question):

    q = question.lower()

    cities = ["hyderabad", "bangalore", "delhi", "chennai", "mumbai", "pune"]
    products = ["laptop", "phone", "tablet", "monitor", "keyboard", "mouse"]

    city_filter = ""
    product_filter = ""

    # ---------- FUZZY CITY MATCH ----------
    city_match = process.extractOne(q, cities)

    if city_match and city_match[1] > 80:
        city = city_match[0]
        city_filter = f"city='{city.capitalize()}'"

    # ---------- FUZZY PRODUCT MATCH ----------
    product_match = process.extractOne(q, products)

    if product_match and product_match[1] > 80:
        product = product_match[0]
        product_filter = f"product='{product.capitalize()}'"

    filters = []

    if city_filter:
        filters.append(city_filter)

    if product_filter:
        filters.append(product_filter)

    where_clause = ""

    if filters:
        where_clause = "WHERE " + " AND ".join(filters)

    # ---------- AVERAGE ----------
    if any(word in q for word in ["average", "mean"]):
        return f"SELECT AVG(amount) FROM sales {where_clause}"

    # ---------- TOTAL ----------
    elif any(word in q for word in ["total", "sum"]):
        return f"SELECT SUM(amount) FROM sales {where_clause}"

    # ---------- LOWEST / CHEAPEST ----------
    elif any(word in q for word in ["lowest","cheapest","least","minimum","min","cheap"]):

        numbers = re.findall(r'\d+', q)

        if numbers:
            limit = numbers[0]

        elif "sales" in q:
            limit = 5

        else:
            limit = 1

        return f"SELECT * FROM sales {where_clause} ORDER BY amount ASC LIMIT {limit}"

    # ---------- HIGHEST / TOP ----------
    elif any(word in q for word in ["highest","top","max","best","most"]):

        numbers = re.findall(r'\d+', q)

        if numbers:
            limit = numbers[0]

        elif "sale" in q and "sales" not in q:
            limit = 1

        else:
            limit = 5

        return f"SELECT * FROM sales {where_clause} ORDER BY amount DESC LIMIT {limit}"

    # ---------- SHOW ALL ----------
    elif any(word in q for word in ["all","list","show"]):
        return f"SELECT * FROM sales {where_clause}"

    else:
        return None
import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

# (a) INNER JOIN - customer name with every order amount
print("Customer orders (joined):")

cur.execute("""
SELECT c.name, o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY c.name;
""")

for row in cur.fetchall():
    print(row)


# (b) GROUP BY - total amount spent per customer
print("\nTotal spend per customer:")

cur.execute("""
SELECT c.name, SUM(o.amount) AS total_spent
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC;
""")

for row in cur.fetchall():
    print(row)


# (c) GROUP BY with HAVING - cities with average order > Rs.5000
print("\nCities with avg order > 5000:")

cur.execute("""
SELECT c.city, AVG(o.amount) AS avg_order
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING AVG(o.amount) > 5000
ORDER BY avg_order DESC;
""")

for row in cur.fetchall():
    print(row)

conn.close()


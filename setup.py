import sqlite3

# Connect to database
conn = sqlite3.connect("orders.db")
cur = conn.cursor()

# Remove old tables if they exist
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS customers")

# Create customers table
cur.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

# Create orders table
cur.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# Insert 6 customers
customers = [
    (1, "Ali", "Islamabad"),
    (2, "Sara", "Lahore"),
    (3, "Bilal", "Karachi"),
    (4, "Ayesha", "Islamabad"),
    (5, "Hamza", "Lahore"),
    (6, "Zain", "Peshawar")
]

cur.executemany("""
INSERT INTO customers (customer_id, name, city)
VALUES (?, ?, ?)
""", customers)

# Insert 10 orders
orders = [
    (1, 1, 4500),
    (2, 1, 7200),
    (3, 2, 3000),
    (4, 2, 8000),
    (5, 3, 9800),
    (6, 4, 6000),
    (7, 4, 5500),
    (8, 5, 5800),
    (9, 5, 6200),
    (10, 6, 4000)
]

cur.executemany("""
INSERT INTO orders (order_id, customer_id, amount)
VALUES (?, ?, ?)
""", orders)

conn.commit()
conn.close()

print("Database created successfully.")
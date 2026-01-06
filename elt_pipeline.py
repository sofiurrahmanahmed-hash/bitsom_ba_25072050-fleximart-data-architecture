import pandas as Pd
customers = Pd.read_csv("customer_RAW.csv")
products = Pd.read_csv("product_RAW.csv")
sales = Pd.read_csv("Sales_RAW.csv")customers.drop_duplicates(inplace=True)

# Handle missing emails
customers['email'] = customers['email'].replace('', None)

# Standardize phone format (+91-XXXXXXXXXX)
customers['phone'] = (
    customers['phone']
    .astype(str)
    .str.replace(r'\D', '', regex=True)
    .str[-10:]
)
customers['phone'] = '+91-' + customers['phone']

# Add surrogate key
customers.insert(0, 'customer_sk', range(1, len(customers) + 1))


# ----- PRODUCTS -----
# Remove duplicates
products.drop_duplicates(inplace=True)

# Handle missing price (drop)
products = products.dropna(subset=['price'])

# Standardize category names
products['category'] = (
    products['category']
    .str.lower()
    .str.strip()
    .str.capitalize()
)

# Handle null stock values
products['stock'] = products['stock'].fillna(0)

# Add surrogate key
products.insert(0, 'product_sk', range(1, len(products) + 1))


# ----- SALES -----
# Remove duplicates
sales.drop_duplicates(inplace=True)

# Convert date format to YYYY-MM-DD
sales['sale_date'] = pd.to_datetime(
    sales['sale_date'], errors='coerce'
).dt.date

# Remove records with missing foreign keys
sales.dropna(subset=['customer_id', 'product_id'], inplace=True)

# Add surrogate key
sales.insert(0, 'sale_sk', range(1, len(sales) + 1))

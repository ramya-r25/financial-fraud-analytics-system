from faker import Faker
import random
import mysql.connector
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PASSWORD_HERE",
    database="fraud_analytics_system"
)

cursor = conn.cursor()

# Locations
locations = [
    "Bangalore", "Mysore", "Mumbai", "Delhi",
    "Hyderabad", "Chennai", "Pune", "Kolkata",
    "Ahmedabad", "Jaipur", "Lucknow",
    "Kochi", "Visakhapatnam", "Indore"
]

# Merchants
merchants = [
    "Amazon", "Flipkart", "Myntra", "Ajio", "Nykaa",
    "Swiggy", "Zomato", "Uber", "Ola", "BookMyShow",
    "BigBasket", "Reliance Digital", "Croma",
    "Tata Cliq", "Meesho", "Paytm Mall",
    "Dominos", "Pizza Hut", "Starbucks",
    "IRCTC", "MakeMyTrip", "RedBus",
    "JioMart", "Apollo Pharmacy", "Decathlon"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]

transaction_types = [
    "Debit",
    "Credit"
]

devices = [
    "Android",
    "iPhone",
    "Web"
]

start_date = datetime(2025, 1, 1)

# Generate 10000 transactions
for i in range(10000):

    transaction_id = f"TXN{i+1000}"

    customer_name = fake.name()

    mobile_number = fake.msisdn()[:10]

    # Realistic Amount Distribution

    amount_type = random.choices(
        ["small", "medium", "large", "very_large"],
        weights=[60, 25, 10, 5]
    )[0]

    if amount_type == "small":
        transaction_amount = round(
            random.uniform(50, 2000), 2
        )

    elif amount_type == "medium":
        transaction_amount = round(
            random.uniform(2000, 10000), 2
        )

    elif amount_type == "large":
        transaction_amount = round(
            random.uniform(10000, 50000), 2
        )

    else:
        transaction_amount = round(
            random.uniform(50000, 120000), 2
        )

    payment_method = random.choice(
        payment_methods
    )

    transaction_type = random.choice(
        transaction_types
    )

    # 18 Months Data

    transaction_time = (
        start_date +
        timedelta(
            days=random.randint(0, 540),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
    )

    # Weighted Locations

    location = random.choices(
        locations,
        weights=[
            20, 10, 18, 16,
            15, 12, 10, 8,
            6, 5, 5,
            4, 4, 3
        ]
    )[0]

    # Weighted Merchants

    merchant_name = random.choices(
        merchants,
        weights=[
            18,16,10,8,7,
            12,12,8,8,6,
            10,6,5,
            5,5,4,
            4,4,3,
            8,5,4,
            5,4,3
        ]
    )[0]

    device_type = random.choice(
        devices
    )

    ip_address = fake.ipv4()

    query = """
    INSERT INTO transactions
    (
        transaction_id,
        customer_name,
        mobile_number,
        transaction_amount,
        payment_method,
        transaction_type,
        transaction_time,
        location,
        merchant_name,
        device_type,
        ip_address
    )

    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        transaction_id,
        customer_name,
        mobile_number,
        transaction_amount,
        payment_method,
        transaction_type,
        transaction_time,
        location,
        merchant_name,
        device_type,
        ip_address
    )

    cursor.execute(query, values)

conn.commit()

print("10000 realistic transactions inserted successfully!")

cursor.close()
conn.close()

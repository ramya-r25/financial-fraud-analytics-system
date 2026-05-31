from faker import Faker
import random
import mysql.connector

# Initialize Faker
fake = Faker()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ramya@2506",
    database="fraud_analytics_system"
)

cursor = conn.cursor()

# Lists for realistic data
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

locations = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Mysore"
]

merchants = [
    "Amazon",
    "Flipkart",
    "Swiggy",
    "Zomato",
    "Myntra",
    "Paytm",
    "PhonePe"
]

devices = [
    "Android",
    "iPhone",
    "Web"
]

# Generate 5000 transactions
for i in range(5000):

    transaction_id = f"TXN{i+1000}"

    customer_name = fake.name()

    mobile_number = fake.msisdn()[:10]

    transaction_amount = round(
        random.uniform(100, 100000),
        2
    )

    payment_method = random.choice(payment_methods)

    transaction_type = random.choice(transaction_types)

    transaction_time = fake.date_time_this_year()

    location = random.choice(locations)

    merchant_name = random.choice(merchants)

    device_type = random.choice(devices)

    ip_address = fake.ipv4()

    # SQL Query
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

# Commit Changes
conn.commit()

print("5000 realistic transactions inserted successfully!")

# Close Connection
cursor.close()
conn.close()
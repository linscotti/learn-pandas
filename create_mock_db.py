# Create a mock database with 100 rows of data
import pandas as pd
from faker import Faker


# Initialize Faker
fake = Faker()

data = {
    "Date": [fake.date() for _ in range(100)],
    "Product": [fake.word() for _ in range(100)],
    "Sales": [fake.random_int(min=18, max=90) for _ in range(100)],
    "Quantity": [fake.random_int(min=18, max=90) for _ in range(100)],
}

df = pd.DataFrame(data)

df.to_csv("mock_data.csv", index=False)

print("CSV file 'mock_data_csv' has been created successfully")

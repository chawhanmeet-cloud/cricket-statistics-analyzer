import pandas as pd
from sqlalchemy import create_engine

# MySQL connection
engine = create_engine(
    "mysql+mysqlconnector://root:password@localhost/cricket_analyser"
)

# Read data from MySQL into Pandas
query = "SELECT * FROM score;"
df = pd.read_sql(query, engine)

# Display data
print("\nCricket Data:")
print(df)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nAverage Runs:")
print(df["runs"].mean())

# Close the connection
engine.dispose()

print("\nMySQL connection closed.")
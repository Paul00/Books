import sqlite3
import pandas as pd
connection = sqlite3.connect('database.sqlite')
print("Database opened successfully")

tables=pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", connection)
print(tables)

countries = pd.read_sql("SELECT * FROM Country;", connection)
countries.head()

selected_players=pd.read_sql_query("SELECT * FROM Player WHERE height >= 180  AND weight >= 170 ", connection)
print(selected_players)

connection.close()

engine = create_engine('postgresql://postgres:461436@localhost:5432/postgres')

import sqlalchemy as sa

engine = sa.create_engine('postgresql://postgres:461436@localhost:5432/postgres')

import pandas as pd
df = pd.read_csv("/Users/rafaela/test/webscraping.csv")
df.to_sql('webscraping', engine)
engine.table_names()
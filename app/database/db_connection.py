from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

df=pd.read_csv('app/dataset/Amazon Dataset.csv')

engine = create_engine(os.getenv("DATABASE_URL"))

df.to_sql("Amazon_Sales",
          engine, 
          if_exists="replace",
          index=False)

# print("Done")
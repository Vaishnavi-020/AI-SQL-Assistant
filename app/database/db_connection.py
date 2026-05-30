from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()


engine = create_engine(os.getenv("DATABASE_URL"))

files={
    'customers':'app/dataset/customers (1).csv',
    'orders':'app/dataset/orders (1).csv',
    'products':'app/dataset/products (1).csv'
}

for table_name,filepath in files.items():
    df=pd.read_csv(filepath)
    df.columns=(
        df.columns.str.strip().str.lower()
    )
    if 'order_date' in df.columns:
        df['order_date']=pd.to_datetime(df['order_date'],dayfirst=True,errors="coerce")
    if 'signup_date' in df.columns:
        df['signup_date']=pd.to_datetime(df['signup_date'],dayfirst=True,errors="coerce")
    df.to_sql(table_name,
              engine,
              if_exists="replace",
              index=False
              )

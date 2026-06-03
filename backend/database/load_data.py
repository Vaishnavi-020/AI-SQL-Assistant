from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd
import streamlit as st

load_dotenv()


engine = create_engine(os.getenv("DATABASE_URL"))

if not engine:
    engine=st.secrets["DATABASE_URL"]

files={
    'customers':'backend/dataset/customers (1).csv',
    'orders':'backend/dataset/orders (1).csv',
    'products':'backend/dataset/products (1).csv'
}

for table_name,filepath in files.items():
    df=pd.read_csv(filepath)
    df.columns=(
        df.columns.str.strip().str.lower()
    )
    if 'order_date' in df.columns:
        df['order_date']=pd.to_datetime(df['order_date'],format='%d-%m-%Y',errors="coerce")
    if 'signup_date' in df.columns:
        df['signup_date']=pd.to_datetime(df['signup_date'],format='%Y-%m-%d',errors="coerce")
    df.to_sql(table_name,
              engine,
              if_exists="replace",
              index=False
              )

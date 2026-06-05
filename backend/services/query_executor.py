from database.load_data import engine
import pandas as pd
from sqlalchemy import text

def execute_query(sql_query):
    try:
        with engine.connect() as conn:
            result=conn.execute(text(sql_query))

            df=pd.DataFrame(result.fetchall(),
                            columns=result.keys())
            
            return df
        
    except Exception as e:
        print(f"Database Error: {e}")
        return None
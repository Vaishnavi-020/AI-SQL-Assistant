from sqlalchemy import inspect
from db_connection import engine

def load_schema():
    inspector=inspect(engine)

    tables=inspector.get_table_names()
    schema_text=""
    for table in tables:
        columns=inspector.get_columns(table)
        column_names=[
            column["name"] for column in columns
        ]
        schema_text+=f""" Table:{table}
        Columns:{', '.join(column_names)}
        """

    return schema_text

load_schema()
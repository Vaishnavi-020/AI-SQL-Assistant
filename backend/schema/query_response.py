from pydantic import BaseModel

class QueryResponse(BaseModel):
    sql_query:str
    results:list
    analysis:str
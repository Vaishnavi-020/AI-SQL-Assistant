from llm import chain
from database.schema_loader import load_schema
from database.query_executor import execute_query

schema=load_schema()

question=input("Ask a question:")

response=chain.invoke({
    "schema":schema,
    "question":question
})

sql_query=response.content.strip()

sql_query=sql_query.replace("```sql","")
sql_query=sql_query.replace("```","").strip()

if not sql_query.lower().startswith(("select","with")):
    raise ValueError("Only SELECT queries allowed.")

print("Generated SQL:")
print(sql_query)

fetched_data=execute_query(sql_query)
print(f"\nFetched_data:")
print(fetched_data)
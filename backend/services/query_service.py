from database.schema_loader import load_schema
from model.llm_model import llm
from model.prompt_template import get_prompt

def generate_sql(question):
    schema=load_schema()
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")
    prompt=get_prompt(schema=schema,question=question)
    response=llm.invoke(prompt)

    sql_query=response.content.strip()

    sql_query=sql_query.replace("```sql","")
    sql_query=sql_query.replace("```","").strip()

    if not sql_query.lower().startswith(("select","with")):
        raise ValueError("Only SELECT queries allowed.")
    
    return sql_query
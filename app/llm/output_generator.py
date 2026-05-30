from .prompt_template import get_prompt,analysis_prompt,scope_prompt
from app.utils.query_executor import execute_query
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from app.database.schema_loader import load_schema
import certifi

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

def generate_sql(question):
    schema=load_schema()
    scope=scope_prompt(schema=schema,question=question)
    scope_response=llm.invoke(scope)
    is_valid=scope_response.content.strip().upper()
    if is_valid=="NO":
        raise ValueError(
            "This question is outside the scope of the database."
        )
    prompt=get_prompt(schema=schema,question=question)
    response=llm.invoke(prompt)

    sql_query=response.content.strip()

    sql_query=sql_query.replace("```sql","")
    sql_query=sql_query.replace("```","").strip()

    if not sql_query.lower().startswith(("select","with")):
        raise ValueError("Only SELECT queries allowed.")
    
    return sql_query

def generate_analysis(question,sql_query,df):
    if df is None or df.empty:
        return "No data available for analysis"
    df_string=df.head(20).to_string(index=False)
    prompt=analysis_prompt(question=question,sql_query=sql_query,df=df_string)
    response=llm.invoke(prompt)

    analysis=response.content

    return analysis
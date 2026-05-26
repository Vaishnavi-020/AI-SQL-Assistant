from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from database.schema_loader import load_schema
import os
from dotenv import load_dotenv
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv()

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

schema=load_schema()

prompt=PromptTemplate(template="""
    You are an expert PostgreSQL assistant.

    Database Schema:
    {schema}

    Rules:
    1. Generate ONLY valid PostgreSQL SQL.
    2. Return ONLY the SQL query.
    3. No explanation, markdown, or extra text.
    4. Use only table and column names present in the schema.
    5. Use appropriate JOINs when needed.
    6. Add LIMIT 10 when the user does not specify a limit.
    7. If aggregation is needed, use GROUP BY properly.
    8. For sorting, use ORDER BY when relevant.
    9. Never hallucinate tables or columns.

    User Question:
    {question}
                      
    SQL Query:
    """,
    input_variables=['schema','question'])

chain=prompt|llm

# question="Show Top 3 product categories with highest sale."

# response=chain.invoke({"schema":schema,
#                        "question":question})

# print(response.content)
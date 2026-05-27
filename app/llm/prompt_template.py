from langchain_core.prompts import PromptTemplate


def get_prompt(schema,question):

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
        7. If aggregation is needed, use GROUP BY properly.
        8. For sorting, use ORDER BY when relevant.
        9. Never hallucinate tables or columns.

        User Question:
        {question}
                        
        SQL Query:
        """,
        input_variables=['schema','question'])
    
    formatted_prompt=prompt.format(schema=schema,
                                   question=question)
    
    return formatted_prompt
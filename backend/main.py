from fastapi import FastAPI,HTTPException
from .llm.output_generator import generate_analysis,generate_sql
from .utils.query_executor import execute_query
from .schema.question_schema import QueryRequest

app =FastAPI()

@app.post("/query")
async def query(request:QueryRequest):
    question=request.question
    try:
        sql_query=generate_sql(question)
        df=execute_query(sql_query)
        analysis=generate_analysis(question,
                                sql_query,
                                df)
        
        return {
            "sql_query":sql_query,
            "results":df.to_dict(orient="records"),
            "analysis":analysis
        }
    except ValueError as e:
        raise HTTPException(status_code=400,
                            detail=str(e))
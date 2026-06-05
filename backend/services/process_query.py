from services.analysis_service import generate_analysis
from services.query_service import generate_sql
from services.query_executor import execute_query

def process_query_service(question):
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
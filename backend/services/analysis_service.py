from ..model.prompt_template import analysis_prompt
from ..model.llm_model import llm

def generate_analysis(question,sql_query,df):
    if df is None or df.empty:
        return "No data available for analysis"
    df_string=df.head(20).to_string(index=False)
    prompt=analysis_prompt(question=question,sql_query=sql_query,df=df_string)
    response=llm.invoke(prompt)

    analysis=response.content

    return analysis
import streamlit as st
from app.llm.output_generator import generate_sql,generate_analysis
from app.utils.query_executor import execute_query
from app.utils.visualization import visualize

st.title("AI SQL Analytics Assistant")

question=st.text_input(
    "Ask your question"
)

if st.button("Generate"):
    try:
        sql_query=generate_sql(question)

        st.subheader("Generated SQL")
        st.code(sql_query,
                language="sql")
        df=execute_query(sql_query)
        st.subheader("Results")
        st.dataframe(df)

        visualize(df)
        analysis=generate_analysis(question,sql_query,df)
        st.subheader("Explanation")
        st.write(analysis)
    except ValueError as e:
        st.error(
            f"Error: {str(e)}"
        )
    except Exception as e:
        st.error(
            f"Unexpected Error:"
            f"{str(e)}"
        )
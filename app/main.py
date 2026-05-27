import streamlit as st
from llm.sql_generator import generate_sql
from database.query_executor import execute_query
from utils.visualization import visualize

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
    except ValueError as e:
        st.error(
            f"Error: {str(e)}"
        )
    except Exception as e:
        st.error(
            f"Unexpected Error:"
            f"{str(e)}"
        )
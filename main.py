import streamlit as st
from app.llm.output_generator import generate_sql,generate_analysis
from app.utils.query_executor import execute_query
from app.utils.visualization import visualize

st.title("AI SQL Analytics Assistant")

st.subheader("💡 Try These Questions")

example_questions=[
    "Show customer city wise sales",
    "Top 3 best selling products",
    "How has Yoga Mats sales changed over time?",
    "Monthly sales trend",
    "Payment method distribution"
]

st.info(
    """
    Demo Database Loaded with:

    • Orders table  
    • Products table  
    • Customers table  

    Click any example question below or ask your own.
    """
    )

if "question" not in st.session_state:
    st.session_state.question=""

for q in example_questions:
    if st.button(q,use_container_width=True):
        st.session_state.question=q

question=st.text_input(
    "Ask your question",
    key="question"
)

if st.button("Generate"):
    if not question.strip():
        st.warning("Please enter a question")
    else:
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
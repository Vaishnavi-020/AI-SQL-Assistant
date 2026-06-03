import streamlit as st
import requests
import pandas as pd

from visualization import visualize


API_URL = "http://localhost:8000/query"

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
            response=requests.post(API_URL,
                                   json={"question":question})
            response.raise_for_status()

            data=response.json()
            st.subheader("Generated SQL")
            st.code(data["sql_query"],
                    language="sql")
            df=pd.DataFrame(data["results"])

            st.subheader("Results")
            st.dataframe(df)

            visualize(df)
            st.subheader("Explanation")
            st.write(data["analysis"])

        except requests.exceptions.RequestException as e:
            st.error(f"Backend Error: {str(e)}")

        except requests.exceptions.HTTPError:
            st.error(
                response.json()['detail']
            )
        except Exception as e:
            st.error(
                f"Unexpected Error:"
                f"{str(e)}"
            )
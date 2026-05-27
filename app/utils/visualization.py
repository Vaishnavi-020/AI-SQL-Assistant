import streamlit as st
import plotly.express as px

def visualize(df):
    if df.empty:
        st.warning("No data found")
        return
    numeric_cols=df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    datetime_cols=df.select_dtypes(
        include=["datetime64"]
    ).columns.tolist()

    categorical_cols=df.select_dtypes(
        exclude=["number"]
    ).columns.tolist()

    total_cols=len(df.columns)

    if total_cols==1 and numeric_cols:
        st.subheader("Distribution")
        fig=px.histogram(df,x=numeric_cols[0])

        st.plotly_chart(fig,width="stretch")

    elif datetime_cols and numeric_cols:
        x_col=datetime_cols[0]
        y_col=datetime_cols[0]

        st.subheader("Trend Analysis")

        fig=px.line(df,x=x_col,y=y_col)

        st.plotly_chart(fig, width="stretch")

    elif len(df.columns)==2:
        x_col=df.columns[0]
        y_col=df.columns[1]

        if y_col in numeric_cols:
            st.subheader("Bar Chart")

            fig=px.bar(
                df,
                x=x_col,
                y=y_col
            )

            st.plotly_chart(
                fig, width="stretch"
            )

    elif (len(categorical_cols)==1 and len(numeric_cols)==1 and len(df)<=10):
        st.subheader("Pie Chart")

        fig=px.pie(
            df,
            names=categorical_cols[0],
            values=numeric_cols[0]
        )
        st.plotly_chart(
            fig, width="stretch"
        )
    else:
        st.info(
            "No suitable visualization found."
        )
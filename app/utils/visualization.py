import streamlit as st
import plotly.express as px
import pandas as pd

def visualize(df):
    try:
        if df.empty:
            st.warning("No data found")
            return
        df=df.copy()
        for col in df.columns:
            if df[col].dtype==object:
                try:
                    if any(word in col.lower() for word in ['date','time']):
                        df[col]=pd.to_datetime(df[col],format='%d-%m-%Y',errors="coerce")
                except Exception:
                    pass
        for col in df.columns:
            if df[col].dtype==object:    
                try:
                    df[col]=pd.to_numeric(df[col])
                except Exception:
                    pass
        numeric_cols=df.select_dtypes(
            include=["number"]
        ).columns.tolist()

        datetime_cols=df.select_dtypes(
            include=["datetime64[ns]","datetimetz"]
        ).columns.tolist()

        categorical_cols=df.select_dtypes(
            include=["object","category"]
        ).columns.tolist()

        total_cols=len(df.columns)

        if total_cols==1 and numeric_cols:
            st.subheader("Distribution")
            fig=px.histogram(df,x=numeric_cols[0])

            st.plotly_chart(fig,width="stretch")

        elif datetime_cols and numeric_cols:
            x_col=datetime_cols[0]
            y_col=numeric_cols[0]

            st.subheader("Trend Analysis")

            fig=px.line(df,x=x_col,y=y_col)

            st.plotly_chart(fig, width="stretch")

        elif (len(categorical_cols)==1 and len(numeric_cols)==1 and df[categorical_cols[0]].nunique()<=10):
            st.subheader("Pie Chart")

            fig=px.pie(
                df,
                names=categorical_cols[0],
                values=numeric_cols[0]
            )
            st.plotly_chart(
                fig, width="stretch"
            )
        elif len(categorical_cols)>=1 and len(numeric_cols)==1:
            x_col=categorical_cols[0]
            y_col=numeric_cols[0]

            fig=px.bar(
                df,
                x=x_col,
                y=y_col,
                color=categorical_cols[1] if len(categorical_cols)>1 else None
            )
            st.plotly_chart(fig,width="stretch")

        elif len(categorical_cols)==2 and len(numeric_cols)==0:
            x_col=categorical_cols[0]
            y_col=categorical_cols[1]
            fig=px.scatter(
                df,
                x_col,
                y_col
            )
            st.plotly_chart(fig,width="stretch")
        else:
            st.info(
                "No suitable visualization found."
            )
    except Exception as e:
        st.error(f"Visualization error: {e}")
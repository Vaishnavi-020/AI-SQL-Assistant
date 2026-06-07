import pandas as pd 

def clean_dataframe(df):
    for col in df.columns:

        if (
            pd.api.types.is_object_dtype(df[col])
            or pd.api.types.is_string_dtype(df[col])
            ):

            try:
                if any(
                    word in col.lower()
                    for word in ["date","time","month","year"]
                ):
                    df[col] = pd.to_datetime(
                        df[col],
                        errors="coerce"
                    )
            except:
                pass

    for col in df.columns:

        if df[col].dtype == object:

            try:
                df[col] = pd.to_numeric(df[col])
            except:
                pass

    return df
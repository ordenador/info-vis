import pandas as pd
import streamlit as st
import altair as alt
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

data = pd.read_csv("merge.csv")

def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame]): Source dataframe

    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection

selection = aggrid_interactive_table(df=data)

if selection:
    st.write("You selected:")
    st.json(selection["selected_rows"])


c = alt.Chart(data).mark_bar(
    color='red',
    opacity=0.5
).encode(
    x='tempo',
    y='speechiness'
).properties(
    title="Tempo vs Speechiness",
    width=700,
    height=500
)
st.altair_chart(c, use_container_width=True)

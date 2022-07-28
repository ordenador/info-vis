import pandas as pd
import plotly.express as px
import streamlit as st
import altair as alt
# from st_aggrid import AgGrid, GridOptionsBuilder
# from st_aggrid.shared import GridUpdateMode


data = pd.read_csv("merge.csv")


st.set_page_config(
    page_title="Spotify Tracks",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
)


# dashboard title
st.title("Spotify Tracks 2022")


# top-level filters
artist = st.selectbox("Selecciona el artista", pd.unique(data["artist_name"]))
# dataframe filter
artist_filtred = data[data["artist_name"] == artist]

# selectbox for the tracks
track_values = artist_filtred["track_name"].tolist()
track_options = artist_filtred.index.tolist()
track_dic = dict(zip(track_options, track_values))
track_index = st.selectbox("Selecciona el track", track_options, format_func=lambda x: track_dic[x])
# st.write("track_index:", track_index)
# st.write("track_values:", artist_filtred["track_name"].loc[track_index])
track_filtred = artist_filtred.loc[track_index]



radar = pd.DataFrame(dict(
    r=[
        float(track_filtred['acousticness']),
        float(track_filtred['danceability']),
        float(track_filtred['energy']),
        float(track_filtred['instrumentalness']),
        float(track_filtred['liveness']),
        float(track_filtred['speechiness']),
        float(track_filtred['valence'])],
    theta=['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']))


fig = px.line_polar(radar, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
st.plotly_chart(fig, use_container_width=True)


# ag-grid
c = alt.Chart(artist_filtred).mark_bar(
    color='red',
    opacity=0.5
).encode(
    x='tempo',
    y='speechiness'
).properties(
    title="Tempo vs Speechiness",
    width=700,
    height=500
).interactive()
st.altair_chart(c, use_container_width=True)

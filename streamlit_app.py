import ast
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import numpy as np

# funtion to load image from url using PIL
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


data = pd.read_csv("merge.csv")

st.set_page_config(
    page_title="Spotify Tracks",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="expanded",
)

col1, col2= st.columns(2)

with col1:
    # dashboard title
    st.title("Spotify Tracks 2022")

with col2:
    # st.header("Spotify logo")
    image = Image.open("Spotify_Logo_RGB_Green.png")
    st.image(image, caption=None, width=345, use_column_width="never", clamp=False, channels="RGB", output_format="auto")


with st.expander("Diccionario de datos"):
     st.markdown("""
Se utilizan datos descargados desde la Api de Spotify, corresponde a información sobre las características de 1000 tracks de musica. La query utilizada es la siguiente: `'year:2022'`.

* **Danceability**: Describe qué tan adecuada es una pista en función de una combinación de tempo, estabilidad del ritmo, fuerza ordenada y regularidad general. Un valor de 1.0 es más bailable.

* **Energy**: Representa una medida perceptiva de intensidad y actividad. La pista con mucha energía se siente rápida, fuerte y ruidosa.

* **Loudness**: Volumen general de una pista en decibelios (dB). Los valores de sonoridad se promedian en toda la pista. Los valores típicos oscilan entre -60 y 0 db.

* **Speechiness**: Detecta la presencia de palabras habladas en una pista. Los valores superiores a 0,66 describen pistas que probablemente estén formadas en su totalidad por palabras habladas. Los valores por debajo de 0,33 significan que la canción no tiene discurso.

* **Acousticness**: Representa si la pista es acústica. 1.0 representa una alta confianza en que la pista es acústica.

* **Instrumentalness**: Predice si una pista no contiene voces. Las pistas de rap o palabras habladas son claramente “Vocales”. Cuanto más cerca esté el valor de instrumentalidad de 1,0, es más probable que la pista no contenga contenido vocal.

* **Liveness**: Detecta la presencia de una audiencia en la grabación. Los valores de vivacidad más altos representan una mayor probabilidad de que la pista se interprete en vivo.

* **Valence**: Describe la positividad musical transmitida por una pista. Pista con alto valencia sonido más positivo (ejmplo: feliz, alegre, eufórico)

* **Tempo**: El tempo general estimado de una pista en pulsaciones por minuto (BPM). El tempo es la velocidad o el ritmo de una pieza dada y se deriva directamente de la duración promedio del tiempo.
""")
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Características de la pista musical</h1>", unsafe_allow_html=True)


col11, col12= st.columns(2)

with col11:
    # top-level filters
    artist = st.selectbox("Selecciona el artista", pd.unique(data["artist_name"]))
    # dataframe filter
    artist_filtred = data[data["artist_name"] == artist]

with col12:
    # selectbox for the tracks
    track_values = artist_filtred["track_name"].tolist()
    track_options = artist_filtred.index.tolist()
    track_dic = dict(zip(track_options, track_values))
    track_index = st.selectbox("Selecciona el track", track_options, format_func=lambda x: track_dic[x])
    track_filtred = artist_filtred.loc[track_index]

col31, col32= st.columns(2)

with col31:
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
    note = "Gráfico de radar de características de la pista musical."
    fig = px.line_polar(radar, r='r', theta='theta', line_close=True, template='plotly_dark')
    fig.add_annotation(
        showarrow=False,
        text=note,
        xref='x domain',
        x=0.5,
        yref='y domain',
        y=-0.1,
    )
    fig.update_traces(fill='toself')
    st.plotly_chart(fig, use_container_width=True)


with col32:
    url = track_filtred['album_image']
    st.image(load_image(url), caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
    if track_filtred['preview_url'] is not np.nan:
        st.audio(track_filtred['preview_url'])
    else:
        st.write("No existe vista previa disponible")


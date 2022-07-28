# info-vis

[Aplicación desplegada en en streamlitapp](https://ordenador-info-vis-streamlit-app-albmpx.streamlitapp.com/)


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

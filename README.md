# Introducción

Medir el sentimiento de cada uno de los comentarios es un trabajo complejo, ya que la clasificación no solo depende de las palabras y las frases, sino también del entorno en el cual se evalúa. En este caso, los comentarios corresponden a la evaluación de videojuegos, siendo estos:
- Positivo
- Negativo
- Neutro
- Irrelevante

La fuente de estos mismos fue Twitter. Para problemáticas es importante tener un set con etiquetas (volumen importante, relacionado en el entorno). De esta forma podemos entrenar un modelo ajustado a las necesidades. Una disparidad sería, por ejemplo: usar un set con etiquetas relacionado con comentarios de políticos. Las precisiones luego de entrenar con estos datos pueden que sea favorable para datos train, pero para datos test (comentarios de videojuegos), seguro la realidad sea otra.

El objetivo de este proyecto no es solo crear una aplicación para calificar comentarios, sino también evaluar los rendimientos de este cuando variamos de datos (para poder comprender la importancia que tiene la cantidad de datos en estas problemáticas). Además de comparar modelos para descubrir cuáles son aquellos que responden mejor a una problemática de clasificación.

![Texto alternativo](https://github.com/Martinerramuspe/Sentimental_comments-project-supervised/blob/main/02-Api_Streamlit/Portada.png?raw=true)

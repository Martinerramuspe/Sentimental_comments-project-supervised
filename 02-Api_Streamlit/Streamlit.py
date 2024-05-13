import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import spacy
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
def filtrar_columnas(df):
    columnas_a_mantener = [
        'country', 'Text'
    ]
    return df[columnas_a_mantener]

# Función para preprocesar texto
nlp = spacy.load("en_core_web_sm")

# Etapa n°1 : Funciones y clase para preprocesamiento de texto
def preprocess(text):
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    return " ".join(filtered_tokens)

class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()
        X_copy['Preprocessed_Text'] = X_copy['Text'].apply(preprocess)
        X_copy['Combined_Text'] = X_copy['Preprocessed_Text'] + ' ' + X_copy['country']
        return X_copy['Combined_Text']

# Cargar el preprocesador fuera de la función main
archivo_pipeline = r'G:\Mi unidad\sentimental-twitter-project\02-Api_Streamlit\pipeline_preprocesamiento.pkl'
text_preprocessing_pipeline = joblib.load(archivo_pipeline)
# Cargar el modelo fuera de la función main
modelo = r'G:\Mi unidad\sentimental-twitter-project\02-Api_Streamlit\modelo_random_forest.pkl'
rf_model = joblib.load(modelo)


# Función principal de streamlit------------------------------------------------------
def main():
    st.title("MEDIDOR DE SENTIMIENTO")

    # Concatenar la información sobre las clasificaciones de sentimientos en una sola cadena
    info_sentimientos = "Positive: 3 | Irrelevant: 0 | Neutral: 2 | Negative: 1"

    # Agregar un subtítulo con la información sobre las clasificaciones de sentimientos
    st.subheader(info_sentimientos)

    # Creamos imagen portada
    imagen = r'G:\Mi unidad\sentimental-twitter-project\02-Api_Streamlit\Portada.jpg'
    st.image(imagen, use_column_width=True)  # Mostrar la imagen de portada
    
    # Crear input para seleccionar una categoría
    categoria = st.selectbox("Selecciona juego:", ("FIFA","TomClancysRainbowSix","LeagueOfLegends","MaddenNFL","Microsoft","CallOfDuty","Verizon","ApexLegends","Facebook","CallOfDutyBlackopsColdWar","WorldOfCraft","Dota2","NBA2K","Battlefield","TomClancysGhostRecon","johnson&johnson","Overwatch","Xbox(Xseries)","Amazon","PlayStation5(PS5)","GrandTheftAuto(GTA)","CS-GO","Cyberpunk2077","Nvidia","Hearthstone","HomeDepot","Google","Borderlands","PlayerUnknownsBattlegrounds(PUBG)","Fortnite","RedDeadRedemption(RDR)","AssassinsCreed"))

    # Crear input para ingresar texto
    texto = st.text_input("Ingrese  comentario:")

    # Botón para volcar los valores en el DataFrame y realizar la predicción
    if st.button("Transformar"):
        data = {"country": [categoria], "Text": [texto]}
        df = pd.DataFrame(data)
        
        # Aplicar el pipeline de preprocesamiento de texto al DataFrame
        df_processed = text_preprocessing_pipeline.transform(df)
        
        # Realizar la predicción con el modelo
        prediction = rf_model.predict(df_processed)
        
        # Imprimir la predicción
        st.write("El sentimiento de tu comentario es:", prediction)

if __name__ == "__main__":
    main()

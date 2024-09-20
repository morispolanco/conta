import streamlit as st
import requests
import json
import pandas as pd

# Configuración de claves de API desde los secretos
TOGETHER_API_KEY = st.secrets["together"]["api_key"]
SERPER_API_KEY = st.secrets["serper"]["api_key"]

# Función para llamar a la API de Together y obtener respuestas de verificación de regulaciones
def verificar_estado_financiero(financial_statements):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "user", "content": f"Verifica si los siguientes estados financieros cumplen con las regulaciones vigentes de Guatemala: {financial_statements}"}
        ],
        "max_tokens": 2512,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stop": ["<|eot_id|>"],
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error en la verificación de Together API"

# Función para llamar a la API de Serper para obtener información sobre regulaciones específicas
def buscar_regulaciones_guatemala():
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    query = {
        "q": "regulaciones contables de Guatemala"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(query))
    if response.status_code == 200:
        return response.json()["organic"][0]["snippet"]
    else:
        return "Error en la búsqueda de regulaciones"

# Función para leer el archivo xlsx y convertirlo a texto
def leer_archivo_xlsx(file):
    df = pd.read_excel(file)
    return df.to_string(index=False)

# Título de la aplicación
st.title("Verificación de Estados Financieros según las Regulaciones de Guatemala")

# Subida de archivo Excel para los estados financieros
st.header("Sube tus Estados Financieros en formato Excel (.xlsx)")
uploaded_file = st.file_uploader("Subir archivo .xlsx", type=["xlsx"])

if uploaded_file is not None:
    # Leer el archivo y convertir a texto
    financial_statements = leer_archivo_xlsx(uploaded_file)
    st.subheader("Contenido del Archivo Subido")
    st.write(financial_statements)

    # Botón para verificar los estados financieros
    if st.button("Verificar Estados Financieros"):
        resultado_verificacion = verificar_estado_financiero(financial_statements)
        st.subheader("Resultado de la Verificación")
        st.write(resultado_verificacion)
else:
    st.error("Por favor, sube un archivo .xlsx")

# Botón para obtener información adicional sobre regulaciones
st.header("Buscar Regulaciones Contables en Guatemala")
if st.button("Buscar Regulaciones"):
    regulaciones_info = buscar_regulaciones_guatemala()
    st.subheader("Resultado de la Búsqueda de Regulaciones")
    st.write(regulaciones_info)

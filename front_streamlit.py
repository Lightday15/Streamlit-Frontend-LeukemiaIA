import requests
import streamlit as st

# Definición de la URL de la API
API_URL = "http://localhost:8000/predict/"  # Asegúrate de que esta URL sea correcta

app_mode = st.sidebar.selectbox('Menú',['Inicio','Predicción','Recomendaciones', 'Contribuidores'])

if app_mode=='Inicio':
    st.title('LeukemiaIA:')
    st.header('Asistente de IA para el Diagnóstico y Clasificación de leucemia linfoblástica aguda (LLA) a partir de imágenes microscópicas')
    st.markdown('En la práctica clínica, el análisis de imágenes microscópicas es esencial para diagnosticar y clasificar diferentes tipos de leucemia linfoblástica aguda. La implementación de un asistente de inteligencia artificial (IA) puede proporcionar una evaluación objetiva y consistente, mejorando la precisión y eficiencia del diagnóstico.')
    st.image('LeukemiaIA.jpg')
# Sección Predicción
elif app_mode == 'Predicción': 
    st.title('LeukemiaIA: Asistente de IA para el Diagnóstico de Leucemia')
    uploaded_file = st.file_uploader("Selecciona una imagen:", type=["jpg", "jpeg", "png", "bmp", "tif"])
    if st.button('Predecir'):
       if uploaded_file is not None:
           st.image(uploaded_file, caption="Imagen cargada", use_column_width=True)
   
           files = {'file': uploaded_file}
           try:
              response = requests.post(API_URL, files=files)

              if response.status_code == 200:
                 results = response.json()
                 st.success(f"Resultado: {results['resultado']}")
                 st.write(f"Confianza Maligno: {results['confianza_maligno']:.2f}")
                 st.write(f"Confianza Benigno: {results['confianza_benigno']:.2f}")
              else:
                  st.error("Error en la respuesta de la API")
           except Exception as e:
                 st.error(f"Error al conectarse a la API: {e}")
           
       else: 
             st.warning("Por favor, selecciona una imagen para analizar.")
             
             
elif app_mode == 'Recomendaciones':
      # Agregar el video
    st.title("Recomendaciones para la Detección Temprana de Leucemia")
    st.markdown("Aquí tienes un video informativo que explica más sobre la leucemia y su diagnóstico:")
    video_url = "https://www.youtube.com/watch?v=vNF8RBiwIYo&t=44s" 
    st.video(video_url)
     
    st.title("Recomendaciones")
    st.markdown('''
    ### 1. Conocer los Síntomas Comunes  
    - Fatiga constante y debilidad.  
    - Fiebre o escalofríos frecuentes.  
    - Infecciones recurrentes o duraderas.  
    - Pérdida de peso inexplicable.  
    - Hematomas o sangrados excesivos.  
    - Inflamación de los ganglios linfáticos.  
    - Sudoración excesiva, especialmente durante la noche.

    ### 2. Evaluaciones Médicas Periódicas  
    - **Hemogramas completos:** Identificar anormalidades en sangre.  
    - **Pruebas genéticas:** Detectar alteraciones cromosómicas.  
    - **Biopsias de médula ósea:** Evaluar signos de cáncer directamente.

    ### 3. Identificación de Factores de Riesgo  
    - **Antecedentes familiares:** Historia de leucemia en la familia.  
    - **Exposición a productos químicos peligrosos:** Como benceno.  
    - **Trastornos genéticos:** Como el síndrome de Down.

    ### 4. Hábitos de Vida Saludables  
    - Ejercicio regular y alimentación equilibrada.  
    - Evitar tabaco y alcohol en exceso.

    ### 5. Educación y Concienciación  
    - Participar en campañas de detección y charlas informativas.  
    ''')
elif app_mode == 'Contribuidores':
    
    st.title("Contribuidores del Proyecto")

    st.markdown("## Equipo de Desarrollo e Investigación")

    # Contribuidor: Valentina Parada Carrillo
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image("valentina.png", width=120)  # Asegúrate de tener la imagen en la misma carpeta o usa una URL
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.markdown('''**Lightday Valentina Parada Carrillo**  
                     - **Profesión :** Ingeniera de Sistemas     
                     - **Rol en el Proyecto:** Líder del Proyecto y desarrollo de la API         
                     - **Contacto:** [LinkedIn](https://www.linkedin.com/in/lightdaycarrillo)
                    ''', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Contribuidor: Laura Estefanía Valbuena Roa
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image("laura.png", width=120)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.markdown('''**Laura Estefanía Valbuena Roa**   
                     - **Profesión :** Ingeniera Telematica y Analista de datos    
                     - **Rol en el Proyecto:** Análisis de datos y diseño del modelo de IA        
                     - **Contacto:** [LinkedIn](https://www.linkedin.com/in/laura-estefania-valbuena-roa-234068168/)
                    ''', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Contribuidor: Alejandra Ivone Arias
    col1, col2 = st.columns([1, 4])
    with col1:
       st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
       st.image("alejandra.png", width=120)
       st.markdown("</div>", unsafe_allow_html=True)
    with col2:
       st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
       st.markdown('''**Alejandra Ivone Arias**  
        - **Profesión:** Especialista en Ingeniería de Sistemas de Información y Consultora BI  
        - **Rol en el Proyecto:** Análisis de datos y desarrollo front-end        
        - **Contacto:** [LinkedIn](https://www.linkedin.com/in/alejandra-ivone-arias/)
         ''', unsafe_allow_html=True)
       st.markdown("</div>", unsafe_allow_html=True)

# Contribuidor: Kelyn Botina Trujillo
    col1, col2 = st.columns([1, 4])
    with col1:
       st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
       st.image("kelyn.png", width=120)
       st.markdown("</div>", unsafe_allow_html=True)
    with col2:
       st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
       st.markdown('''**Kelyn Botina Trujillo**   
        - **Profesión:** Ingeniera en Automática Industrial e Investigadora en Análisis de Datos  
        - **Rol en el Proyecto:** Documentación, Validación y optimización del modelo predictivo.
        - **Contacto:** [LinkedIn](https://www.linkedin.com/in/ingkelynbt/)''', unsafe_allow_html=True)
       st.markdown("</div>", unsafe_allow_html=True)


    
    st.markdown("### Agradecimientos Especiales")
    st.markdown(
    """
    <div style="text-align: left;">
        <div style="text-align: center;">
            <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjY3MXVqbGo4cXVubDVxYmVocnZodHpveHVsYm11dHBxMnJ4ZnBmNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jnWME57yUdqJFr8lH0/giphy.webp" width="300">
            <h3 style="text-align: center;"> Programa M1000IA </h3>
         </div>
        <p>
        Queremos expresar nuestro más profundo agradecimiento al <strong>Programa M1000IA</strong>, 
        a la <strong>UTN</strong>, y a las <strong>empresas colaboradoras</strong> por brindarnos 
        la oportunidad de adquirir <strong>conocimientos fundamentales en inteligencia artificial</strong>. 
        Esta experiencia no solo ha ampliado nuestras competencias, sino que también nos permitió 
        participar en el desarrollo del proyecto <strong>"Leukemia IA"</strong>.
        </p>
        <p>
        Este proyecto, enfocado en el <strong>diagnóstico y clasificación de leucemias</strong> mediante 
        el análisis de muestras de médula ósea, representa un <strong>avance significativo</strong> en la aplicación 
        de IA en el sector salud. Sin la formación y el acompañamiento del programa, no habría sido posible 
        alcanzar este logro.
        </p>
        <p>
        Agradecemos especialmente el <strong>compromiso de los tutores y el equipo del programa</strong> por su dedicación, 
        apoyo constante y por motivarnos a desarrollar <strong>soluciones con impacto social y valor práctico</strong>. 
        Esta experiencia ha marcado un paso importante en nuestro crecimiento profesional dentro del 
        campo de la <strong>IA aplicada</strong>.
        </p>
    </div>
    """, 
    unsafe_allow_html=True 
    )
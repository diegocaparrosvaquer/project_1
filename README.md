# Transit Shift & Ticket Analytics

Este proyecto es un asistente de inteligencia artificial enfocado en el análisis de turnos y tickets para el sector de transporte. Permite a los usuarios cargar archivos CSV, realizar consultas en lenguaje natural y obtener resultados en forma de tablas, resúmenes y gráficos.

## Descripción

El sistema se desarrolla en Python y hace uso exclusivo de Pandas para la manipulación, limpieza y análisis de datos. La aplicación permite:
- Cargar y validar archivos CSV con hasta 200.000 entradas.
- Realizar operaciones de análisis utilizando consultas en lenguaje natural, que se traducen en operaciones sobre DataFrames.
- Generar visualizaciones interactivas y exportar resultados a diferentes formatos (CSV, PDF, HTML).

El enfoque modular del proyecto facilita la escalabilidad y mantenimiento, permitiendo añadir nuevas funcionalidades o ampliar las consultas según las necesidades del usuario.

## Estructura del Proyecto
Proyecto_TransitAnalytics/
├── data/
│ └── sample.csv # Archivos CSV de ejemplo o de producción.
├── notebooks/
│ └── Exploratory_Analysis.ipynb # Notebooks para análisis exploratorio y pruebas interactivas.
├── src/
│ ├── init.py
│ ├── data_loader.py # Funciones para la carga de archivos CSV usando Pandas.
│ ├── data_cleaner.py # Módulos para la limpieza y preprocesamiento de los datos.
│ ├── analysis.py # Funciones para realizar consultas, filtrados y cálculos estadísticos.
│ ├── query_parser.py # Mapeo de consultas en lenguaje natural a operaciones en Pandas.
│ ├── visualizations.py # Generación de gráficos y visualizaciones (Matplotlib o Plotly).
│ └── exporter.py # Exportación de resultados a CSV, PDF o HTML.
├── main.py # Punto de entrada de la aplicación, integrando todos los módulos.
├── requirements.txt # Lista de dependencias del proyecto.
└── README.md # Este archivo de documentación.

## Tecnologías Utilizadas

- **Python:** Lenguaje principal de desarrollo.
- **Pandas:** Manipulación y análisis de datos.
- **NumPy:** Operaciones numéricas y manejo de arrays.
- **Streamlit (opcional):** Aplicación web interactiva para carga de archivos y visualización.
- **Matplotlib / Plotly:** Generación de gráficos y dashboards.
- **Jupyter Notebooks:** Análisis exploratorio e iteración de prototipos.

## Cómo Empezar

1. **Clonar el repositorio:**
bash
git clone https://github.com/tu_usuario/TransitShiftTicketAnalytics.git
cd TransitShiftTicketAnalytics

2. **Instalar dependencias:**

   Es recomendable crear un entorno virtual:
bash
python -m venv venv
source venv/bin/activate # En Linux/Mac
venv\Scripts\activate # En Windows

   Instalar las librerías:
bash
pip install -r requirements.txt

3. **Ejecutar la Aplicación:**

   Dependiendo de la implementación, puedes arrancar la aplicación mediante:
bash
python main.py

   O, si usas Streamlit para la interfaz web:
bash
streamlit run main.py

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue las buenas prácticas de Git y asegúrate de realizar pruebas antes de proponer cambios. Si deseas añadir nuevas funcionalidades o mejoras, abre un "issue" o envía un "pull request".

## Licencia

[GNU Affero General Public License v3.0] - Detalles sobre la licencia del proyecto.

## Contacto

- **Autor:** [Diegco Caparros Vaquer]
- **Email:** [diegocaparrosvaquer@gmail.com]

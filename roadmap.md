# Roadmap de Transit Shift & Ticket Analytics

Este documento describe el roadmap para el desarrollo del proyecto, el cual permite el análisis de archivos CSV (turnos, tickets, tarifas, etc.) utilizando Pandas. El sistema responde a consultas en lenguaje natural, generando visualizaciones y exportando resultados.

---

## 1. Fase de Planificación e Investigación (Semanas 1-2)

- **
Definición de Objetivos y Alcance:
**  
  - Establecer las preguntas que responderá el sistema (por ejemplo, “¿Cuántos tickets vendió JUAN FRANCISCO en mayo?”, “¿Cuál es la tarifa promedio por línea?”, etc.).  
  - Determinar el alcance del análisis con archivos CSV de aproximadamente 200.000 registros.  
  - Definir la experiencia de usuario final y las funcionalidades a desarrollar.

- **
Selección de Tecnologías:
**  
  - Lenguaje de programación: **
Python
**.  
  - Procesamiento y análisis de datos: **
Pandas
**, **
NumPy
**.  
  - Visualización: **
Matplotlib
** o **
Plotly
**.  
  - Interfaz de usuario: **
Streamlit
** (o alternativas como Flask para una solución más personalizada).

- **
Diseño Arquitectónico y Estructura del Proyecto:
**  
  - Definir el flujo de datos: carga → validación/limpieza → análisis → visualización/exportación.  
  - Establecer la estructura modular del proyecto (módulos de carga, limpieza, análisis, parseo de consultas, visualizaciones y exportación).

---

## 2. Fase de Procesamiento y Limpieza de Datos (Semanas 3-5)

- **
Carga del CSV:
**  
  - Implementar el módulo `data_loader.py` para leer y cargar archivos CSV con Pandas.  
  - Gestionar la optimización de la carga (uso de `dtype` y procesamiento en chunks si es necesario).

- **
Limpieza y Normalización de Datos:
**  
  - Desarrollar el módulo `data_cleaner.py` para corregir problemas de codificación y gestionar valores nulos.  
  - Estandarizar formatos (fechas, números y textos) según requiera el análisis.

- **
Validación Inicial:
**  
  - Realizar pruebas con archivos de ejemplo para verificar la integridad de la carga y la limpieza de los datos.

---

## 3. Fase de Desarrollo del Motor de Análisis y Consulta (Semanas 6-9)

- **
Creación del Módulo de Análisis:
**  
  - Desarrollar el módulo `analysis.py` con funciones que permitan filtrar, agrupar y calcular métricas (sumatorias, promedios, conteos, etc.) utilizando Pandas.

- **
Implementación del Parseo de Consultas en Lenguaje Natural:
**  
  - Crear el módulo `query_parser.py` que mapee consultas en lenguaje natural a operaciones sobre DataFrames.  
  - Desarrollar reglas y plantillas para interpretar consultas comunes y probar ejemplos.

- **
Optimización del Procesamiento:
**  
  - Ajustar el rendimiento de las operaciones con Pandas para manejar eficientemente los ~200.000 registros.

---

## 4. Fase de Desarrollo de la Interfaz de Usuario y Visualizaciones (Semanas 10-12)

- **
Diseño e Implementación de la Interfaz:
**  
  - Desarrollar la interfaz interactiva con **
Streamlit
** que permita:
    - La carga de archivos CSV.
    - La entrada de consultas en lenguaje natural.
    - La visualización de resultados en tablas y gráficos.

- **
Generación de Visualizaciones:
**  
  - Desarrollar el módulo `visualizations.py` para crear gráficos mediante Matplotlib o Plotly que faciliten la interpretación de los resultados.

- **
Funcionalidad de Exportación:
**  
  - Implementar el módulo `exporter.py` para exportar los resultados a formatos como CSV, PDF o HTML.

---

## 5. Fase de Pruebas, Feedback y Optimización (Semanas 13-15)

- **
Pruebas Funcionales y de Integración:
**  
  - Ejecutar pruebas completas del sistema, desde la carga del CSV hasta la exportación de resultados.

- **
Feedback de Usuarios:
**  
  - Organizar sesiones de prueba con usuarios internos para evaluar la usabilidad, rendimiento y precisión del sistema.

- **
Ajustes y Optimización:
**  
  - Recoger feedback y refinar tanto la eficiencia del procesamiento (optimización del uso de memoria y tiempos de respuesta) como la experiencia de usuario.

---

## 6. Fase de Despliegue y Mantenimiento (Semanas 16 en adelante)

- **
Documentación y Capacitación:
**  
  - Crear y actualizar la documentación técnica y funcional del proyecto.  
  - Realizar sesiones de formación para el equipo y usuarios finales.

- **
Despliegue en Producción:
**  
  - Desplegar el sistema en un entorno de producción, asegurando su estabilidad y rendimiento óptimo.

- **
Seguimiento y Actualizaciones:
**  
  - Establecer reuniones periódicas para monitorear el desempeño del sistema y planificar futuras mejoras o nuevas funcionalidades.

---

Este roadmap define un plan claro y estructurado para el desarrollo del proyecto de análisis de CSV utilizando Pandas. Podrás ajustarlo en función del progreso y feedback recibido durante cada fase.

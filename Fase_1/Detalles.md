### Objetivos y Alcance del Sistema

A continuación se detalla lo que se espera que el sistema responda, el alcance del análisis y la experiencia de usuario final:

---

#### 1. Preguntas que responderá el sistema

El sistema estará diseñado para contestar preguntas clave relacionadas con turnos, tickets y tarifas. Algunos ejemplos de preguntas son:

- **
Tickets y Ventas:
**
  - ¿Cuántos tickets vendió JUAN FRANCISCO en mayo?
  - ¿Cuántos boletos se emitieron en total durante un mes específico?

- **
Tarifas y Cobros:
**
  - ¿Cuál es la tarifa promedio por línea?
  - ¿Qué porcentaje de los viajes se cobró de forma completa vs. parcial (indicando casos donde el importe cobrado difiere del importe facturado)?

- **
Análisis de Rutas:
**
  - ¿Cuál es la línea o ruta con mayor volumen de viajes?
  - ¿Qué rutas tienen mayor incidencia de viajes "sin cobrar" o con problemas de cobro?

- **
Pagos y Transacciones:
**
  - ¿Cuáles son los totales de importes cobrados por cada tipo de tarifa?
  - ¿Cuántas transacciones se realizaron utilizando tarjetas o Bono en comparación con otros métodos?

- **
Anomalías e Indicadores:
**
  - ¿Existen discrepancias notables entre el importe facturado y el cobrado?
  - ¿Cuáles son los casos atípicos (por ejemplo, importes nulos o discrepantes, saldos inconsistentes en Bono)?

---

#### 2. Alcance del Análisis

- **
Volumen de Datos:
**  
  El sistema gestionará archivos CSV que contengan aproximadamente 200.000 registros, lo que implica desarrollar estrategias de carga y procesamiento eficientes (por ejemplo, uso de procesamiento en *
chunks
* o especificación de tipos de datos precisos).

- **
Calidad y Variedad de Datos:
**  
  - Los CSV pueden presentar problemas de codificación y formatos mixtos en campos de fecha, numéricos y textos que deberán ser corregidos durante la fase de limpieza.
  - El análisis abarcará múltiples dimensiones como tiempos, rutas, tipos de tarifa y métodos de pago, permitiendo generar informes detallados y resúmenes estadísticos.

- **
Escalabilidad:
**  
  Aunque el volumen inicial es de 200.000 registros, el sistema debe diseñarse para ser escalable, de forma que se pueda ampliar el análisis en función de futuros incrementos en la cantidad de información.

---

#### 3. Experiencia de Usuario y Funcionalidades a Desarrollar

- **
Interfaz de Usuario:
**  
  - **
Carga de Datos:
** El usuario podrá subir archivos CSV mediante una interfaz intuitiva (por ejemplo, utilizando **
Streamlit
**).  
  - **
Consulta en Lenguaje Natural:
** La aplicación ofrecerá un campo de entrada donde el usuario pueda escribir consultas de forma natural (por ejemplo, "¿Cuántos tickets vendió JUAN FRANCISCO en mayo?") y el sistema interpretará y ejecutará la consulta.
  - **
Visualización Dinámica:
** Los resultados se mostrarán en tablas interactivas y gráficos, facilitando la interpretación visual de los datos.

- **
Funcionalidades Clave:
**  
  - **
Limpieza y Validación Automática:
** Procesos automatizados para corregir errores de codificación, estandarizar formatos y gestionar datos faltantes o inconsistentes.
  - **
Análisis y Reportes:
**  
    - Resúmenes y cálculos estadísticos (totales, promedios, máximos/mínimos, porcentajes).  
    - Visualizaciones interactivas (barras, líneas, gráficos de distribución) para entender tendencias y patrones.
  - **
Exportación de Resultados:
** Los usuarios podrán exportar los resultados del análisis en diversos formatos (CSV, PDF o HTML), facilitando el uso del reporte en otras herramientas o presentaciones.
  - **
Detección de Anomalías:
** Identificación y etiquetado automático de comportamientos atípicos (por ejemplo, importes inconsistentes, falta de cobro, registros duplicados).

- **
Usabilidad y Accesibilidad:
**  
  - La interfaz será diseñada para ser amigable y accesible, con instrucciones claras y flujos de interacción sencillos, permitiendo a usuarios no técnicos utilizar la herramienta.
  - Se integrarán elementos de ayuda contextual y documentación en línea para orientar al usuario en el uso de las funcionalidades.

---

Esta definición de objetivos y alcance ayudará a guiar el desarrollo del sistema, asegurando que se aborden las necesidades analíticas y se optimice la experiencia del usuario final.

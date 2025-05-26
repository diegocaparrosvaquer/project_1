## Fase de Procesamiento y Limpieza de Datos (Semanas 3-5)

En esta fase se enfocará en asegurar que los datos del CSV se carguen correctamente y estén limpios para el análisis. A continuación se plantean los procedimientos y ejemplos de código para cada parte:

---

### **1. Carga del CSV**

**
Objetivo:
**  
Implementar el módulo `data_loader.py` para leer y cargar archivos CSV utilizando Pandas, optimizando la carga mediante la especificación de tipos de datos y, en caso de ser necesario, utilizando procesamiento en *
chunks
*.

**
Procedimientos y Ejemplo de Código:
**

- **
Especificar Tipos de Datos:
**  
  Definir un diccionario `dtype` para reducir el uso de memoria y acelerar la lectura.

- **
Carga en 
*
Chunks
*
 (si el archivo es muy grande):
**  
  Utilizar el parámetro `chunksize` de `pd.read_csv()` para procesar el archivo en partes.

**
Ejemplo en 
`data_loader.py`
:
**
python
import pandas as pd

def load_csv(file_path, use_chunks=False, chunksize=50000):
# Define dtypes para columnas (ajustar según la estructura real del CSV)
dtypes = {
"Fecha y hora": "str",
"Máquina": "int64",
"Conductor": "str",
"Vehículo": "int64",
"Línea": "int64",
"Sub-línea": "int64",
"Salida del viaje": "str", # Convertir a datetime posteriormente si es necesario
"Núm. Boleto": "int64",
"Origen": "str",
"Destino": "str",
"Tarifa": "str",
"Importe": "float",
"Cobrado": "float",
"Tarjeta": "str",
"Bono": "str",
"Saldo": "str",
"eTicket": "str"
}

if use_chunks:
    chunks = []
    for chunk in pd.read_csv(file_path, sep="\t", 
                             dtype=dtypes, 
                             chunksize=chunksize, 
                             encoding="utf-8"):
        chunks.append(chunk)
    df = pd.concat(chunks, ignore_index=True)
else:
    df = pd.read_csv(file_path, sep="\t", dtype=dtypes, encoding="utf-8")

return df
Ejemplo de uso:
if name == "main":
df = load_csv("path/to/your/file.csv", use_chunks=True)
print(df.head())

*Notas:*  
- Cambia el separador `sep` si tu CSV no usa tabulaciones (`\t`), por ejemplo, puede ser una coma (`,`) o punto y coma (`;`).  
- Verifica la codificación (por ejemplo, `utf-8`) para evitar problemas con caracteres especiales.

---

### **2. Limpieza y Normalización de Datos**

**Objetivo:**  
Desarrollar el módulo `data_cleaner.py` para corregir problemas de codificación, gestionar valores nulos y estandarizar formatos (fechas, números y textos).

**Procedimientos y Ejemplo de Código:**

- **Corrección de Codificación y Nombres de Columnas:**  
  Asegurarse de que los nombres de las columnas sean legibles y estandarizados (por ejemplo, "Máquina" en lugar de "M�quina").

- **Conversión de Formatos:**  
  Convertir campos de fecha a `datetime`, números a `float` o `int` y asegurarse de que el texto esté en un formato uniforme.

- **Gestión de Valores Nulos:**  
  Rellenar valores nulos o eliminarlos según la relevancia del dato.

**Ejemplo en `data_cleaner.py`:**
python
import pandas as pd

def rename_columns(df):
# Renombrar columnas mal codificadas o inconsistentes
df.rename(columns=lambda x: x.strip().replace("�", "á"), inplace=True)
return df

def convert_date_columns(df):
# Convertir la columna 'Fecha y hora' a datetime
df["Fecha y hora"] = pd.to_datetime(df["Fecha y hora"], errors="coerce")
return df

def fill_missing_values(df):
# Ejemplo: rellenar valores nulos en columnas numéricas y de texto
numeric_cols = ["Importe", "Cobrado"]
for col in numeric_cols:
df[col] = pd.to_numeric(df[col], errors="coerce")
df[col].fillna(0, inplace=True)

text_cols = ["Conductor", "Tarifa", "Origen", "Destino"]
for col in text_cols:
    df[col] = df[col].fillna("Desconocido")

return df
def clean_data(df):
df = rename_columns(df)
df = convert_date_columns(df)
df = fill_missing_values(df)
# Aquí se pueden incluir más procedimientos de limpieza según se necesite.
return df

Ejemplo de uso:
if name == "main":
# Supongamos que ya tenemos el DataFrame cargado
import data_loader # Asegúrate de que data_loader.py esté en el mismo directorio o en el path
df = data_loader.load_csv("path/to/your/file.csv", use_chunks=False)
df_clean = clean_data(df)
print(df_clean.head())

---

### **3. Validación Inicial**

**Objetivo:**  
Realizar pruebas con archivos de ejemplo para verificar la integridad de la carga y la limpieza de los datos. Asegurarse de que las transformaciones se han aplicado correctamente.

**Procedimientos:**

- **Testeo Manual:**  
  - Cargar un archivo de ejemplo pequeño y observar los primeros registros.
  - Verificar manualmente que los datos (fechas, números y textos) se han convertido y limpiado correctamente.

- **Testeo Automatizado:**  
  - Implementar pruebas unitarias (usando, por ejemplo, `pytest`) para validar funciones específicas del proceso de carga y limpieza.

**Ejemplo Simple de Validación en un Script de Prueba:**
python
import data_loader
import data_cleaner

def test_data_loading_and_cleaning(file_path):
# Cargar datos
df = data_loader.load_csv(file_path, use_chunks=False)

# Validar cantidad de registros
assert not df.empty, "El DataFrame está vacío."

# Aplicar limpieza
df_clean = data_cleaner.clean_data(df)

# Verificar que la columna 'Fecha y hora' se ha convertido a datetime
assert pd.api.types.is_datetime64_any_dtype(df_clean["Fecha y hora"]), "La columna 'Fecha y hora' no se ha convertido correctamente."

# Verificar que no existan valores nulos en columnas críticas, por ejemplo, 'Importe'
assert df_clean["Importe"].isnull().sum() == 0, "Existen valores nulos en la columna 'Importe'."

print("Pruebas completadas exitosamente.")
if name == "main":
test_data_loading_and_cleaning("path/to/your/file.csv")

Estos procedimientos y ejemplos de código te permiten establecer una robusta fase de procesamiento y limpieza de datos, garantizando que antes de la fase de análisis, los datos estén estructurados, limpios y en un formato consistente para el procesamiento con Pandas.

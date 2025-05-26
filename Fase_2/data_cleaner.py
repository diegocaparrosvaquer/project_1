import pandas as pd

def rename_columns(df):
    # Corregir columnas mal codificadas y limpiar espacios
    df.rename(columns=lambda x: x.strip()
              .replace("�", "á")
              .replace("N�", "Nú")
              .replace("M�", "Má")
              .replace("Veh�culo", "Vehículo")
              .replace("L�nea", "Línea")
              .replace("Sub-l�nea", "Sub-línea"), inplace=True)
    return df

def convert_date_columns(df):
    # Convertir 'Fecha y hora' con formato día/mes/año hora:minuto
    df["Fecha y hora"] = pd.to_datetime(df["Fecha y hora"], format="%d/%m/%Y %H:%M", errors="coerce")
    return df

def convert_numeric_columns(df):
    # Convertir columnas monetarias que usan coma decimal a float
    for col in ["Importe", "Cobrado"]:
        # Reemplazar coma decimal por punto y convertir a float
        df[col] = df[col].str.replace(",", ".", regex=False)
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

    # Convertir columnas numéricas que pueden tener NaNs a Int64 nullable
    for col in ["Máquina", "Vehículo", "Línea", "Sub-línea", "Nú Boleto"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    return df

def fill_missing_values(df):
    # Rellenar valores nulos en columnas de texto con 'Desconocido'
    text_cols = ["Conductor", "Tarifa", "Origen", "Destino", "Tarjeta", "Bono", "Saldo", "eTicket"]
    for col in text_cols:
        df[col] = df[col].fillna("Desconocido")

    return df

def clean_data(df):
    df = rename_columns(df)
    df = convert_date_columns(df)
    df = convert_numeric_columns(df)
    df = fill_missing_values(df)

    # Limpieza adicional: eliminar espacios al final en 'Conductor' y otros textos
    df["Conductor"] = df["Conductor"].str.strip().str.replace("\\", "", regex=False)

    return df

if __name__ == "__main__":
    import data_loader
    df = data_loader.load_csv("path/to/your/file.csv", use_chunks=False)
    df_clean = clean_data(df)
    print(df_clean.head())

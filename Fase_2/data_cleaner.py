import pandas as pd

def rename_columns(df):
    # Corrige nombres mal codificados y limpia espacios
    df.rename(
        columns=lambda x: (
            x.strip()
             .replace("�", "á")
             .replace("N�", "Nú")
             .replace("M�", "Má")
             .replace("Veh�culo", "Vehículo")
             .replace("L�nea", "Línea")
             .replace("Sub-l�nea", "Sub-línea")
             .replace("N�", "Nú")
        ),
        inplace=True,
    )
    return df

def convert_date_columns(df):
    # Convierte fecha con formato día/mes/año hora:minuto
    df["Fecha y hora"] = pd.to_datetime(
        df["Fecha y hora"], format="%d/%m/%Y %H:%M", errors="coerce"
    )
    return df

def convert_numeric_columns(df):
    # Corrige coma decimal y convierte a float
    for col in ["Importe", "Cobrado"]:
        if col in df.columns:
            df[col] = df[col].str.replace(",", ".", regex=False)
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

    # Convertir columnas a enteros nulos (Int64)
    for col in ["Máquina", "Vehículo", "Línea", "Sub-línea", "Nú Boleto"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    return df

def clean_text_columns(df):
    text_cols = ["Conductor", "Tarifa", "Origen", "Destino", "Tarjeta", "Bono", "Saldo", "eTicket"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].fillna("Desconocido").astype(str).str.strip()
            # Eliminar barras invertidas sobrantes
            df[col] = df[col].str.replace("\\", "", regex=False)
    return df

def clean_data(df):
    df = rename_columns(df)
    df = convert_date_columns(df)
    df = convert_numeric_columns(df)
    df = clean_text_columns(df)
    return df


if __name__ == "__main__":
    import data_loader

    df = data_loader.load_csv("datos_ejemplo.csv")
    df_clean = clean_data(df)
    print(df_clean.info())
    print(df_clean.head())

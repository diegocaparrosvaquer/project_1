import pandas as pd

def load_csv(file_path, use_chunks=False, chunksize=50000):
    """
    Carga un CSV usando pandas, optimizando tipos de datos.
    Soporta carga en chunks para archivos grandes.
    """
    # Definición de tipos para optimizar memoria
    dtypes = {
        "Máquina": "Int64",
        "Conductor": "string",
        "Vehículo": "Int64",
        "Línea": "Int64",
        "Sub-línea": "Int64",
        "Nú Boleto": "Int64",
        "Tarifa": "string",
        "Importe": "string",  # Se limpiará después
        "Cobrado": "string",  # Se limpiará después
        "Tarjeta": "string",
        "Bono": "string",
        "Saldo": "string",
        "eTicket": "string"
    }

    if use_chunks:
        chunks = []
        for chunk in pd.read_csv(
            file_path, sep="\t", dtype=dtypes, chunksize=chunksize, encoding="utf-8"
        ):
            chunks.append(chunk)
        df = pd.concat(chunks, ignore_index=True)
    else:
        df = pd.read_csv(file_path, sep="\t", dtype=dtypes, encoding="utf-8")

    return df


if __name__ == "__main__":
    # Prueba carga directa
    df = load_csv("datos_ejemplo.csv")
    print(df.head())


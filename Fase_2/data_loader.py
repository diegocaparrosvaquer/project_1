import pandas as pd

def load_csv(file_path, use_chunks=False, chunksize=50000):
    dtypes = {
        "Fecha y hora": "str",
        "Máquina": "Int64",
        "Conductor": "str",
        "Vehículo": "Int64",
        "Línea": "Int64",
        "Sub-línea": "Int64",
        "Salida del viaje": "str",
        "N� Boleto": "Int64",
        "Origen": "str",
        "Destino": "str",
        "Tarifa": "str",
        "Importe": "str",  # Lo cargamos como str para limpiar coma decimal después
        "Cobrado": "str",  # Igual que Importe
        "Tarjeta": "str",
        "Bono": "str",
        "Saldo": "str",
        "eTicket": "str"
    }

    if use_chunks:
        chunks = []
        for chunk in pd.read_csv(file_path, sep="\t", dtype=dtypes, 
                                 chunksize=chunksize, encoding="utf-8"):
            chunks.append(chunk)
        df = pd.concat(chunks, ignore_index=True)
    else:
        df = pd.read_csv(file_path, sep="\t", dtype=dtypes, encoding="utf-8")

    return df

if __name__ == "__main__":
    df = load_csv("path/to/your/file.csv", use_chunks=False)
    print(df.head())

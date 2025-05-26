import pandas as pd

def tickets_vendidos_por_mes(df, vendedor, año, mes):
    df['Fecha y hora'] = pd.to_datetime(df['Fecha y hora'])
    filtro = (df['Conductor'] == vendedor) & \
             (df['Fecha y hora'].dt.year == año) & \
             (df['Fecha y hora'].dt.month == mes)
    return df.loc[filtro, 'Nº Boleto'].nunique()

def boletos_emitidos_total_mes(df, año, mes):
    df['Fecha y hora'] = pd.to_datetime(df['Fecha y hora'])
    filtro = (df['Fecha y hora'].dt.year == año) & (df['Fecha y hora'].dt.month == mes)
    return df.loc[filtro, 'Nº Boleto'].count()

def tarifa_promedio_por_linea(df):
    return df.groupby('Línea')['Tarifa'].mean()

def porcentaje_cobro_completo_vs_parcial(df):
    total = len(df)
    completo = (df['Importe'] == df['Cobrado']).sum()
    parcial = (df['Importe'] != df['Cobrado']).sum()
    return {
        'completo': completo / total * 100,
        'parcial': parcial / total * 100
    }

def linea_con_mayor_volumen_viajes(df):
    return df['Línea'].value_counts().idxmax()

def rutas_con_mayor_viajes_sin_cobrar(df):
    df_sin_cobro = df[df['Cobrado'] == 0]
    return df_sin_cobro['Línea'].value_counts()

def totales_cobrados_por_tipo_tarifa(df):
    return df.groupby('Tarifa')['Cobrado'].sum()

def transacciones_por_metodo_pago(df):
    tarjeta = df['Tarjeta'].notna().sum()
    bono = df['Bono'].notna().sum()
    otros = len(df) - tarjeta - bono
    return {'Tarjeta': tarjeta, 'Bono': bono, 'Otros': otros}

def discrepancias_importe_vs_cobrado(df):
    discrepancias = df[df['Importe'] != df['Cobrado']]
    return discrepancias

def casos_atipicos(df):
    # Ejemplo básico: importes nulos o saldo negativo en Bono
    return df[(df['Importe'].isna()) | (df['Saldo'] < 0)]

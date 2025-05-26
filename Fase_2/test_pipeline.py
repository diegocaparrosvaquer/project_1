import data_loader
import data_cleaner

def test_load_and_clean():
    df = data_loader.load_csv("datos_ejemplo.csv")
    print("Datos cargados:", df.shape)

    df_clean = data_cleaner.clean_data(df)
    print("Datos limpios:", df_clean.shape)

    # Verificamos que no haya fechas nulas
    assert df_clean["Fecha y hora"].notna().all(), "Fecha con valores nulos!"

    # Verificamos que importe y cobrado sean numéricos positivos o cero
    assert (df_clean["Importe"] >= 0).all(), "Importe tiene valores negativos!"
    assert (df_clean["Cobrado"] >= 0).all(), "Cobrado tiene valores negativos!"

    print("Validación inicial completada correctamente.")

if __name__ == "__main__":
    test_load_and_clean()

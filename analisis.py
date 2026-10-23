import pandas as pd


def resumir_entrevistas_por_estudiante(dataframe):
    """Agrupa la información por estudiante para resumir cuántas veces ha solicitado

    una entrevista y cuándo fue su registro más reciente.
    """
    # Nombres de columnas idénticos a tu Google Sheets
    col_nombre = "Nombre del Estudiante o Apoderado"
    col_fecha = "Marca temporal"

    if col_nombre not in dataframe.columns or col_fecha not in dataframe.columns:
        return "Error: No se encuentran las columnas de Nombre o Marca temporal."

    # Normalizar nombres de los estudiantes (quitar espacios vacíos y poner formato Título)
    df_limpio = dataframe.copy()
    df_limpio[col_nombre] = (
        df_limpio[col_nombre].astype(str).str.strip().str.title()
    )

    # Agrupar por estudiante, contar citas y obtener la fecha más reciente
    resumen_estudiantes = (
        df_limpio.groupby(col_nombre)
        .agg(Total_Citas=(col_nombre, "count"), Ultimo_Registro=(col_fecha, "max"))
        .reset_index()
    )

    # Renombrar la columna para que se vea ordenada en la terminal
    resumen_estudiantes.columns = [
        "Estudiante / Apoderado",
        "Total de Citas",
        "Último Registro",
    ]

    # Ordenar de mayor a menor número de solicitudes
    resumen_estudiantes = resumen_estudiantes.sort_values(
        by="Total de Citas", ascending=False
    )

    return resumen_estudiantes

from conexion_sheets import obtener_datos
import pandas as pd  # Asegúrate de dejar este import aquí arriba si no estaba al inicio

# 1. Traer los registros
datos_crudos = obtener_datos()

# 2. Convertirlos a DataFrame de Pandas
df = pd.DataFrame(datos_crudos)

# 3. Mostrar la tabla resumen en la consola
print("\n=== MOSTRANDO EL RESUMEN DE ESTUDIANTES ===")
resultado = resumir_entrevistas_por_estudiante(df)
print(resultado)

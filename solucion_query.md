import sqlite3
import pandas as pd

# Conecta a la base de datos SQLite
conn = sqlite3.connect("tu_base_de_datos.db")

# Define la consulta SQL que combina las dos tablas utilizando un JOIN
query = """
SELECT D.*, DIM.Calidad_del_Aire
FROM Demografia AS D
JOIN Dimensiones AS DIM ON D.City = DIM.Nombre_de_Ciudad
"""

# Ejecuta la consulta y carga los resultados en un DataFrame
result = pd.read_sql_query(query, conn)

# Muestra las primeras 10 columnas
print(result.iloc[:, :10])


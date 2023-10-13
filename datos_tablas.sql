import sqlite3

conn = sqlite3.connect("tu_base_de_datos.db")
cursor = conn.cursor()

# Comando SQL para crear la tabla de demografía
create_table_demografia = """
CREATE TABLE Demografia (
    City TEXT,
    State TEXT,
    Median Age REAL,
    Female Population INTEGER,
    Male Population INTEGER,
    Total Population INTEGER,
    Foreign-born INTEGER,
    State Code TEXT,
    Race INT,
    Race INT,
    Count INT,
    Number of Veterans INT
);
"""

# Comando SQL para crear la tabla de dimensiones
create_table_dimensiones = """
CREATE TABLE Dimensiones (
    Nombre_de_Ciudad TEXT,
    Calidad_del_Aire REAL
);
"""

# Ejecuta los comandos SQL
cursor.execute(create_table_demografia)
cursor.execute(create_table_dimensiones)


tabla_demografia.to_sql('Demografia', conn, if_exists='replace', index=False)
tabla_dimensiones.to_sql('Dimensiones', conn, if_exists='replace', index=False)


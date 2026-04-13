
análisis de datos en batch utilizando Apache Spark.
El problema que se quiere analizar es el comportamiento de los precios 
de viviendas.El conjunto de datos utilizado es un dataset de viviendas, 
el cual contiene información como precios, características y atributos de las 
casas.Este dataset fue seleccionado porque permite analizar patrones en los 
precios y realizar estadísticas descriptivas.

Aquí se carga el dataset en Spark utilizando un DataFrame, habilitando 
encabezados y detección automática de tipos de datos.

df = spark.read.csv("house_mini.csv", header=True, inferSchema=True)

Se visualizan los primeros registros para entender la estructura de los datos.

df.show()

Aquí se observa el esquema del dataset, es decir, los nombres de las columnas 
y sus tipos de datos.

df.printSchema()

Se realiza limpieza de datos eliminando valores nulos para mejorar la calidad 
del análisis.

df_clean = df.dropna()

Se visualizan los datos ya limpios.

df_clean.show()

Se realiza un análisis estadístico descriptivo, obteniendo medidas como 
promedio, mínimo y máximo.

df_clean.describe().show()

Aquí se filtran las viviendas con precios mayores a 100000 para analizar 
casos específicos.

df_clean.filter(df_clean.price > 100000).show()

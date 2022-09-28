import pandas as pd

tablaempleados=pd.read_csv('./empleados.csv')

#print(tablaempleados)
#print(tablaempleados.to_string())

#filtro 1 quiero obtener todos los datos de los analistas 1

tablaempleados1=tablaempleados[tablaempleados["cargo"]=="analista1"].head(50)
archivoHTML=tablaempleados1.to_html()

archivoTEXTO=open("datosanalista1.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()


'''tablaempleados2=tablaempleados[tablaempleados["cargo"]=="analista2"].head(50)
archivoHTML=tablaempleados2.to_html()

archivoTEXTO=open("datosanalista2.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()'''

#dataFrame[(dataFrame["salario"]>5900000) & (dataFrame["cargo"]=="analista2")]


'''tablaempleados3=tablaempleados[(tablaempleados["salario"]>4000000) & (tablaempleados["edad"]<30)].head(50)

archivoHTML=tablaempleados3.to_html()
archivoTEXTO=open("datosanalista3.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()'''



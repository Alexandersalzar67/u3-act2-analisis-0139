import pandas as pd
import numpy as np
print("Analisis de datos empleados Alexander Salazar nc =0139")

empleados = {
    "Empleado": ["Elena", "Sergio", "Lucia", "Gonzalo", "Valeria", "Diego"],
    "Departamento": ["Ventas", "IT", "HR", "IT", "Ventas", "Finanzas"],
     "Horas_Capacitacion": [40, 80, 25, 60, 90, 15],
    "Evaluacion_Desempeno": [8.5, 9.2, 7.0, 8.8, 9.6, 6.5]
}
df = pd.DataFrame(empleados)
print(df)
print("+-------Agrupar por una sola columna------+")
agrupado = df.groupby('Departamento')
print(agrupado)
print("+------Horas_Capacitacion-------+")
# Average salary by department
print(agrupado ['Horas_Capacitacion'].mean())
print("+------Evaluacion_Desempeno-------+")
# Maximum age in each department
print(agrupado ['Evaluacion_Desempeno'].max())
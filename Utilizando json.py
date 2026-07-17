import json

Datos_Estudiante= """ { "nombre":"Santiago", 
                   "nota1": "3.0", 
                   "nota2": "1.0", 
                   "nota3": "4.5"
}
"""
datos = json.loads(Datos_Estudiante)
print(f"nombre: {datos['nombre']}")
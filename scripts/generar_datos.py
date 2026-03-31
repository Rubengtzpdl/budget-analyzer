import pandas as pd
import numpy as np

np.random.seed(42)

categorias = ["Renta", "Comida", "Transporte", "Entretenimiento", 
              "Salud", "Ropa", "Servicios", "Educacion", "Ahorro", "Otros"]

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

data = []
for mes in meses:
    ingreso = np.random.randint(18000, 22000)
    for cat in categorias:
        limites = {
            "Renta": (5000, 6000), "Comida": (2000, 3500),
            "Transporte": (800, 1500), "Entretenimiento": (500, 2000),
            "Salud": (200, 800), "Ropa": (300, 1500),
            "Servicios": (500, 1000), "Educacion": (500, 1500),
            "Ahorro": (1000, 3000), "Otros": (200, 800)
        }
        gasto = np.random.randint(*limites[cat])
        data.append({"mes": mes, "categoria": cat, "gasto": gasto, "ingreso": ingreso})

df = pd.DataFrame(data)
df.to_excel("data/raw/gastos.xlsx", index=False)
print("Datos generados")
print(df.head(10))
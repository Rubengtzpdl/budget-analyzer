import pandas as pd

df = pd.read_excel("data/raw/gastos.xlsx")

# Resumen por categoría
resumen = df.groupby("categoria")["gasto"].agg(["sum", "mean", "max"]).round(2)
resumen.columns = ["total_anual", "promedio_mensual", "maximo_mensual"]
resumen = resumen.sort_values("total_anual", ascending=False)

# Ingreso vs gasto por mes
por_mes = df.groupby("mes").agg(
    total_gasto=("gasto", "sum"),
    ingreso=("ingreso", "first")
).reset_index()
por_mes["ahorro_real"] = por_mes["ingreso"] - por_mes["total_gasto"]
por_mes["tasa_ahorro_%"] = (por_mes["ahorro_real"] / por_mes["ingreso"] * 100).round(2)

# Clasificación de meses
def clasificar(tasa):
    if tasa >= 20: return "Excelente"
    elif tasa >= 10: return "Regular"
    else: return "Crítico"

por_mes["clasificacion"] = por_mes["tasa_ahorro_%"].apply(clasificar)

resumen.to_excel("data/processed/resumen_categorias.xlsx")
por_mes.to_excel("data/processed/resumen_mensual.xlsx", index=False)

print("Análisis completado")
print("\nGastos por categoría:")
print(resumen)
print("\nAhorro por mes:")
print(por_mes[["mes", "total_gasto", "ingreso", "ahorro_real", "tasa_ahorro_%", "clasificacion"]])
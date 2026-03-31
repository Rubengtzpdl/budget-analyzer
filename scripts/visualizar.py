import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
resumen = pd.read_excel("data/processed/resumen_categorias.xlsx")
por_mes = pd.read_excel("data/processed/resumen_mensual.xlsx")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Análisis de Presupuesto Personal 2025", fontsize=16, fontweight="bold")

# 1 - Gasto total por categoría
axes[0][0].barh(resumen["categoria"], resumen["total_anual"], color="#3498DB")
axes[0][0].set_title("Gasto Total Anual por Categoría")
axes[0][0].set_xlabel("MXN")

# 2 - Pie chart de distribución
axes[0][1].pie(resumen["total_anual"], labels=resumen["categoria"], autopct="%1.1f%%", startangle=90)
axes[0][1].set_title("Distribución de Gastos")

# 3 - Ingreso vs Gasto por mes
meses = por_mes["mes"]
x = range(len(meses))
axes[1][0].bar(x, por_mes["ingreso"], label="Ingreso", color="#2ECC71", alpha=0.7)
axes[1][0].bar(x, por_mes["total_gasto"], label="Gasto", color="#E74C3C", alpha=0.7)
axes[1][0].set_xticks(x)
axes[1][0].set_xticklabels(meses)
axes[1][0].set_title("Ingreso vs Gasto Mensual")
axes[1][0].legend()

# 4 - Tasa de ahorro
colores = ["#2ECC71" if t >= 20 else "#F39C12" if t >= 10 else "#E74C3C" 
           for t in por_mes["tasa_ahorro_%"]]
axes[1][1].bar(meses, por_mes["tasa_ahorro_%"], color=colores)
axes[1][1].axhline(y=20, color="green", linestyle="--", label="Meta 20%")
axes[1][1].axhline(y=10, color="orange", linestyle="--", label="Mínimo 10%")
axes[1][1].set_title("Tasa de Ahorro Mensual (%)")
axes[1][1].legend()

plt.tight_layout()
plt.savefig("reports/analisis_presupuesto.png", dpi=150)
plt.show()
print("✅ Visualizaciones guardadas")
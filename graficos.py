import matplotlib.pyplot as plt
from analisis import agrupar_por_producto, calcular_ventas, contar_registros
from conexion_sheets import obtener_datos

datos = obtener_datos()
resumen = agrupar_por_producto(datos)
total_reg = contar_registros(datos)
total_ven = calcular_ventas(datos)

productos = list(resumen.keys())
cantidades = list(resumen.values())
colores = ["#38B2F6", "#10B981", "#F59E0B", "#8B5CF6"]

# 1. PRIMER GRÁFICO: BARRAS
plt.figure(figsize=(7, 4))
plt.bar(
    productos, cantidades, color=colores[:len(productos)], edgecolor="black"
)

plt.title("1. Unidades Vendidas por Producto", fontsize=14, fontweight="bold")
plt.xlabel("Producto")
plt.ylabel("Unidades Vendidas")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

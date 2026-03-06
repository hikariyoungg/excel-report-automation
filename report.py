import pandas as pd

'''
Script básico para:
- Lea un excel
- Limpie los datos
- Calcula ingresos
- Genera un nuevo excel con el reporte de ventas

'''

# leer el archivo excel 
df = pd.read_excel('ventasNovaTechSupplies_Fic.xlsx')

# Limpiar los datos
df = df.dropna()  # Eliminar filas con valores nulos
df["ingreso"] = df["cantidad"] * df["precio_unitario"]

# Calcular ingresos totales por producto
ventas_producto = df.groupby("producto")["ingreso"].sum()
ventas_vendedor = df.groupby("vendedor")["ingreso"].sum()
total_ingresos = df["ingreso"].sum()

# Guardar el reporte en un nuevo archivo excel
with pd.ExcelWriter("reporte_ventas.xlsx") as writer:
    df.to_excel(writer, sheet_name="Datos Limpios", index=False)
    ventas_producto.to_excel(writer, sheet_name="Ventas por Producto")
    ventas_vendedor.to_excel(writer, sheet_name="Ventas por Vendedor")

print(" ✅ Reporte generado exitosamente: reporte_ventas.xlsx")
print(f"Total ingresos de ventas: ${total_ingresos:.2f}")

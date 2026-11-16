import json
import math

with open('data.json', 'r') as file:
    data = json.load(file)

#print(data)

#Total facturado

facturado_total=0
for item in data["ventas"]:
    facturado_id=item["cantidad"]*item["precio_unitario"]
    facturado_total += facturado_id
print('-Total Facturado:', round(facturado_total, 2), '€')

#Ventas por categoría

ventas_categoria={}
for item in data["ventas"]:
    categoria=item["categoria"]
    facturado_id=item["cantidad"]*item["precio_unitario"]
    if categoria not in ventas_categoria:
        ventas_categoria[categoria]=0
    ventas_categoria[categoria] += facturado_id

for cat in ventas_categoria:
    ventas_categoria[cat]=round(ventas_categoria[cat],2)
print("-Ventas por categoria:", ventas_categoria)    

#Producto mas vendido

unidades_producto={}
for item in data["ventas"]:
    producto = item["producto"]
    cantidad = item["cantidad"]
    if producto not in unidades_producto:
        unidades_producto[producto]=0
    unidades_producto[producto] += cantidad

prod_mas_vendido= ""
max_unidades=-math.inf
for prod, unidades in unidades_producto.items():
    if unidades>max_unidades:
        max_unidades=unidades
        prod_mas_vendido=prod
print("-El producto mas vendido es: ",  prod_mas_vendido, ", con " , max_unidades , " unidades.")
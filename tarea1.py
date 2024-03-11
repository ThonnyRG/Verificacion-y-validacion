def calcular_precio(cantidad):
    precio_base = 125
    costo_caja = 50
    descuento = 0
    if cantidad > 1000:
        descuento = 0.10
    elif cantidad > 100:
        descuento = 0.05
    cajas = (cantidad + 3) // 4
    precio_total = (precio_base * cantidad * (1 - descuento)) + (cajas * costo_caja)
    return precio_total, cajas, descuento

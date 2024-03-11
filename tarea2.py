def calcular_monedas(monto):
    monedas = [10, 5, 2, 1]
    resultado = []
    for moneda in monedas:
        cantidad = monto // moneda
        monto = monto % moneda
        resultado.append((moneda, cantidad))
    return resultado

monto = int(input ("ingresa la cantidad en pesos: "))
resultado = calcular_monedas(monto)
for moneda, cantidad in resultado:
    print("Monedas de $" + moneda + ":" + cantidad)
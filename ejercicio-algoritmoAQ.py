#Ejercicio auto eléctrico

positivos = [ 
{"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Corta" }, 
{ "edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "Si", "distancia_trabajo": "Media"}, 
{"edad": "Mayor", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Larga"}]

negativos = [ 
{"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "No", "distancia_trabajo": "Corta" }, 
{"edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "No", "distancia_trabajo": "Media"}, 
{"edad": "Mayor", "ingreso": "Bajo", "tiene_garaje": "No", "distancia_trabajo": "Larga"}] 

regla={}
atributos=[]
ejemplo=positivos[0]
for key in ejemplo:
    print("Clave: ",key)
    atributos.append(key)

for atributo in atributos:
    valores_positivos= []
    valores_negativos= []

    for ej in positivos:
        valor = ej[atributo]
        print("++valor: ", valor)
        if valor not in valores_positivos:
            valores_positivos.append(valor)

    for ej in negativos:
        valor = ej[atributo]
        print("--valor: ",valor)
        if valor not in valores_negativos:
            valores_negativos.append(valor)

    valores_validos=[]
    for valor in valores_positivos:
        encontrado = False
        for i in valores_negativos:
            if valor == i:
                encontrado = True
                break
        if not encontrado:
            valores_validos.append(valor)

    if len(valores_validos) > 0:
        regla[atributo] = valores_validos

print("\nRegla inducida para identificar clientes que van a comprar un auto eléctrico:")
for atributo in regla:
    print("-", atributo, regla[atributo])

print("\nRegla de clasificación:")
for atributo in regla:
    for valor in regla[atributo]:
        print("SI", atributo, "=", valor)
        print("ENTONCES Compra_Auto_Electrico = Sí")


print("\nVerificación de ejemplos positivos:")
for ej in positivos:
    cumple = True

    for atributo in regla:
        if ej[atributo] not in regla[atributo]:
            cumple = False

    print(ej, "-> Compra auto eléctrico:", cumple)


print("\nVerificación de ejemplos negativos:")
for ej in negativos:
    cumple = True

    for atributo in regla:
        if ej[atributo] not in regla[atributo]:
            cumple = False

    print(ej, "-> Compra auto eléctrico:", cumple)
# TP 2 — Clasificación con Algoritmo AQ

**Materia:** Procesamiento de Aprendizaje Automático

## Objetivo

Aplicar el algoritmo **AQ** para identificar las características que distinguen a los clientes que compran un automóvil eléctrico de los que no.

## 1. Análisis de ejemplos

Se comparan los ejemplos positivos y negativos considerando los atributos:

- Edad
- Ingreso
- Tiene garaje
- Distancia al trabajo

## 2. Aplicación de AQ

Se implementa en Python el procedimiento AQ, comparando los valores de cada atributo en los ejemplos positivos y negativos para identificar aquellos que permiten distinguir ambas clases.

## 3. Regla de clasificación

A partir de los ejemplos analizados, se obtiene una regla de clasificación y se verifica que cubra los ejemplos positivos y excluya los negativos.

**Regla:**

> SI tiene_garaje = Si  
> ENTONCES Compra_Auto_Electrico = Sí

## Tecnologías

- Python
- Algoritmo AQ

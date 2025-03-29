#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Gestión de Operaciones de Compra BRL-ARS
Automatiza el proceso de generación de presupuestos para compra de BRL con ARS
"""

import json
import os
from datetime import datetime

# Constantes
CARPETA_OPERACIONES = "Operaciones de COMPRA"
ARCHIVO_CONTADOR = "contador_ticket.txt"
PREFIJO_TICKET = "TC"

def generar_codigo_ticket():
    """Genera un código de ticket único e incremental.
    
    Returns:
        str: Código de ticket en formato TCXXYYYY
    """
    if not os.path.exists(ARCHIVO_CONTADOR):
        with open(ARCHIVO_CONTADOR, "w") as f:
            f.write("01,0000")  # Inicializa el contador

    with open(ARCHIVO_CONTADOR, "r") as f:
        prefijo, numero = f.read().strip().split(",")
        prefijo, numero = int(prefijo), int(numero)

    # Incrementa y maneja overflow
    numero += 1
    if numero >= 10000:
        numero = 0
        prefijo += 1

    with open(ARCHIVO_CONTADOR, "w") as f:
        f.write(f"{prefijo:02d},{numero:04d}")

    return f"{PREFIJO_TICKET}{prefijo:02d}{numero:04d}"

def formatear_numero(numero):
    """Formatea números para cálculos internos.
    
    Args:
        numero (float): Número a formatear
        
    Returns:
        int/float: Número formateado
    """
    return int(numero) if numero == int(numero) else round(numero, 2)

def formatear_numero_mensaje(numero):
    """Formatea números para visualización (formato argentino).
    
    Args:
        numero (float): Número a formatear
        
    Returns:
        str: Número formateado con separadores
    """
    if numero == int(numero):
        return "{:,}".format(int(numero)).replace(",", ".")
    return "{:,.2f}".format(numero).replace(",", "X").replace(".", ",").replace("X", ".")

def formatear_numero_json(numero):
    """Formatea números para almacenamiento en JSON.
    
    Args:
        numero (float): Número a formatear
        
    Returns:
        int/float: Número optimizado para JSON
    """
    return formatear_numero(numero)

def calcular_operacion(cotizacion_brl_usd, cotizacion_usd_ars, importe_brl, ganancia_brl, ganancia_ars):
    """Realiza todos los cálculos financieros de la operación.
    
    Args:
        cotizacion_brl_usd (float): Cotización BRL/USD
        cotizacion_usd_ars (float): Cotización USD/ARS
        importe_brl (float): Importe a comprar en BRL
        ganancia_brl (float): Ganancia por USD en BRL
        ganancia_ars (float): Ganancia por USD en ARS
        
    Returns:
        dict: Diccionario con todos los resultados calculados
    """
    resultados = {}
    
    # Cálculos principales
    resultados['importe_usd'] = importe_brl / cotizacion_brl_usd
    resultados['total_ars'] = resultados['importe_usd'] * cotizacion_usd_ars
    resultados['tipo_cambio_brl_ars'] = resultados['total_ars'] / importe_brl
    
    # Cálculo de ganancias
    resultados['ganancia_brl_total'] = resultados['importe_usd'] * ganancia_brl
    resultados['ganancia_ars_por_usd'] = resultados['importe_usd'] * ganancia_ars
    resultados['ganancia_ars_por_brl'] = resultados['ganancia_brl_total'] * resultados['tipo_cambio_brl_ars']
    resultados['ganancia_total_ars'] = resultados['ganancia_ars_por_usd'] + resultados['ganancia_ars_por_brl']
    
    return resultados

def generar_mensaje_cliente(nombre, apellido, importe_brl, tipo_cambio, total_ars):
    """Genera el mensaje formal para el cliente.
    
    Args:
        nombre (str): Nombre del cliente
        apellido (str): Apellido del cliente
        importe_brl (float): Importe en BRL
        tipo_cambio (float): Tipo de cambio aplicado
        total_ars (float): Total en ARS
        
    Returns:
        str: Mensaje formateado para el cliente
    """
    return f"""
Estimado/a {nombre} {apellido},

Agradecemos su consulta y le presentamos el detalle de su presupuesto para la compra de {formatear_numero_mensaje(importe_brl)} BRL:

- *Moneda*: BRL
- *Importe de la operación*: {formatear_numero_mensaje(importe_brl)} BRL
- *Tipo de cambio BRL a ARS*: {formatear_numero_mensaje(tipo_cambio)} ARS por BRL
- *Total a recibir en pesos argentinos*: {formatear_numero_mensaje(total_ars)} ARS

Quedamos a su disposición para cualquier consulta adicional o para proceder con la operación.

Atentamente,
*Su equipo de operaciones*
"""

def guardar_operacion(datos_operacion, carpeta_operaciones):
    """Guarda la operación en un archivo JSON.
    
    Args:
        datos_operacion (dict): Diccionario con todos los datos de la operación
        carpeta_operaciones (str): Carpeta destino
        
    Returns:
        str: Ruta del archivo guardado
    """
    if not os.path.exists(carpeta_operaciones):
        os.makedirs(carpeta_operaciones)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"{timestamp}_{datos_operacion['apellido_cliente'].upper()}_{datos_operacion['nombre_cliente'].upper()}_COMPRA_{int(datos_operacion['importe_brl'])}BRL.json"
    ruta_archivo = os.path.join(carpeta_operaciones, nombre_archivo)
    
    with open(ruta_archivo, "w") as archivo_json:
        json.dump(datos_operacion, archivo_json, indent=4)
    
    return ruta_archivo

def main():
    """Función principal del script."""
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE COMPRA BRL/ARS".center(50))
    print("="*50 + "\n")
    
    # Captura de datos
    codigo_cliente = int(input("Ingrese el código del cliente: "))
    apellido_cliente = input("Ingrese el apellido del cliente: ").capitalize()
    nombre_cliente = input("Ingrese el nombre del cliente: ").capitalize()
    
    print("\n" + "-"*50)
    print("DATOS DE LA OPERACIÓN".center(50))
    print("-"*50)
    
    cotizacion_brl_usd = float(input("\nIngrese la cotización de BRL a USD: "))
    cotizacion_usd_ars = float(input("Ingrese la cotización de USD a ARS: "))
    importe_brl = float(input("Ingrese el importe en BRL que desea comprar: "))
    ganancia_brl = float(input("Ingrese la ganancia en BRL por cada USD vendido: "))
    ganancia_ars = float(input("Ingrese la ganancia en ARS por cada USD vendido: "))
    
    # Procesamiento
    resultados = calcular_operacion(
        cotizacion_brl_usd, cotizacion_usd_ars, 
        importe_brl, ganancia_brl, ganancia_ars
    )
    
    codigo_ticket = generar_codigo_ticket()
    
    # Generar mensaje para el cliente
    mensaje_cliente = generar_mensaje_cliente(
        nombre_cliente, apellido_cliente,
        importe_brl, resultados['tipo_cambio_brl_ars'], 
        resultados['total_ars']
    )
    
    # Mostrar resultados
    print("\n" + "="*50)
    print("PRESUPUESTO PARA EL CLIENTE".center(50))
    print("="*50)
    print(mensaje_cliente)
    
    # Generar línea de ticket
    fecha_actual = datetime.now().strftime("%d/%m")
    linea_ticket = f"{codigo_ticket} - {fecha_actual} - {apellido_cliente} {nombre_cliente} - COMPRA x BRL {formatear_numero_mensaje(importe_brl)}."
    
    print("\n" + "="*50)
    print("TICKET DE OPERACIÓN".center(50))
    print("="*50)
    print(linea_ticket)
    
    # Preparar datos para JSON
    datos_operacion = {
        "codigo": codigo_cliente,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "apellido_cliente": apellido_cliente,
        "nombre_cliente": nombre_cliente,
        "tipo_moneda": "BRL",
        "cotizacion_brl_usd": formatear_numero_json(cotizacion_brl_usd),
        "cotizacion_usd_ars": formatear_numero_json(cotizacion_usd_ars),
        "cotizacion_brl_ars": formatear_numero_json(resultados['tipo_cambio_brl_ars']),
        "importe_brl": formatear_numero_json(importe_brl),
        "importe_usd": formatear_numero_json(resultados['importe_usd']),
        "total_ars": formatear_numero_json(resultados['total_ars']),
        "ganancia_por_brl": formatear_numero_json(ganancia_brl),
        "ganancia_por_usd": formatear_numero_json(ganancia_ars),
        "ganancia_brl_total": formatear_numero_json(resultados['ganancia_brl_total']),
        "ganancia_ars_por_usd": formatear_numero_json(resultados['ganancia_ars_por_usd']),
        "ganancia_ars_por_brl": formatear_numero_json(resultados['ganancia_ars_por_brl']),
        "ganancia_total_ars": formatear_numero_json(resultados['ganancia_total_ars']),
        "operacion": "COMPRA",
        "ticket": codigo_ticket
    }
    
    # Guardar operación
    ruta_archivo = guardar_operacion(datos_operacion, CARPETA_OPERACIONES)
    
    print("\n" + "="*50)
    print("RESUMEN EJECUTIVO".center(50))
    print("="*50)
    print(f"""
CODIGO: {codigo_cliente}
NOMBRE: {nombre_cliente}
APELLIDO: {apellido_cliente}
ENTREGAMOS: {formatear_numero_mensaje(resultados['total_ars'])} ARS
RECIBIMOS: {formatear_numero_mensaje(importe_brl)} BRL
TC: {formatear_numero_mensaje(resultados['tipo_cambio_brl_ars'])} ARS por BRL
""")
    
    print(f"\nDatos guardados en: {ruta_archivo}\n")

if __name__ == "__main__":
    main()

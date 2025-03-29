# BRL-ARS-Exchange-Manager

## 📌 Sistema de Gestión de Operaciones BRL-ARS

Este proyecto contiene dos scripts en Python que automatizan la generación de presupuestos para la compra y venta de reales brasileños (BRL) contra pesos argentinos (ARS). El sistema permite calcular montos, generar mensajes para clientes y almacenar las operaciones en archivos JSON.

## 🚀 Características

✅ Generación automática de códigos de ticket para cada operación.

✅ Cálculo de montos basados en cotizaciones BRL/USD y USD/ARS.

✅ Generación de un mensaje formal para clientes con detalles de la operación.

✅ Almacenamiento de cada operación en un archivo JSON.

✅ Formateo de números para visualización y almacenamiento.

# 📁 Estructura del Proyecto

📂 Sistema_Gestion_Operaciones

│── 📜 compra_brl_ars.py

│── 📜 venta_brl_ars.py

│── 📂 Operaciones de COMPRA/

│── 📂 Operaciones de VENTA/

│── 📜 contador_ticket.txt

│── 📜 README.md

## 📌 Scripts Disponibles

## 🔹 venta_brl_ars.py

Automatiza la venta de BRL y calcula el monto total a recibir en ARS.

Entrada requerida:

    Cotización BRL/USD y USD/ARS.

    Monto de BRL a vender.

    Ganancia por USD en BRL y ARS.

Salida:

    Monto en ARS resultante.

    Ticket de operación generado.

    Mensaje para el cliente.

    Registro de la operación en un archivo JSON.

## 🔹 compra_brl_ars.py

Automatiza la compra de BRL y calcula el monto total en ARS necesario para la operación.

Entrada requerida:

    Cotización BRL/USD y USD/ARS.

    Monto de BRL a comprar.

    Ganancia por USD en BRL y ARS.

Salida:

    Monto en ARS a pagar.

    Ticket de operación generado.

    Mensaje para el cliente.

    Registro de la operación en un archivo JSON.

# 📊 Ejemplo de Uso

Ejecuta cualquiera de los scripts desde la terminal:

_python3 venta_brl_ars.py_

O para compras:

_python3 compra_brl_ars.py_

Sigue las instrucciones en pantalla y el sistema generará automáticamente los cálculos y archivos de registro.


# 🔧 Requisitos

    Python 3.6+

    Librerías estándar de Python (json, os, datetime)

    
# 🚀 Ejemplo de salida    

    ==================================================
      SISTEMA DE GESTIÓN DE VENTA BRL/ARS      
    ==================================================
    
    Ingrese el código del cliente: 1425
    Ingrese el apellido del cliente: gonzález
    Ingrese el nombre del cliente: maría
    
    --------------------------------------------------
                   DATOS DE LA OPERACIÓN              
    --------------------------------------------------
    
    Ingrese la cotización de BRL a USD: 5.2
    Ingrese la cotización de USD a ARS: 210.5
    Ingrese el importe en BRL que desea vender: 1000
    Ingrese la ganancia en BRL por cada USD vendido: 0.1
    Ingrese la ganancia en ARS por cada USD vendido: 20.5
    
    ==================================================
                 PRESUPUESTO PARA EL CLIENTE          
    ==================================================
    
    Estimado/a María González,
    
    Agradecemos su consulta y le presentamos el detalle de su presupuesto para la compra de 1.000 BRL:
    
    - *Moneda*: BRL
    - *Importe de la operación*: 1.000 BRL
    - *Tipo de cambio BRL a ARS*: 40,48 ARS por BRL
    - *Total a abonar en pesos argentinos*: 40.480,77 ARS
    
    Quedamos a su disposición para cualquier consulta adicional o para proceder con la operación.
    
    Atentamente,
    *Su equipo de operaciones de Gwinn*
    
    
    ==================================================
                   TICKET DE OPERACIÓN               
    ==================================================
    TC010025 - 30/03 - González María - VENTA x BRL 1.000.
    
    ==================================================
                     RESUMEN EJECUTIVO               
    ==================================================
    
    CODIGO: 1425
    NOMBRE: María
    APELLIDO: González
    ENTREGAMOS: 1.000 BRL
    RECIBIMOS: 40.480,77 ARS
    TC: 40,48 ARS por BRL
    
    
    Datos guardados en: Operaciones de venta/2023-03-30_16-45-22_GONZÁLEZ_MARÍA_venta_1000BRL.json


## 📜 Notas

    Los archivos JSON con los detalles de cada operación se guardarán en las carpetas Operaciones de COMPRA y Operaciones de VENTA.

    El código de ticket se genera secuencialmente y se almacena en contador_ticket.txt.

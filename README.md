# BRL-ARS-Exchange-Manager

📌 Sistema de Gestión de Operaciones BRL-ARS

Este proyecto contiene dos scripts en Python que automatizan la generación de presupuestos para la compra y venta de reales brasileños (BRL) contra pesos argentinos (ARS). El sistema permite calcular montos, generar mensajes para clientes y almacenar las operaciones en archivos JSON.
🚀 Características

✅ Generación automática de códigos de ticket para cada operación.
✅ Cálculo de montos basados en cotizaciones BRL/USD y USD/ARS.
✅ Generación de un mensaje formal para clientes con detalles de la operación.
✅ Almacenamiento de cada operación en un archivo JSON.
✅ Formateo de números para visualización y almacenamiento.
📁 Estructura del Proyecto

📂 Sistema_Gestion_Operaciones
│── 📜 compra_brl_ars.py
│── 📜 venta_brl_ars.py
│── 📂 Operaciones de COMPRA/
│── 📂 Operaciones de VENTA/
│── 📜 contador_ticket.txt
│── 📜 README.md

📌 Scripts Disponibles
🔹 venta_brl_ars.py

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

🔹 compra_brl_ars.py

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

📊 Ejemplo de Uso

Ejecuta cualquiera de los scripts desde la terminal:

python3 venta_brl_ars.py

O para compras:

python3 compra_brl_ars.py

Sigue las instrucciones en pantalla y el sistema generará automáticamente los cálculos y archivos de registro.
🔧 Requisitos

    Python 3.6+

    Librerías estándar de Python (json, os, datetime)

📜 Notas

    Los archivos JSON con los detalles de cada operación se guardarán en las carpetas Operaciones de COMPRA y Operaciones de VENTA.

    El código de ticket se genera secuencialmente y se almacena en contador_ticket.txt.

# Kiosko Universitario UCB

Proyecto integrador de la materia **Programación I**  
Universidad Católica Boliviana "San Pablo"  
Sede: La Plata 
Autor: **Fabricio Rivero**


## Descripción del proyecto

El sistema **Kiosko Universitario UCB** es una aplicación de consola desarrollada en **Python** que permite gestionar los productos de un kiosko universitario.  
Permite registrar, modificar, eliminar y buscar productos, además de generar reportes, ordenar el inventario y guardar toda la información en archivos CSV.

Este proyecto aplica los conceptos fundamentales de **programación modular**, **estructuras de datos (listas y diccionarios)**, **persistencia en archivos** y **validaciones de entrada**.


##  Funcionalidades principales

✅ Ver inventario  
✅ Agregar productos con validaciones (sin valores negativos, vacíos o repetidos)  
✅ Eliminar productos por código  
✅ Actualizar stock existente  
✅ Mostrar productos con bajo stock  
✅ Calcular el valor total del inventario  
✅ Buscar productos por nombre o categoría  
✅ Ordenar el inventario por precio o cantidad  
✅ Guardar automáticamente los datos en `datos.csv`



## Validaciones implementadas

- No se permite precio o cantidad igual o menor a 0  
- No se permiten campos vacíos  
- No se permiten códigos duplicados  
- Solo números válidos en cantidad y precio  
- Mensajes claros para el usuario ante errores

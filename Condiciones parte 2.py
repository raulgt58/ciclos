
#se crea diccionario
data = {'2412':{"nombre":'Webcam',"Pago en efectivo":float(330.00),"Pago con tarjeta":float(365.00)},
        '2413':{"nombre":'Audífonos',"Pago en efectivo":425,"Pago con tarjeta":460},
        '2414':{"nombre":"Memoria USB","Pago en efectivo":40,"Pago con tarjeta":50},
        '2415':{"nombre":'Mouse',"Pago en efectivo":250,"Pago con tarjeta":260},
        '2416':{"nombre":'Impresora',"Pago en efectivo":230,"Pago con tarjeta":250},
        '2417':{"nombre":'Cartucho de Tinta',"Pago en efectivo":95,"Pago con tarjeta":115},
        '2418':{"nombre":'Disco Duro 2TB',"Pago en efectivo":450,"Pago con tarjeta":480},
        '2419':{"nombre":'Bocina portable',"Pago en efectivo":500,"Pago con tarjeta":550},
        }

#se crea segundo diccionario
carre = {
         }
#Se imprime el listado de productos
print("A continuación se presenta el listado de nuestros productos con su respectivo precio")
print()
print('Codigo\t','Producto\t', 'Pago en efectivo\t', 'Pago con tarjeta\t')
print()
print('2412\t',"Webcam\t\t\t",'Q 330\t\t','Q 365')
print('2413\t','Audifonos\t\t', 'Q 425\t\t', 'Q 460')
print('2414\t','Memoria USB\t\t', 'Q 40\t\t', 'Q 50')
print('2415\t','Mouse\t\t\t', 'Q 250\t\t', 'Q 260')
print('2416\t','Impresora\t\t', 'Q 230\t\t', 'Q 250')
print('2417\t','Cartucho de tinta\t', 'Q 95\t\t', 'Q 115')
print('2418\t','Disco duro 2TB\t\t', 'Q 450\t\t', 'Q 480')
print('2419\t','Bocina portable\t', 'Q 500\t\t', 'Q 550')
print()
        
#se inicia primer ciclo para toda la facturación
facturacion = "inicio"  
while facturacion != "Fin":
    
    #segundo ciclo para los productos
    producto = "Inicio"
    while producto != "Fin":

        producto = input("Ingrese codigo del producto que desea ")
        cantidad = int(input("Que cantidad de unidades desea del producto "))
        pregunta= input("Desea agregar otro producto ")
        
        carre[(data[producto]["nombre"])] = cantidad
       

        producto = producto.capitalize()
        if pregunta == "no":
             break
    pregunta2 = input("¿Desea eliminar un producto de la carretilla? ")
    
    if pregunta2 == "Si":
        pregunta3 = input("Ingrese el nombre del producto que desea eliminar ")
        del(carre[pregunta3])
        break
    elif pregunta2 == "No":
        break
        
print("Su carretilla final",carre)

    
    
 
    
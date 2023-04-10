print("Carlos Javier De La Torre R. ...Taller Python ViveLab SENA... ")
print("=======================================================================")
print("       Ejercicio de Condicionales SIMULACION FACTURA                   ")
print("=======================================================================\n")
print()
nombre=input("Por favor ingrese su Nombre: ")
print()
articulo=input("Por favor ingrese nombre del Articulo: ")
cantidad=int(input("Por favor ingrese la Cantidad: "))
vrUnitario=float(input("Por favor ingrese Vr Unitario: "))
subTotal=0
total=0
iva=0.19
vrIva=0
pago=0
if cantidad>0:
  cobraIva=input("Por favor indique  si aplica IVA(19%) Escriba 's', no aplica escriba'n': ")
  if cobraIva=="s" or cobraIva=="S":
    subTotal=(cantidad*vrUnitario)
    vrIva=(subTotal*iva)
    total=(subTotal+vrIva)
    print(f"Valor a pagar, SubTotal {subTotal} , IVA {vrIva} , TOTAL {total} ")
    pago=float(input("Por favor digite valor recibido por Caja: "))
    if pago<total:
      print("Favor revisar Ingresó menos dinero ...")
      pago=float(input("Por favor digite valor recibido por Caja: "))
      cambio=(pago-total)
      print(f"SubTotal.............. $ {subTotal}")
      print(f"Valor IVA ............ $  {vrIva}")
      print(f"TOTAL .................$ {   total}")
      print("----------------------------------------")
      print(f"Cambio a favor de {nombre}, $ {cambio} ")
      print("----------------------------------------")
      print("Gracias por utilizar este Programita... Bye")
    else:
      cambio=(pago-total)
      print(f"SubTotal.............. $ {subTotal}")
      print(f"Valor IVA ............ $  {vrIva}")
      print(f"TOTAL .................$ {   total}")
      print("----------------------------------------")
      print(f"Cambio a favor de {nombre}, $ {cambio} ")
      print("----------------------------------------")
      print("Gracias por utilizar este Programita... Bye")

  if cobraIva=="n" or cobraIva=="N":
    subTotal=(cantidad*vrUnitario)
    print(f"Valor a pagar SIN IVA, TOTAL {subTotal}")
    pago=float(input("Por favor digite valor recibido por Caja: "))
    if pago<=subTotal:
      print("Favor revisar Ingresó Menos dinero ***")
      pago=float(input("Por favor digite valor recibido por Caja: "))
      cambio=(pago-subTotal)
      print(f"SubTotal...............$ {subTotal}")
      print(f"TOTAL .................$ {subTotal}")
      print("........................................")
      print(f"Cambio a favor de {nombre}, $ {cambio} ")
      print("........................................")
      print("Gracias por utilizar este Programita... Bye")
    else:
      cambio=(pago-subTotal)
      print(f"SubTotal...............$ {subTotal}")
      print(f"TOTAL .................$ {subTotal}")
      print("........................................")
      print(f"Cambio a favor de {nombre}, $ {cambio} ")
      print("........................................")
      print("Gracias por utilizar este Programita... Bye")
      
else:
  exit
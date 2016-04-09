# -*- coding: utf-8 -*-
print "1) Calculadora"
print "2) Par o Impar"
var=int(raw_input("elige"))
if var==1:
    print "elige 2 numeros"
    var2=int(raw_input("ingresa un numero"))
    var3=int(raw_input("ingresa otro numero"))        
    print "elige un operador"
    print "1)suma"
    print "2)resta"
    print "3)multiplicacion"
    if var3!=0:
        print "4)division"
        print "5)residuo"
    var4=int(raw_input("¿Que operador?"))
    if var4==1:
        print"suma:", var2+var3
    if var4==2:
        print"resta:", var2-var3
    if var4==3:
        print "multiplicacion:", var2*var3
    if var4==4:
        print "division:", var2/var3
    if var4==5:
        print "residuo:" , var2%var3
if var==2:
    var5=int(raw_input("elige un numero"))
    if var5%2==0:
        print "par"
    if var5%2!=0:
        print"impar"
    

   
        
             
             
                  
             

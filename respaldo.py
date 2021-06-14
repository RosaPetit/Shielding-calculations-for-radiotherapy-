# Todos los componentes se encuentran en este módulo
import tkinter as tk  

# Tk es la clase que crea el componente raíz o ventana principal
app = tk.Tk()   
# Su método mainloop() inicia el bucle infinito del programa
app.mainloop()  

import numpy as np
import matplotlib.pyplot as plt


#begin workload 
p=50 #patients per day
g=2.5 #grey per patient
we=5 # day per week
w1= 0.7  #fraction  w
w2=0.3  #fraction  w
wt= 52 #total week in a year

MV6=p*g*we*w1*wt*1.1 #grey per year
MV15= p*g*we*w2*wt*1.1 

#end workload

#Shielding Calculations

barrier= input ("Which type of barriers do you want, primary (1) or sencondary(2)?:")

if barrier=="1": 
  print ("Primary barrier") 
  p1=float(input("Value of shielding design dose 'P' (Sv/y):"))
  T= float(input ("Value of ocupancy factor 'T': "))
  U= float(input ("Value of use factor 'U':"))
  d= float( input ("Value of distance primary beam 'd' (m):"))
  TVL1= float( input ("Value of primary barrier for TVL1:"))
  TVLe= float(input ("Value of primary barrier for TVLe:"))

  D= d**2
  B=(p1*D)/(MV6*T*U)
  n=-np.log10(B)
  thickness=TVL1+((n-1)*TVLe)

  print (" The barrier thickness is \n",thickness)

elif barrier == "2": 

  print ("Primary barrier") 
  p=float(input("Value of shielding design dose 'P' (Sv/y):"))
  T= float(input ("Value of ocupancy factor 'T': "))
  U= float(input ("Value of use factor 'U':"))
  d= float( input ("Value of distance primary beam 'd' (m):"))
  TVL1= float( input ("Value of primary barrier for TVL1:"))
  TVLe= float(input ("Value of primary barrier for TVLe:"))

  D= d**2
  B=(p1*D)/(MV6*T*U)
  n=-np.log10(B)
  thickness=TVL1+((n-1)*TVLe)
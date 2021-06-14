
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


print("This program is to perform shielding calculations for Linac room \n")

print("First part: Workload calculations \n")

pa=float(input("Patients per day:"))
gy=float(input("Gray per patient (Gy):"))
we=float(input("Day per week:"))
w1=float(input("Fraction of workload (leackage):"))
wt=float(input("Total weeks:"))
qc=float(input("Quality control percentage:"))

ww= pa*gy*we*w1*wt # workload sin el porcentaje de QC

qc1= (qc/100)*ww #Adicion de porcentaje 

w= ww+qc1 #workload total este es el usado para los calculos

print("The worload is:\n",w)

print("Second part: Shieldind Calculations \n")

energy= input ("Choose the energy  6MV, 10MV, 15MV, 18MV:")

if energy=="6":
  print("1 --> Primary shielding")
  print("2 --> Secondary shielding ")
  print("3 --> Scatter from Patient Shielding Calculations")
  print("4 --> Scatter of the Primary Beam from the Bunker Wall ")
  print("5 --> Scatter from the Patient")
  print("6 --> Scatter of Head Leakage Radiation from the Bunker Walls")
  print("7 --> Transmission of Head Leakage Radiation through the Maze Wall")
  print("8 --> Total dose rate at the maze entrance and door shielding")

  types=input("Choose the type of shielding:\n")
  
  if types=="1": 
    #Primary shielding 

    #print("Types of areas avilables: \n ")
    #print("1 --> Fully area")
    #print("2 --> Abjecent treament room")
    #print("3 --> Corridor")
    #print("4 --> Linac bunker")
    #print("5 --> Toilet, storage areas")
    #print("6 --> Outdoor areas")
   
    #T= input("Choose the type of area:\n")

    p1=float(input("Value of shielding design dose 'P' (Sv/y):"))
    T= float(input ("Value of ocupancy factor 'T': "))
    U= float(input ("Value of use factor 'U':"))
    d= float( input ("Value of distance primary beam 'd' (m):"))
    TVL1= float( input ("Value of primary barrier for TVL1:"))
    TVLe= float(input ("Value of primary barrier for TVLe:"))

    D= d**2
    B=(p1*D)/(w*T*U)
    n=-np.log10(B)
    thickness=TVL1+((n-1)*TVLe)

    print("The barrier of primary shielding thickness is (cm)",thickness)

  elif types=="2":
  #Secondary shieldong
    
    fww=float(input("Workload factor for VMT:")) 
    p1=float(input("Value of shielding design dose 'P' (Sv/y):"))
    T= float(input ("Value of ocupancy factor 'T': "))
    #U= float(input ("Value of use factor 'U':"))
    L= float(input("L leakage factor: "))
    d= float( input ("Value of distance primary beam 'd' (m):"))
    TVL1= float( input ("Value of secondary barrier for TVL1:"))
    TVLe= float(input ("Value of secondary barrier for TVLe:"))
    
    
    fw= (fww/100)*ww  #Workload factor for VMT or IMRT
    w= ww+fw
    #new workload for secondary barrier 
    D= d**2
    B=(p1*D)/(w*T*L)
    n=-np.log10(B)
    thickness=TVL1+((n-1)*TVLe)

    print("The barrier of secondsary shielding thickness is (cm)",thickness)
  elif types=="3":
  #Scatter from Patient Shielding Calculations



    print("papa")
  elif types=="4":
  #Scatter of the Primary Beam from the Bunker Wall 
    print("papa")
  elif types=="5":
  #Scatter from the Patient
    print("papa")
  elif types=="6": 
  #Scatter of Head Leakage Radiation from the Bunker Walls
    print("papa")
  elif types=="7":
  #Transmission of Head Leakage Radiation through the Maze Wall
    print("papa")
  elif types=="8":
  # Total dose rate at the maze entrance and door shielding
    print("papa")
elif energy=="10":
  print("papa")
  
elif energy=="15":
  print("papa")
  

elif energy=="18":
  
  print("papa")






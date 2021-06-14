
import numpy as np
import matplotlib.pyplot as plt

print("This program is to perform shielding calculations for Linac room")

print("First part: Workload calculations")

pa=float(input("patients per day:"))
gy=float(input("gray per patient (Gy):"))
we=float(input("day per week:"))
w1=float(input("fraction of workload (leackage):"))
wt=float(input("total weeks:"))
qc=float(input("quality control percentage:"))

ww= pa*gy*we*w1*wt # workload sin el porcentaje de QC

qc1= (qc/100)*ww #Adicion de porcentaje 

w= ww+qc1

print("The worload is:",w)

#begin workload 



#begin workload 
p=50 #patients per day
g=2.5 #grey per patient
we=5 # day per week
w1= 0.7  #fraction  w
w2=0.3  #fraction  w
wt= 52 #total week in a year

#MV6=p*g*we*w1*wt*1.1 #grey per year
#MV15= p*g*we*w2*wt*1.1 

#end workload
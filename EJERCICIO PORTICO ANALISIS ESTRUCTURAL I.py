#%%
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
#print("ingresar todas las unidades en metros y kN")

Base=0.3
Altura=0.35
R=0.4
a=2.05
b=1.8
c=4
d=2.7
H=5
K=5000
q=60
p=70
E=20000000

LA=H
LB=H
LC=a+b
LD=np.sqrt((a+b)**2+d**2)
LE=c
# Elemento de la pila A en locales

L=LA
A=np.pi*R**2
I=np.pi/4*R**4
AE=A*E
EI=E*I
tetaA=np.pi/2

Landa=(K/(4*EI))**0.25
s=np.sin(Landa*L)
c=np.cos(Landa*L)
sh=np.sinh(Landa*L)
ch=np.cosh(Landa*L)

k22=4*EI*Landa**3*(s*c+sh*ch)/(sh**2-s**2)
k23=2*EI*Landa**2*(s**2+sh**2)/(sh**2-s**2)
k25=-4*EI*Landa**3*(s*ch+c*sh)/(sh**2-s**2)
k26=4*EI*Landa**2*s*sh/(sh**2-s**2)
k33=2*EI*Landa*(sh*ch-s*c)/(sh**2-s**2)
k36=2*EI*Landa*(s*ch-c*sh)/(sh**2-s**2)

MatrizALoc=np.zeros([6,6])

MatrizALoc[0,0]=AE/L
MatrizALoc[1,0]=0
MatrizALoc[2,0]=0
MatrizALoc[3,0]=-AE/L
MatrizALoc[4,0]=0
MatrizALoc[5,0]=0

MatrizALoc[0,1]=0
MatrizALoc[1,1]=k22
MatrizALoc[2,1]=k23
MatrizALoc[3,1]=0
MatrizALoc[4,1]=k25

MatrizALoc[5,1]=k26

MatrizALoc[0,2]=0
MatrizALoc[1,2]=k23
MatrizALoc[2,2]=k33
MatrizALoc[3,2]=0
MatrizALoc[4,2]=-k26
MatrizALoc[5,2]=k36

MatrizALoc[0,3]=-AE/L
MatrizALoc[1,3]=0
MatrizALoc[2,3]=0
MatrizALoc[3,3]=AE/L
MatrizALoc[4,3]=0
MatrizALoc[5,3]=0


MatrizALoc[0,4]=0
MatrizALoc[1,4]=k25
MatrizALoc[2,4]=-k26
MatrizALoc[3,4]=0
MatrizALoc[4,4]=k22
MatrizALoc[5,4]=-k23

MatrizALoc[0,5]=0
MatrizALoc[1,5]=k26
MatrizALoc[2,5]=k36
MatrizALoc[3,5]=0
MatrizALoc[4,5]=-k23
MatrizALoc[5,5]=k33

#print(MatrizALoc)

# sistema en coordenadas globales ver apuntes como obtener la trasnpuesta(mero cmalelllooo hpta)

TA=np.zeros([6,6])

TA[0,0]= np.cos(tetaA)
TA[1,0]=-np.sin(tetaA)

TA[0,1]=np.sin(tetaA)
TA[1,1]=np.cos(tetaA)

TA[2,2]=1

TA[3,3]= np.cos(tetaA)
TA[4,3]=-np.sin(tetaA)

TA[3,4]=np.sin(tetaA)
TA[4,4]=np.cos(tetaA)

TA[5,5]=1

#print(TA)

MatrizAGlo=np.matrix.transpose(TA)@MatrizALoc@TA

#print(MatrizAGlo)


# Elemento B pila del suelo

L=LB
A=np.pi*R**2
I=np.pi/4*R**4
AE=A*E
EI=E*I
tetaB=np.pi/2

Landa=(K/(4*EI))**0.25 

s=np.sin(Landa*L)
c=np.cos(Landa*L)
sh=np.sinh(Landa*L)
ch=np.cosh(Landa*L)

k22=4*EI*Landa**3*(s*c+sh*ch)/(sh**2-s**2)
k23=2*EI*Landa**2*(s**2+sh**2)/(sh**2-s**2)
k25=-4*EI*Landa**3*(s*ch+c*sh)/(sh**2-s**2)
k26=4*EI*Landa**2*s*sh/(sh**2-s**2)
k33=2*EI*Landa*(sh*ch-s*c)/(sh**2-s**2)
k36=2*EI*Landa*(s*ch-c*sh)/(sh**2-s**2)

MatrizBLoc=np.zeros([6,6])

MatrizBLoc[0,0]=AE/L
MatrizBLoc[1,0]=0
MatrizBLoc[2,0]=0
MatrizBLoc[3,0]=-AE/L
MatrizBLoc[4,0]=0
MatrizBLoc[5,0]=0

MatrizBLoc[0,1]=0
MatrizBLoc[1,1]=k22
MatrizBLoc[2,1]=k23
MatrizBLoc[3,1]=0
MatrizBLoc[4,1]=k25
MatrizBLoc[5,1]=k26

MatrizBLoc[0,2]=0
MatrizBLoc[1,2]=k23
MatrizBLoc[2,2]=k33
MatrizBLoc[3,2]=0
MatrizBLoc[4,2]=-k26
MatrizBLoc[5,2]=k36

MatrizBLoc[0,3]=-AE/L
MatrizBLoc[1,3]=0
MatrizBLoc[2,3]=0
MatrizBLoc[3,3]=AE/L
MatrizBLoc[4,3]=0
MatrizBLoc[5,3]=0

MatrizBLoc[0,4]=0
MatrizBLoc[1,4]=k25
MatrizBLoc[2,4]=-k26
MatrizBLoc[3,4]=0
MatrizBLoc[4,4]=k22
MatrizBLoc[5,4]=-k23

MatrizBLoc[0,5]=0
MatrizBLoc[1,5]=k26
MatrizBLoc[2,5]=k36
MatrizBLoc[3,5]=0
MatrizBLoc[4,5]=-k23
MatrizBLoc[5,5]=k33

#print(MatrizBLoc)

# De manera Globales
TB=np.zeros([6,6])

TB[0,0]= np.cos(tetaB)
TB[1,0]=-np.sin(tetaB)

TB[0,1]=np.sin(tetaB)
TB[1,1]=np.cos(tetaB)

TB[2,2]=1

TB[3,3]= np.cos(tetaB)
TB[4,3]=-np.sin(tetaB)

TB[3,4]=np.sin(tetaB)
TB[4,4]=np.cos(tetaB)

TB[5,5]=1

#print(TB)


MatrizBGlo=np.matrix.transpose(TB)@MatrizBLoc@TB


#print(MatrizBGlo)


#Elemento C 
# locales
L=LC
A=Base*Altura
I=Base*Altura**3/12
AE=A*E
EI=E*I
tetaC=np.pi/2

MatrizCLoc=np.zeros([6,6])

MatrizCLoc[0,0]=AE/L
MatrizCLoc[1,0]=0
MatrizCLoc[2,0]=0
MatrizCLoc[3,0]=-AE/L
MatrizCLoc[4,0]=0
MatrizCLoc[5,0]=0          

MatrizCLoc[0,1]=0
MatrizCLoc[1,1]=12*EI/L**3
MatrizCLoc[2,1]=6*EI/L**2
MatrizCLoc[3,1]=0
MatrizCLoc[4,1]=-12*EI/L**3
MatrizCLoc[5,1]=6*EI/L**2

MatrizCLoc[0,2]=0
MatrizCLoc[1,2]=6*EI/L**2
MatrizCLoc[2,2]=4*EI/L
MatrizCLoc[3,2]=0    
MatrizCLoc[4,2]=-6*EI/L**2
MatrizCLoc[5,2]=2*EI/L

MatrizCLoc[0,3]=-AE/L
MatrizCLoc[1,3]=0
MatrizCLoc[2,3]=0
MatrizCLoc[3,3]=AE/L
MatrizCLoc[4,3]=0
MatrizCLoc[5,3]=0  

MatrizCLoc[0,4]=0  
MatrizCLoc[1,4]=-12*EI/L**3
MatrizCLoc[2,4]=-6*EI/L**2
MatrizCLoc[3,4]=0  
MatrizCLoc[4,4]=12*EI/L**3
MatrizCLoc[5,4]=-6*EI/L**2

MatrizCLoc[0,5]=0
MatrizCLoc[1,5]=6*EI/L**2
MatrizCLoc[2,5]=2*EI/L
MatrizCLoc[3,5]=0
MatrizCLoc[4,5]=-6*EI/L**2
MatrizCLoc[5,5]=4*EI/L

# matriz de empotramientos

FEmpCLoc=np.zeros([6,1])

FEmpCLoc[0,0]=0
FEmpCLoc[1,0]=p*b**2*(3*a+b)/(L)**3
FEmpCLoc[2,0]=p*a*b**2/(L)**2
FEmpCLoc[3,0]=0
FEmpCLoc[4,0]=p*a**2*(a+3*b)/(L)**3
FEmpCLoc[5,0]=-p*a**2*b/L**2

# parte globales hallar la MatrizCGlobal

TC=np.zeros([6,6])

TC[0,0]= np.cos(tetaC)
TC[1,0]=-np.sin(tetaC)

TC[0,1]=np.sin(tetaC)
TC[1,1]=np.cos(tetaC)

TC[2,2]=1

TC[3,3]= np.cos(tetaC)
TC[4,3]=-np.sin(tetaC)

TC[3,4]=np.sin(tetaC)
TC[4,4]=np.cos(tetaC)

TC[5,5]=1

MatrizCGlo=np.matrix.transpose(TC)@MatrizCLoc@TC
FEmpCGlo=np.matrix.transpose(TC)@FEmpCLoc


#print(MatrizCGlo)


#print(FEmpCGlo)


# ELEMENTO D EN LOCALES

L=LD
A=Base*Altura
I=Base*Altura**3/12
AE=A*E
EI=E*I
tetaD=np.arctan2(a+b,-d)

qxLoc=(q*d)*np.cos(3*np.pi/2-tetaD)/L
qyLoc=(q*d)*np.sin(3*np.pi/2-tetaD)/L

#print(qxLoc)
#print(qyLoc)

MatrizDLoc=np.zeros([6,6])

MatrizDLoc[0,0]=AE/L
MatrizDLoc[1,0]=0
MatrizDLoc[2,0]=0
MatrizDLoc[3,0]=-AE/L
MatrizDLoc[4,0]=0
MatrizDLoc[5,0]=0          

MatrizDLoc[0,1]=0
MatrizDLoc[1,1]=12*EI/L**3
MatrizDLoc[2,1]=6*EI/L**2
MatrizDLoc[3,1]=0
MatrizDLoc[4,1]=-12*EI/L**3
MatrizDLoc[5,1]=6*EI/L**2

MatrizDLoc[0,2]=0
MatrizDLoc[1,2]=6*EI/L**2
MatrizDLoc[2,2]=4*EI/L
MatrizDLoc[3,2]=0    
MatrizDLoc[4,2]=-6*EI/L**2
MatrizDLoc[5,2]=2*EI/L

MatrizDLoc[0,3]=-AE/L
MatrizDLoc[1,3]=0
MatrizDLoc[2,3]=0
MatrizDLoc[3,3]=AE/L
MatrizDLoc[4,3]=0
MatrizDLoc[5,3]=0  

MatrizDLoc[0,4]=0  
MatrizDLoc[1,4]=-12*EI/L**3
MatrizDLoc[2,4]=-6*EI/L**2
MatrizDLoc[3,4]=0  
MatrizDLoc[4,4]=12*EI/L**3
MatrizDLoc[5,4]=-6*EI/L**2

MatrizDLoc[0,5]=0
MatrizDLoc[1,5]=6*EI/L**2
MatrizDLoc[2,5]=2*EI/L
MatrizDLoc[3,5]=0
MatrizDLoc[4,5]=-6*EI/L**2
MatrizDLoc[5,5]=4*EI/L

#print(MatrizDLoc)


FEmpDLoc=np.zeros([6,1])

FEmpDLoc[0,0]=-qxLoc*L/2
FEmpDLoc[1,0]=-qyLoc*L/2
FEmpDLoc[2,0]=-qyLoc*L**2/12
FEmpDLoc[3,0]=-qxLoc*L/2
FEmpDLoc[4,0]=-qyLoc*L/2
FEmpDLoc[5,0]=qyLoc*L**2/12

#coordenadas globales

TD=np.zeros([6,6])

TD[0,0]= np.cos(tetaD)
TD[1,0]=-np.sin(tetaD)

TD[0,1]=np.sin(tetaD)
TD[1,1]=np.cos(tetaD)

TD[2,2]=1

TD[3,3]= np.cos(tetaD)
TD[4,3]=-np.sin(tetaD)

TD[3,4]=np.sin(tetaD)
TD[4,4]=np.cos(tetaD)

TD[5,5]=1

#print(TD)


MatrizDGlo=np.matrix.transpose(TD)@MatrizDLoc@TD

#print(MatrizDGlo)

FEmpDGlo=np.matrix.transpose(TD)@FEmpDLoc

#print(FEmpDGlo)

# ELEMENTO E
# LOCALES

L=LE
A=Base*Altura
I=Base*Altura**3/12
AE=A*E
EI=E*I
tetaE=0

MatrizELoc=np.zeros([6,6])

MatrizELoc[0,0]=AE/L
MatrizELoc[1,0]=0
MatrizELoc[2,0]=0
MatrizELoc[3,0]=-AE/L
MatrizELoc[4,0]=0
MatrizELoc[5,0]=0          

MatrizELoc[0,1]=0
MatrizELoc[1,1]=12*EI/L**3
MatrizELoc[2,1]=6*EI/L**2
MatrizELoc[3,1]=0
MatrizELoc[4,1]=-12*EI/L**3
MatrizELoc[5,1]=6*EI/L**2

MatrizELoc[0,2]=0
MatrizELoc[1,2]=6*EI/L**2
MatrizELoc[2,2]=4*EI/L
MatrizELoc[3,2]=0    
MatrizELoc[4,2]=-6*EI/L**2
MatrizELoc[5,2]=2*EI/L

MatrizELoc[0,3]=-AE/L
MatrizELoc[1,3]=0
MatrizELoc[2,3]=0
MatrizELoc[3,3]=AE/L
MatrizELoc[4,3]=0
MatrizELoc[5,3]=0  

MatrizELoc[0,4]=0  
MatrizELoc[1,4]=-12*EI/L**3
MatrizELoc[2,4]=-6*EI/L**2
MatrizELoc[3,4]=0  
MatrizELoc[4,4]=12*EI/L**3
MatrizELoc[5,4]=-6*EI/L**2

MatrizELoc[0,5]=0
MatrizELoc[1,5]=6*EI/L**2
MatrizELoc[2,5]=2*EI/L
MatrizELoc[3,5]=0
MatrizELoc[4,5]=-6*EI/L**2
MatrizELoc[5,5]=4*EI/L

#print(MatrizELoc)

FEmpELoc=np.zeros([6,1])

FEmpELoc[0,0]=0
FEmpELoc[1,0]=q*LE/2
FEmpELoc[2,0]=q*LE**2/12
FEmpELoc[3,0]=0
FEmpELoc[4,0]=q*LE/2
FEmpELoc[5,0]=-q*LE**2/12

#coordendas en globales

TE=np.zeros([6,6])

TE[0,0]= np.cos(tetaE)
TE[1,0]=-np.sin(tetaE)

TE[0,1]=np.sin(tetaE)
TE[1,1]=np.cos(tetaE)

TE[2,2]=1

TE[3,3]= np.cos(tetaE)
TE[4,3]=-np.sin(tetaE)

TE[3,4]=np.sin(tetaE)
TE[4,4]=np.cos(tetaE)

TE[5,5]=1

#print(TE)

MatrizEGlo=np.matrix.transpose(TE)@MatrizELoc@TE
#print(MatrizEGlo)

FEmpEGlo=np.matrix.transpose(TE)@FEmpELoc
#print(FEmpEGlo)





#   3.0 Calculo de los desplazamientos nodales

#   3.1 Matriz de rigidez para el calculo de los desplazamientos

MatrizDes=np.zeros([14,14])

#Ecuacion M1

MatrizDes[0,0]=MatrizAGlo[2,2]
MatrizDes[0,2]=MatrizAGlo[2,3]
MatrizDes[0,3]=MatrizAGlo[2,4]
MatrizDes[0,4]=MatrizAGlo[2,5]

#Ecuacion M2

MatrizDes[1,1]=MatrizBGlo[2,2]
MatrizDes[1,5]=MatrizBGlo[2,3]
MatrizDes[1,6]=MatrizBGlo[2,4]
MatrizDes[1,7]=MatrizBGlo[2,5]

#Ecuacion FX3

MatrizDes[2,0]=MatrizAGlo[3,2]
MatrizDes[2,2]=MatrizAGlo[3,3]+MatrizCGlo[0,0]
MatrizDes[2,3]=MatrizAGlo[3,4]+MatrizCGlo[0,1]
MatrizDes[2,4]=MatrizAGlo[3,5]+MatrizCGlo[0,2]
MatrizDes[2,8]=MatrizCGlo[0,3]
MatrizDes[2,9]=MatrizCGlo[0,4]
MatrizDes[2,10]=MatrizCGlo[0,5]

#Ecuacion FY3

MatrizDes[3,0]=MatrizAGlo[4,2]
MatrizDes[3,2]=MatrizAGlo[4,3]+MatrizCGlo[1,0]
MatrizDes[3,3]=MatrizAGlo[4,4]+MatrizCGlo[1,1]
MatrizDes[3,4]=MatrizAGlo[4,5]+MatrizCGlo[1,2]
MatrizDes[3,8]=MatrizCGlo[1,3]
MatrizDes[3,9]=MatrizCGlo[1,4]
MatrizDes[3,10]=MatrizCGlo[1,5]

#Ecuacion M3

MatrizDes[4,0]=MatrizAGlo[5,2]
MatrizDes[4,2]=MatrizAGlo[5,3]+MatrizCGlo[2,0]
MatrizDes[4,3]=MatrizAGlo[5,4]+MatrizCGlo[2,1]
MatrizDes[4,4]=MatrizAGlo[5,5]+MatrizCGlo[2,2]
MatrizDes[4,8]=MatrizCGlo[2,3]
MatrizDes[4,9]=MatrizCGlo[2,4]
MatrizDes[4,10]=MatrizCGlo[2,5]

#Ecuacion FX4

MatrizDes[5,1]=MatrizBGlo[3,2]
MatrizDes[5,5]=MatrizBGlo[3,3]+MatrizDGlo[0,0]
MatrizDes[5,6]=MatrizBGlo[3,4]+MatrizDGlo[0,1]
MatrizDes[5,7]=MatrizBGlo[3,5]+MatrizDGlo[0,2]
MatrizDes[5,11]=MatrizDGlo[0,3]
MatrizDes[5,12]=MatrizDGlo[0,4]
MatrizDes[5,13]=MatrizDGlo[0,5]

#Ecuacion FY4

MatrizDes[6,1]=MatrizBGlo[4,2]
MatrizDes[6,5]=MatrizBGlo[4,3]+MatrizDGlo[1,0]
MatrizDes[6,6]=MatrizBGlo[4,4]+MatrizDGlo[1,1]
MatrizDes[6,7]=MatrizBGlo[4,5]+MatrizDGlo[1,2]
MatrizDes[6,11]=MatrizDGlo[1,3]
MatrizDes[6,12]=MatrizDGlo[1,4]
MatrizDes[6,13]=MatrizDGlo[1,5]

#Ecuacion M4

MatrizDes[7,1]=MatrizBGlo[5,2]
MatrizDes[7,5]=MatrizBGlo[5,3]+MatrizDGlo[2,0]
MatrizDes[7,6]=MatrizBGlo[5,4]+MatrizDGlo[2,1]
MatrizDes[7,7]=MatrizBGlo[5,5]+MatrizDGlo[2,2]
MatrizDes[7,11]=MatrizDGlo[2,3]
MatrizDes[7,12]=MatrizDGlo[2,4]
MatrizDes[7,13]=MatrizDGlo[2,5]

#Ecuacion FX5

MatrizDes[8,2]=MatrizCGlo[3,0]
MatrizDes[8,3]=MatrizCGlo[3,1]
MatrizDes[8,4]=MatrizCGlo[3,2]
MatrizDes[8,8]=MatrizCGlo[3,3]+MatrizEGlo[0,0]
MatrizDes[8,9]=MatrizCGlo[3,4]+MatrizEGlo[0,1]
MatrizDes[8,10]=MatrizCGlo[3,5]+MatrizEGlo[0,2]
MatrizDes[8,11]=MatrizEGlo[0,3]
MatrizDes[8,12]=MatrizEGlo[0,4]
MatrizDes[8,13]=MatrizEGlo[0,5]

#Ecuacion FY5

MatrizDes[9,2]=MatrizCGlo[4,0]
MatrizDes[9,3]=MatrizCGlo[4,1]
MatrizDes[9,4]=MatrizCGlo[4,2]
MatrizDes[9,8]=MatrizCGlo[4,3]+MatrizEGlo[1,0]
MatrizDes[9,9]=MatrizCGlo[4,4]+MatrizEGlo[1,1]
MatrizDes[9,10]=MatrizCGlo[4,5]+MatrizEGlo[1,2]
MatrizDes[9,11]=MatrizEGlo[1,3]
MatrizDes[9,12]=MatrizEGlo[1,4]
MatrizDes[9,13]=MatrizEGlo[1,5]

#Ecuacion M5

MatrizDes[10,2]=MatrizCGlo[5,0]
MatrizDes[10,3]=MatrizCGlo[5,1]
MatrizDes[10,4]=MatrizCGlo[5,2]
MatrizDes[10,8]=MatrizCGlo[5,3]+MatrizEGlo[2,0]
MatrizDes[10,9]=MatrizCGlo[5,4]+MatrizEGlo[2,1]
MatrizDes[10,10]=MatrizCGlo[5,5]+MatrizEGlo[2,2]
MatrizDes[10,11]=MatrizEGlo[2,3]
MatrizDes[10,12]=MatrizEGlo[2,4]
MatrizDes[10,13]=MatrizEGlo[2,5]

#Ecuacion FX6

MatrizDes[11,5]=MatrizDGlo[3,0]
MatrizDes[11,6]=MatrizDGlo[3,1]
MatrizDes[11,7]=MatrizDGlo[3,2]
MatrizDes[11,8]=MatrizEGlo[3,0]
MatrizDes[11,9]=MatrizEGlo[3,1]
MatrizDes[11,10]=MatrizEGlo[3,2]
MatrizDes[11,11]=MatrizDGlo[3,3]+MatrizEGlo[3,3]
MatrizDes[11,12]=MatrizDGlo[3,4]+MatrizEGlo[3,4]
MatrizDes[11,13]=MatrizDGlo[3,5]+MatrizEGlo[3,5]

#Ecuacion FY6

MatrizDes[12,5]=MatrizDGlo[4,0]
MatrizDes[12,6]=MatrizDGlo[4,1]
MatrizDes[12,7]=MatrizDGlo[4,2]
MatrizDes[12,8]=MatrizEGlo[4,0]
MatrizDes[12,9]=MatrizEGlo[4,1]
MatrizDes[12,10]=MatrizEGlo[4,2]
MatrizDes[12,11]=MatrizDGlo[4,3]+MatrizEGlo[4,3]
MatrizDes[12,12]=MatrizDGlo[4,4]+MatrizEGlo[4,4]
MatrizDes[12,13]=MatrizDGlo[4,5]+MatrizEGlo[4,5]

#Ecuacion M6

MatrizDes[13,5]=MatrizDGlo[5,0]
MatrizDes[13,6]=MatrizDGlo[5,1]
MatrizDes[13,7]=MatrizDGlo[5,2]
MatrizDes[13,8]=MatrizEGlo[5,0]
MatrizDes[13,9]=MatrizEGlo[5,1]
MatrizDes[13,10]=MatrizEGlo[5,2]
MatrizDes[13,11]=MatrizDGlo[5,3]+MatrizEGlo[5,3]
MatrizDes[13,12]=MatrizDGlo[5,4]+MatrizEGlo[5,4]
MatrizDes[13,13]=MatrizDGlo[5,5]+MatrizEGlo[5,5]

#print(MatrizDes)


#   3.2 Vector de fuerzas de empotramiento

FEmpDes=np.zeros([14,1])

FEmpDes[2,0]=FEmpCGlo[0]
FEmpDes[3,0]=FEmpCGlo[1]
FEmpDes[4,0]=FEmpCGlo[2]
FEmpDes[5,0]=FEmpDGlo[0]
FEmpDes[6,0]=FEmpDGlo[1]
FEmpDes[7,0]=FEmpDGlo[2]
FEmpDes[8,0]=FEmpCGlo[3]+FEmpEGlo[0]
FEmpDes[9,0]=FEmpCGlo[4]+FEmpEGlo[1]
FEmpDes[10,0]=FEmpCGlo[5]+FEmpEGlo[2]
FEmpDes[11,0]=FEmpDGlo[3]+FEmpEGlo[3]
FEmpDes[12,0]=FEmpDGlo[4]+FEmpEGlo[4]
FEmpDes[13,0]=FEmpDGlo[5]+FEmpEGlo[5]

#print(FEmpDes)


#  Desplazamientos nodales

DesNodales=np.linalg.solve(MatrizDes,-FEmpDes)

q1=DesNodales[0,0]
q2=DesNodales[1,0]
u3=DesNodales[2,0]
v3=DesNodales[3,0]
q3=DesNodales[4,0]
u4=DesNodales[5,0]
v4=DesNodales[6,0]
q4=DesNodales[7,0]
u5=DesNodales[8,0]
v5=DesNodales[9,0]
q5=DesNodales[10,0]
u6=DesNodales[11,0]
v6=DesNodales[12,0]
q6=DesNodales[13,0]

u1=0
v1=0
u2=0
v2=0

#print(DesNodales)


# Calculo de las reacciones

#  Matriz de rigIdez

MatrizReacciones=np.zeros([4,14])

# Ecuacion FX1

MatrizReacciones[0,0]=MatrizAGlo[0,2]
MatrizReacciones[0,2]=MatrizAGlo[0,3]
MatrizReacciones[0,3]=MatrizAGlo[0,4]
MatrizReacciones[0,4]=MatrizAGlo[0,5]

# Ecuacion FY1

MatrizReacciones[1,0]=MatrizAGlo[1,2]
MatrizReacciones[1,2]=MatrizAGlo[1,3]
MatrizReacciones[1,3]=MatrizAGlo[1,4]
MatrizReacciones[1,4]=MatrizAGlo[1,5]

# Ecuacion FX2

MatrizReacciones[2,1]=MatrizBGlo[0,2]
MatrizReacciones[2,5]=MatrizBGlo[0,3]
MatrizReacciones[2,6]=MatrizBGlo[0,4]
MatrizReacciones[2,7]=MatrizBGlo[0,5]

# Ecuacion FY2

MatrizReacciones[3,1]=MatrizBGlo[1,2]
MatrizReacciones[3,5]=MatrizBGlo[1,3]
MatrizReacciones[3,6]=MatrizBGlo[1,4]
MatrizReacciones[3,7]=MatrizBGlo[1,5]


# Reacciones

Rea=MatrizReacciones@DesNodales

FX1=Rea[0,0]
FY1=Rea[1,0]
FX2=Rea[2,0]
FY2=Rea[3,0]



#print(Rea)


#Calculo del campo de desplazamientos

#Elemento A 

[ui,vi,qi,uj,vj,qj]=TA@[u1,v1,q1,u3,v3,q3]

xA=sp.symbols('xA')


#Desplazamiento axial

uA=(1-xA/LA)*ui+xA/LA*uj
#print(uA)
#Desplazamiento normal

A=(-(s**2*ch**2+c**2*sh**2)*vi+(s*c-sh*ch)*qi/Landa+2*s*sh*vj+(c*sh-s*ch)*qj/Landa)/(sh**2-s**2)
B=((s*c+sh*ch)*vi+sh**2/Landa*qi-(s*ch+c*sh)*vj+s*sh/Landa*qj)/(sh**2-s**2)
C=(-(s*c+sh*ch)*vi-s**2/Landa*qi+(s*ch+c*sh)*vj-s*sh/Landa*qj)/(sh**2-s**2)
D=vi

vA=A*sp.sin(Landa*xA)*sp.sinh(Landa*xA)+B*sp.sin(Landa*xA)*sp.cosh(Landa*xA)+C*sp.cos(Landa*xA)*sp.sinh(Landa*xA)+D*sp.cos(Landa*xA)*sp.cosh(Landa*xA)
#print(vA)
# Elemento B

[ui,vi,qi,uj,vj,qj]=TB@[u2,v2,q2,u4,v4,q4]

xB=sp.symbols('xB')

# Desplazamiento axial

uB=(1-xB/LB)*ui+xB/LB*uj
#print(uB)

# Desplazamiento normal

A=(-(s**2*ch**2+c**2*sh**2)*vi+(s*c-sh*ch)*qi/Landa+2*s*sh*vj+(c*sh-s*ch)*qj/Landa)/(sh**2-s**2)
B=((s*c+sh*ch)*vi+sh**2/Landa*qi-(s*ch+c*sh)*vj+s*sh/Landa*qj)/(sh**2-s**2)
C=(-(s*c+sh*ch)*vi-s**2/Landa*qi+(s*ch+c*sh)*vj-s*sh/Landa*qj)/(sh**2-s**2)
D=vi

vB=A*sp.sin(Landa*xB)*sp.sinh(Landa*xB)+B*sp.sin(Landa*xB)*sp.cosh(Landa*xB)+C*sp.cos(Landa*xB)*sp.sinh(Landa*xB)+D*sp.cos(Landa*xB)*sp.cosh(Landa*xB)
#print(vB)


#Elemento C

L=LC
A=Base*Altura
I=Base*Altura**3/12
AE=A*E
EI=E*I

[ui,vi,qi,uj,vj,qj]=TC@[u3,v3,q3,u5,v5,q5]

xC=sp.symbols('xC')

#Desplazamiento axial

uC=(1-xC/LC)*ui+xC/LC*uj
#print(uC)


#Desplazamiento normal

vCH=(1-3*(xC/L)**2+2*(xC/L)**3)*vi+(xC/L)*(1-xC/L)**2*qi*L+(3*(xC/L)**2-2*(xC/L)**3)*vj+(xC/L)**2*(-1+xC/L)*qj*L
vCFInf=-p*(a*b**2/(2*EI)*(xC/L)**2-b**2*(L+2*a)/(6*EI)*(xC/L)**3)
vCFSup=-p*((xC-a)**3/(6*EI)+a*b**2/(2*EI)*(xC/L)**2-b**2*(L+2*a)/(6*EI)*(xC/L)**3)

vCInf=vCH+vCFInf
vCSup=vCH+vCFSup
vCTOTAL=vCInf+vCSup
#Elemento D

L=LD
A=Base*Altura
I=Base*Altura**3/12
AE=A*E
EI=E*I

[ui,vi,qi,uj,vj,qj]=TD@[u4,v4,q4,u6,v6,q6]

xD=sp.symbols('xD')

#Desplazamiento axial

uDH=(1-xD/LD)*ui+xD/LD*uj
uDF=qxLoc*LD**2/(2*AE)*(xD/LD-(xD/LD)**2)

uD=uDH+uDF

#Desplazamiento normal

vDH=(1-3*(xD/L)**2+2*(xD/L)**3)*vi+(xD/L)*(1-xD/L)**2*qi*L+(3*(xD/L)**2-2*(xD/L)**3)*vj+(xD/L)**2*(-1+xD/L)*qj*L
vDF=qyLoc*L**4/(24*EI)*((xD/L)**2-2*(xD/L)**3+(xD/L)**4)

vD=vDH+vDF

#Elemento E

L=LE
A=Base*Altura
I=Base*Altura**3/12
AE=A*E
EI=E*I

[ui,vi,qi,uj,vj,qj]=TE@[u5,v5,q5,u6,v6,q6]

xE=sp.symbols('xE')

#Desplazamiento axial

uE=(1-xE/LE)*ui+xE/LE*uj

#Desplazamiento normal

vEH=(1-3*(xE/L)**2+2*(xE/L)**3)*vi+(xE/L)*(1-xE/L)**2*qi*L+(3*(xE/L)**2-2*(xE/L)**3)*vj+(xE/L)**2*(-1+xE/L)*qj*L
vEF=-q*L**4/(24*EI)*((xE/L)**2-2*(xE/L)**3+(xE/L)**4)

vE=vEH+vEF


#Revision del equilibrio de la estructura

SFx=FX1+FX2+p+sp.integrate(K*vA,(xA,0,H))+sp.integrate(K*vB,(xB,0,H))
SFy=FY1+FY2-q*(LE+d)
SM1=FY2*(LE+d)-p*(H+a)-q*LE**2/2-q*d*(LE+d/2)-sp.integrate(K*vA*xA,(xA,0,H))-sp.integrate(K*vB*xB,(xB,0,H))


#Calculo del campo fuerzas internas

#Elemento A

A=np.pi*R**2
I=np.pi/4*R**4
AE=A*E
EI=E*I

PA= AE*sp.diff(uA,xA,1)
MA= EI*sp.diff(vA,xA,2)
VA=-EI*sp.diff(vA,xA,3)
#Elemento B

A=np.pi*R**2
I=np.pi/4*R**4
AE=A*E
EI=E*I

PB= AE*sp.diff(uB,xB,1)
MB= EI*sp.diff(vB,xB,2)
VB=-EI*sp.diff(vB,xB,3)

#Elemento C

L=LC
A=Base*Altura
I=Base*Altura**3/12
AE=A*E
EI=E*I

PC=AE*sp.diff(uC,xC,1)
MCInf= EI*sp.diff(vCInf,xC,2)
MCSup= EI*sp.diff(vCSup,xC,2)
VCInf=-EI*sp.diff(vCInf,xC,3)
VCSup=-EI*sp.diff(vCSup,xC,3)

#Elemento D

L=LD
A=Base*Altura
I=Base*Altura**3/12
AE=A*E
EI=E*I

PD= AE*sp.diff(uD,xD,1)
MD= EI*sp.diff(vD,xD,2)
VD=-EI*sp.diff(vD,xD,3)

#Elemento E

L=LE
A=Base*Altura
I=Base*Altura**3/12
AE=A*E
EI=E*I

PE= AE*sp.diff(uE,xE,1)
ME= EI*sp.diff(vE,xE,2)
VE=-EI*sp.diff(vE,xE,3)

#%%Diagramas escalas a realizar dentro del dibujo

EscalaDesplaza=100
EscalaAxial=0.01
EscalaCortante=0.02
EscalaMomento=0.02

EL=400

xAN=np.linspace(0,LA,EL)
xBN=np.linspace(0,LB,EL)
xCN=np.linspace(0,LC,EL)
xDN=np.linspace(0,LD,EL)
xEN=np.linspace(0,LE,EL)


uANum=np.zeros([EL])
uBNum=np.zeros([EL])
uCNum=np.zeros([EL])
uDNum=np.zeros([EL])
uENum=np.zeros([EL])

vANum=np.zeros([EL])
vBNum=np.zeros([EL])
vCNum=np.zeros([EL])
vDNum=np.zeros([EL])
vENum=np.zeros([EL])

PANum=np.zeros([EL])
PBNum=np.zeros([EL])
PCNum=np.zeros([EL])
PDNum=np.zeros([EL])
PENum=np.zeros([EL])

MANum=np.zeros([EL])
MBNum=np.zeros([EL])
MCNum=np.zeros([EL])
MDNum=np.zeros([EL])
MENum=np.zeros([EL])

VANum=np.zeros([EL])
VBNum=np.zeros([EL])
VCNum=np.zeros([EL])
VDNum=np.zeros([EL])
VENum=np.zeros([EL])

for i in range(EL):
    uANum[i]=uA.subs(xA,xAN[i])
    uBNum[i]=uB.subs(xB,xBN[i])
    uCNum[i]=uC.subs(xC,xCN[i])
    uDNum[i]=uD.subs(xD,xDN[i])
    uENum[i]=uE.subs(xE,xEN[i])
    
    vANum[i]=vA.subs(xA,xAN[i])
    vBNum[i]=vB.subs(xB,xBN[i])
    vDNum[i]=vD.subs(xD,xDN[i])
    vENum[i]=vE.subs(xE,xEN[i])

    PANum[i]=PA.subs(xA,xAN[i])
    PBNum[i]=PB.subs(xB,xBN[i])
    PCNum[i]=PC.subs(xC,xCN[i])
    PDNum[i]=PD.subs(xD,xDN[i])
    PENum[i]=PE.subs(xE,xEN[i])

    MANum[i]=MA.subs(xA,xAN[i])
    MBNum[i]=MB.subs(xB,xBN[i])
    MDNum[i]=MD.subs(xD,xDN[i])
    MENum[i]=ME.subs(xE,xEN[i])

    VANum[i]=VA.subs(xA,xAN[i])
    VBNum[i]=VB.subs(xB,xBN[i])
    VDNum[i]=VD.subs(xD,xDN[i])
    VENum[i]=VE.subs(xE,xEN[i])

    if xCN[i]<a:
        vCNum[i]=vCInf.subs(xC,xCN[i])
        MCNum[i]=MCInf.subs(xC,xCN[i])
        VCNum[i]=VCInf.subs(xC,xCN[i])
    else:
        vCNum[i]=vCSup.subs(xC,xCN[i])
        MCNum[i]=MCSup.subs(xC,xCN[i])
        VCNum[i]=VCSup.subs(xC,xCN[i])


#%%Figura de la elastica

plt.figure(1,figsize=(8,4))

plt.plot([0,LE+d],[0,0],color='k',linewidth=1)
plt.plot([0,LE+d],[H,H],color='k',linewidth=1)
plt.plot([0,0],[0,H],color='k',linewidth=1)
plt.plot([LE+d,LE+d],[0,H],color='k',linewidth=1)
plt.plot([0,0],[H,H+a+b],color='k',linewidth=1)
plt.plot([LE,LE+d],[H+a+b,H],color='k',linewidth=1)
plt.plot([0,LE],[H+a+b,H+a+b],color='k',linewidth=1)

#   Elemento A
xGloA=0+(xAN+uANum*EscalaDesplaza)*np.cos(tetaA)-vANum*np.sin(tetaA)*EscalaDesplaza
yGloA=0+(xAN+uANum*EscalaDesplaza)*np.sin(tetaA)+vANum*np.cos(tetaA)*EscalaDesplaza    

#   Elemento B
xGloB=LE+d+(xBN+uBNum*EscalaDesplaza)*np.cos(tetaB)-vBNum*np.sin(tetaB)*EscalaDesplaza
yGloB=0+(xBN+uBNum*EscalaDesplaza)*np.sin(tetaB)+vBNum*np.cos(tetaB)*EscalaDesplaza 

#   Elemento C
xGloC=(xCN+uCNum*EscalaDesplaza)*np.cos(tetaC)-vCNum*np.sin(tetaC)*EscalaDesplaza
yGloC=H+(xCN+uCNum*EscalaDesplaza)*np.sin(tetaC)+vCNum*np.cos(tetaC)*EscalaDesplaza  

#   Elemento D
xGloD=LE+d+(xDN+uDNum*EscalaDesplaza)*np.cos(tetaD)-vDNum*np.sin(tetaD)*EscalaDesplaza
yGloD=H+(xDN+uDNum*EscalaDesplaza)*np.sin(tetaD)+vDNum*np.cos(tetaD)*EscalaDesplaza

#   Elemento E
xGloE=(xEN+uENum*EscalaDesplaza)*np.cos(tetaE)-vENum*np.sin(tetaE)*EscalaDesplaza
yGloE=H+a+b+(xEN+uENum*EscalaDesplaza)*np.sin(tetaE)+vENum*np.cos(tetaE)*EscalaDesplaza

plt.plot(xGloA,yGloA,color='k',linestyle='--')
plt.plot(xGloB,yGloB,color='k',linestyle='--')
plt.plot(xGloC,yGloC,color='k',linestyle='--')
plt.plot(xGloD,yGloD,color='k',linestyle='--')
plt.plot(xGloE,yGloE,color='k',linestyle='--')

plt.text(0.2,0.1,'(0,0)')
plt.text(5.2,0.1,'(0,0)')
plt.text(-3.4,H+0.1,'('+str('%.3e' % u3)+','+str('%.3e' % v3)+')')
plt.text(5-3.6,H+0.1,'('+str('%.3e' % u4)+','+str('%.3e' % v4)+')')
plt.text(-3.4,H+a+b,'('+str('%.3e' % u5)+','+str('%.3e' % v5)+')')
plt.text(LE+0.2,H+a+b,'('+str('%.3e' % u6)+','+str('%.3e' % v6)+')')

plt.grid('on')
plt.axis('equal')
plt.xlabel(r'$x$ [m]',fontsize=12)
plt.ylabel(r'$y$ [m]',fontsize=12)
plt.tick_params(labelsize=12)

print(plt.figure)
#%%Figura del campo de fuerza axial

plt.figure(2,figsize=(8,4))

plt.plot([0,LE+d],[0,0],color='k',linewidth=1)
plt.plot([0,LE+d],[H,H],color='k',linewidth=1)
plt.plot([0,0],[0,H],color='k',linewidth=1)
plt.plot([LE+d,LE+d],[0,H],color='k',linewidth=1)
plt.plot([0,0],[H,H+a+b],color='k',linewidth=1)
plt.plot([LE,LE+d],[H+a+b,H],color='k',linewidth=1)
plt.plot([0,LE],[H+a+b,H+a+b],color='k',linewidth=1)

#   Elemento A
xGloA=0+xAN*np.cos(tetaA)-PANum*np.sin(tetaA)*EscalaAxial
yGloA=0+xAN*np.sin(tetaA)+PANum*np.cos(tetaA)*EscalaAxial    

#   Elemento B
xGloB=LE+d+xBN*np.cos(tetaB)-PBNum*np.sin(tetaB)*EscalaAxial
yGloB=0+xBN*np.sin(tetaB)+PBNum*np.cos(tetaB)*EscalaAxial  

#   Elemento C
xGloC=xCN*np.cos(tetaC)-PCNum*np.sin(tetaC)*EscalaAxial
yGloC=H+xCN*np.sin(tetaC)+PCNum*np.cos(tetaC)*EscalaAxial

#   Elemento D
xGloD=LE+d+xDN*np.cos(tetaD)-PDNum*np.sin(tetaD)*EscalaAxial
yGloD=H+xDN*np.sin(tetaD)+PDNum*np.cos(tetaD)*EscalaAxial

#   Elemento E
xGloE=xEN*np.cos(tetaE)-PENum*np.sin(tetaE)*EscalaAxial
yGloE=H+a+b+xEN*np.sin(tetaE)+PENum*np.cos(tetaE)*EscalaAxial

plt.plot(xGloA,yGloA,color='k',linestyle='--')
plt.plot(xGloB,yGloB,color='k',linestyle='--')
plt.plot(xGloC,yGloC,color='k',linestyle='--')
plt.plot(xGloD,yGloD,color='k',linestyle='--')
plt.plot(xGloE,yGloE,color='k',linestyle='--')

plt.text(1,0.1*H,'%4.6g' % PA.subs(xA,0))
plt.text(1,0.9*H,'%4.6g' % PA.subs(xA,LA))
plt.text(LE+d+1.6,0.1*H,'%4.6g' % PB.subs(xB,0))
plt.text(LE+d+1.6,0.9*H,'%4.6g' % PB.subs(xB,LB))
plt.text(1,H+0.1*H,'%4.6g' % PC.subs(xC,0))
plt.text(1,H+LC+0.15,'%4.6g' % PC.subs(xC,LC))
plt.text(LE+d+1.1,H+1.0,'%4.6g' % PD.subs(xD,0))
plt.text(LE+1.0,H+LC+0.2,'%4.6g' % PD.subs(xD,LD))
plt.text(0,H+LC-1,'%4.6g' % PE.subs(xE,0))
plt.text(LE-0.7,H+LC-1,'%4.6g' % PE.subs(xE,LE))

plt.grid('on')
plt.axis('equal')
plt.xlabel(r'$x$ [m]',fontsize=12)
plt.ylabel(r'$y$ [m]',fontsize=12)
plt.tick_params(labelsize=12)

print(plt.figure)


#%%Figura del campo de fuerza cortante

plt.figure(3,figsize=(8,4))

plt.plot([0,LE+d],[0,0],color='k',linewidth=1)
plt.plot([0,LE+d],[H,H],color='k',linewidth=1)
plt.plot([0,0],[0,H],color='k',linewidth=1)
plt.plot([LE+d,LE+d],[0,H],color='k',linewidth=1)
plt.plot([0,0],[H,H+a+b],color='k',linewidth=1)
plt.plot([LE,LE+d],[H+a+b,H],color='k',linewidth=1)
plt.plot([0,LE],[H+a+b,H+a+b],color='k',linewidth=1)


#   Elemento A
xGloA=0+xAN*np.cos(tetaA)-VANum*np.sin(tetaA)*EscalaCortante
yGloA=0+xAN*np.sin(tetaA)+VANum*np.cos(tetaA)*EscalaCortante    

#   Elemento B
xGloB=LE+d+xBN*np.cos(tetaB)-VBNum*np.sin(tetaB)*EscalaCortante
yGloB=0+xBN*np.sin(tetaB)+VBNum*np.cos(tetaB)*EscalaCortante  

#   Elemento C
xGloC=xCN*np.cos(tetaC)-VCNum*np.sin(tetaC)*EscalaCortante
yGloC=H+xCN*np.sin(tetaC)+VCNum*np.cos(tetaC)*EscalaCortante    

#   Elemento D
xGloD=LE+d+xDN*np.cos(tetaD)-VDNum*np.sin(tetaD)*EscalaCortante
yGloD=H+xDN*np.sin(tetaD)+VDNum*np.cos(tetaD)*EscalaCortante

#   Elemento E
xGloE=xEN*np.cos(tetaE)-VENum*np.sin(tetaE)*EscalaCortante
yGloE=H+a+b+xEN*np.sin(tetaE)+VENum*np.cos(tetaE)*EscalaCortante 

plt.plot(xGloA,yGloA,color='k',linestyle='--')
plt.plot(xGloB,yGloB,color='k',linestyle='--')
plt.plot(xGloC,yGloC,color='k',linestyle='--')
plt.plot(xGloD,yGloD,color='k',linestyle='--')
plt.plot(xGloE,yGloE,color='k',linestyle='--')

plt.text(0.1,0,'%4.6g' % VA.subs(xA,0))
plt.text(0.1,0.9*H,'%4.6g' % VA.subs(xA,LA))
plt.text(LE+d+0.3,0,'%4.6g' % VB.subs(xB,0))
plt.text(LE+d+1.0,0.9*H,'%4.6g' % VB.subs(xB,LB))
plt.text(0.1,H,'%4.6g' % VCInf.subs(xC,0))
plt.text(-2.0,H+LC-0.1*H,'%4.6g' % VCSup.subs(xC,LC))
plt.text(LE+d-2.4,H+0.1*H-1,'%4.6g' % VD.subs(xD,0))
plt.text(LE+0.1*LE,H+LC-0.1*H,'%4.6g' % VD.subs(xD,LD))
plt.text(0.3,H+LC+0.05*H-2.4,'%4.6g' % VE.subs(xE,0))
plt.text(LE-0.05*LE+0.2,H+LC+0.05*H+0.5,'%4.6g' % VE.subs(xE,LE))

plt.grid('on')
plt.axis('equal')
plt.xlabel(r'$x$ [m]',fontsize=12)
plt.ylabel(r'$y$ [m]',fontsize=12)
plt.tick_params(labelsize=12)

#print(plt.figure)

#%% Figura del campo de momento flector

plt.figure(4,figsize=(8,4))

plt.plot([0,LE+d],[0,0],color='k',linewidth=1)
plt.plot([0,LE+d],[H,H],color='k',linewidth=1)
plt.plot([0,0],[0,H],color='k',linewidth=1)
plt.plot([LE+d,LE+d],[0,H],color='k',linewidth=1)
plt.plot([0,0],[H,H+a+b],color='k',linewidth=1)
plt.plot([LE,LE+d],[H+a+b,H],color='k',linewidth=1)
plt.plot([0,LE],[H+a+b,H+a+b],color='k',linewidth=1)

#   Elemento A
xGloA=0+xAN*np.cos(tetaA)-MANum*np.sin(tetaA)*EscalaMomento
yGloA=0+xAN*np.sin(tetaA)+MANum*np.cos(tetaA)*EscalaMomento    

#   Elemento B
xGloB=LE+d+xBN*np.cos(tetaB)-MBNum*np.sin(tetaB)*EscalaMomento
yGloB=0+xBN*np.sin(tetaB)+MBNum*np.cos(tetaB)*EscalaMomento    

#   Elemento C
xGloC=xCN*np.cos(tetaC)-MCNum*np.sin(tetaC)*EscalaMomento
yGloC=H+xCN*np.sin(tetaC)+MCNum*np.cos(tetaC)*EscalaMomento    

#   Elemento D
xGloD=LE+d+xDN*np.cos(tetaD)-MDNum*np.sin(tetaD)*EscalaMomento
yGloD=H+xDN*np.sin(tetaD)+MDNum*np.cos(tetaD)*EscalaMomento 

#   Elemento E
xGloE=xEN*np.cos(tetaE)-MENum*np.sin(tetaE)*EscalaMomento
yGloE=H+a+b+xEN*np.sin(tetaE)+MENum*np.cos(tetaE)*EscalaMomento 

plt.plot(xGloA,yGloA,color='k',linestyle='--')
plt.plot(xGloB,yGloB,color='k',linestyle='--')
plt.plot(xGloC,yGloC,color='k',linestyle='--')
plt.plot(xGloD,yGloD,color='k',linestyle='--')
plt.plot(xGloE,yGloE,color='k',linestyle='--')

plt.text(0.1,0.1,'%4.6g' % 0)
plt.text(0.3,0.9*H,'%4.6g' % MA.subs(xA,LA))
plt.text(LE+d+0.1,0.1,'%4.6g' % 0)
plt.text(LE+d-2.9,0.9*H,'%4.6g' % MB.subs(xB,LB))
plt.text(0.3,H+0.2,'%4.6g' % MCInf.subs(xC,0))
plt.text(0+1,H+LC-0.1*H,'%4.6g' % MCSup.subs(xC,LC))
plt.text(LE+d-2.9,H-0.9,'%4.6g' % MD.subs(xD,0))
plt.text(LE+0.1*LE+0.5,H+LC-0.2,'%4.6g' % MD.subs(xD,LD))
plt.text(-1.5,H+LC-0.8,'%4.6g' % ME.subs(xE,0))
plt.text(LE-0.05*LE+0.4,H+LC+0.05*H+0.1,'%4.6g' % ME.subs(xE,LE))

plt.grid('on')
plt.axis('equal')
plt.xlabel(r'$x$ [m]',fontsize=12)
plt.ylabel(r'$y$ [m]',fontsize=12)
plt.tick_params(labelsize=12)


#print(plt.figure)

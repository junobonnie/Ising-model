# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:08:37 2019

@author: user
"""
import random as r
import math as m

Length=1
Width=30
Height=30

spinNum = Length*Width*Height
uH = [[[0.0]*Length for i in range(Width)] for j in range(Height)]
dH = [[[0.0]*Length for i in range(Width)] for j in range(Height)]
spin = ['up','down']

#B=10
#u=0.5   
#e=0.1
#k=0.1
#T=100

B=0.5*3*0.9274/4
u=1
e=1.269*1.38
k=1.38
T=10
spinList=[]
for i in range(0,int(spinNum/2)):
    spinList.append(spin[0])
for i in range(int(spinNum/2),spinNum):
    spinList.append(spin[1])
r.shuffle(spinList)
def spinH(i,j,k):
    global B, u, e
    global Length, Width, Height
    for s in spin:
        H = [[[0.0]*Length for i in range(Width)] for j in range(Height)]
        if(s == 'up'):
            H[i][j][k] = -u*B
        else:
            H[i][j][k] = u*B
        if(i-1 >= 0):
            if(spinList[Width*Length*(i-1)+Length*j+k] == s):    
                H[i][j][k] = H[i][j][k] - e*(u**2)
            else:
                H[i][j][k] = H[i][j][k] + e*(u**2)    
        if(j-1 >= 0):
            if(spinList[Width*Length*i+Length*(j-1)+k] == s):    
                H[i][j][k] = H[i][j][k] - e*(u**2)
            else:
                H[i][j][k] = H[i][j][k] + e*(u**2)
        if(k-1 >= 0):
            if(spinList[Width*Length*i+Length*j+k-1] == s):    
                H[i][j][k] = H[i][j][k] - e*(u**2)
            else:
                H[i][j][k] = H[i][j][k] + e*(u**2)       
                    
        if(i+1 <= Height-1):
            if(spinList[Width*Length*(i+1)+Length*j+k] == s):    
                H[i][j][k] = H[i][j][k] - e*(u**2)
            else:
                H[i][j][k] = H[i][j][k] + e*(u**2)
        if(j+1 <= Width-1):
            if(spinList[Width*Length*i+Length*(j+1)+k] == s):    
                H[i][j][k] = H[i][j][k] - e*(u**2)
            else:
                H[i][j][k] = H[i][j][k] + e*(u**2)        
        if(k+1 <= Length-1):
            if(spinList[Width*Length*i+Length*j+k+1] == s):    
                H[i][j][k] = H[i][j][k] - e*(u**2)
            else:
                H[i][j][k] = H[i][j][k] + e*(u**2)
                
        if(s == 'up'):
            uH[i][j][k] = H[i][j][k]
        else:
            dH[i][j][k] = H[i][j][k]
            
def spinChange():
    global k
    global T
    global spinNum
    global Length, Width, Height
    for i in range(spinNum):
        spinH(i//(Length*Width),(i%(Length*Width))//Length,i%Length)
        
    LnZ_tot=0
    for i in range(spinNum):

        Z = m.exp(-uH[i//(Length*Width)][(i%(Length*Width))//Length][i%Length]/(k*T))+m.exp(-dH[i//(Length*Width)][(i%(Length*Width))//Length][i%Length]/(k*T))
        P = m.exp(-uH[i//(Length*Width)][(i%(Length*Width))//Length][i%Length]/(k*T))/Z
        if(r.random()<0.5):
            if(r.random()<P):
                spinList[i] = 'up'
            else:
                spinList[i] = 'down'
        LnZ_tot=LnZ_tot+m.log(Z)
    N_up = 0
    N_down = 0      
    for i in range(spinNum):
        if(spinList[i] == 'up'):
            N_up = N_up+1
        else:
            N_down = N_down+1
    
#    for i in range(0,Height):
#        print(spinList[i])
    print("N↑=%d N↓=%d"%(N_up, N_down))  
    return [N_up,LnZ_tot]

f = open(r"C:\Users\user\Desktop\업_스핀101.txt", 'w')
f2 = open(r"C:\Users\user\Desktop\엔트로피101.txt", 'w')
for i in range(1,1001):
    print(i,end=":")
    data = spinChange()
    f.write(str(data[0])+"\n")
    f2.write(str(data[1])+"\n")
f.close()
f2.close()
    
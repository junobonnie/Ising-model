# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:33:36 2019

@author: user
"""

from tkinter import *
import random as r
import math as m

uH = [[0.0]*20 for i in range(20)]
dH = [[0.0]*20 for i in range(20)]
spin = ['  ↑ ','  ↓ ']
B=0
u=0.5   
e=0.1  
k=0.1
T=0.1
pause = False
class MyAPP(Tk):
    def __init__(self):
        Tk.__init__(self)
        
#        self.t_label = IntVar(self,0)
#        self.label = Label(self)#,textvariable = self.t_label)
#        self.label.pack()
        
        self.spinList = []
        for i in range(0,200):
            self.spinList.append(Button(self,text='  ↑ ', font=('Raavi',12,'bold'), relief="flat", bg='red'))
        for i in range(200,400):
            self.spinList.append(Button(self,text='  ↓ ', font=('Raavi',12,'bold'), relief="flat", bg='blue'))
        r.shuffle(self.spinList)
        for i in range(0,400):
            self.spinList[i].configure(command= lambda indexK=i: self.clickChange(indexK))
        #===========================================
        for i in range(0,20):
            for j in range(0,20):
                self.spinList[20*i+j].place(x=35*j,y=35+33*i)
        self.label2 = Label(self, text="N↑=200 N↓=200", width=20, relief='solid',bd=3, font=('Raavi',12,'bold'), fg="black")
        self.label2.place(x=400,y=5)
    def spinH(self,i,j):
        global B
        global e
        for s in spin:
            H = [[0.0]*20 for i in range(20)]
            if(s == '  ↑ '):
                H[i][j] = -u*B
            else:
                H[i][j] = u*B
            if(i-1 >= 0):
                if(self.spinList[20*(i-1)+j]['text'] == s):    
                    H[i][j] = H[i][j] - e*(u**2)
                else:
                    H[i][j] = H[i][j] + e*(u**2)    
            if(j-1 >= 0):
                if(self.spinList[20*i+j-1]['text'] == s):    
                    H[i][j] = H[i][j] - e*(u**2)
                else:
                    H[i][j] = H[i][j] + e*(u**2)
            if(j+1 <= 19):
                if(self.spinList[20*i+j+1]['text'] == s):    
                    H[i][j] = H[i][j] - e*(u**2)
                else:
                    H[i][j] = H[i][j] + e*(u**2)
            if(i+1 <= 19):
                if(self.spinList[20*(i+1)+j]['text'] == s):    
                    H[i][j] = H[i][j] - e*(u**2)
                else:
                    H[i][j] = H[i][j] + e*(u**2)
            if(s == '  ↑ '):
                uH[i][j] = H[i][j]
            else:
                dH[i][j] = H[i][j]
    #===========================================
    def spinChange(self):
        global k
        global T
        global time
        if(button1["text"] == '시작하기'):
            button1.configure(command = self.restart)
            button1["text"] = '멈추기' 
        if(pause == False):
            for i in range(400):
                self.spinH(i//20,i%20)
            
            for i in range(400):
                Z = m.exp(-uH[i//20][i%20]/(k*T))+m.exp(-dH[i//20][i%20]/(k*T))
                P = m.exp(-uH[i//20][i%20]/(k*T))/Z
                if(r.random()<0.5):
                    if(r.random()<P):
                        self.spinList[i]['text'] = '  ↑ '
                        self.spinList[i]['bg'] = 'red'
                    else:
                        self.spinList[i]['text'] = '  ↓ '
                        self.spinList[i]['bg'] = 'blue'
            N_up = 0
            N_down = 0      
            for i in range(400):
                if(self.spinList[i]['text'] == '  ↑ '):
                    N_up = N_up+1
                else:
                    N_down = N_down+1
            self.label2["text"] = "N↑=%d N↓=%d"%(N_up, N_down)
        self.after(200,self.spinChange)              
                
    def clickChange(self,i):
        if(self.spinList[i]['text'] == '  ↑ '):    
            self.spinList[i]['text'] = '  ↓ '
            self.spinList[i]['bg'] = 'blue'
        else:
            self.spinList[i]['text'] = '  ↑ '
            self.spinList[i]['bg'] = 'red'
    def restart(self):
        global pause
        if pause == True:
            pause = False 
            button1["text"] = '멈추기'
        else:
            pause = True
            button1["text"] = '계속하기'
            
window = MyAPP()
window.title("2차원 이징 모델")#창제목설정
window.geometry("750x750")#창크기설정
window.resizable(1,1)
label1 = Label(window, text="B=%.2f, u=%.2f, e=%.2f, T=%.2f"%(B,u,e,T), width=30, relief='solid',bd=3, font=('Raavi',12,'bold'), fg="black")
label1.place(x=60,y=5)
button1 = Button(window,text='시작하기',width=6,height=4,font=('Raavi',5,'bold'),command=window.spinChange)
button1.place(x=0,y=0) 
#window.spinChange()
window.mainloop()
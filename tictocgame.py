# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:06:03 2018

@author: ABHINAVMITTAL
"""

from tkinter import*
from tkinter import messagebox

home =Tk()    # figure  k is small
home.geometry('670x455')
home.title('Tic_Toc_Game') #title

top=Frame(home)
top.grid()

win=Frame(home)
win.grid()

click_number = IntVar()
click_number.set(0)
turnnumber = IntVar(0)

m=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

def displaymessage(mess):
    messagebox.showinfo("Game_Result",mess)
    m.clear()
    for i in range(12):
        m.append(-1)
    reset()

def reset():
    click_number.set(0)
    turnnumber.set(0)
    firstplayer.set('')
    secondplayer.set('')
    button1.config(state='active',text='')
    button2.config(state='active',text='')
    button3.config(state='active',text='')
    button4.config(state='active',text='')
    button5.config(state='active',text='')
    button6.config(state='active',text='')
    button7.config(state='active',text='')
    button8.config(state='active',text='')
    button9.config(state='active',text='')
    mess=''
    
def click(a):
    d=click_number.get()
    #print(d)
    d=d+1
    click_number.set(d)
    if(a==1):
        d=turnnumber.get()
        m[a]=d
        if(d==0):
            button1['text']='0'
            d=1
        else:
            button1['text']='X'
            d=0
        turnnumber.set(d)
        button1.config(state="disabled")
    elif(a==2):
        d=turnnumber.get()
        m[a]=d
        if(d==0):
            button2['text']='0'
            d=1
        else:
            button2['text']='X'
            d=0
        turnnumber.set(d)
        button2.config(state="disabled")
    elif(a==3):
        d=turnnumber.get()
        m[a]=d
        if(d==0):
            button3['text']='0'
            d=1
        else:
            button3['text']='X'
            d=0
        turnnumber.set(d)
        button3.config(state="disabled")
    elif(a==4):
        d=turnnumber.get()
        m[a]=d
        if(d==0):
            button4['text']='0'
            d=1
        else:
            button4['text']='X'
            d=0
        turnnumber.set(d)
        button4.config(state="disabled")
    elif(a==5):
        d=turnnumber.get()
        m[a]=d
        if(d==0):
            button5['text']='0'
            d=1
        else:
            button5['text']='X'
            d=0
        turnnumber.set(d)
        button5.config(state="disabled")
    elif(a==6):
        d=turnnumber.get()
        m[a]=d
        if(d==0):
            button6['text']='0'
            d=1
        else:
            button6['text']='X'
            d=0
        turnnumber.set(d)
        button6.config(state="disabled")
    elif(a==7):
        d=turnnumber.get()
        m[a]=d
        if(d==0):
            button7['text']='0'
            d=1
        else:
            button7['text']='X'
            d=0
        turnnumber.set(d)
        button7.config(state="disabled")
    elif(a==8):
        d=turnnumber.get()
        m[a]=d
        if(d==0):
            button8['text']='0'
            d=1
        else:
            button8['text']='X'
            d=0
        turnnumber.set(d)
        button8.config(state="disabled")
    elif(a==9):
        d=turnnumber.get()
        m[a]=d
        if(d==0):
            button9['text']='0'
            d=1
        else:
            button9['text']='X'
            d=0
        turnnumber.set(d)
        button9.config(state="disabled")
    if(click_number.get() < 9 ):  
        if((m[1]==1 and m[2]==1 and m[3]==1) or (m[1]==1 and m[4]==1 and m[7]==1) or (m[1]==1 and m[5]==1 and m[9]==1) or (m[4]==1 and m[5]==1 and m[6]==1) or (m[7]==1 and m[8]==1 and m[9]==1) or (m[2]==1 and m[5]==1 and m[8]==1) or (m[3]==1 and m[6]==1 and m[9]==1) or (m[3]==1 and m[5]==1 and m[7]==1)):
            mess='Winner is %s'%(secondplayer.get())
            displaymessage(mess)
        elif((m[1]==0 and m[2]==0 and m[3]==0) or (m[1]==0 and m[4]==0 and m[7]==0) or (m[1]==0 and m[5]==0 and m[9]==0) or (m[4]==0 and m[5]==0 and m[6]==0) or (m[7]==0 and m[8]==0 and m[9]==0) or (m[2]==0 and m[5]==0 and m[8]==0) or (m[3]==0 and m[6]==0 and m[9]==0) or (m[3]==0 and m[5]==0 and m[7]==0)):
            mess='Winner is %s'%(firstplayer.get())
            displaymessage(mess)
    if(click_number.get() == 9):
        if((m[1]==1 and m[2]==1 and m[3]==1) or (m[1]==1 and m[4]==1 and m[7]==1) or (m[1]==1 and m[5]==1 and m[9]==1) or (m[4]==1 and m[5]==1 and m[6]==1) or (m[7]==1 and m[8]==1 and m[9]==1) or (m[2]==1 and m[5]==1 and m[8]==1) or (m[3]==1 and m[6]==1 and m[9]==1) or (m[3]==1 and m[5]==1 and m[7]==1)):
            mess='Winner is %s'%(secondpalyer.get())
            displaymessage(mess)
        elif((m[1]==0 and m[2]==0 and m[3]==0) or (m[1]==0 and m[4]==0 and m[7]==0) or (m[1]==0 and m[5]==0 and m[9]==0) or (m[4]==0 and m[5]==0 and m[6]==0) or (m[7]==0 and m[8]==0 and m[9]==0) or (m[2]==0 and m[5]==0 and m[8]==0) or (m[3]==0 and m[6]==0 and m[9]==0) or (m[3]==0 and m[5]==0 and m[7]==0)):
            mess='Winner is %s'%(firstplayer.get())
            displaymessage(mess)
        else:
            mess='Draw'
            displaymessage(mess)
    #print(m)
firstplayer=StringVar()
secondplayer=StringVar()

firstplayer1=Label(top,text='First Player:',font = ("Arial", 20, "bold"),fg ='blue' )
firstplayer1.grid(row=1,column=0)

firstplayerEntry=Entry(top,textvariable=firstplayer,font = ("Arial", 15, "bold"))
firstplayerEntry.grid(row=1,column=1)

secondplayer2=Label(top,text='Second Player:',font = ("Arial", 20, "bold"),fg='red')
secondplayer2.grid(row=2,column=0)

secondplayerEntry=Entry(top,textvariable=secondplayer,font = ("Arial", 15, "bold"))
secondplayerEntry.grid(row=2,column=1)

button1=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,bd=5,fg='green',command=lambda :click(1))   #name of figure,text on button,height=no. of lines,width=no. of char,fg=color of text,bg=background color,command=to perform an action after clicking on button
button1.grid(row=3,column=0)

button2=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,bd=5,fg='green',command=lambda :click(2))
button2.grid(row=3,column=1)

button3=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,bd=5,fg='green',command=lambda :click(3))
button3.grid(row=3,column=2)

button4=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,bd=5,fg='green',command=lambda :click(4))   #name of figure,text on button,height=no. of lines,width=no. of char,fg=color of text,bg=background color,command=to perform an action after clicking on botton
button4.grid(row=4,columnspan=1)

button5=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,bd=5,fg='green',command=lambda :click(5))
button5.grid(row=4,column=1)

button6=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,bd=5,fg='green',command=lambda :click(6))
button6.grid(row=4,column=2)

button7=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,bd=5,fg='green',command=lambda :click(7))   #name of figure,text on button,height=no. of lines,width=no. of char,fg=color of text,bg=background color,command=to perform an action after clicking on botton
button7.grid(row=5,columnspan=1)

button8=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,bd=5,fg='green',command=lambda :click(8))
button8.grid(row=5,column=1)

button9=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,bd=5,fg='green',command=lambda :click(9))
button9.grid(row=5,column=2)

win.mainloop()

from tkinter import*
from tkinter import messagebox

win =Tk()    # figure  k is small  
win.title('First_GUI') #title
win.grid()  #geometry

click_number = IntVar()
turnnumber = IntVar(0)
one = IntVar(0)
one.set(-1)
two = IntVar(0)
two.set(-1)
three = IntVar(0)
three.set(-1)
four = IntVar(0)
four.set(-1)
five = IntVar(0)
five.set(-1)
six = IntVar(0)
six.set(-1)
seven = IntVar(0)
seven.set(-1)
eight = IntVar(0)
eight.set(-1)
nine = IntVar(0)
nine.set(-1)

def displaymessage(mess):
    messagebox.showinfo("Game_Result",mess)


def click(a):
    d=click_number.get()
    d=d+1
    click_number.set(d)
    if(a==1):
        d=turnnumber.get()
        one.set(d)
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
        two.set(d)
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
        three.set(d)
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
        four.set(d)
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
        five.set(d)
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
        six.set(d)
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
        seven.set(d)
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
        eight.set(d)
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
        nine.set(d)
        if(d==0):
            button9['text']='0'
            d=1
        else:
            button9['text']='X'
            d=0
        turnnumber.set(d)
        button9.config(state="disabled")
    if(click_number.get() < 9 ):  
        if((one.get()==1 and two.get()==1 and three.get()==1) or (one.get()==1 and four.get()==1 and seven.get()==1) or (one.get()==1 and five.get()==1 and nine.get()==1) or (four.get()==1 and five.get()==1 and six.get()==1) or (seven.get()==1 and eight.get()==1 and nine.get()==1) or (two.get()==1 and five.get()==1 and eight.get()==1) or (three.get()==1 and six.get()==1 and nine.get()==1) or (three.get()==1 and five.get()==1 and seven.get()==1)):
            mess='Winner is 1'
            displaymessage(mess)
            click_number.set(10)
        if((one.get()==0 and two.get()==0 and three.get()==0) or (one.get()==0 and four.get()==0 and seven.get()==0) or (one.get()==0 and five.get()==0 and nine.get()==0) or (four.get()==0 and five.get()==0 and six.get()==0) or (seven.get()==0 and eight.get()==0 and nine.get()==0) or (two.get()==0 and five.get()==0 and eight.get()==0) or (three.get()==0 and six.get()==0 and nine.get()==0) or (three.get()==0 and five.get()==0 and seven.get()==0)):
            mess='Winner is 0'
            displaymessage(mess)
            click_number.set(10)
    if(click_number.get() == 9):
        if((one.get()==1 and two.get()==1 and three.get()==1) or (one.get()==1 and four.get()==1 and seven.get()==1) or (one.get()==1 and five.get()==1 and nine.get()==1) or (four.get()==1 and five.get()==1 and six.get()==1) or (seven.get()==1 and eight.get()==1 and nine.get()==1) or (two.get()==1 and five.get()==1 and eight.get()==1) or (three.get()==1 and six.get()==1 and nine.get()==1) or (three.get()==1 and five.get()==1 and seven.get()==1)):
            mess='Winner is 1'
            displaymessage(mess)
            click_number.set(10)
        elif((one.get()==0 and two.get()==0 and three.get()==0) or (one.get()==0 and four.get()==0 and seven.get()==0) or (one.get()==0 and five.get()==0 and nine.get()==0) or (four.get()==0 and five.get()==0 and six.get()==0) or (seven.get()==0 and eight.get()==0 and nine.get()==0) or (two.get()==0 and five.get()==0 and eight.get()==0) or (three.get()==0 and six.get()==0 and nine.get()==0) or (three.get()==0 and five.get()==0 and seven.get()==0)):
            mess='Winner is 0'
            displaymessage(mess)
            click_number.set(10)
        else:
            mess='Draw'
            displaymessage(mess)
            click_number.set(10)

button1=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,fg='green',bg='pink',command=lambda :click(1))   #name of figure,text on button,height=no. of lines,width=no. of char,fg=color of text,bg=background color,command=to perform an action after clicking on botton
button1.grid(row=1,column=0)

button2=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,fg='green',bg='pink',command=lambda :click(2))
button2.grid(row=1,column=1)

button3=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,fg='green',bg='pink',command=lambda :click(3))
button3.grid(row=1,column=2)

button4=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,fg='green',bg='pink',command=lambda :click(4))   #name of figure,text on button,height=no. of lines,width=no. of char,fg=color of text,bg=background color,command=to perform an action after clicking on botton
button4.grid(row=2,column=0)

button5=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,fg='green',bg='pink',command=lambda :click(5))
button5.grid(row=2,column=1)

button6=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,fg='green',bg='pink',command=lambda :click(6))
button6.grid(row=2,column=2)

button7=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,fg='green',bg='pink',command=lambda :click(7))   #name of figure,text on button,height=no. of lines,width=no. of char,fg=color of text,bg=background color,command=to perform an action after clicking on botton
button7.grid(row=3,column=0)

button8=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,fg='green',bg='pink',command=lambda :click(8))
button8.grid(row=3,column=1)

button9=Button(win,text='',font = ("Arial", 20, "bold"), height=3,width=12,fg='green',bg='pink',command=lambda :click(9))
button9.grid(row=3,column=2)

win.mainloop()

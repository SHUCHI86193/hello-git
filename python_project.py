from tkinter import*
import random
import datetime
import time

root=Tk()
root.geometry("1500x6000")
root.title("BILLING COUNTER")



f1=Frame(root, width=1500, relief=SUNKEN)
f1.pack(side=TOP)

f2=Frame(root,height=600, width=5000, relief=SUNKEN)
f2.pack(side=LEFT)
l=time.asctime(time.localtime(time.time()))

lb=Label(f1,font=('ALGERIAN',40,'bold'),text="RESTAURANT MANAGEMENT SYSTEM", fg="Black",bd=8,anchor='w')
lb.grid(row=0,column=0)
lb=Label(f1,font=('arial',20,'bold'),text=l,fg="Steel Blue",bd=8,anchor='w')
lb.grid(row=1,column=0)



#taking values

def calc():
    
    x=random.randint(1,50000)
    randomRef=str(x)
    rand.set(randomRef)

    if(fries.get()==""):
        cf=0
    else:
        cf=float(fries.get())

    if(lunch.get()==""):
        lu=0
    else:
        lu=float(lunch.get())

    if(biryani.get()==""):
        bir=0
    else:
        bir=float(biryani.get())

    if(pizza.get()==""):
        piz=0
    else:
        piz=float(pizza.get())

    if(cheese.get()==""):
        ch=0
    else:
        ch=float(cheese.get())

    if(drink.get()==""):
        dr=0
    else:
        dr=float(drink.get())

    cof=cf*150
    col=lu*250
    cob=bir*300
    cop=piz*500
    coc=ch*100
    cod=dr*150

    tot=cof+col+cob+cop+coc+cod
    costofmeal="Rs",str('%.2f'% (cof+col+cob+cop+coc+cod))
    service_charge=((cof+col+cob+cop+coc+cod)*0.01)
    ser_form="Rs",str('%.2f'%service_charge)
    taxx=((cof+col+cob+cop+coc+cod)*0.05)
    p_tax="Rs",str('%.2f'%taxx)
    totall="Rs",str('%.2f'%(taxx+tot+service_charge))

    cost.set(costofmeal)
    service.set(ser_form)
    tax.set(p_tax)
    subtotal.set(costofmeal)
    total.set(totall)

def reset():
    rand.set("")
    drink.set("")
    fries.set("")
    cost.set("")
    lunch.set("")
    service.set("")
    biryani.set("")
    tax.set("")
    pizza.set("")
    subtotal.set("")
    cheese.set("")
    total.set("")

def ex():
    root.destroy()

def pricelist():
    win= Tk()
    win.title("PRICE-LIST")
    lb=Listbox(win, height=6, bd=8, font=('arial',13,'bold'), bg="powder blue")
    lb.pack()
    lb.insert(END,"FRIES = Rs 150")
    lb.insert(END,"THALI = Rs 250")
    lb.insert(END,"BIRYANI = Rs 300")
    lb.insert(END,"PIZZA = Rs 500")
    lb.insert(END,"BURGER = Rs 100")
    lb.insert(END,"DRINKS = Rs 150")
    

#labels and textfields
rand= StringVar()
drink= StringVar()
fries= StringVar()
cost= StringVar()
lunch= StringVar()
service= StringVar()
biryani= StringVar()
tax= StringVar()
pizza= StringVar()
subtotal= StringVar()
cheese= StringVar()
total= StringVar()

l1=Label(f2,font=('arial',15,'bold'),text="Order No.",bd=16,anchor='w')
l1.grid(row=0,column=0)
t1=Entry(f2,font=('arial',15,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='left')
t1.grid(row=0,column=1)

l2=Label(f2,font=('arial',15,'bold'),text="Drinks",bd=16,anchor='w')
l2.grid(row=0,column=3)
t2=Entry(f2,font=('arial',15,'bold'),textvariable=drink,bd=10,insertwidth=4,bg="powder blue",justify='right')
t2.grid(row=0,column=4)

l3=Label(f2,font=('arial',15,'bold'),text="Fries",bd=16,anchor='w')
l3.grid(row=1,column=0)
t3=Entry(f2,font=('arial',15,'bold'),textvariable=fries,bd=10,insertwidth=4,bg="powder blue",justify='left')
t3.grid(row=1,column=1)

l4=Label(f2,font=('arial',15,'bold'),text="Cost",bd=16,anchor='w')
l4.grid(row=1,column=3)
t4=Entry(f2,font=('arial',15,'bold'),textvariable=cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
t4.grid(row=1,column=4)

l5=Label(f2,font=('arial',15,'bold'),text="Thali",bd=16,anchor='w')
l5.grid(row=2,column=0)
t5=Entry(f2,font=('arial',15,'bold'),textvariable=lunch,bd=10,insertwidth=4,bg="powder blue",justify='left')
t5.grid(row=2,column=1)

l6=Label(f2,font=('arial',15,'bold'),text="Service Charge",bd=16,anchor='w')
l6.grid(row=2,column=3)
t6=Entry(f2,font=('arial',15,'bold'),textvariable=service,bd=10,insertwidth=4,bg="powder blue",justify='right')
t6.grid(row=2,column=4)

l7=Label(f2,font=('arial',15,'bold'),text="Biryani",bd=16,anchor='w')
l7.grid(row=3,column=0)
t7=Entry(f2,font=('arial',15,'bold'),textvariable=biryani,bd=10,insertwidth=4,bg="powder blue",justify='left')
t7.grid(row=3,column=1)

l8=Label(f2,font=('arial',15,'bold'),text="Tax",bd=16,anchor='w')
l8.grid(row=3,column=3)
t8=Entry(f2,font=('arial',15,'bold'),textvariable=tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
t8.grid(row=3,column=4)

l9=Label(f2,font=('arial',15,'bold'),text="Pizza",bd=16,anchor='w')
l9.grid(row=4,column=0)
t9=Entry(f2,font=('arial',15,'bold'),textvariable=pizza,bd=10,insertwidth=4,bg="powder blue",justify='left')
t9.grid(row=4,column=1)

l10=Label(f2,font=('arial',15,'bold'),text="SubTotal",bd=16,anchor='w')
l10.grid(row=4,column=3)
t10=Entry(f2,font=('arial',15,'bold'),textvariable=subtotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
t10.grid(row=4,column=4)

l11=Label(f2,font=('arial',15,'bold'),text="Burger",bd=16,anchor='w')
l11.grid(row=5,column=0)
t11=Entry(f2,font=('arial',15,'bold'),textvariable=cheese,bd=10,insertwidth=4,bg="powder blue",justify='left')
t11.grid(row=5,column=1)

l12=Label(f2,font=('arial',15,'bold'),text="Total",bd=16,anchor='w')
l12.grid(row=5,column=3)
t12=Entry(f2,font=('arial',15,'bold'),textvariable=total,bd=10,insertwidth=4,bg="powder blue",justify='right')
t12.grid(row=5,column=4)

#buttons

btn1=Button(f2,font=('ALGERIAN',15,'bold'),text="PRICE",bg="powder blue",bd=10,height=2,width=20,command=pricelist)
btn1.grid(row=6,column=1)

btn2=Button(f2,font=('ALGERIAN',15,'bold'),text="TOTAL",bg="powder blue",bd=10,height=2,width=20,command=calc)
btn2.grid(row=6,column=2)

btn3=Button(f2,font=('ALGERIAN',15,'bold'),text="RESET",bg="powder blue",bd=10,height=2,width=20,command=reset)
btn3.grid(row=6,column=3)

btn4=Button(f2,font=('ALGERIAN',15,'bold'),text="EXIT",bg="powder blue",bd=10,height=2,width=20,command=ex)
btn4.grid(row=6,column=4)

root.mainloop()

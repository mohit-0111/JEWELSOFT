from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter.filedialog import asksaveasfile
import prices
import mysql.connector

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1011',
    database='bill'
)




root=Tk()
style=ttk.Style()
style.theme_use('vista')
root.geometry('500x400')
root.title('jewellery billing')
root.config(background='lavender')
'''bg=PhotoImage(file='j2.png')
Label(root,image=bg).place(x=500,y=0)
bkg=PhotoImage(file='bis.png')
Label(root,image=bkg).place(x=0,y=293)'''



x=prices.gold_price()
y=prices.silver_price()

Label(root,text='Sangam Jewellers',font=("Times", "24", "bold italic"),bg='lavender',fg='teal').pack()
Label(root,text='Customer Name ',bg='teal',fg='pink').place(x=0,y=50)
Label(root,text='Phone No ',bg='teal',fg='pink').place(x=200,y=50)
Label(root,text='Select Item',bg='teal',fg='pink').place(x=0,y=90)
Label(root,text='Enter Weight',bg='teal',fg='pink').place(x=180,y=90)
Label(root,text='purity',bg='teal',fg='pink').place(x=330,y=90)
Label(root,text='GOLD: ',bg='teal',fg='pink').place(x=0,y=150)
Label(root,text='SILVER: ',bg='teal',fg='pink').place(x=0,y=200)
Label(root,text=int(x[3:5]+x[6:9]),fg='red',bg='lavender').place(x=50,y=150)
Label(root,text=y[1:],fg='red',bg='lavender').place(x=50,y=200)


p=StringVar()
purity=ttk.Combobox(root,width=8,textvariable=p)
gol=['916','833','750']
sil=['DS70','925','I925']
purity.place(x=380,y=90)

t=StringVar()
#total=Entry(root,width=10,textvariable=t).place(x=70,y=150)
w=StringVar()
weight=Entry(root,width=8,textvariable=w).place(x=260,y=90)
cn=StringVar()
name=Entry(root,width=15,textvariable=cn).place(x=100,y=50)
pn=StringVar()
phone=Entry(root,width=12,textvariable=pn).place(x=270,y=50)

def gold():
    itemchoosen['values']=goldd
    purity['values']=gol
def silver():
    itemchoosen['values']=silverr
    purity['values']=sil
v = IntVar()
Radiobutton(root, text = 'GOLD', variable = v,value = 1,command=gold).place(x=150,y=250)
Radiobutton(root, text = 'SILVER', variable = v,value = 2,command=silver).place(x=150,y=280)

goldd=['chain','ring','bangles','tikka','bali','tops','locket','necklace','kada','bracelet']
silverr=['chain','L ring','G ring','payal','bicchiya','bangles','bali','tops','locket','bacha kada','bracelet','watch','bansuri']

n=StringVar()
itemchoosen=ttk.Combobox(root,width=10,textvariable=n)
itemchoosen.place(x=70,y=90)
itemchoosen.current()




def reset():
    cn.set('')
    pn.set('')
    purity.set('')
    w.set('')
    itemchoosen.set('')
    lis.clear()
    
        
#____________________________________________________________________________________________________

def vill():
    
    x=prices.gold_price()
    yhy=str(prices.silver_price())
    cname=cn.get()
    pno=pn.get()
    d1=date.today()
    cur_date=d1.strftime("%d-%m-%Y")
    
    

    boot=Tk()
    boot.geometry('800x500')
    boot.title('BILL')
    

    Label(boot,text='Sangam Jewellers',font=("Times", "24", "bold italic"),fg='teal').pack()
    Label(boot,text='chhoti line jagadhri , yamunanagar',fg='black',font=("Times", "10", "bold italic")).pack()
    
    
    
    Label(boot,text='                           |                           |                           |                           |                           |                           |                           |').place(x=10,y=70)
    Label(boot,text='---------------------------------------------------------------------------------------------------------------------').place(x=90,y=90)
    Label(boot,text='                           |                           |                           |                           |                           |                           |                           |').place(x=10,y=110)
    Label(boot,text='                           |                           |                           |                           |                           |                           |                           |').place(x=10,y=130)
    
    
    Label(boot,text='ITEM',font=("Times", "10", "bold italic")).place(x=115,y=70)
    Label(boot,text='WEIGHT',font=("Times", "10", "bold italic")).place(x=200,y=70)
    Label(boot,text='PURITY',font=("Times", "10", "bold italic")).place(x=285,y=70)
    Label(boot,text='MAKING',font=("Times", "10", "bold italic")).place(x=370,y=70)
    Label(boot,text='LABOR',font=("Times", "10", "bold italic")).place(x=455,y=70)
    Label(boot,text='GST',font=("Times", "10", "bold italic")).place(x=540,y=70)
    Label(boot,text='TOTAL',font=("Times", "10", "bold italic")).place(x=625,y=70)
    
    time_string = strftime('%H:%M:%S %p')

    
    Label(boot,text=cname.capitalize()).place(x=0,y=0)
    Label(boot,text=time_string).place(x=0,y=20)
    Label(boot,text=pno).place(x=0,y=40)
    Label(boot,text='GOLD: ',font=('Times','10','bold')).place(x=0,y=300)
    Label(boot,text='SILVER: ',font=('Times','10','bold')).place(x=0,y=330)
    Label(boot,text=int(x[3:5]+x[6:9]),fg='red',font=('Times','10','bold')).place(x=50,y=300)
    Label(boot,text=yhy[1:],fg='red',font=('Times','10','bold')).place(x=50,y=330)
    Label(boot,text='NOTE : "उधार एक जादू है, हम देंगे और आप गायब हो जाएंगे।"',fg='red',font=("Times", "15", "bold italic")).place(x=0,y=470)
    
    tot=[]
    z=120
    zz=205
    zzz=290
    m_c=375
    l_c=460
    g_c=545
    t_c=630
    y=110
    why=150
    e=100

    rate=int(x[3:5]+x[6:9])
    rat=float(yhy[1:])
    ra=int(250)
    mycursor=mydb.cursor()
    lbr=0
    
    for i in lis:
        i1=i[1]
        i2=i[2]
        
        if v.get()==1:
            r=float(i1)*int(i2)*(int(x[3:5]+x[6:9])*0.0001)
        elif v.get()==2 and (i2=='925' or i2=='T925'):
            r=float(i1)*ra
        elif v.get()==2:
            r=float(i1)*rat
        mking=r*0.1
        if i2=='T7':
            lbr=r*0.25
        
        elif i2=='916':
            lbr=r*0.1
        elif i2=='833' or i2=='750':
            lbr=r*0.02
        g=r*0.03
        
        
        f=r+mking+lbr+g
        Label(boot,text='                           |                           |                           |                           |                           |                           |                           |').place(x=10,y=why)
        Label(boot,text=i[0],fg='teal').place(x=z,y=y)
        Label(boot,text=i[1],fg='teal').place(x=zz,y=y)
        Label(boot,text=i[2],fg='teal').place(x=zzz,y=y)
        Label(boot,text=int(mking),fg='teal').place(x=m_c,y=y)
        Label(boot,text=int(lbr),fg='teal').place(x=l_c,y=y)
        Label(boot,text=int(g),fg='teal').place(x=g_c,y=y)
        Label(boot,text=int(f),fg='teal').place(x=t_c,y=y)
        
        Label(boot,text='CHARGES %',font=('Times','10','bold')).place(x=650,y=300)
        Label(boot,text='MAKING       10 %').place(x=650,y=340)
        Label(boot,text='GST                2 %').place(x=650,y=360)
        Label(boot,text='LABOR          916 - 10%').place(x=650,y=380)
        Label(boot,text='                      833 - 2%').place(x=650,y=400)
        Label(boot,text='                      750 - 2%').place(x=650,y=420)
        
        
        sql='INSERT INTO detail (Name,Phone,Item,Weight,Purity,Rate,Total,Metal,date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        if v.get()==1:
            val=(cname,pno,i[0],i[1],i[2],rate,r+mking+lbr+g,'gold',cur_date)
        elif v.get()==2:
            val=(cname,pno,i[0],i[1],i[2],rate,r+mking+lbr+g,'silver',cur_date)
        mycursor.execute(sql,val)          
        mydb.commit()

        tot.append(int(f))
        y+=20
        why+=20
        
    
    Label(boot,text=sum(tot),font=('Times','10','bold')).place(x=630,y=why-20)
    t.set((tot))
    print('items added successfully')
    
    Button(boot,text='EXIT',command=combine_funcs(root.destroy,boot.destroy)).place(x=400,y=400)
    boot.mainloop()


lis=[]


def add():
    lis.append((itemchoosen.get(),w.get(),p.get()))
Button(root,text='GET BILL',command=vill,bg='teal',fg='pink').place(x=240,y=150)
Button(root,text='ADD ITEM',command=add,bg='teal',fg='pink').place(x=150,y=150)
Button(root,text='EXIT',command=(root.destroy),bg='teal',fg='pink').place(x=250,y=280)
Button(root,text='RESET',command=reset,bg='teal',fg='pink').place(x=330,y=150)


root.mainloop()


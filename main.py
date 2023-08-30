from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib


def clear():

    bathsoapentry.delete(0,END)
    hairproductentry.delete(0,END)
    facewashentry.delete(0,END)
    facepackentry.delete(0,END)
    bodylotionentry.delete(0,END)
    sunscreenentry.delete(0,END)

    riceentry.delete(0,END)
    wheatentry.delete(0,END)
    fruitsentry.delete(0,END)
    vegetablesentry.delete(0,END)
    oilsentry.delete(0,END)
    sugarentry.delete(0,END)
    
    spriteentry.delete(0,END)
    pepsientry.delete(0,END)
    fantaentry.delete(0,END)
    dewentry.delete(0,END)
    colaentry.delete(0,END)
    bovontoentry.delete(0,END)


    bathsoapentry.insert(0,0)
    hairproductentry.insert(0,0)
    facewashentry.insert(0,0)
    facepackentry.insert(0,0)
    bodylotionentry.insert(0,0)
    sunscreenentry.insert(0,0)

    riceentry.insert(0,0)
    wheatentry.insert(0,0)
    fruitsentry.insert(0,0)
    vegetablesentry.insert(0,0)
    oilsentry.insert(0,0)
    sugarentry.insert(0,0)
    
    spriteentry.insert(0,0)
    pepsientry.insert(0,0)
    fantaentry.insert(0,0)
    dewentry.insert(0,0)
    colaentry.insert(0,0)
    bovontoentry.insert(0,0)

    cosmeticstaxentry.delete(0,END)
    groceriestaxentry.delete(0,END)
    cooldrinkstaxentry.delete(0,END)

    cosmeticspriceentry.delete(0,END)
    groceriespriceentry.delete(0,END)
    cooldrinkspriceentry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)
    

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP("smtp.gmail.com",587)
            ob.starttls()
            ob.login(senderentry.get(),passwordentry.get())
            message=email_textarea.get(1.0,END)
            recieveradress=recieverentry.get()
            ob.sendmail(senderentry.get(),recieveradress,message)
            ob.quit()
            messagebox.showinfo("Success","Bill is successfully sent",parent=newWindow)
            newWindow.destroy()
        except:
            messagebox.showerror("Error","something went wrong, please try again",parent=newWindow)
    if textarea.get(1.0,END)=="\n":
        messagebox.showerror("Error","Bill is Empty")
    else:
        newWindow=Toplevel()
        newWindow.grab_set()
        newWindow.title("Send Gmail")
        newWindow.config(bg="blanchedalmond")
        newWindow.resizable(0,0)

        senderframe=LabelFrame(newWindow,
                               text="SENDER",
                               font=("Arial",16,"bold"),
                               bd=6,
                               bg="blanchedalmond",
                               fg="gray20")
        senderframe.grid(row=0,column=0,padx=40,pady=20)


        senderlabel=Label(senderframe,
                           text="Sender Email",
                           font=("Arial",16,"bold"),
                           bg="blanchedalmond",
                           fg="gray20")
        senderlabel.grid(row=0,column=0,padx=10,pady=8)

        senderentry=Entry(senderframe,
                          font=("arial",16,"bold"),
                          bd=2,
                          width=23,
                          relief=GROOVE)
        senderentry.grid(row=0,column=1,padx=10,pady=8)

        passwordlabel=Label(senderframe,
                           text="Password",
                           font=("Arial",16,"bold"),
                           bg="blanchedalmond",
                           fg="gray20")
        passwordlabel.grid(row=1,column=0,padx=10,pady=8)

        passwordentry=Entry(senderframe,
                          font=("arial",16,"bold"),
                          bd=2,
                          width=23,
                          relief=RIDGE,
                          show="*")
        passwordentry.grid(row=1,column=1,padx=10,pady=8)

        recipientframe=LabelFrame(newWindow,
                               text="RECIPIENT",
                               font=("Arial",16,"bold"),
                               bd=6,
                               bg="blanchedalmond",
                               fg="gray20")
        recipientframe.grid(row=1,column=0,padx=40,pady=20)

        recieverlabel=Label(recipientframe,
                           text="Email Adress",
                           font=("Arial",16,"bold"),
                           bg="blanchedalmond",
                           fg="gray20")
        recieverlabel.grid(row=0,column=0,padx=10,pady=8)

        recieverentry=Entry(recipientframe,
                          font=("arial",16,"bold"),
                          bd=2,
                          width=23,
                          relief=GROOVE)
        recieverentry.grid(row=0,column=1,padx=10,pady=8)

        messagelabel=Label(recipientframe,
                           text="Message",
                           font=("Arial",16,"bold"),
                           bg="blanchedalmond",
                           fg="gray20")
        messagelabel.grid(row=1,column=0,padx=10,pady=8)

        email_textarea=Text(recipientframe,
                            font=("arial",14,"bold"),
                            bd=2,
                            relief=SUNKEN,
                            width=42,
                            height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace("=","").replace("-","").replace("\t\t","\t"))

        sendbutton=Button(newWindow,
                          text="SEND",
                          font=("arial",14,"bold"),
                          width=15,
                          command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)




        newWindow.mainloop()


def print_bill():
    if textarea.get(1.0,END)=="\n":
        messagebox.showerror("Error","Bill is Empty")
    else:
        file=tempfile.mktemp(".txt")
        open(file,"w").write(textarea.get(1.0,END))
        os.startfile(file,"print")





def search_bill():
    for i in os.listdir("bills/"):
        if i.split(".")[0]==billnumberEntry.get():
            f=open(f"bills/{i}","r")
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror("Error","Invalid bill number")




if not os.path.exists("bills"):
    os.mkdir("bills")

billnumber=random.randint(500,1000)

def save_bill():
    global billnumber
    result=messagebox.askyesno("Confirm","Do you want to Save the Bill")
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f"bills/{billnumber}.txt","w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success",f"Bill number {billnumber} is saved successfully")
        billnumber=random.randint(500,1000)



def Total():


    global soapprice
    global hairprice
    global facewashprice
    global facepackprice
    global bodylotionprice
    global sunscreenprice,totalbill

    soapprice=int(bathsoapentry.get())*20
    hairprice=int(hairproductentry.get())*150
    facewashprice=int(facewashentry.get())*100
    facepackprice=int(facepackentry.get())*80
    bodylotionprice=int(bodylotionentry.get())*120
    sunscreenprice=int(sunscreenentry.get())*95


    totalcosmeticprice=soapprice+hairprice+facewashprice+facepackprice+bodylotionprice+sunscreenprice
    cosmeticspriceentry.delete(0,END)
    cosmeticspriceentry.insert(0,str(totalcosmeticprice)+" Rs")
    
    cosmetictax=totalcosmeticprice * 0.12
    cosmeticstaxentry.delete(0,END)
    cosmeticstaxentry.insert(0,str(cosmetictax)+" Rs")

    global riceprice,wheatprice,fruitsprice,vegetablesprice,oilprice,sugarprice

    riceprice=int(riceentry.get())*600
    wheatprice=int(wheatentry.get())*250
    fruitsprice=int(fruitsentry.get())*130
    vegetablesprice=int(vegetablesentry.get())*100
    oilprice=int(oilsentry.get())*180
    sugarprice=int(sugarentry.get())*220

    totalgroceriesprice=riceprice+wheatprice+fruitsprice+vegetablesprice+oilprice+sugarprice
    groceriespriceentry.delete(0,END)
    groceriespriceentry.insert(0,str(totalgroceriesprice)+" Rs")

    groceriestax=totalgroceriesprice * 0.09
    groceriestaxentry.delete(0,END)
    groceriestaxentry.insert(0,str(groceriestax)+" Rs")

    global spriteprice,pepsiprice,fantaprice,dewprice,colaprice,bovontoprice

    spriteprice=int(spriteentry.get())*50
    pepsiprice=int(pepsientry.get())*48
    fantaprice=int(fantaentry.get())*62
    dewprice=int(dewentry.get())*80
    colaprice=int(colaentry.get())*45
    bovontoprice=int(bovontoentry.get())*40

    totalcooldrinksprice=spriteprice+pepsiprice+fantaprice+dewprice+colaprice+bovontoprice
    cooldrinkspriceentry.delete(0,END)
    cooldrinkspriceentry.insert(0,str(totalcooldrinksprice)+" Rs")

    cooldrinkstax=totalcooldrinksprice * 0.06
    cooldrinkstaxentry.delete(0,END)
    cooldrinkstaxentry.insert(0,str(cooldrinkstax)+" Rs")

    totalbill=totalcosmeticprice+totalgroceriesprice+totalcooldrinksprice+cosmetictax+groceriestax+cooldrinkstax



def bill_area():
    textarea.delete(1.0,END)
    if nameEntry.get()=="" or phoneEntry.get=="":
        messagebox.showerror("Error","Customer details are Required")
    elif cosmeticspriceentry.get()=="" or groceriespriceentry.get()=="" or cooldrinkspriceentry.get()=="":
        messagebox.showerror("Error","No Products are Selected")
    elif cosmeticspriceentry.get()=="0 Rs" and groceriespriceentry.get()=="0 Rs" and cooldrinkspriceentry.get()=="0 Rs":
        messagebox.showerror("Error","No Products are Selected")
    else:
        textarea.insert(END,"\t\t\t\t**Welcome Customers**\n")
        textarea.insert(END,f"\n\t\tBill Number : {billnumber}\n")
        textarea.insert(END,f"\n\t\tCustomer Number : {nameEntry.get()}\n")
        textarea.insert(END,f"\n\t\tCustomer Phone Number : {phoneEntry.get()}\n")
        textarea.insert(END,"\n\t\t==================================================")
        textarea.insert(END,f"\n\t\tProduct\t\tQuantity\t\tPrice")
        textarea.insert(END,"\n\t\t==================================================")
        
        if bathsoapentry.get()!="0":
            textarea.insert(END,f"\n\t\tBath Soap\t\t{bathsoapentry.get()}\t\t{soapprice} Rs")
        if hairproductentry.get()!="0":
            textarea.insert(END,f"\n\t\tHair Product\t\t{hairproductentry.get()}\t\t{hairprice} Rs")
        if facewashentry.get()!="0":
            textarea.insert(END,f"\n\t\tFace Wash\t\t{facewashentry.get()}\t\t{facewashprice} Rs")
        if facepackentry.get()!="0":
            textarea.insert(END,f"\n\t\tFace Pack\t\t{facepackentry.get()}\t\t{facepackprice} Rs")
        if bodylotionentry.get()!="0":
            textarea.insert(END,f"\n\t\tBody Lotion\t\t{bodylotionentry.get()}\t\t{bodylotionprice} Rs")
        if sunscreenentry.get()!="0":
            textarea.insert(END,f"\n\t\tSun Screen\t\t{sunscreenentry.get()}\t\t{sunscreenprice} Rs")
        
        if riceentry.get()!="0":
            textarea.insert(END,f"\n\t\tRice\t\t{riceentry.get()}\t\t{riceprice} Rs")
        if wheatentry.get()!="0":
            textarea.insert(END,f"\n\t\tWheat\t\t{wheatentry.get()}\t\t{wheatprice} Rs")
        if fruitsentry.get()!="0":
            textarea.insert(END,f"\n\t\tFruits\t\t{fruitsentry.get()}\t\t{fruitsprice} Rs")
        if vegetablesentry.get()!="0":
            textarea.insert(END,f"\n\t\tVegetables\t\t{vegetablesentry.get()}\t\t{vegetablesprice} Rs")
        if oilsentry.get()!="0":
            textarea.insert(END,f"\n\t\tOil\t\t{oilsentry.get()}\t\t{oilprice} Rs")
        if sugarentry.get()!="0":
            textarea.insert(END,f"\n\t\tSugar\t\t{sugarentry.get()}\t\t{sugarprice} Rs")

        if spriteentry.get()!="0":
            textarea.insert(END,f"\n\t\tSprite\t\t{spriteentry.get()}\t\t{spriteprice} Rs")
        if pepsientry.get()!="0":
            textarea.insert(END,f"\n\t\tPepsi\t\t{pepsientry.get()}\t\t{pepsiprice} Rs")
        if fantaentry.get()!="0":
            textarea.insert(END,f"\n\t\tFanta\t\t{fantaentry.get()}\t\t{fantaprice} Rs")
        if dewentry.get()!="0":
            textarea.insert(END,f"\n\t\tMountain Dew\t\t{dewentry.get()}\t\t{dewprice} Rs")
        if colaentry.get()!="0":
            textarea.insert(END,f"\n\t\tCoca Cola\t\t{colaentry.get()}\t\t{colaprice} Rs")
        if bovontoentry.get()!="0":
            textarea.insert(END,f"\n\t\tBovonto\t\t{bovontoentry.get()}\t\t{bovontoprice} Rs")
        textarea.insert(END,"\n\t\t==================================================")


        if cosmeticstaxentry.get()!="0.0 Rs":
            textarea.insert(END,f"\n\t\tCosmetic Tax\t\t{cosmeticstaxentry.get()}\n")

        if groceriestaxentry.get()!="0.0 Rs":
            textarea.insert(END,f"\n\t\tGrocery Tax\t\t{groceriestaxentry.get()}\n")

        if cooldrinkstaxentry.get()!="0.0 Rs":
            textarea.insert(END,f"\n\t\tCool Drink Tax\t\t{cooldrinkstaxentry.get()}\n")

        textarea.insert(END,f"\n\n\t\tTotal Bill\t\t{totalbill} Rs\n")
        textarea.insert(END,"\n\t\t==================================================")

        save_bill()
    

window=Tk()

window.title("Retail billing system")
window.geometry("1920x1080")
window.iconbitmap('icon.ico')

headinglabel=Label(window,
                   text="Retail Billing System",
                   font=("Times new roman",30,"bold"),
                   bg="blanchedalmond",
                   fg="gray20",
                   bd=12,
                   relief=GROOVE)
headinglabel.pack(fill=X,pady=10)


customerdetailsframe=LabelFrame(window,
                                text="Customer Details",
                                font=("times new roman",15,"bold"),
                                fg="gray20",
                                bd=8,
                                relief=GROOVE,
                                bg="blanchedalmond")
customerdetailsframe.pack(fill=X)

namelabel=Label(customerdetailsframe,
                text="Name",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
namelabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customerdetailsframe,
                font=("Arial",15),
                bd=7,
                width=18,)
nameEntry.grid(row=0,column=1,padx=8)

phonelabel=Label(customerdetailsframe,
                text="Phone Number",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
phonelabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customerdetailsframe,
                font=("Arial",15),
                bd=7,
                width=18,)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberlabel=Label(customerdetailsframe,
                text="Bill Number",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
billnumberlabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customerdetailsframe,
                font=("Arial",15),
                bd=7,
                width=18,)
billnumberEntry.grid(row=0,column=5,padx=8)

searchbutton=Button(customerdetailsframe,
                    text="SEARCH",
                    font=("arial",12,"bold"),
                    bd=7,
                    width=10,
                    command=search_bill)
searchbutton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(window)
productsFrame.pack(fill=X,pady=20)

cosmeticsframe=LabelFrame(productsFrame,
                          text="Cosmetics",
                          font=("times new roman",15,"bold"),
                          fg="gray20",
                          bd=8,
                          relief=GROOVE,
                          bg="blanchedalmond")
cosmeticsframe.grid(row=0,column=0)

bathsoaplabel=Label(cosmeticsframe,
                    text="Bath soap",
                    font=("times new roman",15,"bold"),
                    bg="blanchedalmond",
                    fg="gray20")
bathsoaplabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

bathsoapentry=Entry(cosmeticsframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
bathsoapentry.grid(row=0,column=1,pady=9,padx=10)
bathsoapentry.insert(0,0)

hairproductlabel=Label(cosmeticsframe,
                    text="Hair Oil",
                    font=("times new roman",15,"bold"),
                    bg="blanchedalmond",
                    fg="gray20")
hairproductlabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

hairproductentry=Entry(cosmeticsframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
hairproductentry.grid(row=1,column=1,pady=9,padx=10)
hairproductentry.insert(0,0)

facewashlabel=Label(cosmeticsframe,
                    text="Face Wash",
                    font=("times new roman",15,"bold"),
                    bg="blanchedalmond",
                    fg="gray20")
facewashlabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

facewashentry=Entry(cosmeticsframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
facewashentry.grid(row=2,column=1,pady=9,padx=10)
facewashentry.insert(0,0)

facepacklabel=Label(cosmeticsframe,
                    text="Face Pack",
                    font=("times new roman",15,"bold"),
                    bg="blanchedalmond",
                    fg="gray20")
facepacklabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

facepackentry=Entry(cosmeticsframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
facepackentry.grid(row=3,column=1,pady=9,padx=10)
facepackentry.insert(0,0)

bodylotionlabel=Label(cosmeticsframe,
                    text="Body Lotion",
                    font=("times new roman",15,"bold"),
                    bg="blanchedalmond",
                    fg="gray20")
bodylotionlabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

bodylotionentry=Entry(cosmeticsframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
bodylotionentry.grid(row=4,column=1,pady=9,padx=10)
bodylotionentry.insert(0,0)

sunscreenlabel=Label(cosmeticsframe,
                    text="Sun Screen",
                    font=("times new roman",15,"bold"),
                    bg="blanchedalmond",
                    fg="gray20")
sunscreenlabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

sunscreenentry=Entry(cosmeticsframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
sunscreenentry.grid(row=5,column=1,pady=9,padx=10)
sunscreenentry.insert(0,0)

groceryframe=LabelFrame(productsFrame,
                          text="Grocery",
                          font=("times new roman",15,"bold"),
                          fg="gray20",
                          bd=8,
                          relief=GROOVE,
                          bg="blanchedalmond")
groceryframe.grid(row=0,column=1)

ricelabel=Label(groceryframe,
                text="Rice",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
ricelabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

riceentry=Entry(groceryframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
riceentry.grid(row=0,column=1,pady=9,padx=10)
riceentry.insert(0,0)

wheatlabel=Label(groceryframe,
                text="Wheat",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
wheatlabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

wheatentry=Entry(groceryframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
wheatentry.grid(row=1,column=1,pady=9,padx=10)
wheatentry.insert(0,0)

fruitslabel=Label(groceryframe,
                text="Fruits",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
fruitslabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

fruitsentry=Entry(groceryframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
fruitsentry.grid(row=2,column=1,pady=9,padx=10)
fruitsentry.insert(0,0)

vegetableslabel=Label(groceryframe,
                text="Vegetables",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
vegetableslabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

vegetablesentry=Entry(groceryframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
vegetablesentry.grid(row=3,column=1,pady=9,padx=10)
vegetablesentry.insert(0,0)

oilslabel=Label(groceryframe,
                text="Oil",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
oilslabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

oilsentry=Entry(groceryframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
oilsentry.grid(row=4,column=1,pady=9,padx=10)
oilsentry.insert(0,0)


sugarlabel=Label(groceryframe,
                text="Sugar",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
sugarlabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

sugarentry=Entry(groceryframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
sugarentry.grid(row=5,column=1,pady=9,padx=10)
sugarentry.insert(0,0)


drinksframe=LabelFrame(productsFrame,
                          text="Cool Drinks",
                          font=("times new roman",15,"bold"),
                          fg="gray20",
                          bd=8,
                          relief=GROOVE,
                          bg="blanchedalmond")
drinksframe.grid(row=0,column=2)

spritelabel=Label(drinksframe,
                text="Sprite",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
spritelabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

spriteentry=Entry(drinksframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
spriteentry.grid(row=0,column=1,pady=9,padx=10)
spriteentry.insert(0,0)


pepsilabel=Label(drinksframe,
                text="Pepsi",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
pepsilabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

pepsientry=Entry(drinksframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
pepsientry.grid(row=1,column=1,pady=9,padx=10)
pepsientry.insert(0,0)


fantalabel=Label(drinksframe,
                text="Fanta",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
fantalabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

fantaentry=Entry(drinksframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
fantaentry.grid(row=2,column=1,pady=9,padx=10)
fantaentry.insert(0,0)

dewlabel=Label(drinksframe,
                text="Mountain Dew",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
dewlabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

dewentry=Entry(drinksframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
dewentry.grid(row=3,column=1,pady=9,padx=10)
dewentry.insert(0,0)

colalabel=Label(drinksframe,
                text="Coca Cola",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
colalabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

colaentry=Entry(drinksframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
colaentry.grid(row=4,column=1,pady=9,padx=10)
colaentry.insert(0,0)

bovontolabel=Label(drinksframe,
                text="Bovonto",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
bovontolabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

bovontoentry=Entry(drinksframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
bovontoentry.grid(row=5,column=1,pady=9,padx=10)
bovontoentry.insert(0,0)

billframe=Frame(productsFrame,
                bd=8,
                relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billarealabel=Label(billframe,
                    text="Bill Area",
                    font=("times new roman",15,"bold"),
                    bd=7,
                    relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billframe,
                    orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,
              height=18,
              width=80,
              yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuframe=LabelFrame(window,
                        text="Bill Menu",
                        font=("times new roman",15,"bold"),
                        fg="gray20",
                        bd=8,
                        relief=GROOVE,
                        bg="blanchedalmond")
billmenuframe.pack(fill=X)

cosmeticspricelabel=Label(billmenuframe,
                text="Cosmetic Price",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
cosmeticspricelabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

cosmeticspriceentry=Entry(billmenuframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
cosmeticspriceentry.grid(row=0,column=1,pady=9,padx=10)

groceriespricelabel=Label(billmenuframe,
                text="Groceries Price",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
groceriespricelabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

groceriespriceentry=Entry(billmenuframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
groceriespriceentry.grid(row=1,column=1,pady=9,padx=10)

cooldrinkspricelabel=Label(billmenuframe,
                text="Cool Drinks Price",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
cooldrinkspricelabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

cooldrinkspriceentry=Entry(billmenuframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
cooldrinkspriceentry.grid(row=2,column=1,pady=9,padx=10)

cosmeticstaxlabel=Label(billmenuframe,
                text="Cosmetics Tax",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
cosmeticstaxlabel.grid(row=0,column=2,pady=9,padx=10,sticky="w")

cosmeticstaxentry=Entry(billmenuframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
cosmeticstaxentry.grid(row=0,column=3,pady=9,padx=10)

groceriestaxlabel=Label(billmenuframe,
                text="Groceries Tax",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
groceriestaxlabel.grid(row=1,column=2,pady=9,padx=10,sticky="w")

groceriestaxentry=Entry(billmenuframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
groceriestaxentry.grid(row=1,column=3,pady=9,padx=10)

cooldrinkstaxlabel=Label(billmenuframe,
                text="Cool Drinks Tax",
                font=("times new roman",15,"bold"),
                bg="blanchedalmond",
                fg="gray20")
cooldrinkstaxlabel.grid(row=2,column=2,pady=9,padx=10,sticky="w")

cooldrinkstaxentry=Entry(billmenuframe,
                    font=("times new roman",15,"bold"),
                    width=10,
                    bd=5)
cooldrinkstaxentry.grid(row=2,column=3,pady=9,padx=10)

buttonframe=Frame(billmenuframe,
                  bd=8,
                  relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

totalbutton=Button(buttonframe,
                   text="Total",
                   font=("arial",16,"bold"),
                   bg="blanchedalmond",
                   fg="gray20",
                   bd=5,
                   width=8,
                   pady=10,
                   command=Total)
totalbutton.grid(row=0,column=0,pady=20,padx=5)

billbutton=Button(buttonframe,
                   text="Bill",
                   font=("arial",16,"bold"),
                   bg="blanchedalmond",
                   fg="gray20",
                   bd=5,
                   width=8,
                   pady=10,
                   command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonframe,
                   text="Email",
                   font=("arial",16,"bold"),
                   bg="blanchedalmond",
                   fg="gray20",
                   bd=5,
                   width=8,
                   pady=10,
                   command=send_email)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(buttonframe,
                   text="Print",
                   font=("arial",16,"bold"),
                   bg="blanchedalmond",
                   fg="gray20",
                   bd=5,
                   width=8,
                   pady=10,
                   command=print_bill)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonframe,
                   text="Clear",
                   font=("arial",16,"bold"),
                   bg="blanchedalmond",
                   fg="gray20",
                   bd=5,
                   width=8,
                   pady=10,
                   command=clear)
clearbutton.grid(row=0,column=4,pady=20,padx=5)

window.mainloop()
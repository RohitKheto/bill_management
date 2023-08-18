from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
import random
from datetime import date,datetime
import os
from tkinter import filedialog

r=""

def Search():
      billarea.delete('1.0','end')
      fullpath=""
      file=f"{customer_details_list[2].get()}.txt"
      rootdir="C:\\Users\\ROHIT KHETO"
      for relPath,dirs,files in os.walk(rootdir):
         if(file in files):
            fullpath=os.path.join(rootdir,relPath,file)

      if(fullpath==""):
         tmsg.showerror('Unknown',"This bill no. is not exist")
      else:
         with open(fullpath,"r") as f:
            t=f.read()
            billarea.insert(END,t)
         

def save():
   global r
   if(r==""):
      pass
   else:
      t=billarea.get('1.0','end')
      f= filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("Text file","*.txt"),("PDF","*.pdf"),("All files","*.*")],initialdir='C:\\Users\\ROHIT KHETO\\Downloads',initialfile=r)
      f.write(t)
      f.close()

 
def receipt():
   billarea.delete("1.0","end")
   global r
   r=random.randint(1000,9999)
   Date=date.today()
   time=datetime.now()
   time=time.strftime("%H:%M:%S")
   if (customer_details_list[0].get())=='' or (customer_details_list[1].get())=='':
      tmsg.showinfo('Incomplete',"Please enter customer details")
   else:
      t=f'''Receipt Ref.             Bill No. : {r}               {Date} 
                                                                          {time}
*****************************************************
                           FAST  FOOD  CENTER
                        Contact  No.  :  9867125621

*****************************************************
Customer Name  :  {customer_details_list[0].get()}
Contact No.  :  {customer_details_list[1].get()}

*****************************************************
Product                                   Qty                  Price
*****************************************************
'''
      billarea.insert(END,t)
      for i in range(0,6):
         if(int(chowmein_Entry[i].get())>0):
            t=f"{chowmein_label[i]}\t\t\t{chowmein_Entry[i].get()}    \tRs. {int(chowmein_price[i])*int(chowmein_Entry[i].get())}\n"
            billarea.insert(END,t)
      for i in range(0,6):
         if(int(roll_Entry[i].get())>0):
            t=f"{roll_label[i]}\t\t\t{roll_Entry[i].get()}    \tRs. {int(roll_price[i])*int(roll_Entry[i].get())}\n"
            billarea.insert(END,t)
      for i in range(0,6):
         if(int(soup_Entry[i].get())>0):
            t=f"{soup_label[i]}\t\t\t{soup_Entry[i].get()}    \tRs. {int(soup_price[i])*int(soup_Entry[i].get())}\n"
            billarea.insert(END,t)
      t="\n*****************************************************"
      billarea.insert(END,t)
      for i in range(0,5):
         t=f"{summary_label[i]}\t\t:  \t\t  {summary_entry[i].get()}\n"
         billarea.insert(END,t)
      t="\n*****************************************************"
      billarea.insert(END,t)
      t=f"{summary_label[5]}\t\t:  \t\t  {summary_entry[5].get()}\n\n*****************************************************\n\t\t    Thank You"
      billarea.insert(END,t)


def total():
   for i in range(0,6):
         summary_entry[i].delete(0,END)

   chowmein_c = 0
   for i in range(0,6):
         chowmein_c += int(chowmein_Entry[i].get())*int(chowmein_price[i])

   roll_c = 0
   for i in range(0,6):
         roll_c += int(roll_Entry[i].get())*int(roll_price[i])

   soup_c = 0
   for i in range(0,6):
         soup_c += int(soup_Entry[i].get())*int(soup_price[i])

   sub_cost = chowmein_c + roll_c + soup_c

   tax_cost = (sub_cost*9)/100

   total_cost = sub_cost + tax_cost

   summary_entry[0].insert(0,f'Rs. {chowmein_c}')
   summary_entry[1].insert(0,f'Rs. {roll_c}')
   summary_entry[2].insert(0,f'Rs. {soup_c}')
   summary_entry[3].insert(0,f'Rs. {sub_cost}')
   summary_entry[4].insert(0,f'Rs. {tax_cost}')
   summary_entry[5].insert(0,f'Rs. {total_cost}')


def clear():
   t=tmsg.askyesno("Clear","Are you sure you want to clear all data ?")
   if t:
      for i in range(0,3):
         customer_details_list[i].delete(0,END)
      for i in range(0,6):
         chowmein_Entry[i].delete(0,END)
         chowmein_Entry[i].insert(0,'0')
      for i in range(0,6):
         roll_Entry[i].delete(0,END)
         roll_Entry[i].insert(0,'0')
      for i in range(0,6):
         soup_Entry[i].delete(0,END)
         soup_Entry[i].insert(0,'0')
      for i in range(0,6):
         summary_entry[i].delete(0,END)
         summary_entry[i].insert(0,'Rs. 0')
      billarea.delete('1.0','end')


def exit_button():
   t=tmsg.askyesno("Quit","Are you sure you want to quit ?")
   if t:
      root.destroy()


# Tk window

root = Tk()

root.geometry("1400x690")
root.minsize(1400,680)
root.maxsize(1400,690)

root.title("BILL MANAGEMENT")

f=Frame(root,bg="navy",borderwidth=5,relief=SUNKEN)
f.pack(fill=X)

# resturant name

f1=Frame(f,bg="navy",borderwidth=5,relief=SUNKEN)
f1.grid(row=0,column=0)
Label(f1,text="FAST  FOOD  CENTRE",bg="navy",fg="white",font=("Book Antiqua", 30 ,"bold"),padx=340,pady=2).pack()



#customer detail

f2=Frame(f,borderwidth=5,relief=RIDGE)
f2.grid(row=1,column=0)

customer_details_frame=LabelFrame(f2,text="Customer Details",fg='red3',borderwidth=5,relief=RIDGE,font=("Book Antiqua", 14 ,"bold"),bg="sky blue")
customer_details_frame.pack(fill=X)

customer_details_text=['Name','Contact No.','Bill No.']
customer_details_list=['name','contact','bill']
i=0
for k in range(0,3):
   Label(customer_details_frame,fg="navy",text=customer_details_text[k],font=("Book Antiqua", 13 ,"bold"),bg="sky blue").grid(row=0,column=i)
   i=i+1
   customer_details_list[k]=Entry(customer_details_frame,fg="navy",font=("Book Antiqua", 13 ,"bold"),bd=3,relief=SUNKEN,justify="center")
   customer_details_list[k].grid(row=0,column=i,padx=40)
   i=i+1
search=Button(customer_details_frame,fg="red3",font=("Book Antiqua", 14 ,"bold"),text="search",borderwidth=5,relief=SUNKEN,command=Search)
search.grid(row=0,column=i)


#Image add

photo=Image.open("1.jpg")
rphoto=photo.resize((260,150))
photo=ImageTk.PhotoImage(rphoto)
Label(f,image=photo).grid(row=0,column=1,rowspan=3)



#Item frames

f3=Frame(root,borderwidth=5,relief=RIDGE)
f3.pack()
Item=['Chowmein','Roll','Soup']
for i in range(0,3):
   Item[i]=LabelFrame(f3,text=Item[i],fg='red3',borderwidth=5,relief=RIDGE,font=("Book Antiqua", 14 ,"bold"),bg="LightBlue1",highlightbackground="midnight blue",highlightthickness=3)
   Item[i].grid(row=0,column=i)
   Label(Item[i],fg="red2",text='Item',font=("Book Antiqua", 14 ,"bold",'underline'),bg="LightBlue1").grid(row=0,column=0,pady=10)
   Label(Item[i],fg="red2",text='Price',font=("Book Antiqua", 14 ,"bold",'underline'),bg="LightBlue1").grid(row=0,column=1,pady=10)
   Label(Item[i],fg="red3",text='Quantity',font=("Book Antiqua", 14 ,"bold",'underline'),bg="LightBlue1").grid(row=0,column=2,pady=10)



#chowmein

chowmein_Entry=['Veg_chowmein','Egg_chowmein','Chicken_chowmein','garlic_chowmein','paneer_chowmein','schezwan_chowmein']
chowmein_label=['Veg. Chowmein','Egg Chowmein','Chicken Chowmein','Garlic Chowmein','Paneer Chowmein','Schezwan Chowmein']
chowmein_price=['80','90','100','90','100','90']


for i in range(0,6):
   j=0
   Label(Item[0],fg="midnight blue",text=chowmein_label[i],font=("Book Antiqua", 12 ,"bold"),bg="LightBlue1").grid(row=(i+1),column=j,pady=10)
   j=j+1
   Label(Item[0],fg="midnight blue",text='Rs. '+chowmein_price[i],font=("Book Antiqua", 12 ,"bold"),bg="LightBlue1").grid(row=(i+1),column=j,padx=20,pady=10)
   j=j+1
   chowmein_Entry[i]=Entry(Item[0],fg="midnight blue",font=("Book Antiqua", 12 ,"bold"),bd=3,relief=SUNKEN,justify="center",width=7)
   chowmein_Entry[i].grid(row=(i+1),column=j,padx=5,pady=10)
   chowmein_Entry[i].insert(0,'0')



#roll

roll_Entry=['Veg_roll','Egg_roll','Chicken_roll','mix_roll','paneer_roll','spring_roll']
roll_label=['Veg. Roll','Egg Roll','Chicken Roll','Mix Roll','Paneer Roll','Spring Roll']
roll_price=['35','40','50','60','45','35']


for i in range(0,6):
   j=0
   Label(Item[1],fg="midnight blue",text=roll_label[i],font=("Book Antiqua", 12 ,"bold"),bg="LightBlue1").grid(row=(i+1),column=j,pady=10)
   j=j+1
   Label(Item[1],fg="midnight blue",text='Rs. '+roll_price[i],font=("Book Antiqua", 12 ,"bold"),bg="LightBlue1").grid(row=(i+1),column=j,padx=20,pady=10)
   j=j+1
   roll_Entry[i]=Entry(Item[1],fg="midnight blue",font=("Book Antiqua", 12 ,"bold"),bd=3,relief=SUNKEN,justify="center",width=7)
   roll_Entry[i].grid(row=(i+1),column=j,padx=5,pady=10)
   roll_Entry[i].insert(0,'0')



#soup

soup_Entry=['Veg_soup','Noodle_soup','Chicken_soup','Mushroom_soup','paneer_soup','Manchow_soup']
soup_label=['Veg. Soup','Noodle Soup','Chicken Soup','Mushroom Soup','Paneer Soup','Manchow Soup']
soup_price=['80','80','90','80','80','80']


for i in range(0,6):
   j=0
   Label(Item[2],fg="midnight blue",text=soup_label[i],font=("Book Antiqua", 12 ,"bold"),bg="LightBlue1").grid(row=(i+1),column=j,pady=10)
   j=j+1
   Label(Item[2],fg="midnight blue",text='Rs. '+soup_price[i],font=("Book Antiqua", 12 ,"bold"),bg="LightBlue1").grid(row=(i+1),column=j,padx=20,pady=10)
   j=j+1
   soup_Entry[i]=Entry(Item[2],fg="midnight blue",font=("Book Antiqua", 12 ,"bold"),bd=3,relief=SUNKEN,justify="center",width=7)
   soup_Entry[i].grid(row=(i+1),column=j,padx=5,pady=10)
   soup_Entry[i].insert(0,'0')



#bill area

bill_label=Frame(f3,borderwidth=5,relief=RIDGE)
bill_label.grid(row=0,column=3)
Label(bill_label,text="BILL  AREA",bg="navy",fg="white",font=("Book Antiqua", 20 ,"bold"),pady=5).pack(fill=X)
scrollbar=Scrollbar(bill_label,width=20)
scrollbar.pack(side=RIGHT,fill=Y)
billarea=Text(bill_label,height=17,width=47,font=("Book Antiqua",'11' ,"bold"),yscrollcommand=scrollbar.set)
billarea.pack()
scrollbar.config(command=billarea.yview)



#calculation area

f4=Frame(root,borderwidth=5,relief=RIDGE)
f4.pack(fill=X)
summary_frame=LabelFrame(f4,text="Billing Summary",fg='red3',borderwidth=5,relief=RIDGE,font=("Book Antiqua", 14 ,"bold"),bg="sky blue")
summary_frame.pack(fill=X)

summary_entry=['chowmein_cost','roll_cost','soup_cost','sub_total','tax','total_cost']
summary_label=['Chowmein Cost','Roll Cost','Soup Cost','Sub Total','GST (9%)','Total']
j=0
k=0
for i in range(0,6):
   if(i>2) and (k>5):
      j=1
      k=0
   Label(summary_frame,fg="navy",text=summary_label[i],font=("Book Antiqua", 13 ,"bold"),bg="sky blue").grid(row=j,column=k,pady=10)
   k=k+1
   summary_entry[i]=Entry(summary_frame,font=("Book Antiqua", 13 ,"bold"),width=15,bd=3,relief=SUNKEN,justify="center")
   summary_entry[i].grid(row=j,column=k,padx=20,pady=10)
   summary_entry[i].insert(0,'Rs. 0')
   k=k+1



#button area

button_area_frame=Frame(summary_frame,borderwidth=5,relief=RIDGE,pady=14,bg='navy')
button_area_frame.grid(row=0,column=6,rowspan=3)

Total=Button(button_area_frame,fg="navy",text='Total',font=("Book Antiqua", 18 ,"bold"),relief=SUNKEN,borderwidth=3,bg="firebrick1",padx=9,pady=5,command=total)
Total.pack(side=LEFT,padx=3)

Receipt=Button(button_area_frame,fg="navy",text='Receipt',font=("Book Antiqua", 18 ,"bold"),relief=SUNKEN,borderwidth=3,bg="firebrick1",padx=9,pady=5,command=receipt)
Receipt.pack(side=LEFT,padx=3)

Save=Button(button_area_frame,fg="navy",text='Save',font=("Book Antiqua", 18 ,"bold"),relief=SUNKEN,borderwidth=3,bg="firebrick1",padx=9,pady=5,command=save)
Save.pack(side=LEFT,padx=3)

Clear=Button(button_area_frame,fg="navy",text='Clear',font=("Book Antiqua", 18 ,"bold"),relief=SUNKEN,borderwidth=3,bg="firebrick1",padx=9,pady=5,command=clear)
Clear.pack(side=LEFT,padx=3)

Exit=Button(button_area_frame,fg="navy",text="Exit",font=("Book Antiqua", 18 ,"bold"),relief=SUNKEN,borderwidth=3,bg="firebrick1",padx=9,pady=5,command=exit_button)
Exit.pack(side=LEFT,padx=3)

root.mainloop()

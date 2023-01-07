#!/usr/bin/env python
# coding: utf-8

# In[1]:

#TKINTER ADALAH LIBRARY YANG DIGUNAKAN UNTUK BEMBUAT KOTAK GUI
from tkinter import *
from PIL import ImageTk, Image

#METHOD 1 PEMBUATAN KOTAK GUI
root=Tk()
#MEMBUAT KONFIGURASI DENGAN WARNA LATAR BELAKANG KOTAK GUI PUTIH
root.configure(bg="white")
#MEMBUAT BESAR UKURAN GUI DENGAN GEOMETRI UKURAN 700X500 PIXEL
root.geometry("700x650")
#MEMBUAT KOTAK GUI TIDAK BISA DI UBAH UKURANNYA SECARA MANUAL
root.resizable(False,False)
#MEMBUAT JUDUL KOTAK GUI
root.title("Prakiraan Cuaca")

#INPUTKAN TULISAN 
label1 = Label(root, text = "Analisis Data Dan Klasifikasi Prakiraan Cuaca Di Kabupaten Tegal Menggunakan Metode Support Vector Machine (SVM)")
#PANGGIL TULISAN
label1.pack()


#MENGINPUTKAN FOTO
# logo=ImageTk.PhotoImage(Image.open("LOGO_UNDIP.jpg"))
# tampil_logo=Label(image=logo)
# tampil_logo.pack()

#INPUTKAN TULISAN 
label2 = Label(root, text = "Risky Via Feriyanti")
label3 = Label(root, text = "21060120420027")
#PANGGIL TULISAN
label2.pack()
label3.pack()

#NPUT FRAME
input_frame =Frame(root)
#PENEMPATAN GRID, PACK DAN PLACE SEBAGAI PEMANGGILAN METHOD
input_frame.pack(padx=10, pady=10, fill='x', expand =True)

#KOMPONEN-KOMPONEN
#1. LABEL NAMA SUHU
nama_pengunjung=Label(input_frame, text= "Ketikkan Nama Pengunjung :")
nama_pengunjung.pack(padx=100, fill='x', expand =True)
#2. MEMASUKKAN NILAI SUHU
Nama=StringVar()
nama_depan_entry=Entry(input_frame,textvariable= Nama)
nama_depan_entry.pack(padx=100, pady=10, fill='x', expand =True)
L = Label(input_frame,padx=5, text="Tekan Klik")
L.pack()
#3. MEMBUAT TOMBOL
def hal():
    label4 = Label(input_frame,padx=5, text ="Selamat Datang !!!")
    label5 = Label(input_frame,textvariable=Nama)
    label6 = Label(input_frame, text= "Apakah ingin melihat prakiraan cuaca?")
    label4.pack()
    label5.pack()
    label6.pack()
        
tombol1 =Button(input_frame, text = "Klik",padx=150,pady=20, bg="red",fg="black", command=hal)
tombol1.pack(fill='x', expand =True)

#tombol2=Button(root, text = "Next", bg="red",fg="black")
#tombol2.pack(padx=50,fill='x', expand =True)


def open():
    global logo
    top=Toplevel()
    top.title(" Halaman kedua ")
    tampil_logo=Label(top, image=logo).pack()
    newlbl=Label(top,text=" close window", command=top.destroy).pack()


btn= Button(root, padx=50, text=" Open Second Window", command=open).pack()

mainloop()


# edited 30 nov (WINDOW 1 SAMPAI PAGAR BANYAK)

# EDITED 30 NOV (WINDOW 2 BELUM MUNCUL TKINTER SEBAB ADA ERROR, JIKA TIDAK ADA ERROR MUNCUL WINDOW)

# In[2]:


import pandas as pd
df=pd.read_excel("datadf.xlsx")
print(df)
X = df[['Tavg','RH_avg','RR','ss','ff_avg']]
y = df['target']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
print(X_train.shape)
print(X_test.shape)
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
#menggunakan SVM library untuk membuat SVM classifier
args = {"model":"svm"}
pemodelan = {"svm": SVC(kernel="rbf", gamma="auto")}
print("[INFO] using '{}' model".format(args["model"]))
model = pemodelan[args["model"]]
#memasukkan training data kedalam classifier
model.fit(X_train, y_train)
#memasukkan testing data ke variabel y_predict
y_predict = model.predict(X_test)
print(y_predict)
#menampilkan classification report
print(classification_report(y_test, y_predict))
import pickle    
New_Model = pickle.dumps(model)
import tkinter as tk
from tkinter import ttk
win=tk.Tk()
#column 1
Suhu=ttk.Label(win,text="Tavg")
Suhu.grid(row=0,column=0,sticky=tk.W)
Suhu_var=tk.StringVar()
Suhu_entrybox=ttk.Entry(win,width=16,textvariable=Suhu_var)
Suhu_entrybox.grid(row=0,column=1)
#Column 2
lembab=ttk.Label(win,text='RH_avg')
lembab.grid(row=1,column=0,sticky=tk.W)
lembab_var=tk.StringVar()
lembab_entrybox=ttk.Entry(win,width=16,textvariable=lembab_var)
lembab_entrybox.grid(row=1,column=1)
#Column 3
hujan=ttk.Label(win,text='RR')
hujan.grid(row=2,column=0,sticky=tk.W)
hujan_var=tk.StringVar()
hujan_entrybox=ttk.Entry(win,width=16,textvariable=hujan_var)
hujan_entrybox.grid(row=2,column=1)
#Column 4
sinar=ttk.Label(win,text='ss')
sinar.grid(row=3,column=0,sticky=tk.W)
sinar_var=tk.StringVar()
sinar_entrybox=ttk.Entry(win,width=16,textvariable=sinar_var)
sinar_entrybox.grid(row=3,column=1)
#Column 5
angin=ttk.Label(win,text='ff_avg')
angin.grid(row=4,column=0,sticky=tk.W)
angin_var=tk.StringVar()
angin_entrybox=ttk.Entry(win,width=16,textvariable=angin_var)
angin_entrybox.grid(row=4,column=1)

import pandas as pd
DF = pd.DataFrame(X)
def action():
    global DB
    import pandas as pd
    DF = pd.DataFrame(columns=['Tavg','RH_avg','RR','ss','ff_avg'])
    TAVG=TAVG_var.get()
    DF.loc[0,'Tavg']=TAVG
    RH=RH_var.get()
    DF.loc[1,'RH_avg']=RH
    RR=RR_var.get()
    DF.loc[0,'RR']=RR
    ss=ss_var.get()
    DF.loc[0,'ss']=ss
    ff=ff_var.get()
    DF.loc[0,'ff_avg']=ff
print('shape df :',DF.shape)
DB=DF
print (DB)
def Output():
    DB['Tavg'] = pd.to_numeric(DB['Tavg'])
    DB['RH_avg'] = pd.to_numeric(DB['RH_avg'])
    DB['RR'] = pd.to_numeric(DB['RR'])
    DB['ss'] = pd.to_numeric(DB['ss'])
    DB['ff_avg'] = pd.to_numeric(DB['ff_avg'])    
    keluaran=model.predict(DB)
    result=0
    if keluaran ==1:
    #>0 and keluaran <1:
        result='Hujan Ringan'
    elif keluaran==2:
        result='Hujan Sedang'
    elif keluaran==3:
        result='Hujan Lebat'
    else :
        result='Cerah'
Predict_entrybox=ttk.Entry(win,width=16)
Predict_entrybox.grid(row=20,column=1)
Predict_entrybox.insert(1,str(result=result + i))
Predict_button=ttk.Button(win,text="Prediksi",command=Output)
Predict_button.grid(row=20,column=0)


win.mainloop()


# In[ ]:


def forward(terus):
    global logo
    global button_next
    
    logo.grid_forget()
    logo=Label(image=logo[image_number-1])
    button_next =Button(root, text="Next", bg="red", fg="black")
    button_next.pack(fill='x', expand = False)
    if terus == 3 :
        button_next = Button(root,text="Next", state=DISABLED)
        
    button_next.grid(row=1, column=2)


# In[ ]:



from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Code Gambar")

img1=ImageTk.PhotoImage(Image.open("4.jpg"))
img2=ImageTk.PhotoImage(Image.open("14.jpg"))
img3=ImageTk.PhotoImage(Image.open("15.jpg"))
img4=ImageTk.PhotoImage(Image.open("29.jpg"))

img_list=[img1, img2, img3, img4]

my_label=Label(image=img1)
my_label.grid(row=0, column=1, columnspan=1)
my_label=Label(image=img2)
my_label.grid(row=0, column=1, columnspan=1)
my_label=Label(image=img3)
my_label.grid(row=0, column=1, columnspan=1)
my_label=Label(image=img4)
my_label.grid(row=0, column=1, columnspan=1)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=img_list[image_number-1])
    button_forward=Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back=Button(root, text="<<", command=lambda: back(image_number-1))
    
    my_label.grid(row=0, column=0, columnspan=3)

def back():
    global my_label
    global button_forward
    global button_back
    
button_back=Button(root, text=" << ", command=back)
button_exit=Button(root, text=" Exit Program", command=root.quit)
button_forward=Button(root, text=" >> ", command=lambda : forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
root.mainloop()


# In[ ]:





# In[ ]:





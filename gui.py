import pickle
from tkinter import ttk
import tkinter as tk
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from tkinter import *
import pandas as pd
from PIL import ImageTk, Image


def getSVM():
    df = pd.read_excel("datadf.xlsx")
    print(df)
    X = df[['Tavg', 'RH_avg', 'RR', 'ss', 'ff_avg']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    print(X_train.shape)
    print(X_test.shape)
    args = {"model": "svm"}
    pemodelan = {"svm": SVC(kernel="rbf", gamma="auto")}
    print("[INFO] using '{}' model".format(args["model"]))
    model = pemodelan[args["model"]]
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    print(y_predict)
    print(classification_report(y_test, y_predict))


def hal():
    label4 = Label(input_frame, padx=5, text="Selamat Datang !!!")
    label5 = Label(input_frame, textvariable=Nama)
    label6 = Label(input_frame, text="Apakah ingin melihat prakiraan cuaca?")
    label4.pack()
    label5.pack()
    label6.pack()

# Halaman Pertama


root = Tk()
root.title('Prakiraan Cuaca')
root.config(bg="#57adff")
root.resizable(False, False)

# getting screen width and height of display
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# setting tkinter root size
root.geometry("%dx%d" % (width, height))
root.state('zoomed')


# icon aplikasi
image_icon = PhotoImage(file='assets/Images/logo.png')
root.iconphoto(False, image_icon)

# add judul
label1 = Label(
    root, text="Analisis Data Dan Klasifikasi Prakiraan Cuaca Di Kabupaten Tegal \n Menggunakan Metode Support Vector Machine (SVM)")
label1.config(bg="#57adff", font=("Poppins", 18))
label1.pack(fill=X, pady=15)

# add logo undip
logo = ImageTk.PhotoImage(Image.open("undip.png"))
tampil_logo = Label(image=logo, bg="#57adff")
tampil_logo.pack(fill=X, pady=5)


# add Identitas Mahasiswa
label2 = Label(
    root, text="Risky Via Feriyanti \n 21060120420027")
label2.config(bg="#57adff", font=("Poppins", 18))
label2.pack()

# Form Input
form_input = Frame(root)
form_input.config(bg="white")
form_input.pack(padx=10, pady=10, fill='x', expand=True)
nama_pengunjung = Label(form_input, text="Ketikkan Nama Pengunjung :")
nama_pengunjung.pack(padx=100, fill='x', expand=True)
Nama = StringVar()
nama_depan_entry = Entry(form_input, textvariable=Nama)
nama_depan_entry.pack(padx=100, pady=10, fill='x', expand=True)
L = Label(form_input, padx=5, text="Tekan Klik")
L.pack()


tombol1 = Button(root, text="Klik", padx=150,
                 pady=20, bg="red", fg="black", command=getSVM)

tombol1.pack(fill='x', expand=True)


# End Halaman Pertama

mainloop()

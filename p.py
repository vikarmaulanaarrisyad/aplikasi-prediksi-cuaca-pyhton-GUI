import pickle
from tkinter import ttk
import tkinter as tk
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from tkinter import *
import pandas as pd
from PIL import ImageTk, Image


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
tampil_logo.pack(fill=X, pady=2)


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


def hal():
    label4 = Label(form_input, padx=5, text="Selamat Datang !!!")
    label5 = Label(form_input, textvariable=Nama)
    label6 = Label(form_input, text="Apakah ingin melihat prakiraan cuaca?")
    label4.pack()
    label5.pack()
    label6.pack()


tombol1 = Button(root, text="Klik", padx=150,
                 pady=20, bg="red", fg="black", command=hal)

tombol1.pack(fill='x', expand=True)

# End Halaman Pertama


# Halaman Dua
# Load the weather data
df = pd.read_excel("datadf.xlsx")

# Select the features and target variable
X = df[['Tavg', 'RH_avg', 'RR', 'ss', 'ff_avg']]
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create the SVM classifier
classifier = SVC(kernel='rbf', gamma='auto')

# Train the classifier
classifier.fit(X_train, y_train)


def open():
    global logo
    top = Toplevel()
    top.title(" Perkiraaan cuaca ")
    top.resizable(False, False)
    top.config(bg="#57adff")

    # icon aplikasi
    image_icon = PhotoImage(file='assets/Images/logo.png')
    top.iconphoto(False, image_icon)

    # getting screen width and height of display
    width = top.winfo_screenwidth()
    height = top.winfo_screenheight()
    # setting tkinter root size
    top.geometry("%dx%d" % (width, height))
    top.state('zoomed')

    Round_box = PhotoImage(file='assets/Images/Rounded Rectangle 1.png')
    Label(top, image=Round_box, bg="#57adff").place(x=30, y=110)

    # label
    label1 = Label(top, text="Suhu", font=(
        "Helvetica", 25), fg="white", bg="#203243",)
    label1.place(x=50, y=122)
    
    label2 = Label(top, text="Kelembapan", font=(
        "Helvetica", 18), fg="white", bg="#203243")
    label2.place(x=50, y=180)
    
    # label3 = Label(top, text="Pressure", font=(
    #     "Helvetica", 18), fg="white", bg="#203243")
    # label3.place(x=50, y=180)
    # label4 = Label(top, text="Wind Speed", font=(
    #     "Helvetica", 18), fg="white", bg="#203243")
    # label4.place(x=50, y=200)
    # label5 = Label(top, text="Description", font=(
    #     "Helvetica", 18), fg="white", bg="#203243")
    # label5.place(x=50, y=220)

    def predict():
        # Get the user input
        Tavg = float(Tavg_var.get())
        RH_avg = float(RH_avg_var.get())
        RR = float(RR_var.get())
        ss = float(ss_var.get())
        ff_avg = float(ff_avg_var.get())

        # Use the model to make a prediction
        prediction = classifier.predict([[Tavg, RH_avg, RR, ss, ff_avg]])
        label_var.set(f"Prediction: {prediction[0]}")

    button = tk.Button(top, text="Predict", command=predict)
    button.pack()

    # Add input fields for the features
    # Tavg_var = tk.StringVar()
    # Tavg_entry = tk.Entry(top, textvariable=Tavg_var)
    # Tavg_entry.pack()
    
    Tavg_var = tk.StringVar()
    Tavg_entry = tk.Entry(top, width=10, font=(
        'poppins', 25), bg="#203243", border=0, fg="white", textvariable=Tavg_var)
    Tavg_entry.place(x=280, y=120)

    RH_avg_var = tk.StringVar()
    RH_avg_entry = tk.Entry(top, width=10, font=(
        'poppins', 25), bg="#203243", border=0, fg="white",  textvariable=RH_avg_var)
    RH_avg_entry.place(x=280, y=180)

    RR_var = tk.StringVar()
    RR_entry = tk.Entry(top, textvariable=RR_var)
    RR_entry.pack()

    ss_var = tk.StringVar()
    ss_entry = tk.Entry(top, textvariable=ss_var)
    ss_entry.pack()

    ff_avg_var = tk.StringVar()
    ff_avg_entry = tk.Entry(top, textvariable=ff_avg_var)
    ff_avg_entry.pack()

    # Add a label to display the prediction
    label_var = tk.StringVar()
    label = tk.Label(top, textvariable=label_var)
    label.pack()


btn = Button(root, padx=50, text=" Open Second Window", command=open).pack()


mainloop()

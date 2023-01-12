import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
import pandas as pd
from sklearn import svm
from sklearn.preprocessing import StandardScaler


class StudentProfile(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nama_judul = tk.Label(self)
        self.nama_judul.config(
            text="Analisis Data Dan Klasifikasi Prakiraan Cuaca Di Kabupaten Tegal \n Menggunakan Metode Support Vector Machine (SVM)")
        self.nama_judul.config(font=("Poppins", 17))
        self.nama_judul.grid(row=0, padx=10, pady=5)

        self.image_logo = Image.open("undip.png")
        self.image_logo = self.image_logo.resize(
            (200, 200), resample=Image.Resampling.LANCZOS)
        self.logo_undip = ImageTk.PhotoImage(self.image_logo)
        self.logo_undip_label = tk.Label(self, image=self.logo_undip)
        self.logo_undip_label.grid(row=1)

        self.nama_mhs = tk.Label(self)
        self.nama_mhs.config(text="Risky Via Feriyanti \n 21060120420027")
        self.nama_mhs.config(font=("Poppins", 17))
        self.nama_mhs.grid(row=2)

        self.nama_pengunjung = tk.Label(self)
        self.nama_pengunjung.config(font=(
            "Poppins", 17))
        self.nama_pengunjung.config(text="Ketikan Nama Anda : ")
        self.nama_pengunjung.grid(row=3)

        self.input_nama_pengunjung = tk.Entry(self)
        self.input_nama_pengunjung.config(font=("Poppins", 15))
        self.input_nama_pengunjung.config(width=30)
        self.input_nama_pengunjung.grid(row=4, pady=10)

        self.btn_submit_form = tk.Button(
            self, text="Submit", command=self.submit_form)
        self.btn_submit_form.config(font=('Poppins', 13, 'bold'))
        self.btn_submit_form.config(justify="center")
        self.btn_submit_form.grid(row=5, pady=5)

    def submit_form(self):
        nama_pengunjung = self.input_nama_pengunjung.get()

        if nama_pengunjung != "":
            self.hasil_input_nama = tk.Label(
                self, text='Selamat Datang ' + nama_pengunjung + ' Klik Selanjutnya, Untuk dapat membuka aplikasi ini',)
            self.hasil_input_nama.config(font=("Poppins", 17))
            self.hasil_input_nama.grid(row=6, padx=10, pady=10)

            self.next_button = tk.Button(
                self, text="Selanjutnya", command=self.show_weather_page)
            self.next_button.config(font=('Poppins', 13, 'bold'))
            self.next_button.grid(row=7)
        if nama_pengunjung == "":
            messagebox.showwarning("Weather Prediction",
                                   "Nama tidak boleh kosong")

    def show_weather_page(self):
        if messagebox.askyesno("Weather Prediction", "Apakah Anda ingin melihat halaman prediksi cuaca?"):
            self.master.switch_frame(WeatherPrediction)


class WeatherPrediction(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nama_judul = tk.Label(self)
        self.nama_judul.config(
            text="Analisis Data Dan Klasifikasi Prakiraan Cuaca Di Kabupaten Tegal \n Menggunakan Metode Support Vector Machine (SVM)")
        self.nama_judul.config(font=("Poppins", 17))
        self.nama_judul.grid(row=0, padx=10, pady=5, sticky="")

        self.left_frame = tk.Frame(self)
        self.left_frame.grid(row=1, column=0, padx=5, pady=10, sticky="w")
        self.right_frame = tk.Frame(self)
        self.right_frame.grid(row=1, column=1, padx=200, pady=10, sticky="w")

        # FORM DAN LABEL SUHU
        self.suhu_label = tk.Label(
            self.left_frame, text="Suhu : ")
        self.suhu_label.config(font=('Poppins', 17))
        self.suhu_label.grid(row=0, column=0, pady=10, sticky="w")

        suhu_var = tk.StringVar()
        self.suhu_entry = tk.Entry(self.left_frame, textvariable=suhu_var)
        self.suhu_entry.config(font=('Poppins', 17))
        self.suhu_entry.config(width=5)
        self.suhu_entry.grid(row=0, column=0, padx=270, pady=10, sticky="w")

        # END FORM DAN LABEL SUHU

        # FORM DAN LABEL KELEMBABAN
        self.kelembaban_label = tk.Label(
            self.left_frame, text="Kelembaban : ")
        self.kelembaban_label.config(font=('Poppins', 17))
        self.kelembaban_label.grid(
            row=1, column=0, pady=10, sticky="w")

        self.kelembaban_entry = tk.Entry(self.left_frame)
        self.kelembaban_entry.config(font=('Poppins', 17))
        self.kelembaban_entry.config(width=5)
        self.kelembaban_entry.grid(
            row=1, column=0, padx=270, pady=10, sticky="w")

        # END FORM DAN LABEL KELEMBABAN

        self.curah_hujan_label = tk.Label(
            self.left_frame, text="Curah hujan : ")
        self.curah_hujan_label.config(font=('Poppins', 17))
        self.curah_hujan_label.grid(row=2, column=0, pady=10, sticky="w")

        self.curah_hujan_entry = tk.Entry(self.left_frame)
        self.curah_hujan_entry.config(font=('Poppins', 17))
        self.curah_hujan_entry.config(width=5)
        self.curah_hujan_entry.grid(
            row=2, column=0, padx=270, pady=10, sticky="w")

        self.kecepatan_angin_label = tk.Label(
            self.left_frame, text="Kecepatan Angin : ")
        self.kecepatan_angin_label.config(font=('Poppins', 17))
        self.kecepatan_angin_label.grid(
            row=3, column=0, pady=10, sticky="w")

        self.kecepatan_angin_entry = tk.Entry(self.left_frame)
        self.kecepatan_angin_entry.config(font=('Poppins', 17))
        self.kecepatan_angin_entry.config(width=5)
        self.kecepatan_angin_entry.grid(
            row=3, column=0, padx=270, pady=10, sticky="w")

        self.penyinaran_matahari_label = tk.Label(
            self.left_frame, text="Penyinaran Matahari : ")
        self.penyinaran_matahari_label.config(font=('Poppins', 17))
        self.penyinaran_matahari_label.grid(
            row=4, column=0, pady=10, sticky="w")

        self.penyinaran_matahari_entry = tk.Entry(self.left_frame)
        self.penyinaran_matahari_entry.config(font=('Poppins', 17))
        self.penyinaran_matahari_entry.config(width=5)
        self.penyinaran_matahari_entry.grid(
            row=4, column=0, padx=270, pady=10, sticky="w")

        self.hasil_prediksi_label = tk.Label(
            self.left_frame, text="Hasil Prediksi")
        self.hasil_prediksi_label.config(font=('Poppins', 17))
        self.hasil_prediksi_label.grid(
            row=6, column=0, pady=10, sticky="w")   

        self.icon_hasil_prediksi = tk.Label(self.left_frame)
        self.icon_hasil_prediksi.config(font=('Poppins', 17))
        self.icon_hasil_prediksi.grid(
            row=6, column=0, padx=170, pady=10, sticky="w")

        self.hasil_prediksi = tk.Label(self.left_frame)
        self.hasil_prediksi.config(font=('Poppins', 17))
        self.hasil_prediksi.grid(
            row=6, column=0, padx=290, pady=10, sticky="w")

        self.predict_button = tk.Button(
            self.left_frame, text="Prediksi", command=self.predict_weather)
        self.predict_button.config(font=('Poppins', 15))
        self.predict_button.grid(row=5, column=0, pady=10, sticky="w")

        self.prev_button = tk.Button(
            self.left_frame, text="Sebelumnya", command=self.show_prev_page)
        self.prev_button.config(font=('Poppins', 15))
        self.prev_button.grid(row=5, column=0, padx=100, pady=10, sticky="w")

        # self.city_label = tk.Label(self.right_frame, text="Kota:")
        # self.city_label.grid(row=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def predict_weather(self):
        # logika untuk memprediksi cuaca

        # 1 : Memuat dataset cuaca
        weather_data = pd.read_excel('datadf.xlsx')

        # 2 : Memisahkan fitur dan label
        X = weather_data[['Tavg', 'RH_avg', 'RR', 'ss', 'ff_avg']]
        y = weather_data['target']

        # 3 : melakukan preprocesing data
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # 4 : Membuat objek SVM dan melatih model dengan dataMembuat objek SVM dan melatih model dengan data
        clf = svm.SVC()
        clf.fit(X, y)

        # 5 : Menangkap inputan user
        suhu = float(self.suhu_entry.get())
        kelembaban = float(self.kelembaban_entry.get())
        curah_hujan = float(self.curah_hujan_entry.get())
        kecepatan_angin = float(self.kecepatan_angin_entry.get())
        penyinaran_matahari = float(self.penyinaran_matahari_entry.get())

        # 6 : Menampung data dari user dan menyimpan ke var input data dengan array
        input_data = [[suhu, kelembaban, curah_hujan,
                       kecepatan_angin, penyinaran_matahari]]

        # 7 : Proses clasifikasi model
        input_data = scaler.transform(input_data)
        predicted_label = clf.predict(input_data)

        # 8 : Hasil prediksi

        print("Prediksi cuaca:", predicted_label[0])

        cek_prediksi = predicted_label[0]

        if cek_prediksi == 1:
            self.image_icon = ImageTk.PhotoImage(Image.open("hujan_ringan.png"))
            self.icon_hasil_prediksi.config(image=self.image_icon)
            self.hasil_prediksi.config(text="Hujan Ringan")
        elif cek_prediksi == 2:
            self.image_icon = ImageTk.PhotoImage(Image.open("hujan_ringan.png"))
            self.icon_hasil_prediksi.config(image=self.image_icon)
            self.hasil_prediksi.config(text="Hujan Sedang")
        elif cek_prediksi == 3:
            self.image_icon = ImageTk.PhotoImage(Image.open("hujan_lebat.png"))
            self.icon_hasil_prediksi.config(image=self.image_icon)
            self.hasil_prediksi.config(text="Hujan Lebat")
        elif cek_prediksi == 4:
            self.image_icon = ImageTk.PhotoImage(Image.open("cerah.png"))
            self.icon_hasil_prediksi.config(image=self.image_icon)
            self.hasil_prediksi.config(text="Cerah")
            
        # pass

    def show_prev_page(self):
        self.master.switch_frame(StudentProfile)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.switch_frame(StudentProfile)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()


if __name__ == '__main__':
    app = App()
    app.title('Analisis Data Dan Klasifikasi Prakiraan Cuaca Di Kabupaten Tegal')
    # getting screen width and height of display
    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()

    # setting tkinter app size
    app.geometry("%dx%d" % (width, height))
    app.state('zoomed')
    app.resizable(False, False)

    # icon aplikasi
    image_icon = tk.PhotoImage(file='assets/Images/logo.png')
    app.iconphoto(False, image_icon)

    app.mainloop()

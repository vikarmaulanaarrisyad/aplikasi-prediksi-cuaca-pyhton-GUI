import tkinter as tk
from PIL import ImageTk, Image


class StudentProfile(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nama_judul = tk.Label(self, font=(
            "Poppins", 18), text="Analisis Data Dan Klasifikasi Prakiraan Cuaca Di Kabupaten Tegal \n Menggunakan Metode Support Vector Machine (SVM)")
        self.nama_judul.grid(row=0, padx=10, pady=5)

        self.image_logo = Image.open("undip.png")
        self.image_logo = self.image_logo.resize((200, 200), Image.ANTIALIAS)
        self.logo_undip = ImageTk.PhotoImage(self.image_logo)
        self.logo_undip_label = tk.Label(self, image=self.logo_undip)
        self.logo_undip_label.grid(row=1)

        self.nama_mhs = tk.Label(self, font=(
            "Poppins", 18), text="Risky Via Feriyanti \n 21060120420027")
        self.nama_mhs.grid(row=2)

        self.nama_pengunjung = tk.Label(self, font=(
            "Poppins", 18), text="Ketikan Nama Anda : ")
        self.nama_pengunjung.grid(row=3)
        self.input_nama_pengunjung = tk.Entry(self, font=("Poppins", 18))
        self.input_nama_pengunjung.grid(row=4)

        self.btn_submit_form = tk.Button(
            self, text="Submit", command=self.submit_form)
        self.btn_submit_form.config(font=('Poppins', 13, 'bold'))
        self.btn_submit_form.grid(row=5, pady=5)

    def submit_form(self):
        nama_pengunjung = self.input_nama_pengunjung.get()

        self.hasil_input_nama = tk.Label(
            self, text='Selamat Datang '+nama_pengunjung + ' Klik Selanjutnya, Untuk dapat membuka aplikasi ini',)
        self.hasil_input_nama.config(font=("Poppins", 18))
        self.hasil_input_nama.grid(row=6)

        self.next_button = tk.Button(
            self, text="Selanjutnya", command=self.show_weather_page)
        self.next_button.config(font=('Poppins', 13, 'bold'))
        self.next_button.grid(row=7)


    def show_weather_page(self):
        self.master.switch_frame(WeatherPrediction)


class WeatherPrediction(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.city_label = tk.Label(self, text="Kota:")
        self.city_label.pack()

        self.city_entry = tk.Entry(self)
        self.city_entry.pack()

        self.predict_button = tk.Button(
            self, text="Prediksi", command=self.predict_weather)
        self.predict_button.pack()

        self.prev_button = tk.Button(
            self, text="Sebelumnya", command=self.show_prev_page)
        self.prev_button.pack()

    def predict_weather(self):
        # logika untuk memprediksi cuaca
        pass

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

import tkinter as tk
from tkinter import PhotoImage, ttk
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class WeatherApp:

    def __init__(self, master):
        self.master = master
        master.title("Perkiraan Cuaca")
        master.title('Prakiraan Cuaca')
        master.resizable(False, False)

        # getting screen width and height of display
        width = master.winfo_screenwidth()
        height = master.winfo_screenheight()
        # setting tkinter root size
        master.geometry("%dx%d" % (width, height))
        master.state('zoomed')

        # icon aplikasi
        image_icon = PhotoImage(file='assets/Images/logo.png')
        master.iconphoto(False, image_icon)

        # Load the weather data
        df = pd.read_excel("datadf.xlsx")

        # Select the features and target variable
        self.X = df[['Tavg', 'RH_avg', 'RR', 'ss', 'ff_avg']]
        self.y = df['target']

        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.3)

        # Create the SVM classifier
        self.classifier = SVC(kernel='rbf', gamma='auto')

        # Train the classifier
        self.classifier.fit(self.X_train, self.y_train)

        # Create the form inputs
        self.create_form_inputs()

        # Create the predict button
        self.create_predict_button()

        # Create the predict button
        self.create_confusion_matrix_button()
        
        self.label_var = tk.StringVar()
        self.label = tk.Label(master, textvariable=self.label_var)
        self.label.grid(column=0, row=8, padx=10, pady=10)
        self.label_var.set("Hasil")

    def create_form_inputs(self):
        self.Tavg_var = tk.StringVar()
        Tavg_label = ttk.Label(self.master, text="Suhu:")
        Tavg_label.grid(column=0, row=0, padx=10, pady=10)
        Tavg_entry = ttk.Entry(self.master, textvariable=self.Tavg_var)
        Tavg_entry.grid(column=1, row=0, padx=10, pady=10)

        self.RH_avg_var = tk.StringVar()
        RH_avg_label = ttk.Label(self.master, text="Kelembapan:")
        RH_avg_label.grid(column=0, row=1, padx=10, pady=10)
        RH_avg_entry = ttk.Entry(self.master, textvariable=self.RH_avg_var)
        RH_avg_entry.grid(column=1, row=1, padx=10, pady=10)

        self.RR_var = tk.StringVar()
        RR_var_label = ttk.Label(self.master, text="Curah Hujan:")
        RR_var_label.grid(column=0, row=2, padx=10, pady=10)
        RR_var_entry = ttk.Entry(self.master, textvariable=self.RR_var)
        RR_var_entry.grid(column=1, row=2, padx=10, pady=10)

        self.SS_var = tk.StringVar()
        ss_var_label = ttk.Label(self.master, text="Kecepatan Angin:")
        ss_var_label.grid(column=0, row=3, padx=10, pady=10)
        ss_var_entry = ttk.Entry(self.master, textvariable=self.SS_var)
        ss_var_entry.grid(column=1, row=3, padx=10, pady=10)

        self.FF_var = tk.StringVar()
        FF_var_label = ttk.Label(self.master, text="Penyinaran Matahari:")
        FF_var_label.grid(column=0, row=4, padx=10, pady=10)
        FF_var_entry = ttk.Entry(self.master, textvariable=self.FF_var)
        FF_var_entry.grid(column=1, row=4, padx=10, pady=10)

        self.label_var = tk.StringVar()
        label_var = ttk.Label(self.master, textvariable=self.label_var)
        label_var.grid(column=0, row=6, padx=10, pady=10)

    def create_predict_button(self):
        predict_button = ttk.Button(
            self.master, text="Prediksi", command=self.predict)
        predict_button.grid(column=1, row=5, padx=10, pady=10)

    def create_confusion_matrix_button(self):
        predict_button = ttk.Button(
            self.master, text="Confusion Matrix", command=self.create_confusion_matrix)
        predict_button.grid(column=2, row=5, padx=10, pady=10)
        
    def create_confusion_matrix(self, prediction):
            # Create the confusion matrix
        cm = confusion_matrix(self.y_test, prediction)

        # Create a figure for the confusion matrix plot
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subsubplot(111)
        ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        ax.set_title("Confusion Matrix")
        if cekTarget == 1:
            label_var.set("Hujan Ringan")
        elif cekTarget == 2:
            label_var.set("Hujan Sedang")
        elif cekTarget == 3:
            label_var.set("Hujan Lebat")
        else:
            label_var.set("Cerah")

    # def consufion_matrix(self,):
    #     # Use the model to make a prediction
    #     prediction = self.classifier.predict(self.X_test)

    #     # Create a figure for the confusion matrix plot
    #     fig = Figure(figsize=(6, 4), dpi=100)
    #     fig.clf()
    #     ax = fig.add_subplot(111)
    #     sns.heatmap(confusion_matrix(self.y_test, prediction),
    #                 annot=True, fmt=".0f", ax=ax)
    #     ax.set_title("Confusion Matrix")
    #     ax.set_xlabel('Target')
    #     ax.set_ylabel('Output')

    #     # Add the confusion matrix plot to the GUI
    #     canvas = FigureCanvasTkAgg(fig, master=self.master)
    #     canvas.draw()
    #     canvas.get_tk_widget().grid(column=5, row=0, columnspan=5,
    #                                 rowspan=12, padx=10, pady=10)

    #     # Add a navigation toolbar to the GUI
    #     toolbar = NavigationToolbar2Tk(canvas, self.master)
    #     toolbar.update()
    #     canvas.get_tk_widget().grid(row=7, column=2, )

    def predict(self):
        # Get the user input
        Tavg = float(self.Tavg_var.get())
        RH_avg = float(self.RH_avg_var.get())
        RR = float(self.RR_var.get())
        ss = float(self.SS_var.get())
        ff_avg = float(self.FF_var.get())

        # Use the model to make a prediction
        # prediction = self.classifier.predict([[Tavg, RH_avg, RR, ss, ff_avg]])
        prediction = self.classifier.predict(self.X_test)
        # cekTarget = prediction[0]

        # if prediction == 1:
        #     self.label_var.set("Hujan Ringan")
        # elif prediction == 2:
        #     self.label_var.set("Hujan Sedang")
        # elif prediction == 3:
        #     self.label_var.set("Hujan Lebat")
        # else:
        #     self.label_var.set("Cerah")


        self.create_confusion_matrix(prediction)


root = tk.Tk()
app = WeatherApp(root)
root.mainloop()

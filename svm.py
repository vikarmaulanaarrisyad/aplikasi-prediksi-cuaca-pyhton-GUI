import tkinter as tk
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

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

# Create the GUI
win = tk.Tk()
win.title("Weather Prediction")
win.geometry("300x200")

# Add a button to trigger the prediction


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


button = tk.Button(win, text="Predict", command=predict)
button.pack()

# Add input fields for the features
Tavg_var = tk.StringVar()
Tavg_entry = tk.Entry(win, textvariable=Tavg_var)
Tavg_entry.pack()

RH_avg_var = tk.StringVar()
RH_avg_entry = tk.Entry(win, textvariable=RH_avg_var)
RH_avg_entry.pack()

RR_var = tk.StringVar()
RR_entry = tk.Entry(win, textvariable=RR_var)
RR_entry.pack()

ss_var = tk.StringVar()
ss_entry = tk.Entry(win, textvariable=ss_var)
ss_entry.pack()

ff_avg_var = tk.StringVar()
ff_avg_entry = tk.Entry(win, textvariable=ff_avg_var)
ff_avg_entry.pack()

# Add a label to display the prediction
label_var = tk.StringVar()
label = tk.Label(win, textvariable=label_var)
label.pack()

# Run the GUI
win.mainloop()

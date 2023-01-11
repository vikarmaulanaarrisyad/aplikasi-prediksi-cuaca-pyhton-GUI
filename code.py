        # Create the confusion matrix
        cm = confusion_matrix(self.y_test, prediction)
        # Create a figure for the confusion matrix plot
        fig = Figure(figsize=(3, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        ax.set_title("Confusion Matrix")

        # Add the confusion matrix plot to the GUI
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().grid(column=3, row=0, rowspan=5, padx=10, pady=10)

        # Add a navigation toolbar to the GUI
        toolbar = NavigationToolbar2Tk(canvas, self.master)
        toolbar.update()
        canvas.get_tk_widget().grid(row=7, column=2, )
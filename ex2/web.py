import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Frame, Canvas, PhotoImage, Button
from PIL import Image, ImageTk

class VisualizationApp:
    def __init__(self, master, data):
        self.master = master
        self.master.title("Vizualizare Date")
        self.data = data

        self.frame = Frame(self.master)
        self.frame.pack()

        self.canvas = Canvas(self.frame,width=800,height=600)
        self.canvas.pack()

        self.plot_all_button = Button(self.master,text="Toate Valorile",command=self.plot_all)
        self.plot_all_button.pack()

        self.plot_first_5_button = Button(self.master,text="Primele 5 Valori",command=self.plot_first_10)
        self.plot_first_5_button.pack()

        self.plot_last_5_button = Button(self.master, text="Ultimele 5 Valori",command=self.plot_last_15)
        self.plot_last_5_button.pack()

    def plot_all(self):
        plt.figure(figsize=(8,6))
        plt.plot(self.data.index,self.data['Durata'],label='Durata',marker='x')
        plt.plot(self.data.index,self.data['Puls'],label='Puls',marker='x')
        plt.plot(self.data.index,self.data['MaxPuls'],label='MaxPuls', marker='x')
        plt.plot(self.data.index,self.data['Calorii'],label='Calorii', marker='x')
        plt.title('Toate valorile')
        plt.legend()

        self.display_plot()

    def plot_first_10(self):
        plt.figure(figsize=(8,6))
        plt.plot(self.data['Durata'][:5],marker='x',label='Durata')
        plt.plot(self.data['Puls'][:5],marker='x',label='Puls')
        plt.title('Primele 5 Valori')
        plt.legend()

        self.display_plot()

    def plot_last_15(self):
        ult = self.data[['Durata','Puls']].tail(5)
        plt.figure(figsize=(8,6))
        plt.plot(ult['Durata'],marker='x',label='Durata')
        plt.plot(ult['Puls'],marker='x',label='Puls')
        plt.title('Ultimele 5 Valori')
        plt.legend()

        self.display_plot()

    def display_plot(self):
        plt.tight_layout()
        plt.savefig("plot.png")
        image = Image.open("plot.png")
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0,0,anchor='nw',image=photo)
        self.canvas.image = photo

if __name__ == "__main__":
    df = pd.read_csv('data.csv')

    root = Tk()
    app = VisualizationApp(root, df)
    root.mainloop()

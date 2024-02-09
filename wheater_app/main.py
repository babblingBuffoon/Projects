from tkinter import *
from tkinter import ttk
import datetime as dt
import api
import requests



def draw_label():
    for i in range(1,5):
        search_label = Label(mainframe , text=f'label {i}')
        search_label.grid(column=i , row=2 , padx=5, pady=5, sticky='nwes')

def weather_data_label():
    for i in range(1,5):
        search_label = Label(mainframe , text=f'data {i}')
        search_label.grid(column=i , row=3 , padx=5, pady=5, sticky='nwes')




############# start of main window


root = Tk()
root.title("Weather App")
root.geometry('600x100')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0 ,  weight=0)
mainframe.columnconfigure(1 ,  weight=2)
mainframe.columnconfigure(2 ,  weight=2)
mainframe.columnconfigure(3 ,  weight=2)
mainframe.columnconfigure(4 ,  weight=2)
mainframe.rowconfigure(1, weight=1)


search_label = Label(mainframe , text='Input city name')
search_label.grid(column=1 , row=1 , padx=5, pady=5 , sticky='nwes')



city_input = StringVar()
s = ttk.Entry(mainframe  , textvariable=city_input , width=30)
s.grid(column = 2 , row = 1, columnspan=2, padx=5 , pady=5, sticky='nwes' )


search_button = StringVar()
btn_img = PhotoImage(file='E:\Projects\wheater_app\ico\search.png').subsample(20, 20)
button = Button(mainframe, text='Search' , image=btn_img , compound='left' , command='', width=20, borderwidth=1)
button.grid(column= 4 , row= 1 , padx=5 , pady=5, sticky='nwes')


draw_label()
weather_data_label()

root.mainloop()
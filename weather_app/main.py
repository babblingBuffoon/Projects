from tkinter import *
import datetime as dt
import api
import requests
import urllib.request
import base64
import json


api_key = '74bd71a9fadb0b618021cfdcd69f68f7'


default_location = 'Widnes'
f = ('Helvetica', 14)

def url():
    try:
        city = city_input.get()
        units = 'metric'
        url = 'https://api.openweathermap.org/data/2.5/weather?appid=' + api.api_key + '&q=' + city + "&units=" + units
        response = requests.get(url).json()
        return response
    except ValueError:
        pass


def input_description():
    t = ' Input city name'
    search_label = Label(mainframe , text= t ,  font=f)
    search_label.grid(column=1 , row=1 , padx=5, pady=5 , sticky='nwes')
    

def time_display():
    time = dt.datetime.now().strftime("%H:%M:%S")
    date_now = dt.datetime.now().strftime("%d-%m-%Y")
    time = Label(mainframe , text= f'{time}\n{date_now}' ,  font=f)
    time.grid(column=1 , row=4 , columnspan=2 , padx=5, pady=5 , sticky='nwes')


def city_input():
    global city_input
    city_input = StringVar()
    s = Entry(mainframe  , textvariable=city_input , borderwidth=3 ,width=20 , font=f)
    s.insert(0 , default_location)
    s.grid(column = 2 , row = 1, columnspan=2, padx=5 , pady=0, sticky='nwes' )


def search_button():
    global search_button
    global btn_img
    global button
    search_button = StringVar()
    #btn_img = PhotoImage(file='search.png').subsample(20, 20)
    button = Button(mainframe, text='Search' , compound='left' , command= display_data , borderwidth=3, width=10 , font = f)
    button.after(100, update)
    button.grid(column= 4, row= 1 , padx=5 , pady=0, sticky='nwes')


def weather_label_info():
    text = ['Current Temp \u2070C' , 'Feels Like \u2070C' , 'Min Temp \u2070C', 'Max Temp \u2070C']
    for i in range (1,5):
        search_label = Label(mainframe , text=f'{text[i-1]}' , font=f)
        search_label.grid(column= i , row=2 , padx=5, pady=5, sticky='nwes')


def update():
    display_data()
    button.after(1000*60*30, update) #milliseconds*seconds*minutes , callback
    print('update done at: '+ str(dt.datetime.now().strftime("%H:%M:%S")))


def display_data():

    response = url()
    if response["cod"] == 200:
        r = [response["main"]["temp"], 
            response["main"]["feels_like"],
            response["main"]["temp_min"],
            response["main"]["temp_max"],
            response['weather'][0]['description']
            ]
        no_data = 'N/A'
        for i in range(len(r)-1):
            d = StringVar()
            d.set(r[i])
            data_label = Label(mainframe , textvariable=d, font=1)
            data_label.grid(column=i+1,  row= 3, padx=5, pady=5, sticky='nwes')
        data_label = Label(mainframe , text=r[4], font=f)    
        data_label.grid(column=3, columnspan=2 ,row= 4, padx=5, pady=5, sticky='nwes')
    else:
        for i in range(4):
            d = StringVar()
            d.set('N/A')
            data_label = Label(mainframe , textvariable=d, font=1)
            data_label.grid(column=i+1,  row= 3, padx=5, pady=5, sticky='nwes')
        data_label = Label(mainframe , text=r[4], font=f)    
        data_label.grid(column=3, columnspan=2 ,row= 4, padx=5, pady=5, sticky='nwes')


""" def icon_display():
    response = url()
    description = [
        response['weather'][0]['description'],
        response['weather'][0]['icon']]
    
    link =  f'https://openweathermap.org/img/wn/{description[1]}.png'
    u = urllib.request.urlopen(link)
    data_raw = u.read()
    u.close()
    icon = PhotoImage(data=base64.encodebytes(data_raw))
    description_label = Label(mainframe , image=icon, font=1)
    description_label.grid(column=4,  row= 4, padx=5, pady=5, sticky='nwes') """


############# start of main window


root = Tk()
root.title("Weather App")
root.geometry()
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

### input label (description)

input_description()

### input widget
city_input()

##### search button
search_button()

### info row
weather_label_info()

####### time display
time_display()
root.mainloop()
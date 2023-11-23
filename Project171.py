from tkinter import *
from datetime import datetime
import pytz

root = Tk()
root.title('World Clock')
root.minsize(450, 450)
root.configure(background = 'snow')

lblTime = Label(root, text = '', bg = 'light blue')
lblTime.place(relx = 0.5, rely = 0.6, anchor = CENTER)

entZone = Entry(root)
entZone.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def getTime(zone):
    home = pytz.timezone(zone)
    timeStr = str(datetime.now())

    timeStr = timeStr[ int(timeStr.index(' ')) + 1 : -1]
    timeStr = timeStr[ 0: int(timeStr.index('.')) ] 
    lblTime['text'] = timeStr

btnTime = Button(root, text = 'Get Current Time', command = lambda: getTime(entZone.get()))
btnTime.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()
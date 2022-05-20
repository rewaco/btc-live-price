#https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,JPY,EUR
import requests
import tkinter as tk
from datetime import datetime


canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("bitcoin tracker")

def trackbitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")
    labelprice.config(text= str(price) + " $")
    Labeltime.config(text= "last updated time" + time)
    canvas.after(1000, trackbitcoin)

    price2 = response["EUR"]
    time2 =datetime.now().strftime("%H:%M:%S")
    labelprice2.config(text= str(price2)+ " €")
    labeltime2.config(text="last updated time"+time2 )

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "bold")

label = tk.Label(canvas, text="Bitcoin dollar live price", font=f1)
label.pack(pady=5)



labelprice = tk.Label(canvas, font=f2)
labelprice.pack(pady=5)

Labeltime = tk.Label(canvas, font=f3)

Labeltime.pack(pady=5)

label2 = tk.Label(canvas,text="Bitcoin euro live price", font=f1)
label2.pack(pady=5)

labelprice2 = tk.Label(canvas,font=f2)
labelprice2.pack(pady=5)

labeltime2 = tk.Label(canvas, font=f3)
labeltime2.pack(pady=5)

trackbitcoin()
canvas.mainloop()

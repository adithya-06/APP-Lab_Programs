#14
from tkinter import *
from tkinter import ttk

def convert():
    initial=float(fromAmount.get())
    final=initial*74.93
    after.set(str(final))

currencyNameList = ["USD", "INR", "GBP", "CAD", "JPY", "CNY", "INR", "AUD", "NZD", "CHF", "SGD", "SEK", "DKK", "NOK", "KRW", "MXN", "ZAR", "BRL", "RUB", "TRY", "CZK", "PLN", "PHP", "RON", "HUF", "MYR", "IDR", "ILS", "BGN", "HRK", "THB", "ISK", "CLP", "PKR", "BHD", "VND", "LKR", "TWD", "SAR", "RSD", "KWD", "JOD", "OMR", "QAR", "KZT", "KGS", "UAH", "TMT", "COP", "KES", "LAK", "TJS", "UZS", "MNT", "MVR", "NPR", "PYG", "BND", "KHR", "VUV", "FJD", "BDT", "KZT", "LBP", "JMD", "LYD", "MAD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CDF", "CHF", "CLP", "CNH", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "EUR"]
root = Tk()

root.title("Python Project")
welcomeLabel = Label(root, text="Welcome to Currency Converter",background="blue",foreground="white",font=('bold',15),width=45)
welcomeLabel.grid(column=0, row=0,columnspan=3)
conversionRateLabel = Label(root, text="1 USD = 74.93 Indian Rupee",font=('bold',10))
conversionRateLabel.grid(column=1, row=1)
dateLabel = Label(root, text="2020-07-22",font=('bold',10))
dateLabel.grid(column=1, row=2)
fromCurrencyDropDown = ttk.Combobox(root, values=currencyNameList)
fromCurrencyDropDown.grid(column=0, row=3)
fromCurrencyDropDown.current(0)
toCurrencyDropDown = ttk.Combobox(root, values=currencyNameList)
toCurrencyDropDown.grid(column=2, row=3)
toCurrencyDropDown.current(1)
fromAmount = Entry(root)
fromAmount.grid(column=0, row=4)
after=StringVar()
toAmount = Entry(root, textvariable=after)
toAmount.grid(column=2, row=4)
convertButton = Button(root, text="Convert", command=convert)
convertButton.grid(column=1, row=5)

root.mainloop()

#15

from cgitb import text
from time import sleep
from tkinter import *
from tkinter import ttk

def delayStop():
    progressBar.after(1000,progressBar.stop())

root = Tk()

root.title("Python GUI")
menu = Menu(root)
menu.add_command(label="File")
menu.add_command(label="Help")
root.config(menu=menu)
tabControl = ttk.Notebook(root)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 1')
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 2')
tabControl.pack(expand=1, fill="both")
theSnakeLabelFrame = ttk.LabelFrame(tab1, text="The Snake")
theSnakeLabelFrame.grid(column=0, row=0, padx=8, pady=4)
disabledCheckBox = Checkbutton(theSnakeLabelFrame, text="Disabled", state="disabled")
disabledCheckBox.grid(column=0, row=0)
checkBoxVar1 = IntVar()
checkBoxVar2 = IntVar()
unCheckedCheckBox = Checkbutton(theSnakeLabelFrame, text="Unchecked",variable=checkBoxVar1)
unCheckedCheckBox.grid(column=1, row=0)
enabledCheckBox = Checkbutton(theSnakeLabelFrame, text="Enabled",variable=checkBoxVar2)
enabledCheckBox.grid(column=2, row=0)
var_0=IntVar()
var_1=IntVar()
var_2=IntVar()
blueRadioButton = Radiobutton(theSnakeLabelFrame, text="Blue", variable=var_0)
blueRadioButton.grid(column=0, row=1)
redRadioButton = Radiobutton(theSnakeLabelFrame, text="Red", variable=var_1)
redRadioButton.grid(column=2, row=1)
goldRadioButton = Radiobutton(theSnakeLabelFrame, text="Gold", variable=var_2)
goldRadioButton.grid(column=1, row=1)
progressBar = ttk.Progressbar(tab1, orient="horizontal", length=200, mode="determinate")
progressBar.grid(column=0, row=1, padx=8, pady=4)
progressBarLabelFrame = ttk.LabelFrame(theSnakeLabelFrame, text="Progress Bar")
progressBarLabelFrame.grid(column=0, row=2)
runProgressBarButton = Button(progressBarLabelFrame, text="Run Progress Bar",command=progressBar.start)
runProgressBarButton.grid(column=0, row=0)
startProgressBarButton = Button(progressBarLabelFrame, text="Start Progress Bar",command=progressBar.start)
startProgressBarButton.grid(column=0, row=1)
stopImmediatelyButton = Button(progressBarLabelFrame, text="Stop Immediately",command=progressBar.stop)
stopImmediatelyButton.grid(column=0, row=2)    
stopAfterSecondButton = Button(progressBarLabelFrame, text="Stop After Second",command=delayStop)
stopAfterSecondButton.grid(column=0, row=3)

root.mainloop()

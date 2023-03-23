import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
from WFF import WFF
myWFF=WFF()
myWFF.__int__("P \\vee Q")
msg=tk.Message(window,text=myWFF.printRule(),font=('楷体',15),bg='white',
               relief='sunken').grid(row=1)
label=tk.Label(window,text='请输入待验证公式').grid(row=1,column=1)
inputTar=tk.Entry(window)
inputTar.grid(row=2,column=1)

def showOutcome():
    targ=inputTar.get()
    myWFF.__int__(targ)
    outputTar='\n'.join(myWFF.outcome())
    messagebox.showinfo('结果',outputTar)
checkButton=tk.Button(window,text='验证',command=showOutcome)
inputTar.bind('<Return>',showOutcome)
checkButton.grid(row=3,column=1)
window.mainloop()





window.mainloop()
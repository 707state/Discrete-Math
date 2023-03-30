try:
    import tkinter as tk
    from tkinter import messagebox
    window=tk.Tk()
    from WFF import WFF
    from database import Restore
    myWFF=WFF()
    msg=tk.Message(window,text=myWFF.printRule(),font=('楷体',15),bg='white',
                   relief='sunken').grid(row=1)
    label=tk.Label(window,text='请输入待验证公式')
    label.grid(row=1,column=1)
    inputTar=tk.Entry(window)
    inputTar.grid(row=2,column=1)
    myRestore=Restore()
    def showInput():
        return inputTar.get()
    def showOutcome():
        targ=showInput()
        myWFF.__int__(targ)
        outputTar='\n'.join(myWFF.outcome())
        messagebox.showinfo('结果: ',outputTar)
    def inputData():
        myRestore.__int__(showInput(), myWFF.outcome())
    def outputData():
        outputDelete=myRestore.PrintHistory()
        allData='\n'.join(outputDelete)
        messagebox.showinfo("历史",allData)
    def deleteData():
        myRestore.DeleteData()
    labelClick=tk.Button(window,text='录入数据',command=inputData)
    labelClick.grid(row=1,column=2)
    labekCheck=tk.Button(window,text='以往数据',command=outputData)
    labekCheck.grid(row=2,column=2)
    labelDelete=tk.Button(window,text='删除所有数据',command=deleteData)
    labelDelete.grid(row=3,column=2)
    checkButton=tk.Button(window,text='验证',command=showOutcome)
    inputTar.bind('<Return>',showInput)
    checkButton.grid(row=3,column=1)
    window.mainloop()
except:
    print("wrong")
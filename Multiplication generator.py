
from tkinter import *
root=Tk()
root.title('Multiplaction Table Generator For Your Maths HomeWork (:')
table = Text(root,width=35,height=40,font=('Courier'))
your_tabels=Label(root,text='Your Tables Down Below:',font=('Courier',10))
def main():
    number1=number.get()
    number2=how_many_times.get()
    try:
        how_many_times1=int(number2)
        number_to_multipl1y = int(number1)
        table.delete("1.0",'end')
        for a in range(how_many_times1):
            full=int(a*number_to_multipl1y)
            global Tables
            Tables=f'''{number_to_multipl1y} x {a+1} = {full+number_to_multipl1y}\n'''
            your_tabels.pack()
            table.insert(float(how_many_times1)+1,Tables)
            table.pack()
    except ValueError:
        from tkinter import messagebox
        messagebox.showerror('message','Please Enter A Vaild Number!!!')

put_here_indicator=Label(root,text='Which Number Put Down Below:',font=('Courier',10))
put_here_indicator_1=Label(root,text='How Many Time Put Down Below:',font=('Courier',10))
start=Button(root,text='Start Multiplication',command=main)
put_here_indicator.pack()
number=Entry(root)
how_many_times=Entry(root)
number.pack()
put_here_indicator_1.pack()
how_many_times.pack()
start.pack()
root.mainloop()

def math():
    price=int(input("Enter price: "))
    qty=int(input("Enter quantity: "))
    amt=price*qty
    if amt>1000:
        print("discount applicable")
        discount=amt*10/100
        amt=amt-discount
        print("Amount payable: ", amt)
    return

def square(x):
    return (x*x)

print("Quadrat: ", square(4))

from MyPackage import power, average, SayHello
SayHello()
x=power(3,2)
print("power(3,2) : ", x)


from tkinter import *
window=Tk()
lbl=Label(window, text="This is the Coding Week Window", fg='red', font=("Helvetica", 10))
lbl.place(x=60, y=50)
btn=Button(window, text="Press the Button", fg='blue')
btn.place(x=80, y=100)
window.title('Coding Week')
window.geometry("300x200+10+10")
window.mainloop()
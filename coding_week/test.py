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
# add widgets here

window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()

from tkinter import *
window=Tk()
btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()
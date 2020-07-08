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
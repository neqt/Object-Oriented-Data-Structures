# จงเขียน Overloading Function สำหรับ Calculator class โดยที่มีรูปแบบ Code ดังนี้ (สามารถเพิ่มพารามิเตอร์ได้)


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self):
        print(self.x+self.y)

    def __sub__(self):
        print(self.x-self.y)

    def __mul__(self):
        print(self.x*self.y)

    def __truediv__(self):
        print(self.x/self.y)


x, y = input("Enter num1 num2 : ").split(",")
n = Calculator(int(x), int(y))

n.__add__()
n.__sub__()
n.__mul__()
n.__truediv__()

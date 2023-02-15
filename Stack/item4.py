# ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
# +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
# -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
# /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# DUP: Duplicate (not double) ค่าบนสุดของ stack
# POP: Pop ค่าบนสุดออกจาก stack และ discard.
# PSH: ทำการ push ตัวเลขลง stack
# หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"

# * Stack Calculator *
# Enter arguments : 5 6 +
# 11


class StackCalc:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.isInvalid = False

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def run(self, value):
        for i in value:
            if i[0] in '0123456789':
                self.push(int(i))
            else:
                if i in '+-*/':
                    a = self.items.pop()
                    b = self.items.pop()
                    if i == '+':
                        self.push(a+b)
                    elif i == '-':
                        self.push(a-b)
                    elif i == '*':
                        self.push(a*b)
                    elif i == '/':
                        self.push(int(a/b))
                elif i == 'DUP':
                    self.push(self.peek())
                elif i == 'POP':
                    self.items.pop()
                elif i == 'PSH':
                    self.push(i)
                else:
                    self.isInvalid = True
                    self.push(i)
                    break
        return self.items

    def getValue(self):
        s = ''
        if not self.isEmpty():
            if self.isInvalid:
                s += 'Invalid instruction: ' + str(self.peek())
            elif self.size() > 1:
                s += str(self.peek())
            else:
                for ele in self.items:
                    s += str(ele)
        else:
                s += '0'
        return s


print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())

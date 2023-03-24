# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา

# A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK
# P           ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1
# *** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty


class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        s = 'Value in Stack = '
        if self.isEmpty():
            s += 'Empty'
        else:
            for ele in self.items:
                s += str(ele) + ' '
        return s


S = Stack()
inp = input("Enter Input : ").split(',')

for i in inp:
    i = i.split()

    if i[0] == 'A':
        S.push(i[1])
        print(f'Add = {i[1]} and Size = {S.size()}')
    elif i[0] == 'P':
        if not S.isEmpty():
            print(f'Pop = {S.pop()} and Index = {S.size()}')
        else:
            print('-1')

print(S)

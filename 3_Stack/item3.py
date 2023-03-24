# ให้รับ Input เป็น Infix และแสดงผลลัพธ์ออกมาเป็น Postfix โดยจะมี Operator 5 แบบ ได้แก่ + - * / ^

# Enter Infix : a+b
# Postfix : ab+


class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

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


inp = input('Enter Infix : ')
S = Stack()
print('Postfix : ', end='')

priority = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
result = ''

for i in inp:
    if i in '+-*/^':
        if S.isEmpty():
            S.push(i)
        else:
            while not S.isEmpty():
                if S.peek() == '(':
                    break
                else:
                    if priority.get(S.peek()) >= priority.get(i):
                        result += str(S.pop())
                    else:
                        break
            S.push(i)
    elif i == '(':
        S.push(i)
    elif i == ')':
        while S.peek() != '(':
            result += str(S.pop())
        S.pop()
    else:
        result += str(i)

print(result, end='')

while not S.isEmpty():
    print(S.pop(), end='')

print()

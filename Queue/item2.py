# จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue
# โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้
# แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ
# แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ
# ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2
# จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด

# Enter people : Lorem_Ipsum
# 1 ['o', 'r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L'] []
# 2 ['r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o'] []
# 3 ['e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o', 'r'] []
# 4 ['m', '_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e'] []
# 5 ['_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm'] []
# 6 ['I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm', '_'] []
# 7 ['p', 's', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] []
# 8 ['s', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p']
# 9 ['u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p', 's']
# 10 ['m'] ['e', 'm', '_', 'I', 'u'] ['s']
# 11 [] ['e', 'm', '_', 'I', 'u'] ['s', 'm']


class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        q = ''
        cnt = 0
        if self.isEmpty():
            q += 'Empty'
        else:
            for ele in self.items:
                q += str(ele)
                cnt += 1
                if cnt < self.size():
                    q += ', '
        return q


q = Queue()
q1 = Queue()
q2 = Queue()
isCount = False
cnt = 0

inp = input('Enter people : ')

for ele in inp:
    q.enQueue(ele)

for i in range(q.size()):
    if not q1.isEmpty() and i % 3 == 0 and i != 0:
        q1.deQueue()
    if not q2.isEmpty() and cnt % 2 == 0 and cnt != 0:
        q2.deQueue()

    if q1.size() < 5:
        q1.enQueue(q.deQueue())
    else:
        q2.enQueue(q.deQueue())
        isCount = True
        
    if isCount:
        cnt += 1

    print(str(i+1), end=' ')
    print(q.items, end=' ')
    print(q1.items, end=' ')
    print(q2.items)

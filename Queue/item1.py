# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา

# E <value> ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue
# D         ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูลปัจจุบันของ Queue

# ***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
# ***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty

# Enter Input : E 1,E 2,E 3,D,D,E 4
# 1
# 1, 2
# 1, 2, 3
# 1 <- 2, 3
# 2 <- 3
# 3, 4
# 1, 2 : 3, 4


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
dq = Queue()

inp = input('Enter Input : ').split(',')

for i in inp:
    i = i.split()

    if i[0] == 'E':
        q.enQueue(i[1])
        print(q)
    elif i[0] == 'D':
        if not q.isEmpty():
            d = q.deQueue()
            print(str(d) + ' <- ', end='')
            if not q.isEmpty():
                print(q)
            else:
                print('Empty')
            dq.enQueue(d)
        else:
            print('Empty')

print(str(dq) + ' : ' + str(q))

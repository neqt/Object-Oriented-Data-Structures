# จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node
# ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

# createList()      สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist
# printList()       สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print
#                   ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว
# mergeOrderList()  สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value
#                   โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

# ****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****
# ****ห้ามสร้าง Class LinkList****

# Enter 2 Lists : 1,3,5,7,10,20,22 4,6,7,8,15
# LL1 : 1 3 5 7 10 20 22
# LL2 : 4 6 7 8 15
# Merge Result : 1 3 4 5 6 7 7 8 10 15 20 22


class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


def createList(l=[]):
    head = p = node(l[0])
    for i in range(1, len(l)):
        p.next = node(l[i])
        p = p.next
    return head


def printList(H):
    s = ''
    while H != None:
        s += str(H.data) + ' '
        H = H.next
    print(s)


def mergeOrderesList(p, q):
    head = cur = node()
    while p != None or q != None:
        if p == None:
            cur.next = q
            q = q.next
        elif q == None:
            cur.next = p
            p = p.next
        elif int(p.data) <= int(q.data):
            cur.next = p
            p = p.next
        else:
            cur.next = q
            q = q.next
        cur = cur.next
    return head.next


#################### FIX comand ####################
L1, L2 = input("Enter 2 Lists : ").split()
LL1 = createList(L1.split(','))
LL2 = createList(L2.split(','))
print('LL1 : ', end='')
printList(LL1)
print('LL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('Merge Result : ', end='')
printList(m)

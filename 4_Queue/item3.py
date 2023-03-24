# รับ string มาเข้าคิวหา secret code โดยรับ input คือ
# code เป็น string ยาว
# hint คือตัวแรกของรหัสที่ถูกต้อง

# **คำใบ้**
# ascii ของ "f" มีค่า = 102
# ascii ของ "g" มีค่า = 103
# ascii ของ "h" มีค่า = 104
# ascii ของ "i" มีค่า = 105
# ascii ของ "j" มีค่า = 106

# Enter code,hint : gjstu`uftu,f
# ['f']
# ['f', 'i']
# ['f', 'i', 'r']
# ['f', 'i', 'r', 's']
# ['f', 'i', 'r', 's', 't']
# ['f', 'i', 'r', 's', 't', '_']
# ['f', 'i', 'r', 's', 't', '_', 't']
# ['f', 'i', 'r', 's', 't', '_', 't', 'e']
# ['f', 'i', 'r', 's', 't', '_', 't', 'e', 's']
# ['f', 'i', 'r', 's', 't', '_', 't', 'e', 's', 't']


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
        return str(self.items)


q = Queue()
code, hint = input("Enter code,hint : ").split(",")

for i in code:
    q.enQueue(chr(ord(i) + int(ord(hint) - ord(code[0]))))
    print(q)
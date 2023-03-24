# สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
# ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

# กิจกรรม                          สถานที่
# 0 = กินข้าว(Eat)                  0 = ร้านอาหาร(Res.)
# 1 = เล่นเกม(Game)                 1 = ห้องเรียน(ClassR.)
# 2 = ทำโจทย์ datastruc(Learn)     2 = ห้างสรรพสินค้า(SuperM.)
# 3 = ดูหนัง(Movie)                 3 = บ้าน(Home)

# โดยการรับ Input จะประกอบด้วย
# กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,
# เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร
#     วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
# จะได้ว่า 0:0 2:0,1:3 3:2

# ***มีการคิดคะแนนดังนี้***
# ·       กิจกรรมเดียวกันแต่คนละสถานที่       +1
# ·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2
# ·       กิจกรรมเดียวกันและสถานที่เดียวกัน     +4
# ·       ไม่เหมือนกันเลย                   -5

# หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน
# โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง

# Enter Input : 0:0 2:0,1:3 3:3,2:1 2:1
# My   Queue = 0:0, 1:3, 2:1
# Your Queue = 2:0, 3:3, 2:1
# My   Activity:Location = Eat:Res., Game:Home, Learn:ClassR.
# Your Activity:Location = Learn:Res., Movie:Home, Learn:ClassR.
# Yes! You're my love! : Score is 8.


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
        for ele in self.items:
            q += str(ele)
            cnt += 1
            if cnt < len(self.items):
                q += ', '
        return q


qm = Queue()
qy = Queue()

inp = input('Enter Input : ').split(',')
for i in inp:
    i = i.split()
    if i[0]:
        qm.enQueue(i[0])
    if i[1]:
        qy.enQueue(i[1])

print('My   Queue = ', end='')
print(qm)
print('Your Queue = ', end='')
print(qy)

print('My   Activity:Location = ', end='')
cnt_my = 0
for j in qm.items:
    act = ''
    loc = ''
    j = j.split(':')
    if j[0] == '0':
        act += 'Eat'
    elif j[0] == '1':
        act += 'Game'
    elif j[0] == '2':
        act += 'Learn'
    elif j[0] == '3':
        act += 'Movie'
    if j[1] == '0':
        loc += 'Res.'
    elif j[1] == '1':
        loc += 'ClassR.'
    elif j[1] == '2':
        loc += 'SuperM.'
    elif j[1] == '3':
        loc += 'Home'
    print(act + ':' + loc, end='')
    cnt_my += 1
    if cnt_my < len(qm.items):
        print(', ', end='')
print()

cnt_yo = 0
print('Your Activity:Location = ', end='')
for j in qy.items:
    act = ''
    loc = ''
    j = j.split(':')
    if j[0] == '0':
        act += 'Eat'
    elif j[0] == '1':
        act += 'Game'
    elif j[0] == '2':
        act += 'Learn'
    elif j[0] == '3':
        act += 'Movie'
    if j[1] == '0':
        loc += 'Res.'
    elif j[1] == '1':
        loc += 'ClassR.'
    elif j[1] == '2':
        loc += 'SuperM.'
    elif j[1] == '3':
        loc += 'Home'
    print(act + ':' + loc, end='')
    cnt_yo += 1
    if cnt_yo < len(qy.items):
        print(', ', end='')
print()

score = 0
for k in range(len(inp)):
    if qm.peek()[0] == qy.peek()[0]:
        if qm.peek()[2] == qy.peek()[2]:
            score += 4
        else:
            score += 1
    else:
        if qm.peek()[2] == qy.peek()[2]:
            score += 2
        else:
            score -= 5
    qm.deQueue()
    qy.deQueue()

if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
elif score > 0:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")

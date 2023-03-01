# สร้าง method insert ในคลาส LinkedList เพื่อแทรกข้อมูลลงใน index ที่กำหนดของ linked list และ return ผลลัพธ์ตามตัวอย่าง
# โดยคลาส LinkedList จะประกอบไปด้วย
# 1. def __init__(self): สำหรับสร้าง linked list
# 2. def __str__(self): return string แสดง ค่าใน linked list
# 3. def isEmpty(self): return list นั้นว่างหรือไม่
# 4. def append(self, data): เพิ่ม data ต่อท้าย linked list
# 5. def insert(self, index, data): insert data ใน index ที่กำหนด
# โดยการแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่
# คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Header Node ดูนะครับ
# *******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********

# ข้อมูลอินพุท จะคั่นด้วยเครื่องหมาย คอมม่า
# ตัวแรก จะเป็น ลิสต์ตั้งต้น คั่นด้วยช่องว่าง (space)
# ตัวต่อไปจะอยู่ในรูปแบบ index:data

# Enter Input : 1 2 3 4, 0:7, 3:9
# ลิสต์ตั้งต้นคือ 1->2->3-> 4
# ข้อมูล 0:0 คือให้เพิ่ม node ลำดับ 0 โดยมีข้อมูลเป็น 7
# ข้อมูล 3:9 คือให้เพิ่ม node ลำดับ 3 โดยมีข้อมูลเป็น 9

# Enter Input : 1 2, 0:0, 3:3
# link list : 1->2
# index = 0 and data = 0
# link list : 0->1->2
# index = 3 and data = 3
# link list : 0->1->2->3


class Node:
    def __init__(self, data):
        self.data = data

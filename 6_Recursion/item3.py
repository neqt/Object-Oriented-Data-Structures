# # ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
# # เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง
# # หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! !
# # *** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11

# # Enter Number : -1
# # Only Positive & Zero Number ! ! !


def generate_binary(n, bi=''):
    if len(bi) == n:
        print(bi)
    else:
        generate_binary(n, bi + '0')
        generate_binary(n, bi + '1')


inp = int(input("Enter Number : "))

if inp < 0:
    print('Only Positive & Zero Number ! ! !')
elif inp == 0:
    print("0")
else:
    generate_binary(inp)

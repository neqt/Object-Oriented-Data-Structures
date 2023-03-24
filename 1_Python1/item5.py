# เขียนภาษา Python เพื่อวาดรูปหยิน-หยาง ซึ่งจะรับ input เป็นขนาดของรูปหยิน-หยาง

# Enter Input : 1
# ..#+++
# .##+#+
# ###+++
# ###+++
# #+#++.
# ###+..


n = int(input("Enter Input : "))

for i in range(n+2):

    for j in range(n+1-i):
        print('.', end='')
    for j in range(i+1):
        print('#', end='')

    for j in range(n+2):
        if i == 0 or i == n+1 or j == 0 or j == n+1:
            print('+', end='')
        else:
            print('#', end='')

    print()


for i in range(n+2):

    for j in range(n+2):
        if i == 0 or i == n+1 or j == 0 or j == n+1:
            print('#', end='')
        else:
            print('+', end='')

    for j in range(n+2-i):
        print('+', end='')
    for j in range(i):
        print('.', end='')

    print()

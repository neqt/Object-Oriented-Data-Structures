# รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง


num1, num2 = map(int, input(
    "*** multiplication or sum ***\nEnter num1 num2 : ").split())

if (num1*num2) > 1000:
    print(f'The result is {num1+num2}')
else:
    print(f'The result is {num1*num2}')

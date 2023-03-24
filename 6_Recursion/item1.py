# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
# หาลำดับ Fibonacci ของ input ที่รับเข้ามาโดยใช้ Recursive

# Enter Number : 1
# fibo(1) = 1


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input('Enter Number : '))
print(f'fibo({num}) = {fibonacci(num)}')
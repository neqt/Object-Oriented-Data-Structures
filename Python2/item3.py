# ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function
# ถ้าหากเป็น 1 argument -> range(a)            | start = 0 , end = a , step = 1
# ถ้าหากเป็น 2 argument -> range(a, b)        | start = a , end = b , step = 1
# ถ้าหากเป็น 3 argument -> range(a, b, c)    | start = a , end = b , step = c

# *** New Range ***
# Enter Input : 10
# (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)

# *** New Range ***
# Enter Input : 3.2 6.32
# (3.2, 4.2, 5.2, 6.2)

# *** New Range ***
# Enter Input : 0.112 6.45 1.35
# (0.112, 1.462, 2.812, 4.162, 5.512)

# *** New Range ***
# Enter Input : 1 7 1.2
# (1.0, 2.2, 3.4, 4.6, 5.8)

# *** New Range ***
# Enter Input : 1.2 5.9 0.45
# (1.2, 1.65, 2.1, 2.55, 3.0, 3.45, 3.9, 4.35, 4.8, 5.25, 5.7)

# def new_range(a, b=None, c=None):
#     temp = []

#     if a != None and b == None and c == None:
#         start = 0
#         end = a
#         step = 1
#     if a != None and b != None and c == None:
#         start = a
#         end = b
#         step = 1
#     if a != None and b != None and c != None:
#         start = a
#         end = b
#         step = c

#     while (start < end):
#         temp.append(start)
#         print(str(start)+" + "+str(step)+" = "+str(start+step)+"\n")
#         # start = sum([start, step])
#         start += step

#     return print(tuple(temp))

def new_range(*args):
    if len(args) == 1:
        start = 0
        end = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]
    else:
        return "Invalid number of arguments"

    lst = [start]
    while start + step < end:
        start += step
        lst.append(start)

    return lst


inp = [float(i) for i in input('*** New Range ***\nEnter Input : ').split()]

if len(inp) == 1:
    print(new_range(inp[0]))
elif len(inp) == 2:
    print(new_range(inp[0], inp[1]))
else:
    print(new_range(inp[0], inp[1], inp[2]))

# หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล
# เช่น
# hbd(65) = "saimai is just 21, in base 32!"
# hdb(21) = "saimai is just 21, in base 10!"
# hdb(8888) = "saimai is just 20, in base 4444!"


def hbd(age):
    return 'saimai is just '+str(20+(age % 2))+', in base '+str(age//2)+'!'


year = input("Enter year : ")
print(hbd(int(year)))


# 1 kyat  = 16pel = 128yway

price = int(input("Enter current gold price: "))
kyat = int(input("enter kyat: "))
pel = int(input("enter pel: "))
yway = int(input("enter yway: "))
yway_subtraction = int(input("Enter yway_subtraction: "))

# pel_addition: float = 0
# kyat_addition: float = 0


def cal():
    if yway > 8:
        return "Yway cannot be over 8"

    elif pel > 16:
        return "Pel cannot be over 16"

    yway_price = price/128
    kyat_addition = kyat*128

    total_yway = yway + (pel*8)
    total_yway = total_yway+kyat_addition

    if yway_subtraction > 0:
        total_yway -= yway_subtraction
        result = yway_price*total_yway
    return result


print(cal)

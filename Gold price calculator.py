
# 1 kyat  = 16pel = 128yway

price = int(input("Enter current gold price: "))
kyat = int(input("enter kyat: "))
pel = int(input("enter pel: "))
yway = int(input("enter yway: "))
yway_subtraction = int(input("Enter yway_subtraction: "))


def cal():  # calculated in price per yway
    yway_price = price/128
    yway_cal = yway/8
    pel_cal = (pel+yway_cal)
    # print(pel_cal)
    kyat_cal = kyat+(pel_cal/16)

    # if you want to subtract for stone with gold
    net_yway = (kyat_cal * 128) - yway_subtraction

    # print(net_yway)
    total_price = net_yway * yway_price

    return total_price


print(cal())

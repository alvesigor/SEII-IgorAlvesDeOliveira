weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ").upper()

if unit == 'K':
    print("Weigth in Lbs: " + str(weight*2.2))
elif unit == 'L':
    print("Weigth in Kg: " + str(weight/2.2))
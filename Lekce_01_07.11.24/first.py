vek = input("Zadej vek: ")

try:
    vek = float(vek)

    if vek > 12 and vek < 20:
        print("Jsi teenager")
    else:
        print("Teenagerem nejsi")
except:
    print("Neplatna hodnota")
import math

unknown = input("請輸入未知數(T(n)/a/n/d/r):")

if unknown == 'Tn':
    a = int(input("請輸入數列首項:"))
    n = int(input("請輸入數列中你想計算的一項:"))

    s_type = input("請輸入該數列為等差或等比:")

    if s_type == "等差":
        T1 = int(input("請輸入數列其中一個項數:"))
        T2 = int(input("請輸入之後一個項數:"))
        d = T2 - T1
        Tn = a + (n-1)*d
        print(f"該項數為:{Tn}")

    if s_type == "等比":
        T1 = int(input("請輸入數列其中一個項數:"))
        T2 = int(input("請輸入之後一個項數:"))
        r = T2 / T1
        Tn = a * r**(n - 1)
        print(f"該項數為:{Tn}")

if unknown == 'a':
    Tn = int(input("請輸入數列其中項數:"))
    n = int(input("請輸入該項數在數列中的位置:"))
    s_type = input("請輸入該數列為等差或等比:")

    if s_type == "等差":
        T1 = int(input("請輸入數列其中一個項數:"))
        T2 = int(input("請輸入之後一個項數:"))
        d = T2 - T1
        a = Tn - (n-1)*d
        print(f"該數列首項為:{a}")

    if s_type == "等比":
        T1 = int(input("請輸入數列其中一個項數:"))
        T2 = int(input("請輸入之後一個項數:"))
        r = T2 / T1
        a = Tn / (r**(n-1))
        print(f"該數列首項為:{a}")

if unknown == 'n':
    Tn = int(input("請輸入數列其中項數:"))
    a = int(input("請輸入數列首項:"))
    s_type = input("請輸入該數列為等差或等比:")

    if s_type == "等差":
        T1 = int(input("請輸入數列其中一個項數:"))
        T2 = int(input("請輸入之後一個項數:"))
        d = T2 - T1
        n = (Tn + d - a)/d
        print(f"該數列項數為:{n}")

    if s_type == "等比":
        T1 = int(input("請輸入數列其中一個項數:"))
        T2 = int(input("請輸入之後一個項數:"))
        r = T2 / T1
        n = (math.log((Tn / a), r)) + 1
        print(f"該數列項數為:{n}")

if unknown == 'd' or unknown == 'r':
    Tn = int(input("請輸入數列其中項數:"))
    n = int(input("請輸入該項數在數列中的位置:"))
    a = int(input("請輸入數列首項:"))

    if unknown == 'd':
        d = (Tn - a) / (n-1)
        print(f"該數列公差為:{d}")

    if unknown == 'r':
        r = (Tn / a) ** (1 / (n - 1))
        print(f"該數列公比為:{r}")

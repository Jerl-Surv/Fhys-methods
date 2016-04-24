H = [9892, 8349, 5834, 7922, 9364, 10084, 9570, 11120, 11174, 11792, 14056, 15418]
#H --> 1 000 000 H
v0 = [60, 52, 45, 37, 30, 25, 21, 18, 15, 12, 9, 7]

#H = f(v0) = A + B / v0 + C * v0
e2min = 100000000
e2max = 0

for A in range(6450, 7000, 10):
    Hp = []
    e2 = 0
    for B in range(63000, 66000, 100):
        for C in range(0, 15, 1):
            for i in range(12):
                Hp.append(int(A + B / v0[i] + C * v0[i]))
                #print(Hp)
                e2 = e2 + (Hp[i] - H[i])**2 
            if e2 < e2min:
                e2min = e2
                #print("H = ", A, " + ", B, " / ", "v0 + ", C, " * v0")
                Ac = A
                Bc = B
                Cc = C
                Hp = []
                e2 = 0
            else:
                Hp = []
                e2 = 0


for i in range(12):
    Hp.append(int(Ac + Bc / v0[i] + Cc * v0[i]))
    e2 = abs(Hp[i] - H[i]) 
    if e2 > e2max:
        e2max = e2
        e2 = 0
        j = i
    else:
        e2 = 0 
eA = ((Ac*(e2max/H[j]))//10)*10
eB = ((Bc*(e2max/H[j]))//100)*100
eC = ((Cc*(e2max/H[j]))//10)*10
print("Finish: H = ", Ac, "+-", eA, " + ", Bc, "+-", eB, " / ", "v0 + ", Cc, "+-", eC, " * v0")
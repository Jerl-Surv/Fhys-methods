H = [957, 862, 917, 1122]
F = [16, 13, 6, 3]

for A in range(0, 600, 10):
    Hp = []
    N = 0
    for B in range(600, 5600, 100):
        for C in range(16, 54, 1):
            for i in range(4):
                Hp.append(int(A + B / F[i] + C * F[i]))
                #print(Hp)
                if (H[i] - 30)<Hp[i]<(H[i] + 30):
                    N = N+1				
            if N > 3:
                print ('It seems ok: ', 'A = ', A, 'B = ', B, 'C = ', C, Hp)
                Hp = []
                N = 0
            else:
                Hp = []
                N = 0
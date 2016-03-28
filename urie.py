H = [960, 860, 920, 1120]
F = [16, 13, 6, 3]

for A in range(0, 340, 10):
    Hp = []
    N = 0
    for B in range(600, 4600, 100):
        for C in range(26, 54, 1):
            for i in range(4):
                Hp.append(int(A + B / F[i] + C * F[i]))
                #print(Hp)
                if (H[i] - 20)<Hp[i]<(H[i] + 20):
                    N = N+1				
            if N > 2:
                print ('It seems ok: ', 'A = ', A, 'B = ', B, 'C = ', C, Hp)
                Hp = []
                N = 0
            else:
                Hp = []
                N = 0

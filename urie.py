H = [960, 860, 920, 1120]
F = [16, 13, 6, 3]

Hp = []
N = 0 

for A in range(0, 340, 10):
	for B in range(600, 4600, 100):
		for C in range(26, 54, 1):
			
#			for i in range(1, 3, 1):
#			    Ft = F[i]
#			    Ht = H[i]
#			    Hpt = A + B/Ft + C*Ft
#				if (Ht-3) < Hpt < (Ht+3):
#					N = N+1

			for i in range(3):
				Hp[i] = A + B / F[i] + C * F[i]
				if (H[i] - 3)<Hp[i]<(H[i] + 3):
					N = N+1	
			
			if N > 2:
				print ('It seems ok: ', 'A = ', A, 'B = ', B, 'C = ', C, Hp)
			Hp = []
			N = 0
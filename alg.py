# Python example:

print("Say two numbers, that the first will be divided by the second for discover the rest of solution.")
D = int(input("\n» "))
d = int(input("\n» "))
Q = 0
R = 0

# Algoritm:
for i in range(D):
    i = i + 1
    r = i*d
    if r > D:
        Q = i - 1
        R = D - (d*Q)
        break
    else:
        continue

print(f" The Rest of {D}/{d} is {R} and the result is {Q}.")

# OOP mode:

class Return:
	def play():
		print("Say two numbers, that the first will be divided by the second for discover the rest of solution.")
		
		D = int(input("\n» "))
		d = int(input("\n» "))
		return(D, d)

	def ret(Divisor, divided):
		Q, R = 0, 0
		for i in range(D):
			i = i + 1
			r = i*d
			if r > D:
				Q = i - 1
				R = D - (d*Q)
				return Q, R
				break
			else:
				continue
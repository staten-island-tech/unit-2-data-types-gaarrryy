n = 0
n2 = 0
n = float(input('what is your number?'))
n == int(n)
n = float(input('what is your second number?'))
n == int(n2)
factors = []

for i in range(1,int(n/2)):
    if n%i == 0:
      if i not in factors:
         factors.append(i)
    if n/i not in factors:
            factors.append(int(n/i))

for i in range(1,int(n2/2)):
    if n2%i == 0:
      if i not in factors:
         factors.append(i)
    if n2/i not in factors:
            factors.append(int(n2/i))

for i in factors:
    print (i)


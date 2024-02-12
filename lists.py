n = int(input("What is your number?"))
n2 = int(input("What is your second number?"))


def gcf(n,n2):
    if n > n2: 
        small = n2
    else: 
        small = n 
    for i in range (1, n+1):
        if (n%i == 0) and (n2%i == 0):
            gcf = i

    return(gcf)

print(gcf(n,n2))
import random
def randperm(n):
    L = []
    for x in range(n):
        L.append(x)
    for i in range(n-1,-1,-1):
        j =  random.randint(0, i)
        L[i], L[j] = L[j], L[i]
    return L


print(randperm(5))
print(randperm(10 ** 6))
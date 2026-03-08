n = int(input("Digite a quantidade de números primos que deseja ver: "))
primos = []
num = 3
while len(primos) < n:
    eh_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        primos.append(num)
    num += 1
print(primos)
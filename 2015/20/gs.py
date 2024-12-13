val = 34000000

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def nb_presents(divisors,house):
    presents = 0
    for divisor in divisors:
        mult = house // divisor
        if mult > 50:
            continue
        else:
            presents += divisor*11
    return presents


presents = 0
house = 1
while(presents < val):
    divisors = find_divisors(house)
    presents = nb_presents(divisors,house)
    house += 1
print(house-1)
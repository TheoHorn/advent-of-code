with open("2024/22/input.txt") as f:
    secrets = set(map(int,f.read().splitlines()))

def mix_and_prune(secret, val):
    ans = secret ^ val
    return ans % 16777216

count = 0
for secret in secrets:
    for i in range(2000):
        val = secret * 64
        secret = mix_and_prune(secret,val)
        val = secret // 32
        secret = mix_and_prune(secret,val)
        val = secret * 2048
        secret = mix_and_prune(secret, val)
    count += secret
print(count)


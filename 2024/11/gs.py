from collections import defaultdict

with open('2024/11/input.txt', 'r') as file:
    nums = defaultdict(int)
    for n in file.read().split():
        nums[int(n)] += 1

def rules(num):
    if num == 0:
        return (1,)
    num_len = len(str(num))
    if num_len % 2 == 1:
        return (2024 * num,)
    return (num // (10**(num_len//2)), num % (10**(num_len//2)))

tokens = {}

def step(nums):
    new_nums = defaultdict(int)
    for n in nums:
        if n not in tokens:
            tokens[n] = rules(n)
        for k in tokens[n]:
            new_nums[k] += nums[n]
    return new_nums

for _ in range(75):
    nums = step(nums)
print(sum([nums[k] for k in nums]))
from collections import defaultdict

with open("2024/22/input.txt") as f:
    secrets = set(map(int, f.read().splitlines()))

def mix_and_prune(secret, val):
    return (secret ^ val) % 16777216

def generate_price_and_changes(secret):
    prices = []
    for _ in range(2000):
        val = secret * 64
        secret = mix_and_prune(secret, val)
        val = secret // 32
        secret = mix_and_prune(secret, val)
        val = secret * 2048
        secret = mix_and_prune(secret, val)

        prices.append(secret % 10) 
    changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    return prices, changes


subseq_first_prices = defaultdict(list)
for secret in secrets:
    prices, changes = generate_price_and_changes(secret)
    seen_subsequences = set() 
    for i in range(len(changes) - 3):
        subseq = tuple(changes[i:i + 4])
        if subseq not in seen_subsequences:
            subseq_first_prices[subseq].append(prices[i + 4])
            seen_subsequences.add(subseq)

# Aggregate the results
subseq_totals = {}
for seq, first_prices in subseq_first_prices.items():
    total = sum(first_prices)
    subseq_totals[seq] = total

# Find the best one
max_total = -1
for seq, total in subseq_totals.items():
    if total > max_total:
        max_total = total
        best_sequence = seq

max_bananas = subseq_totals[best_sequence]

print("Best sequence:", best_sequence)
print("Maximum bananas:", max_bananas)

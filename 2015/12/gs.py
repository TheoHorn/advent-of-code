import json
def sum_numbers(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_numbers(item) for item in data)
    elif isinstance(data, dict):
        return 0 if "red" in data.values() else sum(sum_numbers(value) for value in data.values())
    return 0
with open("2015/12/input.txt", "r") as f:
    json_data = json.load(f)
    print(sum_numbers(json_data))
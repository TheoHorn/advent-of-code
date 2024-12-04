# Advent of Code [2024] 🎄  

Welcome to my solutions for the **Advent of Code [2024]** challenges! Below, you’ll find my thoughts and progress for each day, along with a brief description of the problems tackled.

---

## 🗓 Progress Overview  
| Day | Puzzle Name           | Solution                | Difficulty | My Thoughts           |
|-----|-----------------------|-------------------------|------------|-----------------------|
| 1   | [Historian Hysteria](#day-1) | [Solution](./1/)     | ★☆☆☆☆     | An awaited comeback   |
| 2   | [Red-Nosed Reports](#day-2) | [Solution](./2/)     | ★★☆☆☆      | First problem of the year |
| 3   | [Mull It Over](#day-3)| [Solution](./3/)     | ★☆☆☆☆     | A little bit of regex                  |
| 4   | [Ceres Search](#day-4)| [Solution](./4/)     | ★★☆☆☆      | Brute force is always the best                  |
| 5   | [5](#day-5)                   | [Solution](./5/)     | ★★★★☆      |                      |
| 6   | [6](#day-6)                   | [Solution](./6/)     | ★★★★☆      |                      |
| 7   | [7](#day-7)                   | [Solution](./7/)     | ★★★★☆      |                      |
| 8   | [8](#day-8)                   | [Solution](./8/)     | ★★★★☆      |                      |
| 9   | [9](#day-9)                   | [Solution](./9/)     | ★★★★☆      |                      |
| 10  | [10](#day-10)                 | [Solution](./10/)    | ★★★★☆      |                      |
| 11  | [11](#day-11)                 | [Solution](./11/)    | ★★★★☆      |                      |
| 12  | [12](#day-12)                 | [Solution](./12/)    | ★★★★☆      |                      |
| 13  | [13](#day-13)                 | [Solution](./13/)    | ★★★★☆      |                      |
| 14  | [14](#day-14)                 | [Solution](./14/)    | ★★★★☆      |                      |
| 15  | [15](#day-15)                 | [Solution](./15/)    | ★★★★☆      |                      |
| 16  | [16](#day-16)                 | [Solution](./16/)    | ★★★★☆      |                      |
| 17  | [17](#day-17)                 | [Solution](./17/)    | ★★★★☆      |                      |
| 18  | [18](#day-18)                 | [Solution](./18/)    | ★★★★☆      |                      |
| 19  | [19](#day-19)                 | [Solution](./19/)    | ★★★★☆      |                      |
| 20  | [20](#day-20)                 | [Solution](./20/)    | ★★★★☆      |                      |
| 21  | [21](#day-21)                 | [Solution](./21/)    | ★★★★☆      |                      |
| 22  | [22](#day-22)                 | [Solution](./22/)    | ★★★★☆      |                      |
| 23  | [23](#day-23)                 | [Solution](./23/)    | ★★★★☆      |                      |
| 24  | [24](#day-24)                 | [Solution](./24/)    | ★★★★☆      |                      |


---

## 📜 Daily Breakdown  

### Day [1]: [Historian Hysteria](./1/)  

**Problem Summary:**  
The problem involved comparing two lists of integers and calculating a specific sum based on the frequency of each element in the second list. The goal was to determine how much "difference" there is between the two lists by counting how often each number from the first list appears in the second list and multiplying it by the value of that number.

**Solution:**  
I read the input file and split the lines into two lists of integers. Then, I sorted both lists to facilitate comparison. For each value in the first list, I counted how many times it appeared in the second list, then multiplied the frequency by the value itself and added the result to a cumulative sum. This approach required nested loops to count occurrences and efficiently calculate the final difference.

**My Thoughts:**  
The problem was fairly straightforward once I broke it down into sorting and counting operations. However, the nested loop for counting occurrences in the second list made it less efficient for larger datasets. While solving this, I was reminded of the importance of sorting and looking for patterns to simplify problems. It was enjoyable to solve, though I could see potential for optimizing the algorithm for larger inputs.
---

### Day [2]: [Red-Nosed Reports](./2/)  

**Problem Summary:**  
The task involved analyzing sequences of integers to determine whether they form a valid increasing or decreasing sequence with specific constraints. The problem required checking if the entire sequence, or any subsequence formed by removing one element, satisfies the conditions for being either "increasing" (with differences between consecutive numbers ranging from 1 to 3) or "decreasing" (with differences between consecutive numbers ranging from -1 to -3).

**Solution:**  
I implemented a function `check_sequence` to verify if a given sequence meets the specified constraints. The function checks whether the sequence is strictly increasing or decreasing based on the allowed differences. For each line in the input, I checked both the entire sequence and subsequences formed by removing one element at a time. If any sequence (or subsequence) passed the check, I counted it as "safe."

**My Thoughts:**  
The problem was a bit tricky due to the need to check subsequences by removing one element at a time, which added complexity. The most challenging part was ensuring that the subsequences were correctly validated without unnecessary checks. Once I broke the problem down, it was enjoyable to implement the solution.

----
### Day [3]: [Mull It Over](./3/)  

**Problem Summary:**  
This problem required parsing a file that contained certain expressions involving multiplication (e.g., `mul(a, b)`) and handling certain patterns related to the word "don't." The goal was to extract and compute the sum of products from the expressions while ensuring that specific phrases like "don't()" were excluded from consideration. The problem involved regular expressions (regex) to handle complex text parsing and filtering.

**Solution:**  
I used regular expressions to split the content of the input file based on the occurrence of `do()`, excluding the cases where "don't()" appeared. After splitting the content, I searched for multiplication expressions (`mul(a, b)`) using another regex and extracted the integer values. These values were then multiplied together and summed up to get the final result. The challenge lay in correctly handling the "don't()" occurrences to ensure they didn't interfere with the parsing logic.

**My Thoughts:**  
This problem was a fun exercise in text parsing using regular expressions. Initially, I found it tricky to manage the exclusion of "don't()" cases (i was stupid and did not read correctly the input), but once I figured out it was enjoyable to see how regex could efficiently parse and extract the necessary information. 
---

### Day [4]: [Ceres Search](./4/)

**Problem Summary:**  
This problem involved searching for a specific pattern ("XMAS") in a grid-like structure, represented by a list of strings. The goal was to find the number of occurrences of the sequence "XMAS" in various directions: horizontally, vertically, and diagonally (both directions). The problem required checking different orientations and positions in the grid to ensure every possible match was counted.

**Solution:**  
I iterated through each cell in the grid, checking in all 8 possible directions for the sequence "XMAS". For each direction (right, left, up, down, and the four diagonal directions), I verified if there was enough space in the grid to form the sequence and checked if the characters matched the required sequence. Whenever a match was found, I incremented the count. This approach ensured all directions were covered.

**My Thoughts:**  
This problem was straightforward but required attention to detail, particularly when dealing with multiple directions and ensuring that grid boundaries were respected. It was fun to implement, though at first, I had to think through how to handle edge cases (e.g., when there wasn't enough space in a direction to form the sequence). Overall, I found the problem quite enjoyable.
---


### Day [N]: [N](./N/)  
**Problem Summary:**  
*Write a short summary of the problem. What was it about? What concepts or algorithms were used?*  

**Solution:**  
*Briefly describe your approach. What made the problem interesting or challenging?*  

**My Thoughts:**  
*Share your experience solving the problem. Did you find it easy, frustrating, or enjoyable? Did you learn something new?*  

---

## 🔧 How to Run the Solutions  
1. Clone this repository:  
   ```bash
   git clone https://github.com/TheoHorn/advent-of-code
   cd advent-of-code/[2024]
   ```
2. Run the solution for a specific day (e.g., Day 1):  
   ```bash
   python 1/ss.py # silver-star solution
   python 1/gs.py # gold-star solution
   ```

---

## 📝 Reflections on [2024]  
*Summarize your overall experience for the year. What stood out? Any particularly fun or frustrating days? Did you learn new algorithms, tools, or programming tricks?*

---

Feel free to check out my other Advent of Code years in the [main repository](https://github.com/TheoHorn/advent-of-code). Happy coding! 🌟
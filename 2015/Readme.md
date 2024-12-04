# Advent of Code [2015] 🎄  

Welcome to my solutions for the **Advent of Code [2015]** challenges! Below, you’ll find my thoughts and progress for each day, along with a brief description of the problems tackled.

---

## 🗓 Progress Overview  
| Day | Puzzle Name           | Solution                | Difficulty | My Thoughts           |
|-----|-----------------------|-------------------------|------------|-----------------------|
| 1   | [Not Quite Lisp](#day-1) | [Solution](./1/)     | ★☆☆☆☆      | A straightforward start, setting a positive tone for the challenges ahead |
| 2   | [I Was Told There Would Be No Math](#day-2) | [Solution](./2/)     | ★☆☆☆☆      | Some math involved but still really easy |
| 3   | [Perfectly Spherical Houses in a Vacuum](#day-3)                   | [Solution](./3/)     | ★★☆☆☆      | The first test : a not strightforward solution                     |
| 4   | [The Ideal Stocking Stuffer](#day-4)                   | [Solution](./4/)     | ★☆☆☆☆      | Brute-forcing an hash is always fun                   |
| 5   | [Doesn't He Have Intern-Elves For This?](#day-5)                   | [Solution](./5/)     | ★★☆☆☆      | Kinda frustrating but quite easy still                     |
| 6   | [Title of Day 6](#day-6)                   | [Solution](./6/)     | ★★★★☆      | Write your thoughts                     |
| 7   | [Title of Day 7](#day-7)                   | [Solution](./7/)     | ★★★★☆      | Write your thoughts                     |
| 8   | [Title of Day 8](#day-8)                   | [Solution](./8/)     | ★★★★☆      | Write your thoughts                     |
| 9   | [Title of Day 9](#day-9)                   | [Solution](./9/)     | ★★★★☆      | Write your thoughts                     |
| 10  | [Title of Day 10](#day-10)                 | [Solution](./10/)    | ★★★★☆      | Write your thoughts                     |
| 11  | [Title of Day 11](#day-11)                 | [Solution](./11/)    | ★★★★☆      | Write your thoughts                     |


---

## 📜 Daily Breakdown  

### Day [1]: [Not Quite Lisp](./1/)  

**Problem Summary:**  
This challenge revolved around parsing a sequence of parentheses `(` and `)` to simulate going up or down a set of floors in a building. Each `(` increases the floor number by one, while each `)` decreases it. The task involved determining the final floor after processing the entire sequence and finding the position of the first character that causes the character to enter the basement (floor -1). This required careful tracking of counts and an early exit condition.

**Solution:**  
The provided solution iterates through the input string, maintaining a running tally (`ans`) of the floor number. Each parenthesis is evaluated to either increment or decrement the counter. A conditional check is used to determine when the counter first reaches -1, at which point the 1-based index of the character is printed. This approach efficiently handles the problem in a single pass through the string.

**My Thoughts:**  
This problem was simple but rewarding, as it introduced concepts like sequence traversal and condition-based exits. It was enjoyable to think about edge cases, such as what happens if the string never goes below floor 0. The solution worked well, but it might be fun to explore alternative implementations, such as using a generator to track states lazily. Overall, it was a great warm-up for Advent of Code.

---

### Day [2]: [I Was Told There Would Be No Math](./2/)  

**Problem Summary:**  
The challenge required calculating the total amount of wrapping paper needed for a list of gift boxes. Each box is defined by its dimensions: length (`l`), width (`w`), and height (`h`). The wrapping paper needed includes the surface area of the box plus the area of the smallest side for extra slack. The problem involves basic math operations such as calculating areas and identifying minimum values.

**Solution:**  
The provided code reads dimensions of the boxes from an input file, computes the surface area for each box, and adds the slack area based on the smallest side. The logic involves splitting the dimensions, converting them to integers, and using conditional checks to determine the smallest side. The algorithm is efficient for the input size, though it could be made more concise with helper functions or libraries.

**My Thoughts:**  
This problem was straightforward and enjoyable because it combined basic programming concepts like file handling and arithmetic. While the solution worked, the nested conditionals made the code slightly harder to read. A refactor using sorted dimensions could simplify the logic. Overall, it was a great exercise in problem decomposition and thinking about edge cases, such as dimensions being equal. 

--- 

### Day [3]: [Perfectly Spherical Houses in a Vacuum](./3/)

**Problem Summary:**  
This problem involved tracking the movements of Santa and his robotic helper delivering presents in a grid-like world. Each directional command (`^`, `v`, `<`, `>`) corresponds to a movement to a neighboring house. The challenge was to determine how many unique houses received at least one present based on their combined movements.

**Solution:**  
To solve this, I used sets to track visited houses. Santa and the robot alternated turns, which I managed by separating their movements using indexing. For each character in the input string, I updated the current position and added it to the set of visited coordinates. The final result was the size of this set.

**My Thoughts:**  
This problem was enjoyable due to its simplicity and its emphasis on optimizing movement tracking. It was interesting to manage two entities independently within the same grid.

---

### Day [4]: [The Ideal Stocking Stuffer](./4/)  

**Problem Summary:**  
The problem involves finding the smallest number \( x \) such that when concatenated with a given string (e.g., `"iwrupvqb"`) and hashed using MD5, the resulting hash starts with a specific number of leading zeroes. This is a classic example of brute-forcing a solution to match a hash condition, often seen in cryptography puzzles.

**Solution:**  
I used a brute-force approach, iterating over increasing integers \( x \) starting from 1, concatenating each with the input string, and checking the resulting MD5 hash for the desired prefix of six zeroes (`"000000"`). The solution leverages Python's `hashlib` module to compute the MD5 hash of the string efficiently. Once a match is found, the loop exits, and the solution is printed.  

**My Thoughts:**  
The problem was enjoyable because it demonstrated how cryptographic hash functions can be applied to problem-solving. It was straightforward in terms of implementation but computationally intensive due to the brute-force nature of the solution. The challenge primarily lay in understanding the MD5 hash behavior and ensuring the code efficiently terminates upon finding the solution.

---

### Day [5]: [Doesn't He Have Intern-Elves For This?](./5/)  

**Problem Summary:**  
This problem involves checking strings to determine whether they meet two specific criteria. First, a pair of any two letters must appear at least twice in the string without overlapping. Second, a single character must repeat with exactly one character in between. These conditions reflect a pattern-matching and substring-search challenge, often requiring careful implementation to avoid false positives or missed matches.

**Solution:**  
I iterated through each string in the input file and checked for the two conditions. For the first condition, I extracted all pairs of characters and verified if they reappeared later in the string (without overlap). For the second condition, I checked if any character repeated with exactly one character separating them. If both conditions were satisfied, the string was considered valid, and the counter was incremented. This approach used nested loops for the checks.

**My Thoughts:**  
The problem was both interesting and somewhat frustrating due to the need to balance precision and efficiency in substring searches. Debugging was key to ensuring the logic captured the criteria correctly without false positives. It was rewarding to see the solution work, and I appreciated how the problem sharpened my pattern-matching skills. It was also a good reminder to handle edge cases in string processing.

---

## 🔧 How to Run the Solutions  
1. Clone this repository:  
   ```bash
   git clone https://github.com/TheoHorn/advent-of-code
   cd advent-of-code/[2015]
   ```
2. Run the solution for a specific day (e.g., Day 1):  
   ```bash
   python 1/ss.py #for silver-star
   python 1/gs.py #for gold-star
   ```
--- 

Feel free to check out my other Advent of Code years in the [main repository](https://github.com/TheoHorn/advent-of-code). Happy coding! 🌟
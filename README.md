# Power Set Generator

A simple web application that generates the **power set** of a given set. Users can input a set and view all possible subsets.

---

##  How to Use

1. Enter elements of a set separated by commas (e.g., `a, b, c`)
2. Click the **"Generate Power Set"** button
3. View the power set results displayed below

---

##  Features

- Accepts user input for set elements
- Automatically removes duplicate elements
- Displays original set and all its subsets
- Shows total number of subsets
- Clean and simple interface

---

##  How it Works

This app uses **bit manipulation** to generate all possible subsets:

- A set of `n` elements has `2^n` possible subsets
- Each number from `0` to `2^n - 1` represents a unique subset
- The binary form of each number determines which elements to include


##  Test Cases

### Normal Cases:

- Input: `a, b, c`  
  Output: 8 subsets — `{}`, `{a}`, `{b}`, `{c}`, `{a,b}`, `{a,c}`, `{b,c}`, `{a,b,c}`

- Input: `1, 2, 3`  
  Output: 8 subsets

- Input: `red, blue, green`  
  Output: 8 subsets

### Edge Cases:

- **Empty input**  
  Output: Error message

- **Duplicate elements** (e.g., `a, a, b`)  
  Output: Power set of `{a, b}` — 4 subsets

- **Large set** (more than 10 elements)  
  Output: Error message (set too large)

---

## Limitations

- Maximum **10 elements** allowed (to avoid performance issues)
- **Duplicate elements** are removed automatically


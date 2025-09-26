
# Matrix Statistics Calculator

This project defines a Python function `calculate()` that takes a list of numbers, reshapes them into a **3×3 NumPy matrix**, and computes various statistics.  
It’s a clean way to understand how **NumPy axes** work and how to calculate row-wise, column-wise, and overall values.

---

## Features

The function returns the following statistics:
- **Mean**
- **Variance**
- **Standard Deviation**
- **Max**
- **Min**
- **Sum**

For each statistic, the function gives results in three ways:
1. Calculated **along columns (axis=0)**
2. Calculated **along rows (axis=1)**
3. Calculated for the **entire flattened matrix**

---

## Code

```python
import numpy as np 

def calculate(list_nums):
    if len(list_nums) < 9:
        raise ValueError('List must contain at least nine numbers.')
    
    np_arrays = np.array(list_nums).reshape(3, 3)
    
    calculations = {
        'mean': [
            np.mean(np_arrays, axis=0).tolist(),
            np.mean(np_arrays, axis=1).tolist(),
            np.mean(np_arrays)
        ],
        'variance': [
            np.var(np_arrays, axis=0).tolist(),
            np.var(np_arrays, axis=1).tolist(),
            np.var(np_arrays)
        ],
        'standard deviation': [
            np.std(np_arrays, axis=0).tolist(),
            np.std(np_arrays, axis=1).tolist(),
            np.std(np_arrays)
        ],
        'max': [
            np.max(np_arrays, axis=0).tolist(),
            np.max(np_arrays, axis=1).tolist(),
            np.max(np_arrays)
        ],
        'min': [
            np.min(np_arrays, axis=0).tolist(),
            np.min(np_arrays, axis=1).tolist(),
            np.min(np_arrays)
        ],
        'sum': [
            np.sum(np_arrays, axis=0).tolist(),
            np.sum(np_arrays, axis=1).tolist(),
            np.sum(np_arrays)
        ]
    }

    return calculations
````


## Code Explanation

### 1. Input Validation

```python
if len(list_nums) < 9:
    raise ValueError('List must contain at least nine numbers.')
```

* The function needs **at least 9 numbers** to form a 3×3 matrix.
* If you pass fewer numbers, it raises an error.

---

### 2. Reshape the List into a 3×3 Array

```python
np_arrays = np.array(list_nums).reshape(3, 3)
```

* Converts the Python list into a NumPy array.
* Reshapes it into a **3×3 matrix**.

Example:

```python
[0,1,2,3,4,5,6,7,8] → 
[[0,1,2],
 [3,4,5],
 [6,7,8]]
```

---

### 3. Building the Calculations Dictionary

```python
calculations = {
    'mean': [...],
    'variance': [...],
    ...
}
```

Each statistic returns a list with **three parts**:

1. Column-wise calculation (`axis=0`)
2. Row-wise calculation (`axis=1`)
3. Overall calculation (flattened array)

---

### 4. Example for Mean

```python
'mean': [
    np.mean(np_arrays, axis=0).tolist(),   # mean of each column
    np.mean(np_arrays, axis=1).tolist(),   # mean of each row
    np.mean(np_arrays)                     # mean of all elements
]
```

* **axis=0** → collapse rows → gives means of columns.
* **axis=1** → collapse columns → gives means of rows.
* **No axis** → calculate mean for the whole 3×3 array.

`.tolist()` converts NumPy arrays into regular Python lists for readability.

---

### 5. Other Statistics

The same logic applies for:

* **Variance** → spread of values.
* **Standard deviation** → square root of variance.
* **Max/Min** → largest/smallest values.
* **Sum** → add up values.

All of them are computed column-wise, row-wise, and overall.

---

## Example Usage

```python
print(calculate([0,1,2,3,4,5,6,7,8]))
```

### Output

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.0],
  'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.449...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

---

## How to Think About Axes

Consider the matrix:

```
[[0,1,2],
 [3,4,5],
 [6,7,8]]
```

* **Axis=0 (columns):** Go *down* each column. → `[0,3,6], [1,4,7], [2,5,8]`
* **Axis=1 (rows):** Go *across* each row. → `[0,1,2], [3,4,5], [6,7,8]`
* **Flattened:** Treat everything as a single list of 9 numbers.

---

## Requirements

* Python 3.x
* [NumPy](https://numpy.org/)

Install NumPy:

```bash
pip install numpy
```

---

## Error Handling

If fewer than **9 numbers** are passed, the function raises:

```python
ValueError: List must contain at least nine numbers.
```

---

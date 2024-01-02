# <p align = "center">🐍 Python - Variable Annotations</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

<img src="https://i.imgur.com/DRPXtkk.jpg" width='100%' />

### Learning Objectives
- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with `mypy`

### Tasks
- **0-add.py** : type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float
- **1-concat.py** : type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string
- **2-floor.py** : type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float
- **3-to_str.py** : type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float
- **4-define_variables.py** :
  - Define and annotate the following variables with the specified values:
    - `a` : an integer with a value of 1
    - `pi` : a float with a value of 3.14
    - `i_understand_annotations` : a boolean with a value of True
    - `school` : a string with a value of “Holberton”
- **5-sum_list.py** : type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float
- **6-sum_mixed_list.py** : type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float
- **7-to_kv.py** : type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple
- **8-make_multiplier.py** : type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`
- **9-element_length.py** : annotate the below function’s parameters and return values with the appropriate types :
```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

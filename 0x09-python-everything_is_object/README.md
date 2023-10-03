# 0x09. Python - Everything is object

## Description
This repository contains solutions to tasks and questions related to the topic of Python objects. 

## Files
* `0-answer.txt`: A text file containing the answer to the question "What function would you use to print the type of an object?"
* `1-answer.txt`: A text file containing the answer to the question "How do you get the variable identifier (which is the memory address in the CPython implementation)?"
* `2-answer.txt`: A text file containing the answer to the question "In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
  ```python
  >>> a = 89
  >>> b = 100
  ```
* `3-answer.txt`: A text file containing the answer to the question "In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
  ```python
  >>> a = 89
  >>> b = 89
  ```
* `4-answer.txt`: A text file containing the answer to the question "In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
  ```python
  >>> a = 89
  >>> b = a
  ```
* `5-answer.txt`: A text file containing the answer to the question "In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
  ```python
  >>> l_a = [1, 2, 3]
  >>> l_b = [1, 2, 3]
  ```
* `6-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> l_a = [1, 2, 3]
  >>> l_b = l_a
  >>> print(l_a == l_b)
  ```
* `7-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> l_a = [1, 2, 3]
  >>> l_b = l_a
  >>> print(l_a is l_b)
  ```
* `8-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> l_a = [1, 2, 3]
  >>> l_b = l_a
  >>> l_a.append(4)
  >>> print(l_b)
  ```
* `9-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> l_a = [1, 2, 3]
  >>> l_b = l_a
  >>> l_a = l_a + [4]
  >>> print(l_b)
  ```
* `10-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> l_a = [1, 2, 3]
  >>> l_b = l_a
  >>> l_a += [4]
  >>> print(l_b)
  ```
* `11-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> l_a = [1, 2, 3]
  >>> l_b = l_a
  >>> l_a = l_a.append(4)
  >>> print(l_a)
  ```
* `12-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> def increment(n):
  >>>     n += 1
  >>>     return n
  >>> 
  >>> a = 1
  >>> print(increment(a))
  >>> print(a)
  ```
* `13-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> def increment(n):
  >>>     n.append(4)
  >>>     return n
  >>> 
  >>> l = [1, 2, 3]
  >>> print(increment(l))
  >>> print(l)
  ```
* `14-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> def increment(n):
  >>>     n += [4]
  >>>     return n
  >>> 
  >>> l = [1, 2, 3]
  >>> print(increment(l))
  >>> print(l)
  ```
* `15-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> s_a = "Hello"
  >>> s_b = "World"
  >>> print(s_a + " " + s_b)
  ```
* `16-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> s_a = "Hello"
  >>> s_b = "World"
  >>> s_c = s_a
  >>> s_a += " " + s_b
  >>> print(s_c)
  ```
* `17-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> def change_name(n):
  >>>     n = "John"
  >>>     return n
  >>> 
  >>> name = "Alice"
  >>> print(change_name(name))
  >>> print(name)
  ```
* `18-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> def append_to_list(l):
  >>>     l.append(4)
  >>>     return l
  >>> 
  >>> lst = [1, 2, 3]
  >>> print(append_to_list(lst))
  >>> print(lst)
  ```
* `19-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> def assign_new_list(l):
  >>>     l = [4, 5, 6]
  >>>     return l
  >>> 
  >>> lst = [1, 2, 3]
  >>> print(assign_new_list(lst))
  >>> print(lst)
  ```
* `20-answer.txt`: A text file containing the answer to the question "What do these 3 lines print?"
  ```python
  >>> def assign_new_string(s):
  >>>     s = "Python"
  >>>     return s
  >>> 
  >>> string = "Hello"
  >>> print(assign_new_string(string))
  >>> print(string)
  ```
* `21-answer.txt`: A text file containing the answer to the question "What is the purpose of the bytecode?"
* `22-answer.txt`: A text file containing the answer to the question "What will be printed by the line (print(type(a)))?"
  ```python
  >>> a = 1
  ```
* `23-answer.txt`: A text file containing the answer to the question "In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
  ```python
  >>> a = 1
  >>> b = 1
  ```
* `24-answer.txt`: A text file containing the answer to the question "In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
  ```python
  >>> a = 1
  >>> b = 1
  >>> a is b
  ```
* `25-answer.txt`: A text file containing the answer to the question "In the following code, do `a` and `b` point to the same object? Answer with Yes or No.
  ```python

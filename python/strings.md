# String
- Strings are objects
- They are immutable. They cannot be modified after creation.
- String is a object. And a string variable is just a pointer to the memory.
- When we are adding "Hello" to "Ẅorld" it creates a new object with the updated value.
```python
Code:
str1 = "Hello"
id1 = id(str1)

str1 = str1 + " World"
id1 == id(str1) # False
```

# Iteration
```python
Code:
  arr = [1,2,3,4,5,6,7]
  arr[:3] #1,2,3
  arr[2:5] #3,4,5
  arr[::-1] #7,6,5,4,3,2,1
  arr[::2] #1,3,5,7
  arr[2::-2] #7,5,3
```

# Concat
```python
Code:
  "Hello" + " World"
  f"{name} is {26} years old"
  "{} is {} years old".format("Aritra", 26)
```

# Comparison


# Methods
- strip
  ```python
  Code:
    "Aritra is awesome".strip() #["Aritra", "is", "awesome"]
    "this:is:amazing".strip(":") #["this", "is", "amazing"]
  ```

- join 

- replace
- find

- center

- upper
- lower
- casefold
```python
Code:
  "aritra".upper() # ARITRA
  "aritra".capitalize() # Aritra
  "Aritra".lower() # aritra
  "Aritra".casefold() # aritra
```


- isdigit, isalpha, isalnum


# Conversion from integer
To convert an integer into string, we can do - 
```python
Code:
  str(42)
```

Similarly to convert string to integer we can do - 
```python
Code:
  int("42") # Default is decimal encoding
  int("1010", 2) #Binary encoding
```




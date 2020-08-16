# Notes and Exercises from Python Workout by Reuven Lerner

## Ch 1 Numeric Types

### Exercise 1 - Number guessing game
- Use `randint` in the `random` module to generate a random number
- Make an infinite loop with `while True:`
- Use `input` to get input from a user
- Use `int` to change a string to an integer

### Exercise 2 - Summing numbers
- Usee the "splat" operator (aka *) to allow a function to receive any number of arguments
- If you have an iterable object and want to pass its elements to a function, just preface it with * in the function call

### Exercise 3 - Run timing
- Empty string and the numeric 0 are considered to be `False`
- Use `not` in front of a variable that might be empty to evaluate `False`
- Wrap user input in `try` in case the user gives you an illegal value

### Exercise 4 - Hexadecimal Output
- `enumerate` returns a two-element tuple with each iteration. This provides the numeric index of each iteration.
- `reversed` returns a new iterable
- `**` operator is used for exponentiation

## Ch 2 Strings

### Exercise 5 - Pig Latin
- If you find yourself repeating yourself or writing a long expression, there's probably a better, more pythonic, way of doing things
- The `in` operator works on all sequences (strings, lists, tuples). Using `in` on a dict will work but will only search through the keys, ignoring the values
- Slices are Python's way of retrieving a subset of elements from a sequence

### Exercise 6 - Pig Latin Sentence
- `str.split` can take an argument, which determines which string should be used as the separator between fields
- As a general rule, its not a good idea to build strings with `+=`. Rather, you should add elements to a list using `list.append` and then invoke `str.join`
- List are mutable and adding to a list with `append` is relatively inexpensive in both memory and computation

### Exercise 7 - Ubbi Dubbi
- Iterate over characters in a string, append items to a list

### Exercise 8 - Sorting a string
- The `sorted` function, which takes an iterable, returns a list with its elements sorted
- The idea behind Unicode is that we should be able to use computers to represent any character used in any language from any time
- Unicode assigns each character a unique number (known as *code point*)
- The code point can be very large, so we translate it into a format that can be translated as bytes
- Python uses what's known as UTF-8
- It's easy forget that there's a differences between bytes and characters

## Ch 3 Lists and Tuples

### Exercise 9 - First-last
- Data is strongly typed, variables don't have any types
- We can write a function that expects to take any indexable type and return something appropriate
- Slices allow you to grab just part of any sequence

### Exercise 10 - Summing anything
- A function can take any number of arguments with the "splat" (*) operator
- The "takes any number of arguments" parameter is typically called `*args`
- In Python, everthing is considered `True` in an `if` except `None, False, 0` and empty collections

### Exercise 11 - Alphabetizing names
- Variables defined outside of any function are generally referred to as "constants" and are defined in ALL CAPS
- `itemgetter` takes any number of arguments and returns a function that applies each of those arguments in square brackets
- `sorted` returns a new sorted list from the items in the *iterable* argument
- The optional `key` argument specifies a function of one argument that is used to extract a comparison key
- To create an anonymous function with lambda, use the reserved world lambda and then list any parameters before a colon. Then write the one-line expression that the lambda returns. And indeed, in a Python lambda, you’re restricted to a single expression--no assignment is allowed, and everything must be on a single line

### Exercise 12 - Word with the most repeated letters
- `Counter`, a subclass of `dict` defined in the `collections` module, makes it easy to count things
- Passing a function to the `key` parameter in `max`
- The built-in max function takes a key function, just like sorted, and returns the element that received the highest score.

### Exercise 13 - Printing Tuple Records
- Used `sorted` and `itemgetter` to sort the list of tuples
- Print padding using a colon `(:)` character. `{1:10}` inserts spaces if the data contains fewer than 10 characters

## Ch 4 Dictionaries and sets
- Dicts are called *mappings* in Python, because the hash function *maps* our key to an integer, which we can then use to store our key-value pairs
- Python's dicts:
    - always store key-value pairs together
    - guarantee very fast lookup for keys
    - ensure key uniqueness
    - don't guarantee anything regarding value lookup
- Sets are like dicts without values

### Exercise 14 - Restaurant
- Invoke `strip` to remove space characters
- Check for empty string with `if not`

### Exercise 15 - Rainfall
- Use an infinite loop with `while True:`
- Use `dict.get` with a default, to either get the current value associatd with the key or 0
- Trap errors with `try` and `except`
- `defaultdict`, a class defined in the `collections` module can be used to default a value when you ask for a key that doesn't exist

### Exercise 16 - Dictdiff
- Using `dict.get` for shorter, more elegant, and more maintainable code
- Collect all keys, put them in a `set` to ensure that each appears only once, and then iterate over the `set`
- `dict.keys()` returns a special object type of `dict_keys`
- Union `|`, intersection `&`

### Exercise 17 - How many different numbers?
- A `set` contains unique elements
- If you have a list of values from which you want to remove all of the duplicates, you can just create a set

## Ch 5 Files

### Exercise 18 - Final line
- Knowing how to read specific parts of a file, as opposed to the entire thing, is a useful and practical skill
- `open` arguments
    1. `filename`: is a string representing a valid filename
    2. `mode`: Optional argument. `r, w, a` for read, write, or append. The `b` option is used for reading the file in byte, or binary, mode.
- Use `with` to guarantee that the file has been closed by the end of the block
- Binary mode using `b`
    - Python expects the contents of a file to be valid UTF-8 formatted Unicode strings
    - Binary files don't use Unicode
    - Open a nontext file in *binary* or *bytes* mode using `b` in the `mode` argument
    - There are no lines in a binary file. You should use the `read` method to retrieve a fixed number of bytes
```
with open(filename, 'rb') as f:
    while True:
        one_chunk = f.read(1000)
        if not one_chunk:
            break
        print(f'This chunk contains {len(one_chunk)} bytes')
```

### Exercise 19 - /etc/passwd to dict
- `str.split` returns a list of strings split by the delimiter
- Use `str.startswith` to ignore certain lines
- `with` is a general Python construct known as a *context manager*

### Exercise 20 - Word count
- Use a `dict` to accumulate closely related data
- Use a `set` to track a list of unique items. Use `set.update()` to add items to the set
- `split()` with no arguments splits on whitespace and ignores `\n`

### Exercise 21 - Longest word per file
- Whenever you need to transform a collection of inputs into a collection of outputs, you should use comprehensions
- List comprehensions are the most common, but set and dict comprehensions are also useful
- Use `os.path.join` to combine the directory name with a filename
- The easiest and most standard way to list files in a directory is `os.listdir`, a function in the `os` module. It returns a list of strings, the names of files in the directory
```
filenames = os.listdir('/etc/')
```
- You will need to add the directory name at the beginning with `os.path.join`, which works cross-platform
- The `glob` module allows you to filter the filenames by a pattern. It returns a ist of strings, with each string containing the complete path to the file.
```
filenames = glob.glob('/etc/*.conf')
```
- The `pathlib` module also makes things easier in many ways.
```python
# create a pathlib.Path object
import pathlib
p = pathlib.Path('/etc/')

# iterator that returns files in the directory
for one_filename in p.iterdir():
    print(one_filename)

# get a list of files matching a pattern
for one_filename in p.glob('*.conf'):
    print(one_filename)
```

### Exercise 22 - Reading and writing CSV
- Python comes with a `csv` module that handles writing to and reading from CSV files
- You can use `with` to open two separate files
- Use `csv.reader` to read delimited records. Use the `delimiter` argument to separate on a character other than `,`
- Use `csv.writer` to write delimited records

# Resources
Python Workout by Reuven Lerner, Published by Manning Publications, 2020
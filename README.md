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
- The `glob` module allows you to filter the filenames by a pattern. It returns a list of strings, with each string containing the complete path to the file.
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

### Exercise 23 - JSON
- JSON is a popular format for data exchange, in particular, many web services and APIs send and receive data using JSON
- Python comes with a `json` module, which can be usd to turn JSON-encoded strings into Python objects
- The `json.load` method reads a JSON-encoded string from a file and returns a combination of Python objects
- Valid JSON uses double quotes ("), not single quotes (')
- It's often easier and faster to make use of built-int data structures likes lists, tuples, and dicts instead of creating a class
- Use `defaultdict` from the `collections` module to default the value for a key that does not exist in a `dict`

### Exercise 24 - Reverse Lines
- Transforming files from one format into another and taking data from one file and creating another based on it are common tasks
- `with` takes on or more objects and allows us to assign variables to them
- Reverse a sequence using Python's slice syntax `s[::-1]`. Step size of -1 returns a reversed sequence.
- Remove a newline character from the end of the line with `str.rstrip()`

## Ch 6 Functions
- Never use a mutable value, such as a list or dict, as a parameter's default value. Default values are stored and reused across calls to the function.

### Exercise 25 - XML generator
- `*args*` should be used when you'll put its values into a `for` loop. If you're grabbing elements from `*args` with numeric indexes, you're probably doing something wrong
- make an argument optional by defining a default
- When we define a function with `**kwargs`, we're telling Python that we might pass any name-value pair in the style `name=value`. These argument are used to create a `dict`, traditionally called `kwargs`, whose keys are the keyword names and whose values are the keyword values
- Create a string from the key-value pairs in a `dict` using list comprehension

### Exercise 26 - Prefix notation calculator
- The term *scoping* refers to the visibility of variables from within the program
- Python has four levels of scoping (LEGB):
    1. Local - variable defined inside a function
    2. Enclosing function - A function defined inside another function is known as a *closure*
    3. Global - changing global variables from within a function is almost always a bad idea
    4. Built-ins
- Use a `dict` in which the functions are values instead of `if elif else` conditions

### Exercise 27 - Password generator
- `random.choice` returns one randomly chosen element from a sequence
- Define and return inner functions to create numerous similar functions (closure)
- The inner function is defined when the outer function is executed
- We create a new inner function once for each time the outer function is invoked
- The returned function references a variable in the outer function, where it was originally defined

## Ch 7 Functional programming with comprehensions
- *Functional programming* aims to make programs more reliable by keeping functions short and data immutable
- Short functions are easier to understand, test, and maintain
- Python Comprehensions make it easy to create lists, sets, and dicts based on other data structures

### Exercise 28 - Join numbers
- When you want to translate an iterable into a list, you should use a comprehension
- If you want to execute something for each element of an iterable, then a traditional `for` loop is better
- *Transformations*, taking values in an iterable and producing a new iterable, should be executed with comprehensions
- `str.join` only works on a sequence of strings
- Each list comprehension contains two parts:
    1. The source iterable
    2. The expression we'll invoke once for each element
- Generator expressions work similar to comprehensions but use less memory

### Exercise 29 - Add numbers
- `map` takes two arguments: a function and an iterable. It applies the function to each element of the iterable, returning a new iterable.
- `filter` takes two arguments: a function and an iterable. It applies the function to each element, the output of the function determines whether the element will appear in the output.
- Comprehension are considered to be the modern way of `map` and `filter`
- Any *expression* is anything in Python that returns a value. Comprehensions use expressions.
- `str.split` returns a list of strings
- Use the `str.isdigit` method to filter for items that can be turned into numbers

### Exercise 30 - Flatten a list
- List comprehensions allow us to evaluate an expression on each element of an iterable
- Nested comprehensions allow us to iterate on lists of lists

### Exercise 31 - Pig latin translation of a file
- We can use nested list comprehensions to iterate over each line of the file
- It's more memory efficient to return an iterator object than a list comprehension
- A generator expression, which looks like a list comprehension, but uses round parantheses instead of square brackets
- If you have a generator expression inside a function call, you don't need both sets of parentheses

### Exercise 32 - Flip a dict
- dict comprehensions provide an easy way to create a dict based on an iterable
- Use the `dict.items` method to loop over the elements of a dict
- In a comprehension, I’m trying to create a new object based on an old one. It’s all about the values that are returned by the expression at the start of the comprehension. By contrast, `for` loops are about commands, and executing those commands.

### Exercise 33 - Transform values
- You can receive a function as a function argument, and comprehensions can help us elegantly solve a wide variety of problems

### Exercise 34 - (Almost) supervocalic words
- The `<` operator checks to see if the item on the left is a subset of the item on right when working with a `set`
- The difference between a list comprehension and a set comprehension is a pair of brackets. Square for list (`[]`), Curly braces for set (`{}`)
- Using sets as the basis for textual comparisons is useful

### Exercise 35 - Gematria
- Get letters of the english alphabet using `string.ascii_lowercase`
- Use the `enumerate` built-in iterator to get the index of each item in a sequence

## Ch 8 Modules and packages
- The most commonly used things in the standard library, such as lists and dicts, are built into the language, thanks to a namespace known as `builtins`
- When you use `import` to load a module
    - Python looks for the module in a number of directories, defined in a list of strings called `sys.path`. If Python encounters a file in one of those diretories, it loads the file and stops searching in any other directories
    - There are a number of ways to modify `sys.path`

### Exercise 36 - Sales tax
- Use integers or the `Decimal` class when performing calculations involving money
- Decent error checking is important. Create your own exception class and raise it.

### Exercise 37 - Menu
- This is an example of a *dispatch table*
- Use `**kwargs` parameter to create that dispatch table dynamically
- `if __name__ == '__main__':
    - When a module is loaded, its code is executed from the start of the file until the end
    - The `__name__` variable is equal to `__main__` when the code is running in the initial, default, and top-level namespace provided by Python. Otherwise `__name__` is equal to the module that imported it
    - This should typically only appear once, at the end of your module file

### Modules vs. packages
- A module is a single file, with a '.py' suffix. We can load the module using `import`.
- A package is a directory containing one or more Python modules. Assuming the package is in `sys.path`, you can `import` a module from package: `from mypackage import first`
- To use `import mypackage`:
    - You must have a file named `__init__.py` in the `mypackage` directory
    - Importing `mypackage` effectively means that `__init__.py` is loaded and thus executed. Inside of that file, you can import one or more of the modules within the package
- "Poetry" makes the process of creating a distribution package easier

## Ch 9 Objects

### Exercise 38 - Ice cream scoop
- Every object has a type and one or more attributes
- The `__init__` method is invoked after an object has been created. Its parameters allow us to set attributes on newly created instances.
- The first paramter in every method is traditionally called `self`. `self` isn't actually a reserved word in Python.
- In Python, because everything is public, there’s no real need for getters and setters.
- Classes are *callable*, meaning that they can be invoked with parentheses.
- Whereas other programming languages talk about “instance variables” and “class variables,” Python developers have only one tool, namely the attribute. You can think of the attributes of an object as its own private dict.
- As a general rule, you want to define all of your attributes in `__init__` to ensure that your code is as readable and obvious as possible

### Exercise 39 - Ice cream bowl
- An important technique is *composition*, when one object contains another object
- To print the object, we simply invoke `print()`. This has the effect of calling the __repr__ method on our object, assuming that one is defined.
- You can define __repr__, __str__, or both on your objects. In theory, __repr__ produces strings that are meant for developers and are legitimate Python syntax.
- By contrast, __str__ is how your object should appear to end users.
- Inheritance describes an "is-a" relationship
- Composition describes an "has-a" relationship
- As of Python 3.7, you can cut out some of the boilerplate class-creation code with the `dataclass` decorator. The `@dataclass` decorator writes the __init__ method for you.
``` python
@dataclass
class Scoop():
    flavor : str
```
- Python searches for attributes in a standard path: (ICPO):
    1. Instance
    2. Class
    3. Parents
    4. Object

# Resources
Python Workout by Reuven Lerner, Published by Manning Publications, 2020
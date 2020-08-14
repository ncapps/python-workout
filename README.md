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

# Resources
Python Workout by Reuven Lerner, Published by Manning Publications, 2020
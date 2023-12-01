0x03. Python - Data Structures: Lists, Tuples


Why Python programming is awesome:

Readability: Python has a clean and readable syntax, making it easy for beginners to learn and understand.

Versatility: It supports both procedural and object-oriented programming, making it versatile for various applications.

Extensive Libraries: Python has a vast standard library and numerous third-party libraries for different purposes, saving development time.

Community and Documentation: Python has a large and active community, and there is extensive documentation available, making problem-solving easier.

Interpretation: Python is an interpreted language, allowing for quick development and testing.

What are lists and how to use them:

Lists: In Python, a list is a mutable, ordered collection of items. Each item can be of any data type.

Usage: You can create a list using square brackets [] and separating items with commas. Example: my_list = [1, 2, 'hello', 3.14].

Differences and similarities between strings and lists:

Similarities:

Both can be indexed and sliced.
They can be iterated over.
Differences:

Strings are immutable (you can't change individual characters), while lists are mutable.
Strings have specific string methods, whereas lists have list-specific methods.
Most common methods of lists and how to use them:

Some common list methods include:

append(): Adds an element to the end.
extend(): Adds elements from another list.
insert(): Inserts an element at a specific index.
remove(): Removes a specified element.
pop(): Removes and returns an element at a given index.
index(): Returns the index of the first occurrence of a value
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

Using lists as stacks and queues:

Stacks: Use append() to push items onto the stack and pop() to remove the last item.

Queues: Use append() to enqueue items and pop(0) to dequeue items. However, for efficient queues, use the collections.deque class.
squares = [x**2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]

Tuples and how to use them:

Tuples: Similar to lists but immutable. Created using parentheses ().
my_tuple = (1, 2, 'hello', 3.14)

my_list = [1, 2, 3, 4]
del my_list[2]  # Removes the element at index 2
print(my_list)  # Output: [1, 2, 4]

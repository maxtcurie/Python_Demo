from collections import Counter

# Example list of elements
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Create a Counter object
counter = Counter(elements)

# Print the count of each element
print(counter)

# Access the count of a specific element
print(f"Count of 'apple': {counter['apple']}")
print(f"Count of 'banana': {counter['banana']}")
print(f"Count of 'orange': {counter['orange']}")

# You can also use Counter with a string
string = "hello world"
string_counter = Counter(string)

print(string_counter)
print(f"Count of 'l': {string_counter['l']}")

# Most common elements
print(counter.most_common(2))

# Update the counter with more elements
more_elements = ['banana', 'kiwi', 'banana']
counter.update(more_elements)
print(counter)

# Subtract elements
counter.subtract(['banana', 'apple'])
print(counter)

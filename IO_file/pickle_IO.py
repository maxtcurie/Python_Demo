import pickle

# Sample data
data = {
    "name": "John",
    "age": 30,
    "is_student": False
}

# Serialize the data and save to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Now let's load the data back from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
# Output: {'name': 'John', 'age': 30, 'is_student': False}

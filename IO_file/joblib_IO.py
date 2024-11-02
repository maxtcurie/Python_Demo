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

pickle.dump(data, open('data.pkl', 'wb'))

# Now let's load the data back from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

loaded_data = pickle.load(open('data.pkl', 'rb'))


print(loaded_data)
# Output: {'name': 'John', 'age': 30, 'is_student': False}

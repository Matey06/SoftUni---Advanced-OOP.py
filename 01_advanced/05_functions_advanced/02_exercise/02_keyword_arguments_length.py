def kwargs_length(**kwargs):
    return len(kwargs)

#Test cases
dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))
print("===================================")
dictionary = {}
print(kwargs_length(**dictionary))

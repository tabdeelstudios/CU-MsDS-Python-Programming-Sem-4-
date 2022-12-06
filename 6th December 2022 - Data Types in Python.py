# Lists
# person = ['John', 57, 40000.00, True]
#         #    0     1     2       3
# print(person)

# for val in person:
#     print(val)

# print(person[3])

# #Slicing a list
# firstData = person[2:4]
# print(firstData)

# #Lenght
# print(len(person))

# #Mutable
# person[2] = 'Bangalore'
# print(person)

#concatenation
# finalPersonData = person+firstData
# print(finalPersonData)

# numbers = ["Bangalore", "Jaipur", "Nagpur", "Chennai"]
# print('Before sort : ')
# print(numbers)
# sortNumbers = numbers.sort()
# print('After sort : ')
# print(numbers)

# numbers1 = ["Bangalore", "Jaipur", "Nagpur", "Chennai"]
# print('Before sort : ')
# print(numbers1)
# sortNumbers1 = sorted(numbers1)
# print('After sort : ')
# print(sortNumbers1)
# print(numbers1)


# # Tuples -> ordered and immutable
# person = ('John', 57, 40000.00, True)
# print(person)

# newPerson = person[0:2]
# print(newPerson)

# temp = ("Bangalore", "Jaipur", "Nagpur", "Chennai")
# thirdData = sorted(temp)
# print(thirdData)

# # Sets
# score = {100,200,5000}
# print(score)

# score.add(500)
# print(score)

# score1 = {100,200,5000}
# score2 = {100,500,1000}
# print(score1.union(score2))
# print(score1.intersection(score2))
# print(score1.difference(score2))

# Dictionaries
person = {
    'city':'Bangalore',
    'age':56,
    'name':'John'
}

print(person)

print(person['age'])

person['age']=60
print(person['age'])

person['status']=False
print(person)

print(person.keys())
print(person.values())











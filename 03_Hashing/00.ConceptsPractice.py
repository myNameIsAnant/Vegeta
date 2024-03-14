"""
### *****Number Hashing***** ###
### *****Through List***** ###
"""

hash_list = [0] * 13
myarray = [1, 11, 10, 7, 2, 11, 12, 9, 6, 12, 2, 10, 12, 12, 10, 6, 1, 12, 1, 10]

for i in myarray:
    hash_list[i] += 1  # Pre-Storing
print(myarray)
print(hash_list)
print(hash_list[int(input("Fetch Count of Number(1-12): "))])  # Fetch

"""
### *****Character Hashing***** ###
### *****Through List***** ###
"""
### ***Method 1*** ###
mystring = "aerroooppllaannneeee"
hash_char = [0] * 122
for i in mystring:
    hash_char[ord(i)] += 1
print(hash_char[ord(input("Enter Char to Find Frequency: "))])  # Fetch

### ***Method 2*** ###
mystring = "aerroooppllaannneeee"
hash_char = [0] * 26
for i in mystring:
    hash_char[ord(i) - 97] += 1
print(hash_char[ord(input("Enter Char to Find Frequency: ")) - 97])


"""
### *****Number Hashing***** ###
### *****Through Dictionary***** ###
"""

hash_dict = {}
myarray = [1, 11, 10, 7, 2, 11, 12, 9, 6, 12, 2, 10, 12, 12, 10, 6, 1, 12, 1, 10]

for i in myarray:
    hash_dict[i] = hash_dict.get(i, 0) + 1

print(hash_dict.get(int(input("Fetch Count of Number(1-12): ")), 0))

"""
### *****String Hashing***** ###
### *****Through Dictionary***** ###
"""

hash_dict = {}
mystring = "aerroooppllaannneeee"

for i in mystring:
    hash_dict[i] = hash_dict.get(i, 0) + 1

print(hash_dict.get(input("Enter Char to Find Frequency: "), 0))

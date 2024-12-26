user_info = {
    "user_name" : "devendra_1234",
    "name" : "Devendra",
    "email" : "dddd.@mail.com",
}

print(user_info)

# getting the key and values of the dictionary
print(user_info.keys())
print(user_info.values())

# fetching the value an in dictionary
print(user_info.get("email"))
print(user_info["user_name"])

# adding a item in dictionary
user_info["age"] = 29
print(user_info)

user_info.pop("email")
print(user_info)

print(user_info.items())

# looping the dictionary
for key, value in user_info.items():
    print(key, value)

# copying the dictionary
user_info_copy = user_info.copy()
user_info_copy.pop("age")
print(user_info_copy)

user_info.clear()
print(user_info)

del user_info
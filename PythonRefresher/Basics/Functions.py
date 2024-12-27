def print_full_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

print_full_name("Devendra", "Kumar")

def create_student(first_name, last_name, age):
    new_student = {
        "first_name": first_name,
        "last_name" : last_name,
        "age" : age
    }

    return new_student

print(create_student("Devendra", "Kumar", 25))

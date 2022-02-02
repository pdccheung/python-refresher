user_file = input ("Please provide a name for the file: ")
user_content = input ("What would you like to add to the file? ")
with open (user_file, 'a') as file:
    file.write(user_content)

print(f"This is what your {user_file} file looks like: ")
with open (user_file, 'r') as file: 
    content = file.read()

print(content)
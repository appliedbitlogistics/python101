# A simple hello world python program that prints "Hello World" to a file then reads the file and prints to the console.

message = "Hello World" # Set variable message to "Hello World"

print("Saving File: hello_world.txt")
with open("hello_world.txt", "w") as file: # Open hello_world.txt in write mode
    file.write(message) # Write Hello World to the file

print("Reading File: hello_world.txt")
with open("hello_world.txt", "r") as file: # Open hello_world.txt in read mode
    print(file.read()) # Print Hello World to the console



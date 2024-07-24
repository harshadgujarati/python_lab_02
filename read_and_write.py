# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is some content written to the file.\n")
    file.write("This is another line of text.\n")


# Reading from the file
with open('example.txt', 'r') as file:
    print(file.read())
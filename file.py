import os

# Ask the user for a file name and read the contents of that file
input_filename = "Enter the name of the file to be read: "

# Open the file in read mode
try:
    with open(input_filename, 'r') as file:
        # Read the contents of the file
        contents = file.read()
        # Modify the contents
        modified_contents = contents.replace(' ', '_')
        # Ask the user for a new file name to save the modified contents
        output_filename = input("Enter the name of the file to save the modified contents: ")
        # Write the modified contents to the new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_contents)
            print("File saved successfully.")
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Permission denied to read the file.")
except Exception as e:
    print("An unexpected error occurred:", str(e)) 

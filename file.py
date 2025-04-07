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
    # Instructions to push the code to GitHub
    # 1. Initialize a Git repository in the project directory
    # 2. Add the file to the staging area
    # 3. Commit the changes with a message
    # 4. Add the remote repository URL
    # 5. Push the changes to the remote repository


    # Define the Git commands
    commands = [
        "git init",
        "git add .",
        'git commit -m "Initial commit"',
        "git remote add origin <your-repository-url>",
        "git branch -M main",
        "git push -u origin main"
    ]

    try:
        # Execute each command
        for command in commands:
            os.system(command)
        print("Code pushed to GitHub successfully.")
    except Exception as e:
        print("An error occurred while pushing the code to GitHub:", str(e))  